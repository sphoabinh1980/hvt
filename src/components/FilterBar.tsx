import React from 'react';
import { Search, Download, Upload, Plus, FileText, ChevronDown } from 'lucide-react';
import { ViewMode } from '../types';
import { SearchableDropdown } from './SearchableDropdown';

interface FilterBarProps {
  viewMode: ViewMode;
  effectiveDates: string[];
  selectedDate: string;
  onDateChange: (date: string) => void;
  classes: string[];
  selectedClass: string;
  onClassChange: (cls: string) => void;
  teachers: string[];
  selectedTeacher: string;
  onTeacherChange: (teacher: string) => void;
  onSearch: () => void;
  onExportExcel: () => void;
  onExportAllExcel: () => void;
  onOpenExcelModal: () => void;
  onDownloadTemplate: () => void;
}

export const FilterBar: React.FC<FilterBarProps> = ({
  viewMode,
  effectiveDates,
  selectedDate,
  onDateChange,
  classes,
  selectedClass,
  onClassChange,
  teachers,
  selectedTeacher,
  onTeacherChange,
  onSearch,
  onExportExcel,
  onExportAllExcel,
  onOpenExcelModal,
  onDownloadTemplate,
}) => {
  const [showExportMenu, setShowExportMenu] = React.useState(false);

  return (
    <div className="bg-white rounded-lg shadow-xs border border-slate-200 p-4 mb-6">
      <div className="flex flex-wrap items-end justify-between gap-4">
        {/* Left: Standard Filters matching Screenshots */}
        <div className="flex flex-wrap items-end gap-4">
          {/* Ngày áp dụng */}
          <div className="flex flex-col">
            <label className="text-xs font-semibold text-slate-600 uppercase tracking-wider mb-1.5">
              Ngày áp dụng
            </label>
            <select
              value={selectedDate}
              onChange={(e) => onDateChange(e.target.value)}
              className="w-44 sm:w-48 px-3 py-1.5 bg-white border border-slate-300 rounded-md shadow-xs text-sm text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 cursor-pointer hover:border-slate-400 transition-colors"
            >
              {effectiveDates.map((date) => (
                <option key={date} value={date}>
                  {date}
                </option>
              ))}
            </select>
          </div>

          {/* Lớp hoặc Giáo viên */}
          {viewMode === 'class' ? (
            <SearchableDropdown
              label="Lớp học"
              items={classes}
              selectedItem={selectedClass}
              onSelect={onClassChange}
              placeholder="Chọn lớp..."
              searchPlaceholder="Tìm kiếm lớp..."
            />
          ) : (
            <SearchableDropdown
              label="Giáo viên"
              items={teachers}
              selectedItem={selectedTeacher}
              onSelect={onTeacherChange}
              placeholder="Chọn giáo viên..."
              searchPlaceholder="Tìm kiếm GV..."
            />
          )}

          {/* Nút Tìm kiếm (Kiểu dáng chuẩn Professional Polish) */}
          <button
            type="button"
            onClick={onSearch}
            className="px-4 py-1.5 bg-slate-900 hover:bg-slate-800 text-white text-sm font-medium rounded-md shadow-xs transition-colors flex items-center gap-1.5 h-[34px] self-end"
          >
            <Search className="w-4 h-4" />
            Tìm kiếm
          </button>
        </div>

        {/* Right: Actions for Excel Import/Export & Template */}
        <div className="flex flex-wrap items-center gap-2.5">
          {/* Nút Xuất Excel với menu thả xuống */}
          <div className="relative">
            <button
              type="button"
              onClick={() => setShowExportMenu(!showExportMenu)}
              className="inline-flex items-center gap-2 px-3.5 py-1.5 border border-slate-300 rounded-md text-sm font-medium text-slate-700 bg-white hover:bg-slate-50 shadow-xs transition-colors"
            >
              <Download className="w-4 h-4 text-slate-600" />
              <span>Xuất Excel (.xlsx)</span>
              <ChevronDown className="w-3.5 h-3.5 ml-0.5 text-slate-400" />
            </button>

            {showExportMenu && (
              <div
                className="absolute right-0 mt-1 w-56 bg-white rounded-md shadow-lg border border-slate-200 z-50 py-1 text-sm text-slate-700 animate-in fade-in duration-100"
                onMouseLeave={() => setShowExportMenu(false)}
              >
                <button
                  type="button"
                  onClick={() => {
                    onExportExcel();
                    setShowExportMenu(false);
                  }}
                  className="w-full text-left px-4 py-2 hover:bg-slate-50 hover:text-slate-900 flex items-center gap-2 text-xs font-medium"
                >
                  <FileText className="w-4 h-4 text-emerald-600" />
                  Xuất mẫu hiện tại ({viewMode === 'class' ? selectedClass : `GV ${selectedTeacher}`})
                </button>
                <button
                  type="button"
                  onClick={() => {
                    onExportAllExcel();
                    setShowExportMenu(false);
                  }}
                  className="w-full text-left px-4 py-2 hover:bg-slate-50 hover:text-slate-900 flex items-center gap-2 border-t border-slate-100 text-xs font-medium"
                >
                  <Download className="w-4 h-4 text-emerald-600" />
                  Xuất toàn bộ TKB tất cả các lớp
                </button>
              </div>
            )}
          </div>

          {/* Nút Nhập file Excel */}
          <button
            type="button"
            onClick={onOpenExcelModal}
            className="inline-flex items-center gap-2 px-3.5 py-1.5 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-md shadow-xs transition-colors"
          >
            <Upload className="w-4 h-4" />
            <span>Nhập Excel (.xlsx)</span>
          </button>
        </div>
      </div>
    </div>
  );
};
