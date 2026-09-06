export type DayOfWeek = 2 | 3 | 4 | 5 | 6 | 7;

export const DAYS_OF_WEEK: { key: DayOfWeek; label: string }[] = [
  { key: 2, label: 'THỨ 2' },
  { key: 3, label: 'THỨ 3' },
  { key: 4, label: 'THỨ 4' },
  { key: 5, label: 'THỨ 5' },
  { key: 6, label: 'THỨ 6' },
  { key: 7, label: 'THỨ 7' },
];

export type SessionType = 'sang' | 'chieu';
export type WeekType = 'all' | 'chan' | 'le'; // Tuần chẵn, tuần lẻ, hoặc cả hai

export interface SlotIdentifier {
  session: SessionType;
  period: number; // 1 -> 5
  weekType?: 'chan' | 'le'; // cho buổi chiều
  day: DayOfWeek;
}

export interface TimetableCell {
  subject: string; // Tên môn (VD: TrNg, GDTC, L, T, H, A, TN, S, V, Nângcao)
  teacher?: string; // Tên giáo viên (VD: Ngân, MLoan, nttHương, Đ.Mai, Dũng, C.NHUNG, H.Lan)
  room?: string; // Phòng học nếu có
  className?: string; // Sử dụng khi hiển thị thời khóa biểu của giáo viên (VD: 10 Lý)
  note?: string;
}

export interface ScheduleRowDefinition {
  id: string;
  session: SessionType;
  period: number;
  sessionLabel: string;
  subLabel?: string; // e.g. '(Tuần chẵn)', '(Tuần lẻ)'
  rowSpan?: number;
}

export interface TimetableData {
  id: string;
  effectiveDate: string; // e.g. "06/09/2026"
  classId: string; // e.g. "10 Lý"
  cells: Record<string, TimetableCell>; // key: `${session}_${weekType || 'all'}_${period}_${day}`
  updatedAt: string;
}

export interface TeacherInfo {
  id: string;
  name: string;
  code: string;
  subject?: string;
  phone?: string;
}

export interface SchoolDatabase {
  effectiveDates: string[];
  classes: string[];
  teachers: string[];
  schedules: TimetableData[]; // Danh sách thời khóa biểu các lớp
  lastUpdated: string;
}

export type ViewMode = 'class' | 'teacher';
