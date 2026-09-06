import React from 'react';
import { DAYS_OF_WEEK, TimetableData, TimetableCell } from '../types';
import { Edit2, Sparkles, Clock } from 'lucide-react';

interface ClassTimetableTableProps {
  classNameValue: string;
  effectiveDate: string;
  schedule: TimetableData | undefined;
  onCellClick?: (slotKey: string, cell: TimetableCell | undefined, label: string) => void;
}

const getSubjectStyle = (subject?: string) => {
  if (!subject) {
    return {
      bg: 'bg-slate-50',
      border: 'border-slate-400',
      text: 'text-slate-900',
      teacher: 'text-slate-600',
    };
  }
  const s = subject.trim().toLowerCase();

  // Math (T, Toán)
  if (s.startsWith('t') && !s.startsWith('tin') && !s.startsWith('tn') && !s.startsWith('trng')) {
    return {
      bg: 'bg-blue-50',
      border: 'border-blue-500',
      text: 'text-blue-900',
      teacher: 'text-blue-700',
    };
  }
  // Physics (L, Lý)
  if (s.startsWith('l') && !s.includes('lịch')) {
    return {
      bg: 'bg-amber-50',
      border: 'border-amber-500',
      text: 'text-amber-900',
      teacher: 'text-amber-700',
    };
  }
  // Chemistry & Biology (H, S, Hóa, Sinh)
  if (s.startsWith('h') || (s.startsWith('s') && !s.startsWith('su') && !s.startsWith('shl'))) {
    return {
      bg: 'bg-purple-50',
      border: 'border-purple-500',
      text: 'text-purple-900',
      teacher: 'text-purple-700',
    };
  }
  // Literature (V, Văn)
  if (s.startsWith('v')) {
    return {
      bg: 'bg-rose-50',
      border: 'border-rose-500',
      text: 'text-rose-900',
      teacher: 'text-rose-700',
    };
  }
  // English (A, Anh)
  if (s.startsWith('a') || s.includes('anh')) {
    return {
      bg: 'bg-emerald-50',
      border: 'border-emerald-500',
      text: 'text-emerald-900',
      teacher: 'text-emerald-700',
    };
  }
  // IT / Computer Science (Tin, TN)
  if (s.startsWith('tin') || s === 'tn') {
    return {
      bg: 'bg-indigo-50',
      border: 'border-indigo-500',
      text: 'text-indigo-900',
      teacher: 'text-indigo-700',
    };
  }
  // History & Geography (Sử, SU, Địa, Đ)
  if (s.startsWith('su') || s.startsWith('đ') || s.startsWith('d')) {
    return {
      bg: 'bg-orange-50',
      border: 'border-orange-500',
      text: 'text-orange-900',
      teacher: 'text-orange-700',
    };
  }
  // Physical Education & Defense (GDTC, GDQP, GDĐP)
  if (s.includes('gdtc') || s.includes('gdqp') || s.includes('gdđp')) {
    return {
      bg: 'bg-teal-50',
      border: 'border-teal-500',
      text: 'text-teal-900',
      teacher: 'text-teal-700',
    };
  }
  // Activities / Meeting (TrNg, SHL, Chào cờ, Nângcao)
  if (s.includes('trng') || s.includes('shl') || s.includes('chào cờ') || s.includes('nângcao')) {
    return {
      bg: 'bg-sky-50',
      border: 'border-sky-500',
      text: 'text-sky-900',
      teacher: 'text-sky-700',
    };
  }
  return {
    bg: 'bg-slate-50',
    border: 'border-slate-400',
    text: 'text-slate-900',
    teacher: 'text-slate-600',
  };
};

export const ClassTimetableTable: React.FC<ClassTimetableTableProps> = ({
  classNameValue,
  effectiveDate,
  schedule,
  onCellClick,
}) => {
  const getCell = (key: string): TimetableCell | undefined => {
    return schedule?.cells[key];
  };

  const renderCellContent = (slotKey: string, cellLabel: string) => {
    const cell = getCell(slotKey);
    const hasContent = Boolean(cell && (cell.subject || cell.teacher));
    const style = getSubjectStyle(cell?.subject);

    return (
      <td
        key={slotKey}
        onClick={() => onCellClick?.(slotKey, cell, cellLabel)}
        className="border border-slate-200 text-center p-1.5 h-16 cursor-pointer hover:bg-slate-100/60 transition-colors group relative select-none"
        title="Nhấp để sửa tiết học (đồng bộ thời gian thực)"
      >
        {hasContent && cell ? (
          <div
            className={`h-full w-full ${style.bg} border-l-4 ${style.border} p-2 rounded text-left flex flex-col justify-center min-h-[46px] shadow-2xs`}
          >
            <div className="flex items-center justify-between gap-1">
              <span className={`font-bold ${style.text} text-xs tracking-tight`}>
                {cell.subject}
              </span>
              {cell.room && (
                <span className="text-[10px] text-slate-500 font-normal italic">
                  {cell.room}
                </span>
              )}
            </div>
            {cell.teacher && (
              <span className={`${style.teacher} font-medium text-[11px] opacity-90 truncate mt-0.5`}>
                {cell.teacher}
              </span>
            )}
          </div>
        ) : (
          <div className="h-full min-h-[46px] flex items-center justify-center text-slate-300 group-hover:text-slate-400">
            <span className="text-[11px] text-slate-300 italic group-hover:hidden">Trống</span>
            <span className="text-xs font-light hidden group-hover:inline text-blue-600 font-bold">+</span>
          </div>
        )}

        {/* Hover edit indicator */}
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
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h2 className="text-xl sm:text-2xl font-bold tracking-tight text-slate-900 uppercase">
              THỜI KHÓA BIỂU CỦA LỚP
            </h2>
            <div className="flex flex-wrap items-center gap-3 text-xs sm:text-sm text-slate-600 mt-1">
              <span>
                Lớp: <strong className="text-blue-700 font-semibold">{classNameValue}</strong>
              </span>
              <span className="text-slate-300">•</span>
              <span>
                Ngày áp dụng: <strong className="text-slate-800">{effectiveDate}</strong>
              </span>
            </div>
          </div>

          <div className="flex items-center gap-2 text-xs font-medium text-slate-500 bg-slate-50 px-3 py-1.5 rounded-md border border-slate-200">
            <Clock className="w-3.5 h-3.5 text-slate-400" />
            <span>Nhấp vào ô bất kỳ để chỉnh sửa trực tiếp</span>
          </div>
        </div>
      </div>

      {/* Table Container with horizontal scroll on mobile */}
      <div className="p-4 sm:p-6 pt-4 overflow-x-auto">
        <table className="w-full border-collapse border border-slate-200 text-sm bg-white min-w-[720px]">
          {/* Table Header matching Professional Polish design */}
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
                {/* Cột BUỔI - Gộp 5 dòng và 2 cột cho SÁNG */}
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

                {/* Cột TIẾT */}
                <td className="border border-slate-200 text-center font-bold text-slate-600 bg-slate-50/60 w-16 text-xs">
                  {period}
                </td>

                {/* Các ô Thứ 2 -> Thứ 7 */}
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
              {/* Cột BUỔI chính: CHIỀU gộp 4 dòng */}
              <td
                rowSpan={4}
                className="border border-slate-200 bg-slate-100 text-slate-700 font-bold text-center uppercase tracking-widest select-none w-14 text-sm"
                style={{ writingMode: 'vertical-rl', transform: 'rotate(180deg)' }}
              >
                CHIỀU
              </td>

              {/* Nhãn Tuần chẵn gộp 2 dòng */}
              <td
                rowSpan={2}
                className="border border-slate-200 bg-slate-50 text-[11px] font-semibold text-slate-600 text-center px-1 w-14"
              >
                (Tuần chẵn)
              </td>

              {/* Tiết 1 */}
              <td className="border border-slate-200 text-center font-bold text-slate-600 bg-slate-50/60 w-16 text-xs">
                1
              </td>

              {/* Các ô Thứ 2 -> Thứ 7 cho Tiết 1 Tuần chẵn */}
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
              {/* Nhãn Tuần lẻ gộp 2 dòng */}
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
