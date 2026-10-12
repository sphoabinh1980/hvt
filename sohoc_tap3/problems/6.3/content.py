def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Trước hết cần **nhận dạng** số ba ước. Theo công thức số ước (Tập 1, Bài 7), x = p_{1}^{e_{1}} ··· p_{k}^{e_{k}} có (e_{1} + 1) ··· (e_{k} + 1) ước; '
        'tích này bằng 3 (số nguyên tố) chỉ khi k = 1 và e_{1} = 2. Vậy **x có đúng ba ước khi và chỉ khi x = p² với p nguyên tố**.')
    D.fig(P.fig('three'), 'Ước của 36: chỉ 4 = 2² và 9 = 3² có đúng ba ước.', 14)
    D.p('Do đó đáp số cho a là **số các số nguyên tố p mà p² chia hết a**, tức số thừa số nguyên tố của a có số mũ ≥ 2. Bài toán quy về phân tích a ra thừa số, '
        'nhưng chỉ cần biết số mũ của từng thừa số có ≥ 2 hay không.')

    D.h('2. Cách ngây thơ: Thử chia tới √a')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử chia', 11)
    D.code('Cách ngây thơ: phân tích bằng thử chia tới √a', P.src('naive.cpp'))
    D.p('Sau vòng lặp, phần còn lại (nếu > 1) là một số nguyên tố với số mũ 1, không góp gì. **Độ phức tạp:** O(√a) mỗi số, tức 10^{6} phép chia với a ≈ 10^{12}.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (a ≤ 10^{6}): mỗi số chỉ 10^{3} phép chia: **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               '**Subtask 2** (N ≤ 100): 10^{8} phép chia, kịp: **' + str(P.pts('naive.cpp', 2)) + ' điểm**.',
               '**Subtask 3** (N = 10^{5}, a ≈ 10^{12}): 10^{11} phép chia: **0 điểm**. Kể cả chỉ thử các số nguyên tố ≤ 10^{6} (78 498 số) vẫn là 7,8 · 10^{9} phép chia.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Ta đang cố tìm **mọi** thừa số của a, kể cả thừa số nguyên tố lớn tới 10^{6} hay 10^{12}. Nhưng bài chỉ hỏi về các thừa số có số mũ ≥ 2. '
                                 'Một thừa số q > 10^{4} mà q² | a thì a ≥ q²... và phần còn lại có rất ít khả năng.'])

    D.h('4. Phá bế tắc: Chỉ thử chia tới căn bậc ba')
    D.p('Bóc hết các thừa số nguyên tố p ≤ 10^{4} của a (chỉ 1229 số nguyên tố), đồng thời đếm những p có số mũ ≥ 2. Gọi r là phần còn lại. '
        'Mọi thừa số nguyên tố của r đều > 10^{4}; nếu r có từ ba thừa số trở lên thì r > (10^{4})^{3} = 10^{12} ≥ a: vô lí. Vậy r chỉ rơi vào bốn trường hợp:')
    D.fig(P.fig('cases'), 'Bốn khả năng của phần còn lại r; chỉ r = q² góp thêm một số ba ước.', 15)
    D.p('Kiểm tra r chính phương: s = ⌊√r⌋ tính bằng `sqrtl` rồi **chỉnh lại bằng phép nhân số nguyên** (giảm khi s² > r, tăng khi (s + 1)² ≤ r), '
        'vì căn bậc hai số thực có thể sai ở chữ số cuối.')
    D.sub('Chạy tay ví dụ 2')
    D.table(['a', 'Bóc thừa số ≤ 10^{4}', 'r', 'Trường hợp', 'Đáp số'], [
        ['999 966 000 289', 'không có', '999 983²', 'r = q²', '**1**'],
        ['10^{12}', '2^{12}, 5^{12}: +2', '1', 'r = 1', '**2**'],
        ['995 303 515 103', '9973²: +1', '10 007', 'r = q', '**1**'],
        ['998 696 708 677', '9973^{1}', '10 007²', 'r = q²', '**1**'],
        ['100 160 063', 'không có', '10 007 · 10 009', 'r = q · q\'', '**0**'],
    ], widths=[2, 2.2, 1.8, 1.4, 1])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12)
    D.code('BAUOC.CPP: bóc thừa số ≤ 10^4, xét phần còn lại', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** 1229 phép chia mỗi số: 1,2 · 10^{8} phép chia cho 10^{5} số, ' + tm('opt.cpp', 3) + ' trên máy chấm. Nhanh hơn cách ngây thơ khoảng 800 lần.')
    D.box('blue', 'MỞ RỘNG: KĨ THUẬT "CĂN BẬC BA"', ['Ý tưởng "bóc thừa số tới a^{1/3}, phần còn lại có ≤ 2 thừa số" còn dùng để tính **số ước** d(a) với a ≤ 10^{18}: '
        'bóc tới 10^{6}, rồi r = 1 (×1), r nguyên tố (×2, kiểm tra bằng Miller–Rabin), r = q² (×3), còn lại r = q · q\' (×4).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Đếm r = 1 là số chính phương:** 1 = 1² nhưng không phải p². Chỉ xét r > 1.',
               '**sqrt kiểu double:** với r cỡ 10^{12} vẫn thường đúng, nhưng thói quen chỉnh lại bằng phép nhân là bắt buộc khi r tới 10^{18}.',
               '**Thử chia tới 10^{6}:** đúng nhưng chậm gấp 64 lần (78 498 so với 1229 số nguyên tố).'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'opt.cpp'])
