import express, { Request, Response } from 'express';
import path from 'path';
import fs from 'fs';
import { createServer as createViteServer } from 'vite';
import { INITIAL_DATABASE } from './src/defaultData';
import { SchoolDatabase } from './src/types';

const PORT = 3000;

// SSE Client list for real-time synchronization
interface SSEClient {
  id: string;
  res: Response;
}

let sseClients: SSEClient[] = [];

// In-memory data store with disk persistence fallback
const DATA_DIR = path.join(process.cwd(), 'data');
const DATA_FILE = path.join(DATA_DIR, 'timetables.json');

let database: SchoolDatabase = { ...INITIAL_DATABASE };

// Load persistent data if exists
try {
  if (fs.existsSync(DATA_FILE)) {
    const raw = fs.readFileSync(DATA_FILE, 'utf-8');
    const loaded = JSON.parse(raw);
    if (loaded && loaded.schedules && Array.isArray(loaded.schedules)) {
      database = loaded;
      console.log(`Loaded ${database.schedules.length} schedules from disk`);
    }
  }
} catch (e) {
  console.error('Failed to load database from disk, using defaults:', e);
}

function saveDatabaseToDisk() {
  try {
    if (!fs.existsSync(DATA_DIR)) {
      fs.mkdirSync(DATA_DIR, { recursive: true });
    }
    fs.writeFileSync(DATA_FILE, JSON.stringify(database, null, 2), 'utf-8');
  } catch (e) {
    console.error('Failed to persist database to disk:', e);
  }
}

// Broadcast real-time event to all connected clients
function broadcastRealtimeEvent(eventType: string, data: any) {
  const payload = `event: ${eventType}\ndata: ${JSON.stringify(data)}\n\n`;
  sseClients.forEach((client) => {
    try {
      client.res.write(payload);
    } catch (err) {
      console.error(`Error sending SSE to client ${client.id}:`, err);
    }
  });
}

async function startServer() {
  const app = express();

  app.use(express.json({ limit: '50mb' }));
  app.use(express.urlencoded({ extended: true, limit: '50mb' }));

  // API Routes
  app.get('/api/health', (req: Request, res: Response) => {
    res.json({ status: 'ok', clientCount: sseClients.length });
  });

  // Get current complete database
  app.get('/api/timetable', (req: Request, res: Response) => {
    res.json(database);
  });

  // Real-time Server-Sent Events (SSE) stream
  app.get('/api/events', (req: Request, res: Response) => {
    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');
    res.flushHeaders?.();

    const clientId = `${Date.now()}_${Math.random().toString(36).substring(2, 9)}`;
    const newClient: SSEClient = { id: clientId, res };
    sseClients.push(newClient);

    // Send initial handshake
    res.write(`event: connected\ndata: ${JSON.stringify({ clientId, time: new Date().toISOString() })}\n\n`);

    // Keep connection alive with heartbeat comment every 25 seconds
    const heartbeatTimer = setInterval(() => {
      res.write(': heartbeat\n\n');
    }, 25000);

    req.on('close', () => {
      clearInterval(heartbeatTimer);
      sseClients = sseClients.filter((c) => c.id !== clientId);
    });
  });

  // Update a single cell in a timetable
  app.post('/api/timetable/cell', (req: Request, res: Response) => {
    const { classId, effectiveDate, slotKey, cell } = req.body;

    if (!classId || !effectiveDate || !slotKey) {
      return res.status(400).json({ error: 'Missing required parameters' });
    }

    let schedule = database.schedules.find(
      (s) => s.classId === classId && s.effectiveDate === effectiveDate
    );

    if (!schedule) {
      schedule = {
        id: `schedule_${classId.replace(/\s+/g, '_')}_${effectiveDate.replace(/\//g, '_')}`,
        classId,
        effectiveDate,
        cells: {},
        updatedAt: new Date().toISOString(),
      };
      database.schedules.push(schedule);
    }

    schedule.cells[slotKey] = cell;
    schedule.updatedAt = new Date().toISOString();
    database.lastUpdated = schedule.updatedAt;

    // Add teacher or class if new
    if (cell.teacher && !database.teachers.includes(cell.teacher.trim())) {
      database.teachers.push(cell.teacher.trim());
    }
    if (!database.classes.includes(classId)) {
      database.classes.push(classId);
    }
    if (!database.effectiveDates.includes(effectiveDate)) {
      database.effectiveDates.unshift(effectiveDate);
    }

    saveDatabaseToDisk();

    // Broadcast real-time change to all other tabs/users!
    broadcastRealtimeEvent('cell_updated', {
      classId,
      effectiveDate,
      slotKey,
      cell,
      updatedAt: schedule.updatedAt,
    });

    res.json({ success: true, schedule });
  });

  // Sync / Import database or schedules
  app.post('/api/timetable/sync', (req: Request, res: Response) => {
    const incomingData: Partial<SchoolDatabase> = req.body;

    if (!incomingData.schedules) {
      return res.status(400).json({ error: 'schedules array required' });
    }

    // Merge or replace schedules
    const existingMap = new Map(database.schedules.map((s) => [`${s.classId}_${s.effectiveDate}`, s]));

    incomingData.schedules.forEach((newSch) => {
      const key = `${newSch.classId}_${newSch.effectiveDate}`;
      existingMap.set(key, {
        ...newSch,
        updatedAt: new Date().toISOString(),
      });
    });

    database.schedules = Array.from(existingMap.values());

    if (incomingData.classes) {
      database.classes = Array.from(new Set([...database.classes, ...incomingData.classes]));
    }
    if (incomingData.teachers) {
      database.teachers = Array.from(new Set([...database.teachers, ...incomingData.teachers]));
    }
    if (incomingData.effectiveDates) {
      database.effectiveDates = Array.from(new Set([...incomingData.effectiveDates, ...database.effectiveDates]));
    }

    database.lastUpdated = new Date().toISOString();
    saveDatabaseToDisk();

    // Broadcast sync to everyone
    broadcastRealtimeEvent('database_synced', {
      database,
      updatedAt: database.lastUpdated,
    });

    res.json({ success: true, database });
  });

  // Reset database to default
  app.post('/api/timetable/reset', (req: Request, res: Response) => {
    database = {
      ...INITIAL_DATABASE,
      lastUpdated: new Date().toISOString(),
    };
    saveDatabaseToDisk();

    broadcastRealtimeEvent('database_synced', {
      database,
      updatedAt: database.lastUpdated,
    });

    res.json({ success: true, database });
  });

  // Vite middleware for development or static serving for production
  if (process.env.NODE_ENV !== 'production') {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: 'spa',
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(process.cwd(), 'dist');
    app.use(express.static(distPath));
    app.get('*', (req: Request, res: Response) => {
      res.sendFile(path.join(distPath, 'index.html'));
    });
  }

  app.listen(PORT, '0.0.0.0', () => {
    console.log(`Timetable server running on http://0.0.0.0:${PORT}`);
  });
}

startServer();
