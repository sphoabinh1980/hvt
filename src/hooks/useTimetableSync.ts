import { useState, useEffect, useCallback, useRef } from 'react';
import { SchoolDatabase, TimetableData, TimetableCell } from '../types';
import { INITIAL_DATABASE } from '../defaultData';
import { ToastMessage } from '../components/SyncToast';

const STORAGE_KEY = 'school_timetable_db_v1';

export function useTimetableSync() {
  const [database, setDatabase] = useState<SchoolDatabase>(() => {
    try {
      const cached = localStorage.getItem(STORAGE_KEY);
      if (cached) {
        const parsed = JSON.parse(cached);
        if (parsed && Array.isArray(parsed.schedules) && parsed.schedules.length > 0) {
          return parsed;
        }
      }
    } catch (e) {
      console.warn('Could not read from localStorage:', e);
    }
    return INITIAL_DATABASE;
  });

  const [isRealtimeConnected, setIsRealtimeConnected] = useState(false);
  const [toast, setToast] = useState<ToastMessage | null>(null);
  const eventSourceRef = useRef<EventSource | null>(null);
  const broadcastChannelRef = useRef<BroadcastChannel | null>(null);

  // Save to localStorage whenever database changes
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(database));
    } catch (e) {
      console.warn('Failed to cache in localStorage:', e);
    }
  }, [database]);

  // Initial Fetch from server API
  const fetchFromServer = useCallback(async () => {
    try {
      const res = await fetch('/api/timetable');
      if (res.ok) {
        const data: SchoolDatabase = await res.json();
        if (data && Array.isArray(data.schedules) && data.schedules.length > 0) {
          setDatabase(data);
        }
      }
    } catch (err) {
      console.log('Server not reached yet or offline, working with local cache:', err);
    }
  }, []);

  // Connect to SSE stream and BroadcastChannel
  useEffect(() => {
    fetchFromServer();

    // 1. Cross-tab Broadcast Channel
    if (typeof BroadcastChannel !== 'undefined') {
      const bc = new BroadcastChannel('timetable_channel');
      broadcastChannelRef.current = bc;
      bc.onmessage = (event) => {
        if (event.data?.type === 'SYNC_DATABASE') {
          setDatabase(event.data.database);
          setToast({
            id: String(Date.now()),
            title: 'Đồng Bộ Trực Tiếp',
            description: 'Dữ liệu thời khóa biểu vừa được cập nhật từ một tab khác!',
          });
        }
      };
    }

    // 2. Server-Sent Events (SSE)
    const connectSSE = () => {
      try {
        const es = new EventSource('/api/events');
        eventSourceRef.current = es;

        es.addEventListener('connected', () => {
          setIsRealtimeConnected(true);
        });

        es.addEventListener('cell_updated', (e: MessageEvent) => {
          try {
            const payload = JSON.parse(e.data);
            const { classId, effectiveDate, slotKey, cell, updatedAt } = payload;

            setDatabase((prev) => {
              const updatedSchedules = [...prev.schedules];
              const idx = updatedSchedules.findIndex(
                (s) => s.classId === classId && s.effectiveDate === effectiveDate
              );

              if (idx !== -1) {
                updatedSchedules[idx] = {
                  ...updatedSchedules[idx],
                  cells: {
                    ...updatedSchedules[idx].cells,
                    [slotKey]: cell,
                  },
                  updatedAt,
                };
              } else {
                updatedSchedules.push({
                  id: `schedule_${classId.replace(/\s+/g, '_')}_${effectiveDate.replace(/\//g, '_')}`,
                  classId,
                  effectiveDate,
                  cells: { [slotKey]: cell },
                  updatedAt,
                });
              }

              return {
                ...prev,
                schedules: updatedSchedules,
                lastUpdated: updatedAt,
              };
            });

            setToast({
              id: String(Date.now()),
              title: 'Cập Nhật Thời Gian Thực',
              description: `Tiết học lớp ${classId} vừa được cập nhật (${cell.subject || 'Trống'} - ${cell.teacher || ''})`,
            });
          } catch (err) {
            console.error('Error handling cell_updated event:', err);
          }
        });

        es.addEventListener('database_synced', (e: MessageEvent) => {
          try {
            const payload = JSON.parse(e.data);
            if (payload?.database) {
              setDatabase(payload.database);
              setToast({
                id: String(Date.now()),
                title: 'Đồng Bộ Hệ Thống',
                description: 'Toàn bộ thời khóa biểu vừa được cập nhật qua máy chủ!',
              });
            }
          } catch (err) {
            console.error('Error handling database_synced event:', err);
          }
        });

        es.onopen = () => {
          setIsRealtimeConnected(true);
        };

        es.onerror = () => {
          setIsRealtimeConnected(false);
          es.close();
          // Retry connecting in 5 seconds
          setTimeout(connectSSE, 5000);
        };
      } catch (err) {
        console.warn('SSE connection error:', err);
        setIsRealtimeConnected(false);
      }
    };

    connectSSE();

    return () => {
      eventSourceRef.current?.close();
      broadcastChannelRef.current?.close();
    };
  }, [fetchFromServer]);

  // Cập nhật 1 ô (slot)
  const updateCell = useCallback(
    async (classId: string, effectiveDate: string, slotKey: string, cell: TimetableCell) => {
      const now = new Date().toISOString();

      // Cập nhật lạc quan (Optimistic Update)
      setDatabase((prev) => {
        const updatedSchedules = [...prev.schedules];
        const idx = updatedSchedules.findIndex(
          (s) => s.classId === classId && s.effectiveDate === effectiveDate
        );

        if (idx !== -1) {
          const newCells = { ...updatedSchedules[idx].cells };
          if (!cell.subject && !cell.teacher) {
            delete newCells[slotKey];
          } else {
            newCells[slotKey] = cell;
          }
          updatedSchedules[idx] = {
            ...updatedSchedules[idx],
            cells: newCells,
            updatedAt: now,
          };
        } else {
          updatedSchedules.push({
            id: `schedule_${classId.replace(/\s+/g, '_')}_${effectiveDate.replace(/\//g, '_')}`,
            classId,
            effectiveDate,
            cells: { [slotKey]: cell },
            updatedAt: now,
          });
        }

        const newTeachers = cell.teacher && !prev.teachers.includes(cell.teacher.trim())
          ? [...prev.teachers, cell.teacher.trim()]
          : prev.teachers;

        const newClasses = !prev.classes.includes(classId)
          ? [...prev.classes, classId]
          : prev.classes;

        const updatedDb = {
          ...prev,
          classes: newClasses,
          teachers: newTeachers,
          schedules: updatedSchedules,
          lastUpdated: now,
        };

        // Gửi qua BroadcastChannel
        broadcastChannelRef.current?.postMessage({
          type: 'SYNC_DATABASE',
          database: updatedDb,
        });

        return updatedDb;
      });

      // Gửi lên server để lưu và broadcast SSE
      try {
        await fetch('/api/timetable/cell', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ classId, effectiveDate, slotKey, cell }),
        });
      } catch (err) {
        console.warn('Could not post cell update to server, preserved locally:', err);
      }
    },
    []
  );

  // Xóa 1 ô (slot)
  const deleteCell = useCallback(
    (classId: string, slotKey: string, effectiveDate: string) => {
      updateCell(classId, effectiveDate, slotKey, { subject: '', teacher: '' });
    },
    [updateCell]
  );

  // Nhập hàng loạt từ Excel
  const importSchedules = useCallback(
    async (importedSchedules: TimetableData[], newClasses: string[], newTeachers: string[], newDates: string[]) => {
      const now = new Date().toISOString();

      setDatabase((prev) => {
        const scheduleMap = new Map<string, TimetableData>(
          prev.schedules.map((s) => [`${s.classId}_${s.effectiveDate}`, s])
        );

        importedSchedules.forEach((sch) => {
          scheduleMap.set(`${sch.classId}_${sch.effectiveDate}`, {
            ...sch,
            updatedAt: now,
          });
        });

        const merged: SchoolDatabase = {
          effectiveDates: Array.from(new Set([...newDates, ...prev.effectiveDates])),
          classes: Array.from(new Set([...newClasses, ...prev.classes])),
          teachers: Array.from(new Set([...newTeachers, ...prev.teachers])),
          schedules: Array.from(scheduleMap.values()),
          lastUpdated: now,
        };

        broadcastChannelRef.current?.postMessage({
          type: 'SYNC_DATABASE',
          database: merged,
        });

        return merged;
      });

      try {
        await fetch('/api/timetable/sync', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            schedules: importedSchedules,
            classes: newClasses,
            teachers: newTeachers,
            effectiveDates: newDates,
          }),
        });
      } catch (err) {
        console.warn('Could not sync import to server:', err);
      }

      setToast({
        id: String(Date.now()),
        title: 'Nhập Excel Thành Công',
        description: `Đã nhập và đồng bộ ${importedSchedules.length} thời khóa biểu!`,
      });
    },
    []
  );

  // Khôi phục dữ liệu mặc định
  const resetToDefault = useCallback(async () => {
    setDatabase(INITIAL_DATABASE);
    try {
      await fetch('/api/timetable/reset', { method: 'POST' });
    } catch (e) {
      console.warn('Failed to reset on server:', e);
    }
    setToast({
      id: String(Date.now()),
      title: 'Đã Khôi Phục',
      description: 'Dữ liệu thời khóa biểu đã được đặt lại về mẫu ban đầu.',
    });
  }, []);

  return {
    database,
    isRealtimeConnected,
    toast,
    dismissToast: () => setToast(null),
    updateCell,
    deleteCell,
    importSchedules,
    resetToDefault,
  };
}
