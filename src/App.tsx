import React, { useState, useMemo } from 'react';
import { useTimetableSync } from './hooks/useTimetableSync';
import { ViewMode, TimetableCell } from './types';
import { Navbar } from './components/Navbar';
import { FilterBar } from './components/FilterBar';
import { ClassTimetableTable } from './components/ClassTimetableTable';
import { TeacherTimetableTable } from './components/TeacherTimetableTable';
import { CellEditModal } from './components/CellEditModal';
import { ExcelModal } from './components/ExcelModal';
import { SyncToast } from './components/SyncToast';
import {
  exportClassScheduleToExcel,
  exportTeacherScheduleToExcel,
  exportAllSchedulesToExcel,
  downloadExcelTemplate,
  ParseExcelResult,
} from './utils/excel';
import { RefreshCw, Info, CheckCircle, FileSpreadsheet, Sparkles } from 'lucide-react';

export default function App() {
  const {
    database,
    isRealtimeConnected,
    toast,
    dismissToast,
    updateCell,
    deleteCell,
    importSchedules,
    resetToDefault,
  } = useTimetableSync();

  const [viewMode, setViewMode] = useState<ViewMode>('class');
  const [selectedDate, setSelectedDate] = useState<string>('06/09/2026');
  const [selectedClass, setSelectedClass] = useState<string>('10 Lý');
  const [selectedTeacher, setSelectedTeacher] = useState<string>('Ngân');

  // Modal states
  const [isExcelModalOpen, setIsExcelModalOpen] = useState(false);
  const [isCellModalOpen, setIsCellModalOpen] = useState(false);
  const [editingSlot, setEditingSlot] = useState<{
    slotKey: string;
    cell: TimetableCell | undefined;
    label: string;
  } | null>(null);

  // Fallback to existing dates, classes, teachers if current selection is not available
  const effectiveDates = database.effectiveDates.length > 0 ? database.effectiveDates : ['06/09/2026'];
  const classes = database.classes.length > 0 ? database.classes : ['10 Lý'];
  const teachers = database.teachers.length > 0 ? database.teachers : ['Ngân'];

  const currentSchedule = useMemo(() => {
    return database.schedules.find(
      (s) => s.classId === selectedClass && s.effectiveDate === selectedDate
    );
  }, [database.schedules, selectedClass, selectedDate]);

  // Handle cell click to open editor
  const handleCellClick = (slotKey: string, cell: TimetableCell | undefined, label: string) => {
    setEditingSlot({ slotKey, cell, label });
    setIsCellModalOpen(true);
  };

  // Handle cell save
  const handleSaveCell = (targetClass: string, slotKey: string, updatedCell: TimetableCell) => {
    updateCell(targetClass, selectedDate, slotKey, updatedCell);
  };

  // Handle cell delete
  const handleDeleteCell = (targetClass: string, slotKey: string) => {
    deleteCell(targetClass, slotKey, selectedDate);
  };

  // Handle Excel Import completion
  const handleImportComplete = (result: ParseExcelResult) => {
    importSchedules(result.schedules, result.newClasses, result.newTeachers, result.newDates);
    if (result.newDates.length > 0 && !result.newDates.includes(selectedDate)) {
      setSelectedDate(result.newDates[0]);
    }
    if (result.newClasses.length > 0) {
      setSelectedClass(result.newClasses[0]);
    }
  };

  // Handle Excel Export
  const handleExportCurrent = () => {
    if (viewMode === 'class') {
      exportClassScheduleToExcel(currentSchedule, selectedClass, selectedDate);
    } else {
      exportTeacherScheduleToExcel(selectedTeacher, selectedDate, database.schedules);
    }
  };

  const handleExportAll = () => {
    exportAllSchedulesToExcel(database, selectedDate);
  };

  return (
    <div className="min-h-screen bg-[#F1F5F9] text-slate-900 flex flex-col font-sans selection:bg-blue-100 selection:text-blue-900">
      {/* 1. Header Navigation with Realtime Status */}
      <Navbar
        viewMode={viewMode}
        onViewModeChange={setViewMode}
        isRealtimeConnected={isRealtimeConnected}
        onOpenExcelModal={() => setIsExcelModalOpen(true)}
        onDownloadTemplate={downloadExcelTemplate}
        lastUpdated={database.lastUpdated}
      />

      {/* 2. Main Content Area */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {/* Quick helper banner */}
        <div className="mb-4 bg-white border border-slate-200 rounded-lg p-3 px-4 flex flex-wrap items-center justify-between gap-3 text-xs text-slate-700 shadow-xs">
          <div className="flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-500 shrink-0"></span>
            <span>
              Hệ thống đang chạy chế độ: <strong className="text-slate-900 font-semibold">{viewMode === 'class' ? 'Thời khóa biểu của Lớp' : 'Thời khóa biểu của Giáo viên'}</strong>.
              Dữ liệu tự động đồng bộ theo thời gian thực tới tất cả các phiên làm việc.
            </span>
          </div>
          <div className="flex items-center gap-2">
            <button
              onClick={resetToDefault}
              className="text-slate-500 hover:text-slate-800 underline transition-colors"
            >
              Khôi phục mẫu gốc
            </button>
          </div>
        </div>

        {/* Filters Bar matching screenshots */}
        <FilterBar
          viewMode={viewMode}
          effectiveDates={effectiveDates}
          selectedDate={selectedDate}
          onDateChange={setSelectedDate}
          classes={classes}
          selectedClass={selectedClass}
          onClassChange={setSelectedClass}
          teachers={teachers}
          selectedTeacher={selectedTeacher}
          onTeacherChange={setSelectedTeacher}
          onSearch={() => {}}
          onExportExcel={handleExportCurrent}
          onExportAllExcel={handleExportAll}
          onOpenExcelModal={() => setIsExcelModalOpen(true)}
          onDownloadTemplate={downloadExcelTemplate}
        />

        {/* Timetable view: Class or Teacher */}
        {viewMode === 'class' ? (
          <ClassTimetableTable
            classNameValue={selectedClass}
            effectiveDate={selectedDate}
            schedule={currentSchedule}
            onCellClick={handleCellClick}
          />
        ) : (
          <TeacherTimetableTable
            teacherName={selectedTeacher}
            effectiveDate={selectedDate}
            schedules={database.schedules}
            onCellClick={handleCellClick}
          />
        )}

        {/* School Footer info matching Professional Polish theme */}
        <div className="mt-8 bg-[#1E293B] text-white rounded-lg p-5 flex flex-wrap items-center justify-between gap-4 border border-slate-800 shadow-xs">
          <div>
            <h4 className="font-bold text-xs uppercase tracking-wider text-white">TRƯỜNG THPT CHUYÊN HOÀNG VĂN THỤ</h4>
            <p className="text-xs text-slate-400 mt-0.5">
              Văn Thư • Phường Đồng Tiến, TP. Hòa Bình - Tỉnh Hòa Bình
            </p>
          </div>

          <div className="flex items-center gap-3">
            <div className="bg-slate-800/80 px-3 py-1.5 rounded-md text-xs text-slate-300 border border-slate-700">
              Định dạng xuất chuẩn: <strong className="text-white">.xlsx</strong> (Microsoft Excel)
            </div>
          </div>
        </div>
      </main>

      {/* 3. Cell Edit Modal */}
      <CellEditModal
        isOpen={isCellModalOpen}
        onClose={() => setIsCellModalOpen(false)}
        viewMode={viewMode}
        slotKey={editingSlot?.slotKey || ''}
        slotLabel={editingSlot?.label || ''}
        currentClass={selectedClass}
        currentTeacher={selectedTeacher}
        cellData={editingSlot?.cell}
        classesList={classes}
        teachersList={teachers}
        onSave={handleSaveCell}
        onDelete={handleDeleteCell}
      />

      {/* 4. Excel Import / Export Modal */}
      <ExcelModal
        isOpen={isExcelModalOpen}
        onClose={() => setIsExcelModalOpen(false)}
        database={database}
        currentClass={selectedClass}
        currentTeacher={selectedTeacher}
        effectiveDate={selectedDate}
        onImportComplete={handleImportComplete}
        onExportCurrent={handleExportCurrent}
        onExportAll={handleExportAll}
        onDownloadTemplate={downloadExcelTemplate}
      />

      {/* 5. Real-time Toast Notifications */}
      <SyncToast toast={toast} onDismiss={dismissToast} />
    </div>
  );
}
