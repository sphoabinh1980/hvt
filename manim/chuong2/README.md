# Video Manim — Chương 2 (Bài 4, 5, 6, 7)

Tiếp nối `../chuong1`: cùng khung TikTok **1080×1920, 30 fps**, cùng phong cách và cơ chế thuyết minh → `.srt`.
Mã dùng lại `common.py`, `list_cards`, `line_box` của Chương 1 qua `shared.py`.

| Bài | Nội dung |
|---|---|
| Bài 4 · Cái túi 0/1 và không giới hạn | Mở đầu Chương 2; xe cứu trợ (tham lam theo tỉ số 39 so với tối ưu 42); cây quyết định với trạng thái (3, 5) lặp; bảng f(i, c) điền từng hàng; truy vết chọn kiện 2, 3; một mảng duyệt giảm và lỗi duyệt tăng (lấy một kiện 3 lần); cái túi không giới hạn; DOITEM: 4 tổ hợp so với 9 dãy, quy tắc thứ tự vòng lặp |
| Bài 5 · Cái túi mở rộng | KHOHANG (đáp án 26); tách nhị phân 13 = 1 + 2 + 4 + 6 có minh họa ghép mọi số từ 0 đến 13; BALOVANG đổi vai, bảng lightest dọc (đáp án 7); nguyên tắc chọn chiều cho bảng; tổng con với bitset (dịch và OR) |
| Bài 6 · Dãy con tăng dài nhất | Cắm cờ trên đồi; O(n²) với mảng cha, truy vết 4 7 8 9; mảng d chạy từng bước (nối/thay, vùng tìm nhị phân); cảnh báo d không phải đáp án; xếp toa tàu (Dilworth) |
| Bài 7 · Quy hoạch động trên hai xâu | Bộ gõ đoán từ HOXINHH → HOCSINH, gióng hàng hai xâu; đệ quy 3 nhánh và 25 triệu cặp (i, j); bảng d với ba ô chéo/trên/trái, đáp án 3; truy vết ra chèn C, thay X → S, xóa H; hai hàng; LCS ACCGTA/CAGTTA = AGTA và công thức \|s\| + \|t\| − 2L |

Mọi bảng số được tính bằng code và đối chiếu bằng `assert` với đáp số trong sách
(42, 52, 4/9 cách, 26, lightest(9) = 1250, d = 2 3 6 9, 4 đoàn tàu, d(7, 7) = 3, AGTA, …).

## Dựng lại

```bash
cd manim/chuong2
python build.py              # render + ghép + srt + vietsub + chia phần ≤ 10 phút
python build.py --lessons Bai7   # chỉ render/ghép một bài (cả chương vẫn được ghép lại)
PREVIEW=1 manim render bai4.py B4_03_BangF   # xem nhanh một cảnh
```

Kết quả trong `output/`: `Chuong2_BaiX.mp4/.srt`, `Chuong2_BaiX_vietsub.mp4`, `parts/…_PhanK.*`, `Chuong2_Full.srt`.
