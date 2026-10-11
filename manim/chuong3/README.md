# Video Manim — Chương 3 (Bài 8 – 12)

Cùng khung TikTok **1080×1920, 30 fps** và cơ chế thuyết minh → `.srt` như các chương trước
(dùng lại `chuong1/common.py` và `chuong2/bai4.Table2D` qua `shared.py`).

| Bài | Nội dung |
|---|---|
| Bài 8 · Quy hoạch động trên đoạn | Mở đầu Chương 3; trò bốc xu 3 9 1 2 (lấy đầu lớn hơn được 5, tối ưu được 11); mẹo hiệu số hơn(l, r) và cây lời gọi; điền bảng theo đường chéo, đáp án (S + D)/2; NHANMATRAN: 5 cách đặt ngoặc (5000 → 33000), phép nhân cuối chia tại k, bảng cost, truy vết ((A1A2)(A3A4)) |
| Bài 9 · Trạng thái tập con (bitmask) | 20 bạn và 654 729 075 cách ghép; tập hợp là số nguyên (11 = 1011₂ = {0, 1, 3}) và các phép toán bit; GHEPDOI (tham lam 6, tối ưu 5); đồ thị trạng thái best[mask]; đếm đường Hamilton ways[mask][v]; duyệt tập con (sub − 1) & mask và 3ⁿ |
| Bài 10 · Quy hoạch động chữ số | Số may mắn bậc 5 từ 1 đến 30 (5, 14, 19, 23, 28) và 10¹⁸ (> 30 năm); SOMAYMAN (đáp án 142 857 142 856 594 041); "1 _ _" và "6 _ _" cùng 20 đuôi; count(R) − count(L − 1); cây các số ≤ 274 với đường bị chặn duy nhất; countFrom(pos, rem, tight); chạy tay N = 30 (count = 6, đáp án 5); chỉ nhớ trạng thái tự do, O(19·K·10); khuôn mẫu và bảng STATE |
| Bài 11 · Quy hoạch động trên cây | Dạ tiệc: tham lam mời người 3 được 15, tối ưu 19; DATIEC với cặp (moi, khong) tính từ lá lên gốc; nguy cơ tràn ngăn xếp và thứ tự BFS ngược; vì sao đúng; đổi gốc KHOANGCACH: size, kq(1) = 8, kq(c) = kq(v) − size(c) + (n − size(c)) ⇒ 8 8 10 12 12 14 |
| Bài 12 · Đếm, DAG, xác suất, kì vọng | Ba câu hỏi một ý tưởng; DUONGMOTCHIEU (4 đường); bậc thang 2ᵏ; thuật toán Kahn chạy từng bước (thứ tự 1 2 3 5 4 6); đẩy ways theo thứ tự tô pô; mọi bài QHĐ là một DAG; đường dài nhất; XUCXAC (6/36, 54/216) với biểu đồ phân bố; kì vọng E[s] tính ngược, E[0] = (7/6)⁵ ≈ 2,1614; tổng kết Chương 3 |

Số liệu được tính bằng code và đối chiếu bằng `assert` với đáp số trong sách (kể cả câu hỏi tự kiểm tra:
9 số, 15, 12, 5 đường, 3/36, 7/6). Đồ thị 4 đỉnh trong phần
đường Hamilton là ví dụ minh họa riêng (sách chỉ nêu công thức).

```bash
cd manim/chuong3
python build.py              # render + ghép + srt + vietsub (+ chia phần nếu > 10 phút)
python build.py --lessons Bai10 Bai11   # chỉ render các bài này
PREVIEW=1 manim render bai9.py B9_04_TrangThai   # xem nhanh một cảnh
```
