def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Đặt **f(n) = popcount(0) + popcount(1) + ... + popcount(n)**. Như tổng đoạn là hiệu hai tổng tiền tố, đáp số mỗi màn là **f(R) − f(L − 1)**. '
        'Việc còn lại là tính f(n) với n tới 10^{18}: thay vì cộng theo **hàng** (từng số), ta cộng theo **cột** (từng bit), như bài DEMBIT của Tập 1.')
    D.fig(P.fig('table'), 'Bảng nhị phân của 0..12 và công thức đếm theo cột.', 15.2)

    D.h('2. Cách ngây thơ: Cộng từng số')
    D.code('Cách ngây thơ', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(R − L) mỗi màn: Q ≤ 10, R ≤ 10^{6} chạy ngay (**' + str(P.pts('naive.cpp', 1)) + ' điểm**); 10^{5} màn với đoạn dài thì không.')

    D.h('3. Bế tắc')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Mỗi màn có thể dài 10^{18} số. Nhưng cột bit k của dãy 0, 1, 2, ... **tuần hoàn**: 2^{k} số 0 rồi 2^{k} số 1. '
                                  'Số bit 1 trong một cột chỉ phụ thuộc vào số chu kì trọn vẹn và phần lẻ cuối.'])

    D.h('4. Phá bế tắc: Đếm theo cột')
    D.p('Có n + 1 số từ 0 tới n. Ở cột k, chia n + 1 cho chu kì 2^{k+1} được thương q, dư r: q chu kì trọn vẹn góp q · 2^{k} bit 1; '
        'phần lẻ r số cuối bắt đầu bằng 2^{k} số 0, nên góp max(0, r − 2^{k}). Cộng 61 cột (2^{60} > 10^{18}):')
    D.eq('**f(n) = Σ_{k=0..60} [ q_{k} · 2^{k} + max(0, r_{k} − 2^{k}) ]**')
    D.p('Chương trình `mid.cpp` cài đặt đúng công thức này bằng long long: đúng tới R ≤ 10^{17} (f(10^{17}) ≈ 2,8 · 10^{18}), sai ở subtask 3: **' + S('mid.cpp') + ' điểm**.')
    D.box('purple', 'BẪY: ĐÁP SỐ VƯỢT 2⁶⁴', ['f(10^{18}) = 29 761 222 783 429 247 000 ≈ 2,98 · 10^{19} > 2^{64} ≈ 1,84 · 10^{19}: tràn cả unsigned long long. '
                                             'Ví dụ 2 cho thấy chính đáp số (L = 1) cũng vượt 2^{64}, nên không có mẹo "chỉ trừ cho khéo".',
                                             'Sửa: tích lũy bằng **unsigned __int128** (tới 3,4 · 10^{38}) và tự viết hàm in, vì printf không có định dạng cho __int128.'])
    D.sub('Chạy tay ví dụ 1, màn thứ hai')
    D.p('f(7): n + 1 = 8. Cột 0: 8 = 4 · 2 + 0 → 4; cột 1: 8 = 2 · 4 + 0 → 4; cột 2: 8 = 1 · 8 + 0 → 4; cột 3: 8 = 0 · 16 + 8 → max(0, 8 − 8) = 0. f(7) = 12. '
        'f(4): n + 1 = 5. Cột 0: 2 · 1 + max(0, 1 − 1) = 2; cột 1: 1 · 2 + max(0, 1 − 2) = 2; cột 2: 0 + max(0, 5 − 4) = 1. f(4) = 5. Đáp số 12 − 5 = 7.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của một màn', 13)
    D.code('BITDOAN.CPP: đếm theo cột, unsigned __int128', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(log R) mỗi màn, tức 122 bước; 10^{5} màn chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Đếm số bit 0 (không tính các số 0 ở đầu) hoặc tổng các chữ số trong cơ số 10 của 1..n: cùng ý tưởng "đếm theo cột", chu kì 10^{k+1}.',
                              'Đếm số x ∈ [L, R] có đúng k bit 1: bài 18.3.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**1 << k** với k > 31: dùng 1LL << k.', '**Đáp số vượt 2^{64}**: cần unsigned __int128.', '**L = 1:** cần f(0) = 0; f(−1) cũng phải bằng 0 nếu cho phép L = 0.',
               '**Duyệt k tới 59:** 10^{18} < 2^{60} nên cột 59 có bit 1; duyệt tới 60 cho an toàn.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
