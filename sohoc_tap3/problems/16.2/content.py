def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Số dư biểu diễn qua thương: **n mod i = n − i · ⌊n/i⌋** (Tập 1, Bài 1). Cộng lại với i = 1..k:')
    D.eq('**S = n · k − Σ_{i=1..k} i · ⌊n / i⌋**')
    D.p('Khi i > n thì ⌊n/i⌋ = 0: các số hạng ấy không góp gì vào tổng bên phải (n mod i = n đã nằm trọn trong n · k). '
        'Vậy tổng bên phải chỉ cần chạy tới **min(n, k)**, và nó chính là tổng của bài 16.1 bị chặn trên.')
    D.fig(P.fig('bars'), 'n mod i với n = 20, k = 24. Hàng q là ⌊20/i⌋; mỗi màu là một khối cùng thương.', 15.2)
    D.p('Ví dụ 2 (n = 5, k = 10): 5 · 10 − (1 · 5 + 2 · 2 + 3 · 1 + 4 · 1 + 5 · 1) = 50 − 21 = 29.')

    D.h('2. Cách ngây thơ: Cộng từng số dư')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ', 11)
    D.code('Cách ngây thơ: O(k)', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(k): k ≤ 10^{7} chạy ' + P.scores['naive.cpp']['detail'][0].split()[1] + ' (**' + str(P.pts('naive.cpp', 1)) + ' điểm**); k = 10^{12} thì không.')

    D.h('3. Bế tắc')
    D.box('red', 'ĐIỂM BẾ TẮC', ['k tới 10^{12}: không duyệt từng i được. Phần n · k tính ngay; phần Σ i · ⌊n/i⌋ chia khối như bài 16.1, '
                                  'nhưng có hai điều mới: khối phải dừng ở k, và k có thể lớn hơn n.'])
    D.p('Chương trình `trap.cpp` chia khối thẳng tới k: khi i > n, q = ⌊n/i⌋ = 0 và j = ⌊n/q⌋ là **phép chia cho 0**, chương trình bị lỗi chạy. '
        'Nó chỉ đúng khi k ≤ n (subtask 2): **' + S('trap.cpp') + ' điểm**, còn kém cả cách ngây thơ.')

    D.h('4. Phá bế tắc: Chia khối có chặn')
    D.nums(['Chạy i trên [1, lim] với **lim = min(n, k)**: mọi thương q ≥ 1, không chia cho 0.',
            'Điểm cuối khối **j = min(⌊n/q⌋, lim)**: khối cuối có thể bị cắt ngang tại k, các i trong phần bị cắt vẫn cùng thương q nên công thức không đổi.',
            'Mỗi khối trừ đi q · (i + j)(j − i + 1)/2 theo mô-đun; phép trừ cộng thêm p để không âm.'])
    D.box('blue', 'VÌ SAO KHỐI BỊ CẮT VẪN ĐÚNG?', ['Trong khối [i, ⌊n/q⌋] mọi chỉ số đều có thương q. Cắt bớt thành [i, k] vẫn giữ tính chất ấy; '
                                                  'ta chỉ cộng ít số hạng hơn, đúng những số hạng có chỉ số ≤ k.'])
    D.sub('Chạy tay ví dụ 1')
    D.p('n = k = 20: S = 400 − Σ i · ⌊20/i⌋ = 400 − 339 = 61 (tổng 339 tính ở bài 16.1).')
    D.sub('n = 0')
    D.p('lim = 0, vòng lặp không chạy, S = 0 · k = 0: đúng, mọi số dư bằng 0.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12.5)
    D.code('TONGDU.CPP: chia khối có chặn', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(√n), chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + ' với n = 10^{12}.')
    D.box('blue', 'MỞ RỘNG', ['Σ_{i=L..R} n mod i = S(R) − S(L − 1).',
                              'Σ_{i=1..n} ⌊n/i⌋ · i^{2}: trên khối dùng 1^{2} + ... + r^{2} = r(r + 1)(2r + 1)/6 (bài 16.3).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Chia khối tới k khi k > n:** chia cho 0.',
               '**n · k không lấy dư trước:** 10^{24} tràn.',
               '**Phép trừ theo mô-đun ra số âm:** cộng MOD.',
               '**Tổng khối không dùng __int128** hoặc lấy dư trước khi chia 2 (bẫy của bài 16.1).'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'trap.cpp', 'opt.cpp'])
