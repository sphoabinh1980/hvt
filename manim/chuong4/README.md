# Video Manim — Chương 4 (Bài 13, 14)

Cùng khung TikTok **1080×1920, 30 fps** và cơ chế thuyết minh → `.srt` như các chương trước
(dùng lại `chuong1/common.py` qua `shared.py`).

| Bài | Nội dung |
|---|---|
| Bài 13 · Mảng cộng dồn và hàng đợi đơn điệu | Mở đầu Chương 4 (giữ công thức, đổi cách tính); ếch nhảy 2..300 000; DEMCACHNHAY 7 2 3 (3 cách: 2+2+3, 2+3+2, 3+2+2); bảng f điền theo đoạn [i − R, i − L]; hai đoạn gần trùng nhau; mảng S chạy song song: f(7) = S[6] − S[4] = 3; trừ trong đồng dư (+ MOD); NHAYXA (đường 0 → 1 → 4 → 7 → 8, đáp án 10); ứng viên vô dụng; deque chạy tay từng bước; phân tích khấu hao |
| Bài 14 · Cây Fenwick và lũy thừa ma trận | DEMDAYTANG 3 1 4 1 5 (5 + 6 + 2 = 13); QHĐ O(n²) f = 1 1 3 1 7; tổng tiền tố trên trục giá trị; nén giá trị → 2 1 3 1 4; cây Fenwick 8 ô với đường hỏi 7 → 6 → 4 và thêm 3 → 4 → 8; chạy tay trên trục hạng; Fenwick cho max; MATMADEN (7, 17, 41); đồ thị chuyển màu, ma trận M; lũy thừa nhanh M¹³ = M⁸·M⁴·M¹; điều kiện dùng ma trận; bảng nhận dạng công cụ; tổng kết toàn bộ 14 bài |

Mọi số liệu được tính bằng code và đối chiếu bằng `assert` với đáp số trong sách (kể cả câu hỏi tự kiểm tra:
4 cách, k = 2 cho 7, 1 2 3 cho 7 dãy, n = 4 cho 41).

```bash
cd manim/chuong4
python build.py              # render + ghép + srt + vietsub (+ chia phần nếu > 10 phút)
PREVIEW=1 manim render bai13.py B13_05_HangDoi   # xem nhanh một cảnh
```
