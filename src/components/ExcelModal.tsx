import React, { useState, useRef } from 'react';
import { X, Upload, Download, FileSpreadsheet, CheckCircle, AlertCircle, RefreshCw, FileCheck } from 'lucide-react';
import { parseExcelFile, ParseExcelResult } from '../utils/excel';
import { SchoolDatabase, TimetableData } from '../types';

interface ExcelModalProps {
  isOpen: boolean;
  onClose: () => void;
  database: SchoolDatabase;
  currentClass: string;
  currentTeacher: string;
  effectiveDate: string;
  onImportComplete: (result: ParseExcelResult) => void;
  onExportCurrent: () => void;
  onExportAll: () => void;
  onDownloadTemplate: () => void;
}

export const ExcelModal: React.FC<ExcelModalProps> = ({
  isOpen,
  onClose,
  database,
  currentClass,
  currentTeacher,
  effectiveDate,
  onImportComplete,
  onExportCurrent,
  onExportAll,
  onDownloadTemplate,
}) => {
  const [activeTab, setActiveTab] = useState<'import' | 'export'>('import');
  const [isParsing, setIsParsing] = useState(false);
  const [parseResult, setParseResult] = useState<ParseExcelResult | null>(null);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [dragOver, setDragOver] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  if (!isOpen) return null;

  const handleFileProcess = async (file: File) => {
    setErrorMessage(null);
    setParseResult(null);
    setIsParsing(true);

    try {
      const result = await parseExcelFile(file);
      if (result.success) {
        setParseResult(result);
      } else {
        setErrorMessage(result.message);
      }
    } catch (err: any) {
      setErrorMessage(err.message || 'Có lỗi xảy ra khi đọc tệp Excel.');
    } finally {
      setIsParsing(false);
    }
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      handleFileProcess(file);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setDragOver(false);
    const file = e.dataTransfer.files?.[0];
    if (file) {
      handleFileProcess(file);
    }
  };

  const handleConfirmImport = () => {
    if (parseResult && parseResult.success) {
      onImportComplete(parseResult);
      onClose();
    }
  };

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white rounded-lg shadow-xl max-w-xl w-full overflow-hidden border border-slate-200 animate-in fade-in zoom-in-95 duration-150">
        {/* Modal Header */}
        <div className="bg-[#1E293B] text-white px-6 py-4 flex items-center justify-between border-b border-slate-700">
          <div className="flex items-center gap-2">
            <FileSpreadsheet className="w-5 h-5 text-emerald-400" />
            <h3 className="text-sm font-semibold tracking-tight uppercase text-white">
              Quản Lý Tệp Excel (.xlsx)
            </h3>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-md text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Tab Switching */}
        <div className="flex border-b border-slate-200 bg-slate-50 px-6 pt-3">
          <button
            onClick={() => setActiveTab('import')}
            className={`pb-3 px-4 font-semibold text-xs uppercase tracking-wider border-b-2 transition-colors flex items-center gap-1.5 ${
              activeTab === 'import'
                ? 'border-blue-600 text-blue-700'
                : 'border-transparent text-slate-500 hover:text-slate-800'
            }`}
          >
            <Upload className="w-4 h-4" />
            Nhập dữ liệu Excel (.xlsx)
          </button>
          <button
            onClick={() => setActiveTab('export')}
            className={`pb-3 px-4 font-semibold text-xs uppercase tracking-wider border-b-2 transition-colors flex items-center gap-1.5 ${
              activeTab === 'export'
                ? 'border-blue-600 text-blue-700'
                : 'border-transparent text-slate-500 hover:text-slate-800'
            }`}
          >
            <Download className="w-4 h-4" />
            Xuất dữ liệu ra Excel (.xlsx)
          </button>
        </div>

        {/* Content Body */}
        <div className="p-6">
          {activeTab === 'import' ? (
            <div className="space-y-4">
              <p className="text-xs text-slate-600 leading-relaxed">
                Tải lên tệp <strong>.xlsx</strong> hoặc <strong>.xls</strong> để cập nhật thời khóa biểu. 
                Dữ liệu sau khi nhập sẽ tự động đồng bộ hóa thời gian thực tới tất cả các thiết bị.
              </p>

              {/* Upload Drop Area */}
              <div
                onDragOver={(e) => {
                  e.preventDefault();
                  setDragOver(true);
                }}
                onDragLeave={() => setDragOver(false)}
                onDrop={handleDrop}
                onClick={() => fileInputRef.current?.click()}
                className={`border-2 border-dashed rounded-lg p-6 text-center cursor-pointer transition-all ${
                  dragOver
                    ? 'border-blue-500 bg-blue-50/50'
                    : 'border-slate-300 hover:border-slate-400 bg-slate-50/70'
                }`}
              >
                <input
                  ref={fileInputRef}
                  type="file"
                  accept=".xlsx, .xls"
                  onChange={handleFileChange}
                  className="hidden"
                />

                <div className="flex flex-col items-center justify-center space-y-2">
                  <div className="w-11 h-11 rounded-lg bg-blue-50 flex items-center justify-center text-blue-600 border border-blue-100">
                    {isParsing ? (
                      <RefreshCw className="w-5 h-5 animate-spin text-blue-600" />
                    ) : (
                      <Upload className="w-5 h-5" />
                    )}
                  </div>
                  <div>
                    <span className="font-semibold text-blue-700 hover:underline text-xs">
                      Nhấp để chọn tệp tin
                    </span>
                    <span className="text-slate-500 text-xs"> hoặc kéo thả file Excel vào đây</span>
                  </div>
                  <p className="text-[11px] text-slate-400">Hỗ trợ định dạng: .xlsx, .xls</p>
                </div>
              </div>

              {/* Parsing status / errors */}
              {errorMessage && (
                <div className="p-3 bg-rose-50 border border-rose-200 rounded-md flex items-start gap-2.5 text-xs text-rose-700">
                  <AlertCircle className="w-4 h-4 text-rose-500 shrink-0 mt-0.5" />
                  <div>
                    <span className="font-semibold">Không thể nhập tệp:</span> {errorMessage}
                  </div>
                </div>
              )}

              {parseResult && parseResult.success && (
                <div className="p-4 bg-emerald-50 border border-emerald-200 rounded-md space-y-2 text-xs text-emerald-800">
                  <div className="flex items-center gap-2 font-bold text-xs text-emerald-900">
                    <CheckCircle className="w-4 h-4 text-emerald-600" />
                    {parseResult.message}
                  </div>
                  <ul className="list-disc pl-5 space-y-1 text-emerald-700 text-xs">
                    <li>
                      Thời khóa biểu phân tích được: <strong>{parseResult.importedCount}</strong> lớp/ngày
                    </li>
                    {parseResult.newClasses.length > 0 && (
                      <li>
                        Các lớp: <strong>{parseResult.newClasses.join(', ')}</strong>
                      </li>
                    )}
                    {parseResult.newDates.length > 0 && (
                      <li>
                        Ngày áp dụng: <strong>{parseResult.newDates.join(', ')}</strong>
                      </li>
                    )}
                  </ul>

                  <button
                    onClick={handleConfirmImport}
                    className="w-full mt-3 py-2 px-4 bg-slate-900 hover:bg-slate-800 text-white font-semibold rounded-md shadow-xs transition-colors flex items-center justify-center gap-2 text-xs"
                  >
                    <FileCheck className="w-4 h-4 text-emerald-400" />
                    Xác nhận đồng bộ vào Thời khóa biểu
                  </button>
                </div>
              )}

              {/* Template download guide */}
              <div className="pt-3 border-t border-slate-200 flex items-center justify-between">
                <span className="text-xs text-slate-500">Chưa có tệp đúng chuẩn?</span>
                <button
                  type="button"
                  onClick={onDownloadTemplate}
                  className="inline-flex items-center gap-1.5 text-xs font-semibold text-blue-700 hover:text-blue-900 hover:underline"
                >
                  <Download className="w-3.5 h-3.5" />
                  Tải file mẫu Excel chuẩn (.xlsx)
                </button>
              </div>
            </div>
          ) : (
            /* Export tab */
            <div className="space-y-4">
              <p className="text-xs text-slate-600 leading-relaxed">
                Xuất dữ liệu thời khóa biểu hiện tại ra file <strong>.xlsx</strong> giữ nguyên định dạng bảng biểu, buổi, tiết, thứ và tên giáo viên.
              </p>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                <button
                  type="button"
                  onClick={() => {
                    onExportCurrent();
                    onClose();
                  }}
                  className="p-4 border border-slate-200 rounded-lg bg-slate-50 hover:bg-slate-100/80 transition-all text-left flex flex-col justify-between group shadow-xs"
                >
                  <div>
                    <div className="w-8 h-8 rounded bg-blue-600 text-white flex items-center justify-center mb-2 shadow-xs">
                      <FileSpreadsheet className="w-4 h-4" />
                    </div>
                    <h4 className="font-bold text-xs uppercase tracking-wider text-slate-900 group-hover:text-blue-700">
                      Xuất mẫu đang xem
                    </h4>
                    <p className="text-xs text-slate-500 mt-1">
                      Chỉ xuất thời khóa biểu cho: <strong>{currentClass}</strong> (hoặc giáo viên đang chọn).
                    </p>
                  </div>
                  <span className="inline-flex items-center gap-1 text-xs font-semibold text-blue-700 mt-3">
                    <Download className="w-3.5 h-3.5" /> Tải về ngay
                  </span>
                </button>

                <button
                  type="button"
                  onClick={() => {
                    onExportAll();
                    onClose();
                  }}
                  className="p-4 border border-slate-200 rounded-lg bg-slate-50 hover:bg-slate-100/80 transition-all text-left flex flex-col justify-between group shadow-xs"
                >
                  <div>
                    <div className="w-8 h-8 rounded bg-emerald-600 text-white flex items-center justify-center mb-2 shadow-xs">
                      <Download className="w-4 h-4" />
                    </div>
                    <h4 className="font-bold text-xs uppercase tracking-wider text-slate-900 group-hover:text-emerald-700">
                      Xuất toàn bộ hệ thống
                    </h4>
                    <p className="text-xs text-slate-500 mt-1">
                      File Excel gồm nhiều Sheet cho tất cả các lớp + Sheet bảng dữ liệu tổng hợp.
                    </p>
                  </div>
                  <span className="inline-flex items-center gap-1 text-xs font-semibold text-emerald-700 mt-3">
                    <Download className="w-3.5 h-3.5" /> Tải về tất cả
                  </span>
                </button>
              </div>

              {/* Template download link */}
              <div className="pt-4 border-t border-slate-200 flex items-center justify-between">
                <span className="text-xs text-slate-500">Mẫu trống để nhập liệu:</span>
                <button
                  type="button"
                  onClick={onDownloadTemplate}
                  className="inline-flex items-center gap-1.5 text-xs font-semibold text-blue-700 hover:underline"
                >
                  <Download className="w-3.5 h-3.5" />
                  Tải file mẫu trắng (.xlsx)
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
