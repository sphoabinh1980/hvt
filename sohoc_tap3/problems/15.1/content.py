def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Gọi T(n) là số cách lát hành lang 2 × n. Liệt kê tay với n nhỏ:')
    D.fig(P.fig('gallery'), 'Mọi cách lát với n = 1, 2, 3, 4 (viên dọc màu xanh, cặp viên ngang màu cam).', 13)
    D.p('Dãy 1, 2, 3, 5 gợi ý ngay Fibonacci. Để chắc chắn, nhìn vào **cột cuối cùng** của hành lang:')
    D.fig(P.fig('lastcol'), 'Hai cách phủ phần cuối hành lang.', 15)
    D.bullets(['Cột cuối là **một viên dọc**: phần còn lại là hành lang 2 × (n − 1), có T(n − 1) cách.',
               'Cột cuối bị phủ bởi **viên ngang**: ô còn lại của cột cuối buộc phải là một viên ngang nữa, chồng lên viên kia; phần còn lại là 2 × (n − 2).'])
    D.eq('**T(n) = T(n − 1) + T(n − 2),  T(0) = T(1) = 1  ⇒  T(n) = F(n + 1)**')
    D.p('(với F(1) = F(2) = 1). Bài toán quy về: tính số Fibonacci thứ n + 1 theo mô-đun, với n tới 10^{18}.')

    D.h('2. Cách ngây thơ: Đệ quy theo công thức')
    D.code('Cách ngây thơ: đệ quy', P.src('naive.cpp'))
    D.fig(P.fig('tree'), 'Cây đệ quy của T(6): các bài toán con bị tính lại rất nhiều lần.', 14)
    D.p('**Độ phức tạp:** O(F(n)) ≈ O(1,62^{n}) mỗi hành lang. n ≤ 20 cho khoảng 2 · 10^{4} lời gọi, 1000 hành lang vẫn nhanh: **'
        + str(P.pts('naive.cpp', 1)) + ' điểm** subtask 1. n = 60 đã cần 10^{12} lời gọi.')

    D.h('3. Bế tắc')
    D.p('Lưu lại T(i) (quy hoạch động) cho thuật toán O(n): `mid.cpp` tính mảng T tới n lớn nhất trong các câu hỏi, rồi tra bảng. '
        'Với n ≤ 10^{6} chỉ mất ' + P.scores['mid.cpp']['detail'][1].split()[1] + ', được **' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['n = 10^{18}: không thể cấp phát mảng 10^{18} phần tử, cũng không thể lặp 10^{18} bước dù chỉ giữ hai biến. '
                                  'Mỗi bước "(a, b) → (a + b, a)" là cùng một phép biến đổi tuyến tính: lặp nó n lần là lũy thừa bậc n.'])

    D.h('4. Phá bế tắc: Lũy thừa ma trận')
    D.p('Viết bước truy hồi dưới dạng nhân ma trận:')
    D.eq('[F(k+1), F(k)]^{T} = Q · [F(k), F(k−1)]^{T},   Q = [[1, 1], [1, 0]]')
    D.p('Suy ra Q^{n} = [[F(n+1), F(n)], [F(n), F(n−1)]] (Tập 1, Bài 15) và đáp số là phần tử góc trái trên của Q^{n}. '
        'Lũy thừa nhanh: Q^{n} được tính bằng khoảng 2 log_{2} n ≈ 120 phép nhân ma trận 2 × 2, giống hệt lũy thừa nhanh số nguyên.')
    D.fig(P.fig('pow'), 'Lũy thừa nhanh Q¹⁰: chỉ các bit bằng 1 của n được nhân vào R.', 15)
    D.box('blue', 'VÌ SAO KHÔNG TRÀN SỐ?', ['Các phần tử ma trận luôn < 10^{9} + 7, mỗi tích < 1,0000001 · 10^{18}; tổng hai tích < 2,1 · 10^{18} < 9,2 · 10^{18}. '
                                          'Với ma trận lớn hơn (bài 15.3) phải lấy dư sau mỗi phép cộng.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lũy thừa nhanh ma trận', 11)
    D.code('LATGACH.CPP: lũy thừa ma trận 2 × 2', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(T · 8 log n): 1000 hành lang với n = 10^{18} chỉ khoảng 10^{6} phép nhân số, chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Nhân đôi nhanh (fast doubling): F(2k) = F(k) · (2F(k+1) − F(k)), F(2k+1) = F(k)^{2} + F(k+1)^{2}; ít phép nhân hơn ma trận khoảng 2 lần.',
                              'Hành lang 3 × n với gạch 1 × 2: dùng ma trận trạng thái của cột cuối (bài toán "domino tiling"), n lẻ không có cách lát.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**In F(n) thay vì F(n + 1):** n = 1 cho 1 = F(2), n = 2 cho 2 = F(3).',
               '**Ma trận đơn vị khởi tạo sai** (ví dụ R = Q): kết quả lệch một bậc.',
               '**Dùng int** cho phần tử ma trận: tích tràn.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
