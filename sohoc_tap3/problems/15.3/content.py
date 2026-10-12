def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Gọi A là ma trận kề: A[u][v] = 1 nếu có tuyến u → v. Theo Tập 1, Bài 15, **A^{K}[s][t] là số hành trình độ dài K từ s tới t**: '
        'phần tử (s, t) của A^{K} = A^{K−1} · A là Σ_{u} A^{K−1}[s][u] · A[u][t], tức "đi K − 1 bước tới u, rồi một tuyến u → t".')
    D.fig(P.fig('walks'), 'Ví dụ 1: đồ thị và bốn hành trình độ dài 3 từ 1 tới 3.', 15.2)
    D.p('A^{0} = I là ma trận đơn vị: hành trình độ dài 0 chỉ có từ s về chính s. Ví dụ 2: A = [[1, 1], [1, 0]] là ma trận Q của bài 15.1, '
        'nên A^{10}[1][1] = F(11) = 89 và A^{K}[1][2] = F(K).')

    D.h('2. Cách ngây thơ: Đi từng bước')
    D.fig(P.fig('naive'), 'Sơ đồ khối của quy hoạch động theo số bước', 12)
    D.code('Cách ngây thơ: K bước, mỗi bước duyệt mọi tuyến', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(Q · K · m). Subtask 1: 10 · 1000 · 2500 = 2,5 · 10^{7}: **' + str(P.pts('naive.cpp', 1)) + ' điểm**.')

    D.h('3. Bế tắc')
    D.p('K tới 10^{18}: phải dùng lũy thừa nhanh. `mid.cpp` tính A^{K} cho mỗi câu hỏi: khoảng 120 phép nhân ma trận 50 × 50, mỗi phép 125 000 phép nhân số, '
        'tức 1,5 · 10^{7} mỗi câu hỏi. Q ≤ 10 chạy ' + P.scores['mid.cpp']['detail'][1].split()[1] + ' (**' + S('mid.cpp') + ' điểm**).')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Q = 1000 câu hỏi: 1,5 · 10^{10} phép nhân, quá thời gian. Hai lãng phí: các bình phương A^{2}, A^{4}, ... được tính lại ở **mọi** câu hỏi, '
                                  'và ta tính cả ma trận A^{K} (2500 phần tử) trong khi chỉ cần **một phần tử**.'])

    D.h('4. Phá bế tắc: Tính sẵn lũy thừa, nhân vectơ')
    D.nums(['**Dùng chung các bình phương:** P[i] = A^{2^{i}} chỉ phụ thuộc vào đồ thị; tính một lần 59 phép nhân ma trận, khoảng 7,4 · 10^{6} phép nhân số.',
            '**Chỉ cần hàng s:** A^{K}[s][·] = e_{s} · A^{K}, với e_{s} là vectơ hàng có số 1 ở vị trí s. Vì phép nhân ma trận có tính kết hợp, '
            'e_{s} · A^{K} = (((e_{s} · P[i_{1}]) · P[i_{2}]) · ...), mỗi lần là một phép **vectơ × ma trận**.'])
    D.fig(P.fig('cost'), 'Vectơ × ma trận rẻ hơn ma trận × ma trận n lần.', 15)
    D.fig(P.fig('query'), 'Trả lời một câu hỏi với K = 13.', 15.2)
    D.box('blue', 'VÌ SAO THỨ TỰ NHÂN KHÔNG QUAN TRỌNG?', ['Các P[i] đều là lũy thừa của cùng một ma trận A nên giao hoán với nhau: A^{1} · A^{4} · A^{8} = A^{8} · A^{4} · A^{1} = A^{13}. '
                                                         'Vì thế có thể duyệt bit từ thấp tới cao mà không cần đảo thứ tự.'])
    D.sub('Chống tràn khi cộng dồn 50 tích')
    D.p('Mỗi tích hai phần tử < 10^{9} + 7 là < M2 = (10^{9} + 7)^{2} ≈ 10^{18}; tổng 50 tích tới 5 · 10^{19} tràn cả unsigned long long. '
        'Mẹo: cộng dồn bằng unsigned long long, mỗi khi tổng ≥ M2 thì trừ M2 (không đổi số dư theo MOD). Tổng luôn < 2 · M2 ≈ 2 · 10^{18} < 1,8 · 10^{19}; '
        'chỉ lấy dư một lần ở cuối, nhanh hơn lấy dư sau mỗi phép cộng.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12.5)
    D.code('DUONGK.CPP: lũy thừa tính sẵn + vectơ × ma trận', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(n^{3} log K_{max} + Q · n^{2} log K) ≈ 7,4 · 10^{6} + 1000 · 60 · 2500 = 1,6 · 10^{8} phép nhân, chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '. '
        'Bộ nhớ: 60 ma trận 50 × 50 số 8 byte, 1,2 MB.')
    D.box('blue', 'MỞ RỘNG', ['Đếm hành trình độ dài **không quá** K: thêm một đỉnh "tích lũy" vào đồ thị (ma trận cỡ n + 1), hoặc lũy thừa ma trận khối [[A, I], [0, I]].',
                              'Kĩ thuật "tính sẵn lũy thừa 2^{i}, nhân vectơ" dùng cho mọi dãy truy hồi tuyến tính có nhiều câu hỏi (bài 15.2 với K lớn).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Tràn số khi cộng dồn** 50 tích: lấy dư hoặc trừ M2.',
               '**K = 0:** đáp số 1 nếu s = t; vòng lặp bit không chạy nên v = e_{s}, tự đúng.',
               '**Tuyến u → u** là hành trình độ dài 1, không phải 0.',
               '**Chỉ duyệt 31 bit** (dùng int cho K hoặc 1 << i): K tới 10^{18} cần 60 bit, dùng K >> i & 1 với K kiểu long long.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
