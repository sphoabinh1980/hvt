def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Cần hai con số: B (điểm nguyên trên biên) và I (điểm nguyên nằm hẳn bên trong). Ba công cụ của Tập 1, Bài 20 trả lời đủ:')
    D.bullets(['**B = Σ gcd(|dx|, |dy|)** theo mọi cạnh, kể cả cạnh P_{n}P_{1} (bài 20.1, nhưng đường khép kín: không cộng thêm 1).',
               '**Công thức dây giày:** 2S = |Σ (x_{i} y_{i+1} − x_{i+1} y_{i})|, là số nguyên.',
               '**Định lí Pick:** S = I + B/2 − 1, suy ra **I = (2S − B + 2) / 2**.'])
    D.fig(P.fig('pick'), 'Ví dụ 1: 16 điểm trên biên, 22 điểm bên trong.', 15.2)

    D.h('2. Cách ngây thơ: Thử từng điểm')
    D.code('Cách ngây thơ: kiểm tra mọi điểm nguyên trong hình chữ nhật bao', P.src('naive.cpp'))
    D.p('Mỗi điểm trong hình chữ nhật bao: kiểm tra có nằm trên cạnh nào không (tích chéo bằng 0 và nằm giữa hai đầu mút), nếu không thì kiểm tra trong/ngoài bằng tia sang phải. '
        'O(diện tích · n): với tọa độ ≤ 100, n ≤ 100 là 4 · 10^{4} · 100 · 2 = 8 · 10^{6}: **' + S('naive.cpp') + ' điểm**. Tọa độ tới 10^{6}: 4 · 10^{12} điểm.')

    D.h('3. Bế tắc')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Số điểm cần đếm tới cỡ 4 · 10^{12}: không thể liệt kê. Phải tính I từ những đại lượng tính được trên các **cạnh**: diện tích và số điểm trên biên.'])

    D.h('4. Phá bế tắc: Dây giày + Pick')
    D.p('Một vòng lặp qua n cạnh cho đồng thời 2S và B, rồi I = (2S − B + 2)/2. Phép chia 2 luôn chia hết vì Pick bảo đảm 2S − B + 2 = 2I.')
    D.box('purple', 'BẪY: LẤY TRỊ TUYỆT ĐỐI TỪNG SỐ HẠNG', ['$S2 += llabs(x[i] * y[j] - x[j] * y[i]);',
                                                          'Mỗi số hạng x_{i} y_{i+1} − x_{i+1} y_{i} là 2 lần diện tích **có dấu** của tam giác O P_{i} P_{i+1}; dấu chính là thứ làm phần thừa bên ngoài đa giác tự triệt tiêu. '
                                                          'Chỉ lấy trị tuyệt đối **sau khi cộng hết** (để xử lí trường hợp đỉnh liệt kê theo chiều kim đồng hồ, ví dụ 2). '
                                                          'Chương trình `trap.cpp` sai ở mọi subtask: **' + S('trap.cpp') + ' điểm**.'])
    D.sub('Ví dụ 2: chiều kim đồng hồ và đỉnh thẳng hàng')
    D.p('Tổng dây giày bằng 0 + 0 − 8 − 8 + 0 = −16, lấy trị tuyệt đối 2S = 16. Đỉnh (2, 2) nằm giữa cạnh (0, 4)–(4, 0): hai cạnh (0,4)–(2,2) và (2,2)–(4,0) có gcd 2 và 2, '
        'tổng bằng gcd 4 của cả cạnh: công thức không cần xử lí riêng. B = 4 + 2 + 2 + 4 = 12, I = (16 − 12 + 2)/2 = 3.')
    D.box('blue', 'KIỂU DỮ LIỆU', ['|x|, |y| ≤ 10^{6}: mỗi tích tới 10^{12}, tổng n = 10^{5} số hạng tới cỡ 10^{17}: long long đủ. Đừng dùng double: 2S là số nguyên, hãy giữ nó nguyên.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối', 12.5)
    D.code('DAGIAC.CPP: dây giày + Pick', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(n log C); chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Số điểm nguyên trong **hoặc trên** biên: I + B = (2S + B + 2)/2.',
                              'Pick chỉ đúng với đa giác đơn (không tự cắt) có đỉnh nguyên. Với đa giác có lỗ thủng, công thức trở thành S = I + B/2 − 1 + h (h là số lỗ).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Trị tuyệt đối từng số hạng.**', '**Quên cạnh P_{n}P_{1}** trong cả 2S lẫn B.', '**Cộng gcd + 1 cho mỗi cạnh:** mỗi đỉnh bị đếm hai lần.',
               '**Chia 2 sớm** (tính S = 2S/2 rồi dùng S): mất phần lẻ 0,5.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'trap.cpp', 'opt.cpp'])
