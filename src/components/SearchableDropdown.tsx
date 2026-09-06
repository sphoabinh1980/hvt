import React, { useState, useRef, useEffect } from 'react';
import { ChevronDown, Search, Check } from 'lucide-react';

interface SearchableDropdownProps {
  label: string;
  items: string[];
  selectedItem: string;
  onSelect: (item: string) => void;
  placeholder?: string;
  searchPlaceholder?: string;
}

export const SearchableDropdown: React.FC<SearchableDropdownProps> = ({
  label,
  items,
  selectedItem,
  onSelect,
  placeholder = 'Chọn...',
  searchPlaceholder = 'Tìm kiếm...',
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const dropdownRef = useRef<HTMLDivElement>(null);
  const searchInputRef = useRef<HTMLInputElement>(null);

  // Focus search input when dropdown opens
  useEffect(() => {
    if (isOpen) {
      setTimeout(() => {
        searchInputRef.current?.focus();
      }, 50);
    } else {
      setSearchTerm('');
    }
  }, [isOpen]);

  // Close when clicked outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const filteredItems = items.filter((item) =>
    item.toLowerCase().includes(searchTerm.toLowerCase().trim())
  );

  return (
    <div className="relative inline-block text-left" ref={dropdownRef}>
      <div className="flex flex-col">
        <label className="text-xs font-semibold text-slate-600 uppercase tracking-wider mb-1.5">{label}</label>
        <button
          type="button"
          onClick={() => setIsOpen(!isOpen)}
          className="inline-flex items-center justify-between w-48 sm:w-56 px-3 py-1.5 bg-white border border-slate-300 rounded-md shadow-xs text-sm font-normal text-slate-800 hover:border-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
        >
          <span className="truncate font-medium text-slate-800">{selectedItem || placeholder}</span>
          <ChevronDown className="w-4 h-4 ml-2 text-slate-400 shrink-0" />
        </button>
      </div>

      {isOpen && (
        <div className="absolute z-50 mt-1 w-56 sm:w-64 bg-white border border-slate-200 rounded-md shadow-lg overflow-hidden animate-in fade-in duration-100">
          {/* Inner search input */}
          <div className="p-2 border-b border-slate-200 bg-slate-50">
            <div className="relative">
              <input
                ref={searchInputRef}
                type="text"
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                placeholder={searchPlaceholder}
                className="w-full px-2.5 py-1.5 pr-7 text-xs border border-slate-300 rounded focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 bg-white text-slate-800"
              />
              <Search className="w-3.5 h-3.5 text-slate-400 absolute right-2.5 top-2.5 pointer-events-none" />
            </div>
          </div>

          {/* List of items */}
          <ul className="max-h-56 overflow-y-auto py-1 text-xs text-slate-700">
            {filteredItems.length > 0 ? (
              filteredItems.map((item) => {
                const isSelected = item === selectedItem;
                return (
                  <li key={item}>
                    <button
                      type="button"
                      onClick={() => {
                        onSelect(item);
                        setIsOpen(false);
                      }}
                      className={`w-full text-left px-3 py-1.5 flex items-center justify-between hover:bg-slate-50 hover:text-slate-900 transition-colors ${
                        isSelected ? 'bg-blue-600 text-white font-semibold hover:bg-blue-700 hover:text-white' : ''
                      }`}
                    >
                      <span className="truncate">{item}</span>
                      {isSelected && <Check className="w-4 h-4 shrink-0 ml-1 text-white" />}
                    </button>
                  </li>
                );
              })
            ) : (
              <li className="px-3 py-2 text-xs text-slate-400 text-center">Không tìm thấy kết quả</li>
            )}
          </ul>
        </div>
      )}
    </div>
  );
};
