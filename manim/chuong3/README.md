# Video Manim — Chương 3 (Bài 8, 9)

Cùng khung TikTok **1080×1920, 30 fps** và cơ chế thuyết minh → `.srt` như các chương trước
(dùng lại `chuong1/common.py` và `chuong2/bai4.Table2D` qua `shared.py`).

| Bài | Nội dung |
|---|---|
| Bài 8 · Quy hoạch động trên đoạn | Mở đầu Chương 3; trò bốc xu 3 9 1 2 (lấy đầu lớn hơn được 5, tối ưu được 11); mẹo hiệu số hơn(l, r) và cây lời gọi; điền bảng theo đường chéo, đáp án (S + D)/2; NHANMATRAN: 5 cách đặt ngoặc (5000 → 33000), phép nhân cuối chia tại k, bảng cost, truy vết ((A1A2)(A3A4)) |
| Bài 9 · Trạng thái tập con (bitmask) | 20 bạn và 654 729 075 cách ghép; tập hợp là số nguyên (11 = 1011₂ = {0, 1, 3}) và các phép toán bit; GHEPDOI (tham lam 6, tối ưu 5); đồ thị trạng thái best[mask]; đếm đường Hamilton ways[mask][v]; duyệt tập con (sub − 1) & mask và 3ⁿ |

Số liệu được tính bằng code và đối chiếu bằng `assert` với đáp số trong sách. Đồ thị 4 đỉnh trong phần
đường Hamilton là ví dụ minh họa riêng (sách chỉ nêu công thức).

```bash
cd manim/chuong3
python build.py              # render + ghép + srt + vietsub (+ chia phần nếu > 10 phút)
PREVIEW=1 manim render bai9.py B9_04_TrangThai   # xem nhanh một cảnh
```
