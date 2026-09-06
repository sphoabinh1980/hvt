import React, { useEffect, useState } from 'react';
import { Radio, CheckCircle, Bell, X } from 'lucide-react';

export interface ToastMessage {
  id: string;
  title: string;
  description: string;
  type?: 'info' | 'success' | 'update';
}

interface SyncToastProps {
  toast: ToastMessage | null;
  onDismiss: () => void;
}

export const SyncToast: React.FC<SyncToastProps> = ({ toast, onDismiss }) => {
  useEffect(() => {
    if (toast) {
      const timer = setTimeout(() => {
        onDismiss();
      }, 4000);
      return () => clearTimeout(timer);
    }
  }, [toast, onDismiss]);

  if (!toast) return null;

  return (
    <div className="fixed bottom-5 right-5 z-50 animate-in slide-in-from-bottom-5 duration-200 max-w-sm w-full">
      <div className="bg-white border-l-4 border-emerald-500 rounded-lg shadow-lg p-3.5 flex items-start gap-3 border border-slate-200">
        <div className="w-8 h-8 rounded-full bg-slate-100 text-emerald-600 flex items-center justify-center shrink-0 mt-0.5 border border-slate-200/80">
          <Radio className="w-4 h-4 animate-pulse text-emerald-600" />
        </div>
        <div className="flex-1 min-w-0">
          <h5 className="text-xs font-bold text-slate-900 uppercase tracking-wider">
            {toast.title}
          </h5>
          <p className="text-xs text-slate-600 mt-0.5">{toast.description}</p>
        </div>
        <button
          onClick={onDismiss}
          className="text-slate-400 hover:text-slate-600 p-1 rounded-md transition-colors"
        >
          <X className="w-4 h-4" />
        </button>
      </div>
    </div>
  );
};
