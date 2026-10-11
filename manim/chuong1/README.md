# Video Manim — Chương 1: Nền tảng quy hoạch động

Video dạy học khổ dọc **TikTok Full HD (1080×1920, 30 fps)** cho Chương 1 của tài liệu
*Quy hoạch động — Từ cơ bản đến nâng cao (Tập 1 · Lý thuyết)*, kèm **phụ đề thuyết minh `.srt`**.

| Phần | Nội dung | Thời lượng |
|---|---|---|
| Bài 1 | Từ đệ quy đến bảng phương án: NHAYDA (đếm), cây lời gọi, đệ quy có nhớ, tràn ngăn xếp, điền bảng, ba biến trượt, bốn câu hỏi, PHIQUA (tối ưu, tham lam sai, cấu trúc con tối ưu) | ≈ 16 phút |
| Bài 2 | Quy hoạch động trên dãy: LOINHUAN (Kadane, trạng thái “kết thúc tại i”), HAINAM (“chọn hay bỏ”, thêm chiều trạng thái) | ≈ 11 phút |
| Bài 3 | Quy hoạch động trên lưới và truy vết: THUHOACH (−∞, thứ tự điền, truy vết DRRRDDR), đếm đường đi, tam giác Pascal, giữ một hàng | ≈ 10,5 phút |

Mọi con số trong video (bảng f, g, best, dp, ways, đường đi tham lam 41 quả…) được **tính bằng code**
và có `assert` đối chiếu với đáp số trong sách.

## Kết quả (`output/`)

- `Chuong1_BaiX.mp4` + `Chuong1_BaiX.srt` — video sạch + phụ đề rời (tải lên TikTok/CapCut kèm file srt,
  hoặc dùng làm kịch bản đọc lồng tiếng).
- `Chuong1_BaiX_vietsub.mp4` — phụ đề in cứng, đặt trong dải an toàn phía trên vùng chữ của TikTok.
- `parts/Chuong1_BaiX_PhanK.*` — mỗi bài cắt thành các phần **≤ 10 phút** (giới hạn đăng trong ứng dụng TikTok),
  cắt đúng ranh giới cảnh.
- `Chuong1_Full.mp4` + `.srt` — cả chương liền mạch.

## Bố cục khung hình

Đơn vị Manim: khung rộng 9 × cao 16. Nội dung nằm trong vùng an toàn `x ∈ [-4.1, 3.4]`, `y ∈ [-3.9, 6.5]`,
tránh thanh trên cùng, cột nút bên phải và vùng tên kênh/mô tả phía dưới của TikTok. Dải `y ∈ [-5.3, -3.9]`
dành cho phụ đề.

## Thuyết minh & phụ đề

Mỗi câu thuyết minh được viết trong code bằng `with self.voice("..."):`. Thời lượng câu ước theo số âm tiết
(≈ 3,6 âm tiết/giây + nghỉ 0,45 s); các hoạt cảnh chạy trong khoảng đó, nên hình và lời luôn khớp.
`build.py` ghép mốc thời gian của mọi cảnh thành `.srt` (mỗi phụ đề ≤ 2 dòng).

## Dựng lại

```bash
pip install manim            # cần cairo, pango, ffmpeg; KHÔNG cần LaTeX
cd manim/chuong1
python build.py              # render mọi cảnh (song song) rồi ghép + tạo srt + vietsub
python build.py --no-render  # chỉ ghép lại

# Xem nhanh một cảnh ở độ phân giải thấp:
PREVIEW=1 manim render bai1.py B1_04_CayLoiGoi
```

Phông chữ: Inter (chữ) và DejaVu Sans Mono (code), đều hỗ trợ tiếng Việt.

## Cấu trúc mã

- `common.py` — cấu hình khung dọc, bảng màu, `NarratedScene` (thuyết minh → JSON), `fit_stack` (tự co giãn bố cục),
  hộp kiểu sách, ô mảng, dòng suối/hòn đá/chú ếch, khối code C++.
- `bai1.py`, `bai2.py`, `bai3.py` — các cảnh của từng bài (`B1_00_Intro` … `B3_06_TongKet`).
- `build.py` — render, ghép video, tạo `.srt`, in phụ đề, chia phần.
