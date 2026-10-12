def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Cần nghịch đảo theo mô-đun nguyên tố p của **mọi** số 1, 2, ..., n với n tới 10^{7}, rồi in hai "mã kiểm tra" (tổng theo mô-đun và xor). '
        'Mỗi nghịch đảo riêng lẻ thì đã biết cách tính; cái khó là tính **10^{7}** nghịch đảo trong 1 giây.')

    D.h('2. Cách ngây thơ: Thử mọi x')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử mọi x', 13)
    D.code('Cách ngây thơ: thử x cho tới khi i · x ≡ 1', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** tới p − 1 lần thử cho mỗi i: 1000 · 10^{6} = 10^{9} phép chia lấy dư ngay ở subtask 1. Cách này **không qua nổi subtask nào**.')

    D.h('3. Bế tắc')
    D.p('Cải tiến đầu tiên: nghịch đảo bằng định lí Fermat, inv(i) = i^{p − 2} mod p, khoảng 2 · 31 = 62 phép nhân mỗi số. Chương trình `fermat.cpp` qua subtask 1, 2 '
        '(n ≤ 10^{6}: 6 · 10^{7} phép nhân, ' + tm('fermat.cpp', 2) + '), nhưng n = 10^{7} cần 6 · 10^{8} phép nhân và chia lấy dư: **' + S('fermat.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Mỗi nghịch đảo vẫn được tính độc lập, dù các số 1..n có quan hệ chặt chẽ với nhau. Có cách nào lấy nghịch đảo của i từ nghịch đảo của một số **nhỏ hơn** đã tính?'])

    D.h('4. Phá bế tắc: Công thức truy hồi')
    D.p('Chia p cho i: p = q · i + r với q = ⌊p/i⌋, r = p mod i. Biến đổi theo mô-đun p:')
    D.fig(P.fig('derive'), 'Suy ra công thức truy hồi cho nghịch đảo.', 15.5)
    D.eq('**inv[i] = (p − ⌊p/i⌋) · inv[p mod i] mod p,   inv[1] = 1.**')
    D.p('Vì p mod i < i, khi duyệt i tăng dần thì inv[p mod i] luôn có sẵn: mỗi nghịch đảo chỉ tốn **một phép nhân và hai phép chia**.')
    D.fig(P.fig('table'), 'Bảng truy hồi với p = 11 (ví dụ 1). Hàng cuối là một hoán vị của 1..10.', 15.5)
    D.box('purple', 'CHỐNG TRÀN SỐ VÀ TIẾT KIỆM BỘ NHỚ', ['- (p − q) · inv[r] < p · p < 4 · 10^{18}: vừa long long nhưng không vừa int; ép sang long long trước khi nhân.',
        '- Mảng inv có 10^{7} phần tử, mỗi phần tử < p < 2^{31}: dùng `unsigned int` (40 MB) thay vì long long (80 MB).',
        '- H cộng dồn theo mô-đun; X lấy xor trên **giá trị thật** inv(i) ∈ [1, p − 1], không lấy dư.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 13)
    D.code('NGHICHDAO.CPP: nghịch đảo của 1..n trong O(n)', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(n) thời gian, O(n) bộ nhớ; n = 10^{7} chạy trong ' + tm('opt.cpp', 3) + '.')
    D.box('blue', 'MỞ RỘNG: NGHỊCH ĐẢO CỦA DÃY BẤT KÌ', ['Muốn nghịch đảo n số a_{1}, ..., a_{n} bất kì (không phải 1..n), dùng mẹo **tích tiền tố**: '
        'tính P_{i} = a_{1} ··· a_{i}, lấy nghịch đảo một lần của P_{n}, rồi đi ngược: a_{i}^{−1} = P_{i}^{−1} · P_{i−1}, P_{i−1}^{−1} = P_{i}^{−1} · a_{i}. '
        'Tổng cộng 3n phép nhân và một lần lũy thừa. Cũng là cách tính bảng nghịch đảo giai thừa ở Bài 13.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Tích tràn int:** (p − q) · inv[r] tới 4 · 10^{18}.', '**Mảng long long 80 MB:** vẫn vừa 256 MB nhưng chậm hơn vì tốn bộ nhớ đệm.',
               '**Lấy dư X theo p:** X là xor của giá trị thật, không lấy dư.', '**Dùng `-q * inv[r] % p`:** kết quả âm; dùng p − q.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'fermat.cpp', 'opt.cpp'])
