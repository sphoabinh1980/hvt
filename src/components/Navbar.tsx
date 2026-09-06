import React from 'react';
import { Calendar, FileSpreadsheet, Radio, GraduationCap, UserCheck, Download, Upload } from 'lucide-react';
import { ViewMode } from '../types';

interface NavbarProps {
  viewMode: ViewMode;
  onViewModeChange: (mode: ViewMode) => void;
  isRealtimeConnected: boolean;
  onOpenExcelModal: () => void;
  onDownloadTemplate: () => void;
  lastUpdated: string;
}

export const Navbar: React.FC<NavbarProps> = ({
  viewMode,
  onViewModeChange,
  isRealtimeConnected,
  onOpenExcelModal,
  onDownloadTemplate,
  lastUpdated,
}) => {
  return (
    <header className="bg-[#1E293B] text-white select-none border-b border-slate-800 shadow-sm">
      {/* Top utility bar */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Brand and title */}
          <div className="flex items-center space-x-3">
            <div className="w-9 h-9 rounded bg-blue-600 flex items-center justify-center font-bold text-white shadow-xs">
              <span className="text-base font-semibold">S</span>
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-base sm:text-lg font-semibold tracking-tight text-white flex items-center gap-2">
                  EduSync Thời Khóa Biểu
                </h1>
                <span className="hidden md:inline-block px-2 py-0.5 text-[11px] font-medium bg-slate-800 text-slate-300 border border-slate-700 rounded">
                  v2.4 Pro
                </span>
              </div>
              <p className="text-xs text-slate-400 hidden sm:block">
                Đồng bộ hóa thời gian thực & Quản lý lịch học chuẩn Excel (.xlsx)
              </p>
            </div>
          </div>

          {/* Real-time Status & Quick Actions */}
          <div className="flex items-center space-x-3">
            {/* Real-time Status Badge */}
            <div
              className="flex items-center gap-2 px-3 py-1.5 rounded-md text-xs font-medium bg-slate-800/80 border border-slate-700 text-slate-200"
              title={`Cập nhật lần cuối: ${lastUpdated ? new Date(lastUpdated).toLocaleTimeString('vi-VN') : 'Đang kết nối'}`}
            >
              <span className="relative flex h-2 w-2">
                {isRealtimeConnected && (
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                )}
                <span
                  className={`relative inline-flex rounded-full h-2 w-2 ${
                    isRealtimeConnected ? 'bg-emerald-500' : 'bg-amber-500'
                  }`}
                ></span>
              </span>
              <span className="hidden sm:inline text-xs text-emerald-400">
                {isRealtimeConnected ? 'Đã đồng bộ hóa thời gian thực' : 'Đang kết nối lại'}
              </span>
            </div>

            {/* Quick Excel Action Button in Header */}
            <button
              onClick={onOpenExcelModal}
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-md text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 transition-colors border border-slate-700"
              title="Nhập và xuất dữ liệu Excel (.xlsx)"
            >
              <FileSpreadsheet className="w-4 h-4 text-emerald-400" />
              <span className="hidden md:inline">Quản lý Excel</span>
            </button>
          </div>
        </div>
      </div>

      {/* Navigation tabs matching Professional Polish styling */}
      <div className="bg-[#0F172A] border-t border-slate-800/80 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-2 py-1.5">
          <nav className="flex space-x-1.5">
            <button
              onClick={() => onViewModeChange('class')}
              className={`inline-flex items-center gap-2 px-3.5 py-1.5 text-xs sm:text-sm font-medium rounded-md transition-all ${
                viewMode === 'class'
                  ? 'bg-blue-600 text-white shadow-xs'
                  : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'
              }`}
            >
              <span
                className={`w-2 h-2 rounded-full ${
                  viewMode === 'class' ? 'bg-white' : 'bg-slate-600'
                }`}
              ></span>
              <GraduationCap className="w-4 h-4" />
              Thời khóa biểu Lớp
            </button>

            <button
              onClick={() => onViewModeChange('teacher')}
              className={`inline-flex items-center gap-2 px-3.5 py-1.5 text-xs sm:text-sm font-medium rounded-md transition-all ${
                viewMode === 'teacher'
                  ? 'bg-blue-600 text-white shadow-xs'
                  : 'text-slate-400 hover:bg-slate-800 hover:text-slate-200'
              }`}
            >
              <span
                className={`w-2 h-2 rounded-full ${
                  viewMode === 'teacher' ? 'bg-white' : 'bg-slate-600'
                }`}
              ></span>
              <UserCheck className="w-4 h-4" />
              Thời khóa biểu Giáo viên
            </button>
          </nav>

          <div className="hidden lg:flex items-center gap-4 text-xs text-slate-400">
            <button
              onClick={onDownloadTemplate}
              className="hover:text-slate-200 flex items-center gap-1.5 transition-colors"
            >
              <Download className="w-3.5 h-3.5 text-slate-400" />
              Tải mẫu Excel chuẩn
            </button>
            <span className="text-slate-700">|</span>
            <button
              onClick={onOpenExcelModal}
              className="hover:text-slate-200 flex items-center gap-1.5 transition-colors"
            >
              <Upload className="w-3.5 h-3.5 text-slate-400" />
              Nhập dữ liệu Excel (.xlsx)
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};
