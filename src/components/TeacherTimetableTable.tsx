import React from 'react';
import { DAYS_OF_WEEK, TimetableData, TimetableCell } from '../types';
import { Edit2, BookOpen, Clock } from 'lucide-react';

interface TeacherTimetableTableProps {
  teacherName: string;
  effectiveDate: string;
  schedules: TimetableData[];
  onCellClick?: (slotKey: string, cell: TimetableCell | undefined, label: string) => void;
}

export const TeacherTimetableTable: React.FC<TeacherTimetableTableProps> = ({
  teacherName,
  effectiveDate,
  schedules,
  onCellClick,
}) => {
  // Tìm tất cả các lớp mà giáo viên dạy trong slotKey cụ thể
  const getTeacherSlotData = (slotKey: string) => {
    const teachingSlots: { classId: string; subject: string; room?: string }[] = [];

    const activeSchedules = schedules.filter((s) => s.effectiveDate === effectiveDate);

    for (const sch of activeSchedules) {
      const cell = sch.cells[slotKey];
      if (
        cell &&
        cell.teacher &&
        cell.teacher.trim().toLowerCase() === teacherName.trim().toLowerCase()
      ) {
        teachingSlots.push({
          classId: sch.classId,
          subject: cell.subject,
          room: cell.room,
        });
      }
    }

    return teachingSlots;
  };

  // Tính thống kê số tiết dạy của giáo viên trong tuần
  const calculateTotalTeachingPeriods = () => {
    let count = 0;
    const taughtClasses = new Set<string>();

    const activeSchedules = schedules.filter((s) => s.effectiveDate === effectiveDate);

    for (const sch of activeSchedules) {
      for (const cell of Object.values(sch.cells)) {
        const cellData = cell as TimetableCell;
        if (
          cellData &&
          cellData.teacher &&
          cellData.teacher.trim().toLowerCase() === teacherName.trim().toLowerCase()
        ) {
          count++;
          taughtClasses.add(sch.classId);
        }
      }
    }

    return { total: count, classes: Array.from(taughtClasses) };
  };

  const stats = calculateTotalTeachingPeriods();

  const renderCellContent = (slotKey: string, cellLabel: string) => {
    const slots = getTeacherSlotData(slotKey);
    const hasTeaching = slots.length > 0;

    return (
      <td
        key={slotKey}
        onClick={() => {
          const firstSlot = slots[0];
          const cellData: TimetableCell = firstSlot
            ? { subject: firstSlot.subject, teacher: teacherName, className: firstSlot.classId, room: firstSlot.room }
            : { subject: '', teacher: teacherName };
          onCellClick?.(slotKey, cellData, cellLabel);
        }}
        className="border border-slate-200 text-center p-1.5 h-16 cursor-pointer hover:bg-slate-100/60 transition-colors group relative select-none"
        title={hasTeaching ? 'Đang có tiết dạy (nhấp để sửa)' : 'Trống tiết (nhấp để xếp lịch)'}
      >
        {hasTeaching ? (
          <div className="h-full w-full bg-blue-50 border-l-4 border-blue-500 p-2 rounded text-left flex flex-col justify-center min-h-[46px] shadow-2xs">
            {slots.map((item, i) => (
              <div key={i} className="flex flex-col">
                <div className="flex items-center justify-between gap-1">
                  <span className="font-bold text-blue-900 text-xs tracking-tight">
                    Lớp {item.classId}
                  </span>
                  {item.room && (
                    <span className="text-[10px] text-slate-500 font-normal italic">
                      {item.room}
                    </span>
                  )}
                </div>
                {item.subject && (
                  <span className="text-blue-700 font-medium text-[11px] opacity-90 truncate mt-0.5">
                    Môn: <strong>{item.subject}</strong>
                  </span>
                )}
              </div>
            ))}
          </div>
        ) : (
          <div className="h-full min-h-[46px] flex items-center justify-center text-slate-300 group-hover:text-slate-400">
            <span className="text-[11px] text-slate-300 italic group-hover:hidden">Trống</span>
            <span className="text-xs font-light hidden group-hover:inline text-blue-600 font-bold">+</span>
          </div>
        )}

        <div className="absolute top-1 right-1 opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none">
          <Edit2 className="w-3 h-3 text-slate-400" />
        </div>
      </td>
    );
  };

  return (
    <div className="w-full bg-white rounded-lg shadow-xs border border-slate-200 overflow-hidden">
      {/* Title Header matching Professional Polish layout */}
      <div className="p-4 sm:p-6 pb-4 border-b border-slate-200/80">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <h2 className="text-xl sm:text-2xl font-bold tracking-tight text-slate-900 uppercase">
              THỜI KHÓA BIỂU CỦA GIÁO VIÊN
            </h2>
            <div className="flex flex-wrap items-center gap-3 text-xs sm:text-sm text-slate-600 mt-1">
              <span>
                Giáo viên: <strong className="text-blue-700 font-semibold">{teacherName}</strong>
              </span>
              <span className="text-slate-300">•</span>
              <span>
                Ngày áp dụng: <strong className="text-slate-800">{effectiveDate}</strong>
              </span>
            </div>
          </div>

          {/* Quick Statistics */}
          <div className="flex items-center gap-2.5">
            <div className="flex items-center gap-1.5 px-3 py-1.5 bg-slate-50 text-slate-800 rounded-md border border-slate-200 text-xs sm:text-sm font-medium">
              <Clock className="w-4 h-4 text-blue-600" />
              <span>Tổng: <strong>{stats.total}</strong> tiết/tuần</span>
            </div>
            {stats.classes.length > 0 && (
              <div className="hidden md:flex items-center gap-1.5 px-3 py-1.5 bg-slate-50 text-slate-800 rounded-md border border-slate-200 text-xs sm:text-sm font-medium">
                <BookOpen className="w-4 h-4 text-emerald-600" />
                <span>Dạy: {stats.classes.join(', ')}</span>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Table Container */}
      <div className="p-4 sm:p-6 pt-4 overflow-x-auto">
        <table className="w-full border-collapse border border-slate-200 text-sm bg-white min-w-[720px]">
          <thead>
            <tr className="bg-slate-50 text-slate-700 border-b border-slate-200">
              <th
                colSpan={2}
                className="border border-slate-200 py-3 px-3 font-bold text-xs uppercase tracking-wider text-center w-28 text-slate-600"
              >
                BUỔI
              </th>
              <th className="border border-slate-200 py-3 px-3 font-bold text-xs uppercase tracking-wider text-center w-16 text-slate-600">
                TIẾT
              </th>
              {DAYS_OF_WEEK.map((d) => (
                <th
                  key={d.key}
                  className="border border-slate-200 py-3 px-2 font-bold text-xs uppercase tracking-wider text-center min-w-[105px] text-slate-700"
                >
                  {d.label}
                </th>
              ))}
            </tr>
          </thead>

          <tbody>
            {/* ================= BUỔI SÁNG (Tiết 1 -> Tiết 5) ================= */}
            {[1, 2, 3, 4, 5].map((period, idx) => (
              <tr key={`sang_${period}`} className="hover:bg-slate-50/50">
                {idx === 0 && (
                  <td
                    rowSpan={5}
                    colSpan={2}
                    className="border border-slate-200 bg-slate-100 text-slate-700 font-bold text-center uppercase tracking-widest select-none w-28 text-sm"
                    style={{ writingMode: 'vertical-rl', transform: 'rotate(180deg)' }}
                  >
                    SÁNG
                  </td>
                )}

                <td className="border border-slate-200 text-center font-bold text-slate-600 bg-slate-50/60 w-16 text-xs">
                  {period}
                </td>

                {DAYS_OF_WEEK.map((d) =>
                  renderCellContent(
                    `sang_all_${period}_${d.key}`,
                    `Sáng - Tiết ${period} - ${d.label}`
                  )
                )}
              </tr>
            ))}

            {/* ================= BUỔI CHIỀU ================= */}
            {/* Chiều - Tuần chẵn - Tiết 1 */}
            <tr className="hover:bg-slate-50/50">
              <td
                rowSpan={4}
                className="border border-slate-200 bg-slate-100 text-slate-700 font-bold text-center uppercase tracking-widest select-none w-14 text-sm"
                style={{ writingMode: 'vertical-rl', transform: 'rotate(180deg)' }}
              >
                CHIỀU
              </td>

              <td
                rowSpan={2}
                className="border border-slate-200 bg-slate-50 text-[11px] font-semibold text-slate-600 text-center px-1 w-14"
              >
                (Tuần chẵn)
              </td>

              <td className="border border-slate-200 text-center font-bold text-slate-600 bg-slate-50/60 w-16 text-xs">
                1
              </td>

              {DAYS_OF_WEEK.map((d) =>
                renderCellContent(
                  `chieu_chan_1_${d.key}`,
                  `Chiều (Tuần chẵn) - Tiết 1 - ${d.label}`
                )
              )}
            </tr>

            {/* Chiều - Tuần chẵn - Tiết 2 */}
            <tr className="hover:bg-slate-50/50">
              <td className="border border-slate-200 text-center font-bold text-slate-600 bg-slate-50/60 w-16 text-xs">
                2
              </td>
              {DAYS_OF_WEEK.map((d) =>
                renderCellContent(
                  `chieu_chan_2_${d.key}`,
                  `Chiều (Tuần chẵn) - Tiết 2 - ${d.label}`
                )
              )}
            </tr>

            {/* Chiều - Tuần lẻ - Tiết 1 */}
            <tr className="hover:bg-slate-50/50">
              <td
                rowSpan={2}
                className="border border-slate-200 bg-slate-50 text-[11px] font-semibold text-slate-600 text-center px-1 w-14"
              >
                (Tuần lẻ)
              </td>
              <td className="border border-slate-200 text-center font-bold text-slate-600 bg-slate-50/60 w-16 text-xs">
                1
              </td>
              {DAYS_OF_WEEK.map((d) =>
                renderCellContent(
                  `chieu_le_1_${d.key}`,
                  `Chiều (Tuần lẻ) - Tiết 1 - ${d.label}`
                )
              )}
            </tr>

            {/* Chiều - Tuần lẻ - Tiết 2 */}
            <tr className="hover:bg-slate-50/50">
              <td className="border border-slate-200 text-center font-bold text-slate-600 bg-slate-50/60 w-16 text-xs">
                2
              </td>
              {DAYS_OF_WEEK.map((d) =>
                renderCellContent(
                  `chieu_le_2_${d.key}`,
                  `Chiều (Tuần lẻ) - Tiết 2 - ${d.label}`
                )
              )}
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};
