def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Cần tính Σ_{x=1..n} σ(x) với n tới 10^{12}. Không thể tính từng σ(x); ta **đếm hai lần** (Tập 1, Bài 16): xếp mọi cặp (x, i) với i | x vào một bảng, '
        'cộng theo hàng được tổng các σ(x), cộng theo cột được Σ_{i} i · (số bội của i trong [1, n]).')
    D.fig(P.fig('double'), 'Bảng các cặp (x, i) với i | x, n = 8: cộng theo hàng hay theo cột đều được 56.', 15)
    D.eq('**σ(1) + σ(2) + ... + σ(n) = Σ_{i=1..n} i · ⌊n / i⌋**')

    D.h('2. Cách ngây thơ: Tính từng σ(x)')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ', 12)
    D.code('Cách ngây thơ: σ(x) bằng duyệt ước', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n√n). n = 10^{4} là 6,7 · 10^{5} phép thử: **' + str(P.pts('naive.cpp', 1)) + ' điểm**; n = 10^{7} đã khoảng 2 · 10^{10}.')

    D.h('3. Bế tắc')
    D.p('Công thức đếm hai lần cho thuật toán O(n) (`mid.cpp`): n = 10^{7} chạy ' + P.scores['mid.cpp']['detail'][1].split()[1] + ', **' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['n = 10^{12}: vòng lặp 10^{12} bước. Nhưng ⌊n/i⌋ chỉ nhận không quá 2√n = 2 · 10^{6} giá trị khác nhau, '
                                  'và trên mỗi đoạn i cùng thương q, các số hạng i · q cộng lại thành q · (tổng các i), tính được bằng công thức.'])

    D.h('4. Phá bế tắc: Chia khối ⌊n / i⌋')
    D.fig(P.fig('stair'), 'Bậc thang ⌊20/i⌋ (ví dụ 1): 8 khối, mỗi khối góp q · (i + ... + j).', 15.2)
    D.p('Khối chứa i kết thúc tại j = ⌊n / ⌊n/i⌋⌋ (Tập 1, Bài 16). Trên khối [i, j] cùng thương q:')
    D.eq('q · (i + (i + 1) + ... + j) = q · (i + j)(j − i + 1) / 2')
    D.sub('Chia 2 trước khi lấy dư')
    D.p('Với n = 10^{12}, (i + j)(j − i + 1) tới khoảng 10^{24}: vượt long long, nhưng vừa __int128 (tới 1,7 · 10^{38}). Tích này luôn **chẵn** '
        '(một trong hai thừa số i + j, j − i + 1 chẵn), nên chia 2 trên số nguyên đúng rồi mới lấy dư.')
    D.box('purple', 'BẪY: LẤY DƯ RỒI MỚI CHIA 2', ['$s = (i + j) % MOD * ((j - i + 1) % MOD) / 2 % MOD;',
                                                   'Sau khi lấy dư, tích hai số dư có thể lẻ: phép chia 2 làm tròn xuống và sai. Với n ≤ 10^{7} thì i, j < MOD nên lấy dư không đổi gì: '
                                                   'chương trình `trap.cpp` đúng ở hai subtask đầu, sai ở subtask 3: **' + S('trap.cpp') + ' điểm**. '
                                                   'Nếu muốn lấy dư trước, phải nhân với nghịch đảo của 2 là 500 000 004.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của chia khối', 12.5)
    D.code('TONGSIGMA.CPP: chia khối ⌊n/i⌋', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(√n): khoảng 2 · 10^{6} khối với n = 10^{12}, chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Cùng kĩ thuật: số cặp (x, d) với d | x, x ≤ n, tức d(1) + ... + d(n) = Σ ⌊n/i⌋ (mỗi khối góp q · (j − i + 1)).',
                              'Bài 16.2 dùng đúng tổng này: Σ n mod i = n · k − Σ i · ⌊n/i⌋.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Lấy dư trước khi chia 2.**', '**Tính (i + j)(j − i + 1) bằng long long:** tràn khi n = 10^{12}.',
               '**Quên lấy dư q** trước khi nhân với s: q tới 10^{12}, s tới 10^{9}, tích tràn.', '**Biến i, j kiểu int.**'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'trap.cpp', 'opt.cpp'])
