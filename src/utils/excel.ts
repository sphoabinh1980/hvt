import * as XLSX from 'xlsx';
import { SchoolDatabase, TimetableData, TimetableCell, DAYS_OF_WEEK } from '../types';

export interface ParseExcelResult {
  success: boolean;
  message: string;
  importedCount: number;
  newClasses: string[];
  newTeachers: string[];
  newDates: string[];
  schedules: TimetableData[];
}

/**
 * Xuất Thời khóa biểu của Lớp hiện tại ra file .xlsx
 */
export function exportClassScheduleToExcel(
  schedule: TimetableData | undefined,
  className: string,
  effectiveDate: string
) {
  const wb = XLSX.utils.book_new();

  const rows: (string | number)[][] = [
    [`THỜI KHÓA BIỂU CỦA LỚP: ${className}`],
    [`Ngày áp dụng: ${effectiveDate}`],
    [],
    ['BUỔI', 'TIẾT', 'THỨ 2', 'THỨ 3', 'THỨ 4', 'THỨ 5', 'THỨ 6', 'THỨ 7'],
  ];

  // Buổi Sáng: Tiết 1 - 5
  for (let p = 1; p <= 5; p++) {
    const row: (string | number)[] = [p === 1 ? 'SÁNG' : '', p];
    for (const d of DAYS_OF_WEEK) {
      const cell = schedule?.cells[`sang_all_${p}_${d.key}`];
      if (cell && (cell.subject || cell.teacher)) {
        row.push(cell.teacher ? `${cell.subject}\n(${cell.teacher})` : cell.subject);
      } else {
        row.push('');
      }
    }
    rows.push(row);
  }

  // Buổi Chiều: Tuần chẵn
  for (let p = 1; p <= 2; p++) {
    const row: (string | number)[] = [p === 1 ? 'CHIỀU (Tuần chẵn)' : '', p];
    for (const d of DAYS_OF_WEEK) {
      const cell = schedule?.cells[`chieu_chan_${p}_${d.key}`];
      if (cell && (cell.subject || cell.teacher)) {
        row.push(cell.teacher ? `${cell.subject}\n(${cell.teacher})` : cell.subject);
      } else {
        row.push('');
      }
    }
    rows.push(row);
  }

  // Buổi Chiều: Tuần lẻ
  for (let p = 1; p <= 2; p++) {
    const row: (string | number)[] = [p === 1 ? 'CHIỀU (Tuần lẻ)' : '', p];
    for (const d of DAYS_OF_WEEK) {
      const cell = schedule?.cells[`chieu_le_${p}_${d.key}`];
      if (cell && (cell.subject || cell.teacher)) {
        row.push(cell.teacher ? `${cell.subject}\n(${cell.teacher})` : cell.subject);
      } else {
        row.push('');
      }
    }
    rows.push(row);
  }

  const ws = XLSX.utils.aoa_to_sheet(rows);

  // Căn chỉnh độ rộng cột
  ws['!cols'] = [
    { wch: 18 }, // Buổi
    { wch: 8 },  // Tiết
    { wch: 14 }, // Thứ 2
    { wch: 14 }, // Thứ 3
    { wch: 14 }, // Thứ 4
    { wch: 14 }, // Thứ 5
    { wch: 14 }, // Thứ 6
    { wch: 14 }, // Thứ 7
  ];

  XLSX.utils.book_append_sheet(wb, ws, `TKB_${className.replace(/\s+/g, '_')}`);
  const fileName = `TKB_Lop_${className.replace(/\s+/g, '_')}_${effectiveDate.replace(/\//g, '-')}.xlsx`;
  XLSX.writeFile(wb, fileName);
}

/**
 * Xuất Thời khóa biểu của Giáo viên hiện tại ra file .xlsx
 */
export function exportTeacherScheduleToExcel(
  teacherName: string,
  effectiveDate: string,
  schedules: TimetableData[]
) {
  const wb = XLSX.utils.book_new();

  const rows: (string | number)[][] = [
    [`THỜI KHÓA BIỂU CỦA GIÁO VIÊN: ${teacherName}`],
    [`Ngày áp dụng: ${effectiveDate}`],
    [],
    ['BUỔI', 'TIẾT', 'THỨ 2', 'THỨ 3', 'THỨ 4', 'THỨ 5', 'THỨ 6', 'THỨ 7'],
  ];

  // Helper tìm tiết dạy của giáo viên
  const getTeacherSlot = (slotKey: string) => {
    const matches: string[] = [];
    for (const sch of schedules) {
      if (sch.effectiveDate === effectiveDate) {
        const cell = sch.cells[slotKey];
        if (cell && cell.teacher && cell.teacher.trim().toLowerCase() === teacherName.trim().toLowerCase()) {
          matches.push(`${sch.classId}${cell.subject ? ` (${cell.subject})` : ''}`);
        }
      }
    }
    return matches.join('\n');
  };

  // Buổi Sáng
  for (let p = 1; p <= 5; p++) {
    const row: (string | number)[] = [p === 1 ? 'SÁNG' : '', p];
    for (const d of DAYS_OF_WEEK) {
      row.push(getTeacherSlot(`sang_all_${p}_${d.key}`));
    }
    rows.push(row);
  }

  // Buổi Chiều - Tuần chẵn
  for (let p = 1; p <= 2; p++) {
    const row: (string | number)[] = [p === 1 ? 'CHIỀU (Tuần chẵn)' : '', p];
    for (const d of DAYS_OF_WEEK) {
      row.push(getTeacherSlot(`chieu_chan_${p}_${d.key}`));
    }
    rows.push(row);
  }

  // Buổi Chiều - Tuần lẻ
  for (let p = 1; p <= 2; p++) {
    const row: (string | number)[] = [p === 1 ? 'CHIỀU (Tuần lẻ)' : '', p];
    for (const d of DAYS_OF_WEEK) {
      row.push(getTeacherSlot(`chieu_le_${p}_${d.key}`));
    }
    rows.push(row);
  }

  const ws = XLSX.utils.aoa_to_sheet(rows);
  ws['!cols'] = [
    { wch: 18 },
    { wch: 8 },
    { wch: 16 },
    { wch: 16 },
    { wch: 16 },
    { wch: 16 },
    { wch: 16 },
    { wch: 16 },
  ];

  XLSX.utils.book_append_sheet(wb, ws, `GV_${teacherName.replace(/\s+/g, '_')}`);
  const fileName = `TKB_GiaoVien_${teacherName.replace(/\s+/g, '_')}_${effectiveDate.replace(/\//g, '-')}.xlsx`;
  XLSX.writeFile(wb, fileName);
}

/**
 * Xuất Toàn bộ thời khóa biểu ra file Excel đa sheet (hoặc dạng bảng dữ liệu tổng hợp)
 */
export function exportAllSchedulesToExcel(database: SchoolDatabase, effectiveDate: string) {
  const wb = XLSX.utils.book_new();

  // 1. Sheet Tổng hợp (Data Table)
  const masterRows: (string | number)[][] = [
    ['Ngày áp dụng', 'Lớp', 'Buổi', 'Tiết', 'Loại tuần', 'Thứ', 'Môn học', 'Giáo viên', 'Phòng học'],
  ];

  const dateSchedules = database.schedules.filter((s) => s.effectiveDate === effectiveDate);

  for (const sch of dateSchedules) {
    for (const [key, cell] of Object.entries(sch.cells)) {
      if (!cell || (!cell.subject && !cell.teacher)) continue;
      const parts = key.split('_'); // [session, weekType, period, day]
      if (parts.length === 4) {
        const session = parts[0] === 'sang' ? 'Sáng' : 'Chiều';
        const weekType = parts[1] === 'chan' ? 'Tuần chẵn' : parts[1] === 'le' ? 'Tuần lẻ' : 'Tất cả';
        const period = parts[2];
        const day = `Thứ ${parts[3]}`;
        masterRows.push([
          sch.effectiveDate,
          sch.classId,
          session,
          period,
          weekType,
          day,
          cell.subject || '',
          cell.teacher || '',
          cell.room || '',
        ]);
      }
    }
  }

  const wsMaster = XLSX.utils.aoa_to_sheet(masterRows);
  XLSX.utils.book_append_sheet(wb, wsMaster, 'TongHopDuLieu');

  // 2. Tạo sheet riêng cho từng lớp
  for (const sch of dateSchedules) {
    const rows: (string | number)[][] = [
      [`THỜI KHÓA BIỂU LỚP: ${sch.classId}`],
      [`Ngày áp dụng: ${effectiveDate}`],
      [],
      ['BUỔI', 'TIẾT', 'THỨ 2', 'THỨ 3', 'THỨ 4', 'THỨ 5', 'THỨ 6', 'THỨ 7'],
    ];

    for (let p = 1; p <= 5; p++) {
      const row: (string | number)[] = [p === 1 ? 'SÁNG' : '', p];
      for (const d of DAYS_OF_WEEK) {
        const cell = sch.cells[`sang_all_${p}_${d.key}`];
        row.push(cell && (cell.subject || cell.teacher) ? `${cell.subject}\n(${cell.teacher})` : '');
      }
      rows.push(row);
    }

    for (let p = 1; p <= 2; p++) {
      const row: (string | number)[] = [p === 1 ? 'CHIỀU (Tuần chẵn)' : '', p];
      for (const d of DAYS_OF_WEEK) {
        const cell = sch.cells[`chieu_chan_${p}_${d.key}`];
        row.push(cell && (cell.subject || cell.teacher) ? `${cell.subject}\n(${cell.teacher})` : '');
      }
      rows.push(row);
    }

    for (let p = 1; p <= 2; p++) {
      const row: (string | number)[] = [p === 1 ? 'CHIỀU (Tuần lẻ)' : '', p];
      for (const d of DAYS_OF_WEEK) {
        const cell = sch.cells[`chieu_le_${p}_${d.key}`];
        row.push(cell && (cell.subject || cell.teacher) ? `${cell.subject}\n(${cell.teacher})` : '');
      }
      rows.push(row);
    }

    const ws = XLSX.utils.aoa_to_sheet(rows);
    const sheetTitle = sch.classId.replace(/[\\/*?:[\]]/g, '_').substring(0, 31);
    XLSX.utils.book_append_sheet(wb, ws, sheetTitle);
  }

  const fileName = `ToanBo_TKB_${effectiveDate.replace(/\//g, '-')}.xlsx`;
  XLSX.writeFile(wb, fileName);
}

/**
 * Tải file mẫu Excel chuẩn (.xlsx) để người dùng điền và tải lên
 */
export function downloadExcelTemplate() {
  const wb = XLSX.utils.book_new();

  // Mẫu 1: Định dạng bảng thời khóa biểu lớp (Dễ nhìn giống giao diện)
  const templateClassRows: (string | number)[][] = [
    ['THỜI KHÓA BIỂU CỦA LỚP: 10 Lý'],
    ['Ngày áp dụng: 06/09/2026'],
    ['Hướng dẫn: Dòng trên là tên Môn học, dòng dưới trong ngoặc là tên Giáo viên (Ví dụ: TrNg \\n (Ngân))'],
    ['BUỔI', 'TIẾT', 'THỨ 2', 'THỨ 3', 'THỨ 4', 'THỨ 5', 'THỨ 6', 'THỨ 7'],
    ['SÁNG', 1, 'TrNg\n(Ngân)', 'GDTC', 'L\n(MLoan)', 'T\n(nttHương)', 'L\n(MLoan)', 'H\n(H.Lan)'],
    ['', 2, 'TrNg\n(Ngân)', 'A\n(Đ.Mai)', 'L\n(MLoan)', 'T\n(nttHương)', 'TN\n(Dũng)', 'A\n(Đ.Mai)'],
    ['', 3, 'S\n(Ngân)', 'L\n(MLoan)', 'V\n(C.NHUNG)', 'S\n(Ngân)', 'GDTC', 'GDĐP\n(Ninh)'],
    ['', 4, 'TN\n(Dũng)', 'L\n(MLoan)', 'V\n(C.NHUNG)', 'H\n(H.Lan)', 'T\n(nttHương)', 'SU\n(Hạnh(T))'],
    ['', 5, 'A\n(Đ.Mai)', '', 'GDQP\n(Hảo)', 'H\n(H.Lan)', 'T\n(nttHương)', 'V\n(C.NHUNG)'],
    ['CHIỀU (Tuần chẵn)', 1, 'Nângcao', 'Nângcao', 'Nângcao', 'Nângcao', 'Nângcao', ''],
    ['', 2, 'TrNg\n(nttHương)', 'Nângcao', 'Nângcao', 'Nângcao', 'Nângcao', ''],
    ['CHIỀU (Tuần lẻ)', 1, '', '', '', '', '', ''],
    ['', 2, '', '', '', '', '', ''],
  ];

  const ws1 = XLSX.utils.aoa_to_sheet(templateClassRows);
  ws1['!cols'] = [
    { wch: 18 },
    { wch: 8 },
    { wch: 15 },
    { wch: 15 },
    { wch: 15 },
    { wch: 15 },
    { wch: 15 },
    { wch: 15 },
  ];
  XLSX.utils.book_append_sheet(wb, ws1, 'Mau_TKB_Lop');

  // Mẫu 2: Định dạng bảng dữ liệu tổng hợp (Rất tiện để import nhiều lớp/ngày cùng lúc)
  const templateDataRows: (string | number)[][] = [
    ['Ngày áp dụng', 'Lớp', 'Buổi', 'Tiết', 'Loại tuần', 'Thứ', 'Môn học', 'Giáo viên', 'Phòng học'],
    ['06/09/2026', '10 Tin', 'Sáng', 1, 'Tất cả', 'Thứ 2', 'T', 'nttHương', 'P.101'],
    ['06/09/2026', '10 Tin', 'Sáng', 2, 'Tất cả', 'Thứ 2', 'TN', 'Dũng', 'Lab 1'],
    ['06/09/2026', '10 Tin', 'Sáng', 3, 'Tất cả', 'Thứ 2', 'V', 'C.NHUNG', 'P.101'],
    ['06/09/2026', '10 Tin', 'Sáng', 4, 'Tất cả', 'Thứ 2', 'A', 'Đ.Mai', 'P.101'],
    ['06/09/2026', '10 Tin', 'Sáng', 5, 'Tất cả', 'Thứ 2', 'GDTC', 'Tuấn(GDTC)', 'Sân'],
    ['06/09/2026', '10 Tin', 'Chiều', 1, 'Tuần chẵn', 'Thứ 3', 'Nângcao', 'Dũng', 'Lab 1'],
  ];

  const ws2 = XLSX.utils.aoa_to_sheet(templateDataRows);
  ws2['!cols'] = [
    { wch: 14 },
    { wch: 12 },
    { wch: 10 },
    { wch: 8 },
    { wch: 12 },
    { wch: 10 },
    { wch: 14 },
    { wch: 14 },
    { wch: 12 },
  ];
  XLSX.utils.book_append_sheet(wb, ws2, 'Mau_DanhSach_ChiTiet');

  XLSX.writeFile(wb, 'Mau_Thoi_Khoa_Bieu.xlsx');
}

/**
 * Đọc và phân tích file Excel (.xlsx / .xls) do người dùng tải lên
 */
export async function parseExcelFile(file: File): Promise<ParseExcelResult> {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();

    reader.onload = (e) => {
      try {
        const data = new Uint8Array(e.target?.result as ArrayBuffer);
        const workbook = XLSX.read(data, { type: 'array' });

        const importedSchedules: TimetableData[] = [];
        const newClassesSet = new Set<string>();
        const newTeachersSet = new Set<string>();
        const newDatesSet = new Set<string>();

        // Duyệt qua tất cả các sheet
        for (const sheetName of workbook.SheetNames) {
          const sheet = workbook.Sheets[sheetName];
          const rawRows: any[][] = XLSX.utils.sheet_to_json(sheet, { header: 1, defval: '' });

          if (!rawRows || rawRows.length === 0) continue;

          // Kiểm tra xem sheet có phải là dạng danh sách tổng hợp (có header "Ngày áp dụng" hoặc "Lớp")
          const headerRowIdx = rawRows.findIndex(
            (r) =>
              Array.isArray(r) &&
              r.some((c) => typeof c === 'string' && (c.toLowerCase().includes('ngày áp dụng') || c.toLowerCase().includes('lớp')))
          );

          if (headerRowIdx !== -1 && rawRows[headerRowIdx].some((c: any) => typeof c === 'string' && c.toLowerCase().includes('môn'))) {
            // Định dạng Bảng danh sách chi tiết (Mau_DanhSach_ChiTiet)
            const headers = rawRows[headerRowIdx].map((h: any) => String(h).trim().toLowerCase());
            const colDate = headers.findIndex((h) => h.includes('ngày'));
            const colClass = headers.findIndex((h) => h.includes('lớp'));
            const colSession = headers.findIndex((h) => h.includes('buổi'));
            const colPeriod = headers.findIndex((h) => h.includes('tiết'));
            const colWeekType = headers.findIndex((h) => h.includes('tuần'));
            const colDay = headers.findIndex((h) => h.includes('thứ'));
            const colSubject = headers.findIndex((h) => h.includes('môn'));
            const colTeacher = headers.findIndex((h) => h.includes('giáo viên') || h.includes('gv'));
            const colRoom = headers.findIndex((h) => h.includes('phòng'));

            const groupedBySchedule: Record<string, TimetableData> = {};

            for (let i = headerRowIdx + 1; i < rawRows.length; i++) {
              const row = rawRows[i];
              if (!row || row.length === 0) continue;

              const dateVal = String(row[colDate] || '').trim();
              const classVal = String(row[colClass] || '').trim();
              if (!dateVal || !classVal) continue;

              newDatesSet.add(dateVal);
              newClassesSet.add(classVal);

              const schKey = `${classVal}_${dateVal}`;
              if (!groupedBySchedule[schKey]) {
                groupedBySchedule[schKey] = {
                  id: `schedule_${classVal.replace(/\s+/g, '_')}_${dateVal.replace(/\//g, '_')}`,
                  effectiveDate: dateVal,
                  classId: classVal,
                  cells: {},
                  updatedAt: new Date().toISOString(),
                };
              }

              const sessionVal = String(row[colSession] || '').toLowerCase().includes('chiều') ? 'chieu' : 'sang';
              const periodVal = parseInt(String(row[colPeriod] || '1'), 10) || 1;
              const weekTypeVal = String(row[colWeekType] || '').toLowerCase().includes('chẵn')
                ? 'chan'
                : String(row[colWeekType] || '').toLowerCase().includes('lẻ')
                ? 'le'
                : 'all';

              // Phân tích Thứ (VD: "Thứ 2", "2", "Thu 3")
              const dayStr = String(row[colDay] || '');
              const dayMatch = dayStr.match(/([2-7])/);
              const dayVal = dayMatch ? (parseInt(dayMatch[1], 10) as 2 | 3 | 4 | 5 | 6 | 7) : 2;

              const subjectVal = String(row[colSubject] || '').trim();
              const teacherVal = String(row[colTeacher] || '').trim();
              const roomVal = colRoom !== -1 ? String(row[colRoom] || '').trim() : '';

              if (teacherVal) newTeachersSet.add(teacherVal);

              const slotKey = `${sessionVal}_${weekTypeVal}_${periodVal}_${dayVal}`;
              groupedBySchedule[schKey].cells[slotKey] = {
                subject: subjectVal,
                teacher: teacherVal,
                room: roomVal,
              };
            }

            Object.values(groupedBySchedule).forEach((sch) => importedSchedules.push(sch));
          } else {
            // Định dạng theo bảng mẫu lưới (Thời khóa biểu của lớp như mẫu ảnh chụp)
            let detectedClass = '';
            let detectedDate = '';

            // Tìm thông tin lớp và ngày áp dụng trong các dòng đầu
            for (let i = 0; i < Math.min(rawRows.length, 6); i++) {
              const fullRowText = rawRows[i].map((c) => String(c)).join(' ');
              const classMatch = fullRowText.match(/(?:lớp|của lớp)[:\s]+([^\n\r,\.]+)/i);
              if (classMatch && !detectedClass) {
                detectedClass = classMatch[1].trim();
              }
              const dateMatch = fullRowText.match(/(?:ngày áp dụng|áp dụng từ)[:\s]+([0-9]{1,2}[\/-][0-9]{1,2}[\/-][0-9]{2,4})/i);
              if (dateMatch && !detectedDate) {
                detectedDate = dateMatch[1].trim().replace(/-/g, '/');
              }
            }

            if (!detectedClass) {
              // Thử lấy từ tên sheet
              detectedClass = sheetName.replace(/^(?:TKB_|Mau_TKB_)/i, '').trim() || 'Lớp nhập';
            }
            if (!detectedDate) {
              detectedDate = '06/09/2026';
            }

            newClassesSet.add(detectedClass);
            newDatesSet.add(detectedDate);

            const cells: Record<string, TimetableCell> = {};

            // Tìm dòng header Thứ (Thứ 2, Thứ 3...)
            const thuRowIdx = rawRows.findIndex(
              (r) => Array.isArray(r) && r.some((c) => typeof c === 'string' && c.toUpperCase().includes('THỨ 2'))
            );

            if (thuRowIdx !== -1) {
              const headerRow = rawRows[thuRowIdx].map((c) => String(c).toUpperCase());
              const colThumap: Record<number, number> = {}; // day -> colIndex
              DAYS_OF_WEEK.forEach((d) => {
                const idx = headerRow.findIndex((c) => c.includes(`THỨ ${d.key}`) || c.includes(`T${d.key}`));
                if (idx !== -1) colThumap[d.key] = idx;
              });

              let currentSession: 'sang' | 'chieu' = 'sang';
              let currentWeekType: 'all' | 'chan' | 'le' = 'all';

              for (let r = thuRowIdx + 1; r < rawRows.length; r++) {
                const row = rawRows[r];
                if (!row || row.length === 0) continue;

                const col0 = String(row[0] || '').toUpperCase();
                const col1 = String(row[1] || '').trim();

                if (col0.includes('SÁNG') || col0.includes('SANG')) {
                  currentSession = 'sang';
                  currentWeekType = 'all';
                } else if (col0.includes('CHIỀU') || col0.includes('CHIEU')) {
                  currentSession = 'chieu';
                  if (col0.includes('CHẴN') || col0.includes('CHAN')) {
                    currentWeekType = 'chan';
                  } else if (col0.includes('LẺ') || col0.includes('LE')) {
                    currentWeekType = 'le';
                  }
                }

                const periodMatch = col1.match(/\d+/);
                const period = periodMatch ? parseInt(periodMatch[0], 10) : 1;

                // Đọc các ô Thứ
                for (const d of DAYS_OF_WEEK) {
                  const colIdx = colThumap[d.key];
                  if (colIdx !== undefined && row[colIdx]) {
                    const rawVal = String(row[colIdx]).trim();
                    if (rawVal) {
                      // Phân tích Môn và Giáo viên
                      // Hỗ trợ: "TrNg\nNgân", "TrNg (Ngân)", "TrNg/Ngân"
                      let subject = rawVal;
                      let teacher = '';

                      if (rawVal.includes('\n')) {
                        const lines = rawVal.split('\n').map((l) => l.trim()).filter(Boolean);
                        subject = lines[0] || '';
                        teacher = lines[1] ? lines[1].replace(/[()]/g, '').trim() : '';
                      } else if (rawVal.includes('(') && rawVal.endsWith(')')) {
                        const m = rawVal.match(/^(.*?)\((.*?)\)$/);
                        if (m) {
                          subject = m[1].trim();
                          teacher = m[2].trim();
                        }
                      } else if (rawVal.includes('/')) {
                        const parts = rawVal.split('/');
                        subject = parts[0].trim();
                        teacher = parts[1].trim();
                      }

                      if (teacher) newTeachersSet.add(teacher);

                      const slotKey = `${currentSession}_${currentWeekType}_${period}_${d.key}`;
                      cells[slotKey] = {
                        subject,
                        teacher,
                      };
                    }
                  }
                }
              }

              if (Object.keys(cells).length > 0) {
                importedSchedules.push({
                  id: `schedule_${detectedClass.replace(/\s+/g, '_')}_${detectedDate.replace(/\//g, '_')}`,
                  effectiveDate: detectedDate,
                  classId: detectedClass,
                  cells,
                  updatedAt: new Date().toISOString(),
                });
              }
            }
          }
        }

        if (importedSchedules.length === 0) {
          resolve({
            success: false,
            message: 'Không tìm thấy dữ liệu thời khóa biểu hợp lệ trong file Excel.',
            importedCount: 0,
            newClasses: [],
            newTeachers: [],
            newDates: [],
            schedules: [],
          });
          return;
        }

        resolve({
          success: true,
          message: `Đã nhập thành công ${importedSchedules.length} thời khóa biểu từ file Excel!`,
          importedCount: importedSchedules.length,
          newClasses: Array.from(newClassesSet),
          newTeachers: Array.from(newTeachersSet),
          newDates: Array.from(newDatesSet),
          schedules: importedSchedules,
        });
      } catch (err: any) {
        reject(new Error(`Lỗi khi đọc file Excel: ${err.message}`));
      }
    };

    reader.onerror = () => reject(new Error('Không thể đọc tệp tin'));
    reader.readAsArrayBuffer(file);
  });
}
