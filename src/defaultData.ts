import { SchoolDatabase, TimetableData } from './types';

export const DEFAULT_DATES: string[] = [
  '06/09/2026',
  '18/05/2026',
  '11/05/2026',
  '04/05/2026',
  '13/04/2026',
  '06/04/2026',
  '23/03/2026',
  '16/03/2026',
  '06/03/2026',
  '28/02/2026',
  '27/02/2026',
  '30/01/2026',
  '23/01/2026',
  '16/01/2026',
  '09/01/2026',
  '03/01/2026',
  '26/12/2025',
  '22/12/2025',
  '20/12/2025',
  '07/12/2025',
];

export const DEFAULT_CLASSES: string[] = [
  '10 Lý',
  '10 Hóa',
  '10 Sinh',
  '10 Tin',
  '10 Sử',
  '10 Địa',
  '10 Toán',
  '10 Văn',
  '10 Anh',
  '11 Toán',
  '11 Lý',
  '11 Hóa',
  '12 Toán',
  '12 Văn',
  '12 Anh',
];

export const DEFAULT_TEACHERS: string[] = [
  'Ngân',
  'MLoan',
  'nttHương',
  'Đ.Mai',
  'Dũng',
  'C.NHUNG',
  'H.Lan',
  'Ninh',
  'Hảo',
  'Hạnh(T)',
  'Q.Anh',
  'Tuấn(GDTC)',
  'ThuVân',
  'Bình',
];

// Dữ liệu mẫu khớp đúng 100% với ảnh chụp màn hình cho lớp 10 Lý ngày 06/09/2026
const sample10LySchedule: TimetableData = {
  id: 'schedule_10Ly_06_09_2026',
  effectiveDate: '06/09/2026',
  classId: '10 Lý',
  updatedAt: new Date().toISOString(),
  cells: {
    // SÁNG - Tiết 1
    'sang_all_1_2': { subject: 'TrNg', teacher: 'Ngân' },
    'sang_all_1_3': { subject: 'GDTC', teacher: '' },
    'sang_all_1_4': { subject: 'L', teacher: 'MLoan' },
    'sang_all_1_5': { subject: 'T', teacher: 'nttHương' },
    'sang_all_1_6': { subject: 'L', teacher: 'MLoan' },
    'sang_all_1_7': { subject: 'H', teacher: 'H.Lan' },

    // SÁNG - Tiết 2
    'sang_all_2_2': { subject: 'TrNg', teacher: 'Ngân' },
    'sang_all_2_3': { subject: 'A', teacher: 'Đ.Mai' },
    'sang_all_2_4': { subject: 'L', teacher: 'MLoan' },
    'sang_all_2_5': { subject: 'T', teacher: 'nttHương' },
    'sang_all_2_6': { subject: 'TN', teacher: 'Dũng' },
    'sang_all_2_7': { subject: 'A', teacher: 'Đ.Mai' },

    // SÁNG - Tiết 3
    'sang_all_3_2': { subject: 'S', teacher: 'Ngân' },
    'sang_all_3_3': { subject: 'L', teacher: 'MLoan' },
    'sang_all_3_4': { subject: 'V', teacher: 'C.NHUNG' },
    'sang_all_3_5': { subject: 'S', teacher: 'Ngân' },
    'sang_all_3_6': { subject: 'GDTC', teacher: '' },
    'sang_all_3_7': { subject: 'GDĐP', teacher: 'Ninh' },

    // SÁNG - Tiết 4
    'sang_all_4_2': { subject: 'TN', teacher: 'Dũng' },
    'sang_all_4_3': { subject: 'L', teacher: 'MLoan' },
    'sang_all_4_4': { subject: 'V', teacher: 'C.NHUNG' },
    'sang_all_4_5': { subject: 'H', teacher: 'H.Lan' },
    'sang_all_4_6': { subject: 'T', teacher: 'nttHương' },
    'sang_all_4_7': { subject: 'SU', teacher: 'Hạnh(T)' },

    // SÁNG - Tiết 5
    'sang_all_5_2': { subject: 'A', teacher: 'Đ.Mai' },
    'sang_all_5_3': { subject: '', teacher: '' },
    'sang_all_5_4': { subject: 'GDQP', teacher: 'Hảo' },
    'sang_all_5_5': { subject: 'H', teacher: 'H.Lan' },
    'sang_all_5_6': { subject: 'T', teacher: 'nttHương' },
    'sang_all_5_7': { subject: 'V', teacher: 'C.NHUNG' },

    // CHIỀU - Tuần chẵn - Tiết 1
    'chieu_chan_1_2': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_1_3': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_1_4': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_1_5': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_1_6': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_1_7': { subject: '', teacher: '' },

    // CHIỀU - Tuần chẵn - Tiết 2
    'chieu_chan_2_2': { subject: 'TrNg', teacher: 'nttHương' },
    'chieu_chan_2_3': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_2_4': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_2_5': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_2_6': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_2_7': { subject: '', teacher: '' },

    // CHIỀU - Tuần lẻ - Tiết 1 & 2
    'chieu_le_1_2': { subject: '', teacher: '' },
    'chieu_le_2_2': { subject: '', teacher: '' },
  },
};

// Dữ liệu mẫu cho lớp 10 Hóa ngày 06/09/2026
const sample10HoaSchedule: TimetableData = {
  id: 'schedule_10Hoa_06_09_2026',
  effectiveDate: '06/09/2026',
  classId: '10 Hóa',
  updatedAt: new Date().toISOString(),
  cells: {
    'sang_all_1_2': { subject: 'T', teacher: 'nttHương' },
    'sang_all_1_3': { subject: 'H', teacher: 'H.Lan' },
    'sang_all_1_4': { subject: 'H', teacher: 'H.Lan' },
    'sang_all_1_5': { subject: 'GDTC', teacher: 'Tuấn(GDTC)' },
    'sang_all_1_6': { subject: 'V', teacher: 'C.NHUNG' },
    'sang_all_1_7': { subject: 'A', teacher: 'Đ.Mai' },

    'sang_all_2_2': { subject: 'T', teacher: 'nttHương' },
    'sang_all_2_3': { subject: 'H', teacher: 'H.Lan' },
    'sang_all_2_4': { subject: 'L', teacher: 'MLoan' },
    'sang_all_2_5': { subject: 'S', teacher: 'Ngân' },
    'sang_all_2_6': { subject: 'V', teacher: 'C.NHUNG' },
    'sang_all_2_7': { subject: 'TN', teacher: 'Dũng' },

    'sang_all_3_2': { subject: 'V', teacher: 'C.NHUNG' },
    'sang_all_3_3': { subject: 'T', teacher: 'nttHương' },
    'sang_all_3_4': { subject: 'A', teacher: 'Đ.Mai' },
    'sang_all_3_5': { subject: 'L', teacher: 'MLoan' },
    'sang_all_3_6': { subject: 'TN', teacher: 'Dũng' },
    'sang_all_3_7': { subject: 'GDQP', teacher: 'Hảo' },

    'sang_all_4_2': { subject: 'TrNg', teacher: 'H.Lan' },
    'sang_all_4_3': { subject: 'SU', teacher: 'Hạnh(T)' },
    'sang_all_4_4': { subject: 'S', teacher: 'Ngân' },
    'sang_all_4_5': { subject: 'A', teacher: 'Đ.Mai' },
    'sang_all_4_6': { subject: 'T', teacher: 'nttHương' },
    'sang_all_4_7': { subject: 'GDĐP', teacher: 'Ninh' },

    'sang_all_5_2': { subject: 'TrNg', teacher: 'H.Lan' },
    'sang_all_5_3': { subject: 'GDTC', teacher: 'Tuấn(GDTC)' },
    'sang_all_5_4': { subject: '', teacher: '' },
    'sang_all_5_5': { subject: 'V', teacher: 'C.NHUNG' },
    'sang_all_5_6': { subject: 'H', teacher: 'H.Lan' },
    'sang_all_5_7': { subject: '', teacher: '' },

    'chieu_chan_1_3': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_1_4': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_2_3': { subject: 'Nângcao', teacher: '' },
    'chieu_chan_2_4': { subject: 'Nângcao', teacher: '' },
  },
};

// Dữ liệu mẫu cho lớp 10 Sinh ngày 06/09/2026
const sample10SinhSchedule: TimetableData = {
  id: 'schedule_10Sinh_06_09_2026',
  effectiveDate: '06/09/2026',
  classId: '10 Sinh',
  updatedAt: new Date().toISOString(),
  cells: {
    'sang_all_1_2': { subject: 'S', teacher: 'Ngân' },
    'sang_all_1_3': { subject: 'S', teacher: 'Ngân' },
    'sang_all_1_4': { subject: 'T', teacher: 'nttHương' },
    'sang_all_1_5': { subject: 'A', teacher: 'Đ.Mai' },
    'sang_all_1_6': { subject: 'H', teacher: 'H.Lan' },
    'sang_all_1_7': { subject: 'V', teacher: 'C.NHUNG' },

    'sang_all_2_2': { subject: 'S', teacher: 'Ngân' },
    'sang_all_2_3': { subject: 'T', teacher: 'nttHương' },
    'sang_all_2_4': { subject: 'V', teacher: 'C.NHUNG' },
    'sang_all_2_5': { subject: 'A', teacher: 'Đ.Mai' },
    'sang_all_2_6': { subject: 'H', teacher: 'H.Lan' },
    'sang_all_2_7': { subject: 'L', teacher: 'MLoan' },
  },
};

export const INITIAL_DATABASE: SchoolDatabase = {
  effectiveDates: DEFAULT_DATES,
  classes: DEFAULT_CLASSES,
  teachers: DEFAULT_TEACHERS,
  schedules: [sample10LySchedule, sample10HoaSchedule, sample10SinhSchedule],
  lastUpdated: new Date().toISOString(),
};
