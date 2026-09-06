import React, { useState, useEffect } from 'react';
import { X, Save, Trash2, CheckCircle2 } from 'lucide-react';
import { TimetableCell, ViewMode } from '../types';

interface CellEditModalProps {
  isOpen: boolean;
  onClose: () => void;
  viewMode: ViewMode;
  slotKey: string;
  slotLabel: string;
  currentClass: string;
  currentTeacher: string;
  cellData: TimetableCell | undefined;
  classesList: string[];
  teachersList: string[];
  onSave: (targetClass: string, slotKey: string, updatedCell: TimetableCell) => void;
  onDelete: (targetClass: string, slotKey: string) => void;
}

const COMMON_SUBJECTS = [
  'T',
  'L',
  'H',
  'S',
  'V',
  'A',
  'TN',
  'SU',
  'Đ',
  'GDTC',
  'GDQP',
  'GDĐP',
  'TrNg',
  'Nângcao',
  'SHL',
  'Chào cờ',
];

export const CellEditModal: React.FC<CellEditModalProps> = ({
  isOpen,
  onClose,
  viewMode,
  slotKey,
  slotLabel,
  currentClass,
  currentTeacher,
  cellData,
  classesList,
  teachersList,
  onSave,
  onDelete,
}) => {
  const [subject, setSubject] = useState('');
  const [teacher, setTeacher] = useState('');
  const [targetClass, setTargetClass] = useState('');
  const [room, setRoom] = useState('');

  useEffect(() => {
    if (isOpen) {
      setSubject(cellData?.subject || '');
      setTeacher(viewMode === 'teacher' ? currentTeacher : (cellData?.teacher || ''));
      setTargetClass(viewMode === 'class' ? currentClass : (cellData?.className || classesList[0] || '10 Lý'));
      setRoom(cellData?.room || '');
    }
  }, [isOpen, cellData, currentClass, currentTeacher, viewMode, classesList]);

  if (!isOpen) return null;

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    onSave(targetClass, slotKey, {
      subject: subject.trim(),
      teacher: teacher.trim(),
      room: room.trim() || undefined,
    });
    onClose();
  };

  const handleDelete = () => {
    onDelete(targetClass, slotKey);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white rounded-lg shadow-xl max-w-md w-full overflow-hidden border border-slate-200 animate-in fade-in zoom-in-95 duration-150">
        {/* Header */}
        <div className="bg-[#1E293B] text-white px-6 py-4 flex items-center justify-between border-b border-slate-700">
          <div>
            <h3 className="text-sm font-semibold tracking-tight text-white uppercase">
              Chỉnh Sửa Tiết Học
            </h3>
            <p className="text-xs text-slate-400 mt-0.5">{slotLabel}</p>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-md text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Form */}
        <form onSubmit={handleSave} className="p-6 space-y-4 text-sm">
          {/* Lớp học */}
          <div>
            <label className="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-1">
              Lớp học
            </label>
            {viewMode === 'class' ? (
              <div className="px-3 py-2 bg-slate-50 border border-slate-300 rounded-md font-bold text-slate-900 text-xs">
                {currentClass}
              </div>
            ) : (
              <select
                value={targetClass}
                onChange={(e) => setTargetClass(e.target.value)}
                className="w-full px-3 py-2 bg-white border border-slate-300 rounded-md shadow-xs font-semibold text-xs text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                {classesList.map((cls) => (
                  <option key={cls} value={cls}>
                    {cls}
                  </option>
                ))}
              </select>
            )}
          </div>

          {/* Môn học */}
          <div>
            <label className="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-1">
              Môn học (Ký hiệu hoặc Tên môn)
            </label>
            <input
              type="text"
              value={subject}
              onChange={(e) => setSubject(e.target.value)}
              placeholder="VD: TrNg, T, L, H, V, A, GDTC, Nângcao..."
              className="w-full px-3 py-2 border border-slate-300 rounded-md shadow-xs focus:outline-none focus:ring-2 focus:ring-blue-500 text-xs font-medium text-slate-900"
            />
            {/* Quick subject chips */}
            <div className="flex flex-wrap gap-1.5 mt-2">
              {COMMON_SUBJECTS.map((sub) => (
                <button
                  key={sub}
                  type="button"
                  onClick={() => setSubject(sub)}
                  className={`px-2 py-0.5 text-xs rounded border transition-colors ${
                    subject === sub
                      ? 'bg-blue-600 text-white border-blue-600 font-semibold'
                      : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                  }`}
                >
                  {sub}
                </button>
              ))}
            </div>
          </div>

          {/* Giáo viên phụ trách */}
          <div>
            <label className="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-1">
              Giáo viên giảng dạy
            </label>
            <input
              type="text"
              value={teacher}
              onChange={(e) => setTeacher(e.target.value)}
              placeholder="VD: Ngân, MLoan, nttHương, Đ.Mai..."
              className="w-full px-3 py-2 border border-slate-300 rounded-md shadow-xs focus:outline-none focus:ring-2 focus:ring-blue-500 text-xs font-medium text-blue-700"
            />
            {/* Quick teacher chips */}
            <div className="flex flex-wrap gap-1.5 mt-2 max-h-24 overflow-y-auto">
              {teachersList.slice(0, 10).map((t) => (
                <button
                  key={t}
                  type="button"
                  onClick={() => setTeacher(t)}
                  className={`px-2 py-0.5 text-xs rounded border transition-colors ${
                    teacher === t
                      ? 'bg-slate-900 text-white border-slate-900 font-semibold'
                      : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                  }`}
                >
                  {t}
                </button>
              ))}
            </div>
          </div>

          {/* Phòng học (Tùy chọn) */}
          <div>
            <label className="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-1">
              Phòng học / Ghi chú (tùy chọn)
            </label>
            <input
              type="text"
              value={room}
              onChange={(e) => setRoom(e.target.value)}
              placeholder="VD: P.101, Lab Tin, Sân bóng..."
              className="w-full px-3 py-2 border border-slate-300 rounded-md shadow-xs focus:outline-none focus:ring-2 focus:ring-blue-500 text-xs text-slate-800"
            />
          </div>

          {/* Action Buttons */}
          <div className="flex items-center justify-between pt-4 border-t border-slate-200">
            {cellData?.subject || cellData?.teacher ? (
              <button
                type="button"
                onClick={handleDelete}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium text-rose-600 hover:bg-rose-50 rounded-md transition-colors"
              >
                <Trash2 className="w-4 h-4" />
                Xóa tiết này
              </button>
            ) : (
              <div />
            )}

            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={onClose}
                className="px-3.5 py-1.5 text-xs font-medium text-slate-700 hover:bg-slate-100 rounded-md border border-slate-300 transition-colors shadow-xs"
              >
                Hủy
              </button>
              <button
                type="submit"
                className="inline-flex items-center gap-1.5 px-4 py-1.5 text-xs font-semibold text-white bg-slate-900 hover:bg-slate-800 rounded-md shadow-xs transition-colors"
              >
                <Save className="w-4 h-4" />
                Lưu thay đổi
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
};
