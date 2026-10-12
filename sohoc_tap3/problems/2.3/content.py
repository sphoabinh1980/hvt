def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Cần tìm mọi cặp a < b ≤ N với s(a) = b + k và s(b) = a + k, trong đó s(n) là tổng các ước thực sự của n. '
        'Nhìn kĩ điều kiện thứ nhất: **với mỗi a, chỉ có đúng một ứng viên b = s(a) − k**. Vậy bài toán thực chất là: '
        '**tính được s(n) cho mọi n ≤ N**, rồi kiểm tra từng a trong O(1).')
    D.fig(P.fig('amicable'), 'Cặp số bạn bè 220 và 284 (k = 0): tổng ước thực sự của số này bằng số kia.', 15)
    D.p('Ràng buộc then chốt: N tới 10^{7}, giới hạn **2 giây** và **chỉ 64 MB** bộ nhớ.')

    D.h('2. Cách ngây thơ: Tính s(n) bằng thử ước')
    D.p('Viết hàm s(n) thử mọi d < n; với mỗi a tính b = s(a) − k, kiểm tra a < b ≤ N rồi tính tiếp s(b).')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ', 11)
    D.code('Cách ngây thơ: s(n) bằng thử mọi ước, O(N²)', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** mỗi lần gọi s(n) tốn O(n), cả bài O(N^{2}): 4 · 10^{6} với N = 2000, nhưng 4 · 10^{10} với N = 2 · 10^{5}.')

    D.h('3. Bế tắc')
    D.bullets([
        '**Subtask 1** (N ≤ 2000): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
        'Thay hàm s(n) bằng cách duyệt cặp ước tới √n (bài 2.1), ta được `mid.cpp` với O(N√N): N = 2 · 10^{5} chỉ mất ' + tm('mid.cpp', 2) +
        ', qua thêm **subtask 2**: tổng **' + S('mid.cpp') + ' điểm**.',
        '**Subtask 3** (N = 10^{7}): N√N ≈ 3,2 · 10^{10} phép chia: quá giới hạn.'])
    D.box('red', 'ĐIỂM BẾ TẮC', [
        'Mỗi số n bị "hỏi" riêng: n có những ước nào? Nhưng các câu hỏi này trùng lặp rất nhiều: số 3 là ước của 6, 9, 12, ... và ta đã phát hiện lại '
        'điều đó ở mỗi số. Hãy **đảo chiều câu hỏi**: d là ước của những số nào?'])

    D.h('4. Phá bế tắc: Sàng điều hòa')
    D.p('d là ước thực sự của đúng các số 2d, 3d, 4d, ... Vậy với mỗi d, ta cộng d vào s[2d], s[3d], s[4d], ...; '
        'sau khi duyệt hết d từ 1 tới N/2, mảng s chứa đúng tổng ước thực sự của mọi số.')
    D.fig(P.fig('sieve'), 'Sàng điều hòa với N = 12: hàng d cộng d vào các bội 2d, 3d, ... của nó; hàng cuối là s(m).', 15)
    D.box('purple', 'VÌ SAO NHANH: TỔNG ĐIỀU HÒA', [
        'Với mỗi d, vòng trong chạy N/d − 1 lần. Tổng số phép cộng là N/1 + N/2 + ... + N/(N/2) ≈ N · ln N (tổng điều hòa 1 + 1/2 + 1/3 + ... ≈ ln N). '
        'Với N = 10^{7}: khoảng 1,5 · 10^{8} phép cộng, nhanh hơn N√N gần 200 lần. Tên "sàng điều hòa" đến từ chính tổng ấy.'])
    D.sub('Bẫy bộ nhớ: 64 MB')
    D.p('Thói quen "dùng long long cho chắc" ở đây phải trả giá đắt. Mảng 10^{7} số long long chiếm 80 MB: chương trình `ll.cpp` (giống hệt lời giải mẫu, '
        'chỉ khác kiểu của mảng s) **không chạy nổi dù chỉ một test**, vì bộ nhớ khai báo tĩnh đã vượt giới hạn ngay khi khởi động: **' + S('ll.cpp') + ' điểm**.')
    D.fig(P.fig('memory'), 'Mảng s kiểu int vừa giới hạn 64 MB; kiểu long long thì không.', 13)
    D.p('Kiểu int là đủ vì s(n) < σ(n) ≤ 45 732 192 với mọi n ≤ 10^{7}. Chỉ có một chỗ cần cẩn thận: b = s(a) − k có thể âm (khi k > s(a)), '
        'và a + k có thể tới 2 · 10^{7}: ta so sánh bằng long long để không phải suy nghĩ thêm.')
    D.sub('Chạy tay ví dụ 2 (N = 200, k = 1)')
    D.table(['a', 's(a)', 'b = s(a) − 1', 'a < b ≤ 200?', 's(b)', 's(b) = a + 1?'], [
        ['48', '76', '75', 'có', '49', '**có** → (48, 75)'],
        ['75', '49', '48', 'không (b < a)', '–', '–'],
        ['140', '196', '195', 'có', '141', '**có** → (140, 195)'],
        ['12', '16', '15', 'có', '9', 'không'],
        ['120', '240', '239', 'không (b > N)', '–', '–'],
    ], widths=[0.8, 0.9, 1.3, 1.7, 0.9, 2])
    D.p('Điều kiện a < b đảm bảo mỗi cặp chỉ được in một lần (khi duyệt tới a = 75 thì ứng viên 48 < 75 bị loại).')

    D.h('5. Cách tối ưu: Sàng điều hòa với mảng int')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12)
    D.code('BANBE.CPP: sàng điều hòa, O(N log N), 40 MB', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(N log N) thời gian (khoảng 1,5 · 10^{8} phép cộng), O(N) bộ nhớ (40 MB). Test lớn nhất mất ' + tm('opt.cpp', 3) + '.')
    D.box('blue', 'MỞ RỘNG: SÀNG NHANH HƠN', [
        'Có thể tính σ(n) cho mọi n ≤ N trong O(N) bằng sàng tuyến tính kết hợp tính chất nhân tính σ(p^{e} · m) = σ(p^{e}) · σ(m) (Bài 7). '
        'Nhưng ở đây sàng điều hòa đơn giản đã đủ nhanh, và ít chỗ sai hơn nhiều.'])
    D.h('6. Bẫy thường gặp')
    D.bullets([
        '**Mảng long long 80 MB** vượt giới hạn 64 MB: mất toàn bộ điểm, kể cả các subtask nhỏ.',
        '**Truy cập s[b] khi b ngoài [1, N]:** b có thể âm hoặc lớn hơn N. Kiểm tra a < b ≤ N **trước** khi đọc s[b] (toán tử && dừng sớm).',
        '**In trùng cặp:** quên điều kiện a < b thì mỗi cặp được in hai lần.',
        '**Khai báo mảng 10^{7} trong main:** tràn bộ nhớ ngăn xếp; khai báo toàn cục.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'll.cpp', 'opt.cpp'])
