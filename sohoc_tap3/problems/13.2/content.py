def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Một đường đi từ O(0, 0) tới T(m, n) gồm đúng m bước sang phải và n bước lên trên; nó được xác định khi biết **những bước nào là bước sang phải**. '
        'Vậy không có ô cấm thì có C(m + n, m) đường. Từ (x_{1}, y_{1}) tới (x_{2}, y_{2}) có C((x_{2} − x_{1}) + (y_{2} − y_{1}), x_{2} − x_{1}) đường nếu x_{2} ≥ x_{1}, y_{2} ≥ y_{1}, ngược lại 0.')
    D.fig(P.fig('grid'), 'Ví dụ 2: số đường đi tới mỗi giao lộ tránh hai ô cấm (cách quy hoạch động), và phép bù trừ cho cùng đáp số 7.', 15.5)

    D.h('2. Cách ngây thơ: Quy hoạch động trên lưới')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách quy hoạch động', 12)
    D.code('Cách ngây thơ: quy hoạch động trên (m + 1)(n + 1) giao lộ', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(mn) thời gian và bộ nhớ: 10^{6} với m, n ≤ 1000, nhưng 10^{12} với m, n ≤ 10^{6}.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1**: **' + str(P.pts('naive.cpp', 1)) + ' điểm**; các subtask khác không cấp phát nổi bảng.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Quy hoạch động đếm qua **mọi** giao lộ, trong khi chỉ có tối đa hai giao lộ "đặc biệt". Hãy đếm bằng công thức, rồi trừ đi những đường đi qua ô cấm.'])

    D.h('4. Phá bế tắc: Quy tắc nhân và bù trừ')
    D.nums(['**Đường qua một ô X:** ghép một đường O → X với một đường X → T: paths(O, X) · paths(X, T) (quy tắc nhân).',
            '**Một ô cấm:** đáp số = tất cả − qua X.',
            '**Hai ô cấm A, B:** theo nguyên lí bù trừ (Bài 14): tất cả − qua A − qua B + qua cả A lẫn B.'])
    D.fig(P.fig('venn'), 'Đường qua cả hai ô: tích của ba đoạn.', 15)
    D.p('"Qua cả A lẫn B" phải xét **cả hai thứ tự**: paths(O, A)·paths(A, B)·paths(B, T) + paths(O, B)·paths(B, A)·paths(A, T). Nhiều nhất một trong hai số hạng khác 0 '
        '(chỉ khi một ô nằm phía dưới bên trái ô kia), và cả hai bằng 0 khi hai ô "không so sánh được" (ví dụ 3).')
    D.p('Chương trình `order.cpp` chỉ xét thứ tự "ô cho trước đi trước". Ví dụ 2 cho A(3, 2) trước B(1, 1): đường qua cả hai lại đi qua B trước, nên chương trình in 35 − 40 + 0 ≡ −5, sai. '
        'Qua được subtask 2 (K ≤ 1): **' + S('order.cpp') + ' điểm**.')
    D.box('purple', 'Ô CẤM TRÙNG O HOẶC T', ['Nếu X = O thì paths(O, X)·paths(X, T) = 1 · tất cả: đáp số 0, đúng. Tương tự khi X = T. Công thức tự xử lí, không cần if riêng.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 15)
    D.code('DUONGLUOI.CPP: hệ số nhị thức + bù trừ', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(m + n) chuẩn bị bảng giai thừa (chỉ số tới m + n ≤ 2 · 10^{6}), O(1) cho phần còn lại.')
    D.box('blue', 'MỞ RỘNG: NHIỀU Ô CẤM', ['Với K ô cấm (K tới vài nghìn), sắp xếp các ô theo (x, y) rồi quy hoạch động: g[i] = số đường từ O tới ô i **không qua ô cấm nào khác**, '
        'g[i] = paths(O, i) − Σ_{j trước i} g[j] · paths(j, i). Đáp số là paths(O, T) − Σ g[i] · paths(i, T). O(K²).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Chỉ xét một thứ tự** của hai ô cấm.', '**paths với ô không tới được:** phải trả về 0, không gọi C với chỉ số âm.', '**Kết quả âm** sau phép trừ: cộng MOD.', '**Bảng giai thừa tới 10^{6}:** thiếu, cần m + n.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'order.cpp', 'opt.cpp'])
