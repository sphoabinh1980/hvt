def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('x **không** nguyên tố cùng nhau với n khi và chỉ khi x chia hết cho ít nhất một **ước nguyên tố** của n. '
        'Gọi p_{1}, ..., p_{k} là các ước nguyên tố phân biệt của n, A_{i} là tập bội của p_{i} trong [1, N]. Đáp số là N − |A_{1} ∪ ... ∪ A_{k}|, '
        'và theo nguyên lí bù trừ (Tập 1, Bài 14):')
    D.eq('**đáp số = Σ_{S ⊆ {p_{1}, ..., p_{k}}} (−1)^{|S|} · ⌊N / d_{S}⌋**,   d_{S} = tích các số trong S (d_{∅} = 1).')
    D.p('Bài toán tách thành hai việc: **phân tích n** để lấy danh sách p_{i}, rồi **duyệt 2^{k} tập con**.')
    D.fig(P.fig('grid'), 'Ví dụ 1, câu hỏi thứ nhất (n = 30, N = 100): 8 tập con của {2, 3, 5}.', 15.2)
    D.p('Với n = 12 = 2^{2} · 3 chỉ dùng {2, 3}: 12 − 6 − 4 + 2 = 4 = φ(12). Khi N = n, công thức chính là φ(n) = n · Π(1 − 1/p).')

    D.h('2. Cách ngây thơ: Duyệt mọi x')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách duyệt', 11)
    D.code('Cách ngây thơ: đếm x với gcd(x, n) = 1', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(Q · N · log n). Subtask 1 có Q ≤ 10, N ≤ 10^{6}: 10^{7} lần gcd, chạy ' + P.scores['naive.cpp']['detail'][0].split()[1] + '.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1**: **' + str(P.pts('naive.cpp', 1)) + ' điểm**; với N = 10^{12} vòng lặp vô vọng.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Bù trừ chỉ cần 2^{k} phép chia, nhưng trước đó phải **phân tích n ≤ 10^{12}**: thử chia tới √n = 10^{6}. '
                                  'Với n là số nguyên tố lớn, mỗi câu hỏi tốn 10^{6} phép chia; 1000 câu hỏi là 10^{9} phép chia 64 bit.'])
    D.p('Chương trình `mid.cpp` đã dùng bù trừ nhưng phân tích n bằng cách thử mọi d = 2, 3, 4, ...: ổn với Q ≤ 10 (subtask 2, '
        + P.scores['mid.cpp']['detail'][1].split()[1] + '), nhưng quá thời gian ở subtask 3: **' + S('mid.cpp') + ' điểm**.')

    D.h('4. Phá bế tắc: Chỉ thử chia các số nguyên tố')
    D.fig(P.fig('trial'), 'Số phép chia khi phân tích một số nguyên tố cỡ 10¹².', 15)
    D.p('Trong vòng thử chia, mỗi khi gặp p | n ta chia hết p khỏi n. Vì vậy khi tới một hợp số d, mọi ước nguyên tố của d (nhỏ hơn d) đã bị loại khỏi n, '
        'nên d không bao giờ chia hết n: thử hợp số là phí công. Sàng Eratosthenes một lần cho 78 498 số nguyên tố ≤ 10^{6}; '
        'mỗi câu hỏi chỉ duyệt danh sách này, nhanh hơn khoảng 13 lần.')
    D.box('blue', 'VÌ SAO PHẦN CÒN LẠI LÀ SỐ NGUYÊN TỐ?', ['Sau khi thử hết p với p^{2} ≤ n (n là phần còn lại), nếu n > 1 thì n không có ước nguyên tố nào ≤ √n, '
                                                       'nên n là số nguyên tố. Ví dụ n = 999 999 999 989: vòng lặp chạy hết mà không chia được, ps = {999 999 999 989}.'])
    D.sub('Có bao nhiêu tập con?')
    D.p('Tích 12 số nguyên tố đầu tiên là 7 420 738 134 810 > 10^{12}, nên k ≤ 11 và có tối đa 2^{11} = 2048 tập con. '
        'Mọi tích d_{S} là ước của n nên d_{S} ≤ 10^{12}: không tràn long long. Ví dụ 2, câu hỏi 2: n = 2 · 3 · 5 · ... · 31, đủ 2048 tập con.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12.5)
    D.code('NTCN.CPP: sàng + phân tích + bù trừ', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** sàng O(10^{6} log log 10^{6}); mỗi câu hỏi O(π(√n) + 2^{k} · k) ≈ 78 498 + 22 528 phép tính. '
        'Subtask 3 chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Đếm số x ∈ [L, R] nguyên tố cùng nhau với n: f(R) − f(L − 1).',
                              'Có thể bớt phép nhân bằng cách sinh tập con theo DFS (mang theo tích và dấu), hoặc chỉ giữ các tập con có tích ≤ N: tích > N cho ⌊N/d⌋ = 0.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Bù trừ trên mọi ước** (hoặc dùng 4 cho n = 12) thay vì chỉ ước nguyên tố phân biệt.',
               '**Quên ước nguyên tố lớn còn lại** sau vòng thử chia, ví dụ n = 2 · 499 999 999 979: phần còn lại là một số nguyên tố lớn (với n ≤ 10^{12}, còn lại tối đa một số như vậy).',
               '**Thử chia mọi d** cho 1000 câu hỏi: quá thời gian.',
               '**Dùng int** cho p * p hoặc cho tích d_{S}.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
