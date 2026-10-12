def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Mỗi hình chữ nhật con được xác định bởi cặp hàng (i_{1}, i_{2}) và cặp cột (j_{1}, j_{2}). Cố định cặp hàng, đặt b_{j} = a_{i1,j} + ... + a_{i2,j} (tổng cột j giữa hai hàng). '
        'Hình chữ nhật [i_{1}, i_{2}] × [j_{1}, j_{2}] có tổng b_{j1} + ... + b_{j2}: **bài toán 2 chiều trở thành bài toán 1 chiều** "đếm đoạn con của b có tổng chia hết cho k" '
        '(Tập 1, Bài 19: đếm cặp tiền tố cùng số dư).')
    D.fig(P.fig('reduce'), 'Ví dụ 1: cặp hàng (1, 2) cho dãy b = 5, 7, 9 và 3 hình chữ nhật.', 15.2)

    D.h('2. Cách ngây thơ: Duyệt mọi hình chữ nhật')
    D.code('Cách ngây thơ: O(m²n²) với tổng tiền tố 2 chiều', P.src('naive.cpp'))
    D.p('Có (m(m+1)/2) · (n(n+1)/2) hình chữ nhật, mỗi hình O(1) nhờ tổng tiền tố 2 chiều. m = n = 30: khoảng 2 · 10^{5}, **' + str(P.pts('naive.cpp', 1)) + ' điểm**. '
        'm = n = 400: 6,4 · 10^{9}.')

    D.h('3. Bế tắc')
    D.p('Cố định cặp hàng (80 200 cặp), cập nhật b trong O(n) khi tăng i_{2}, rồi đếm đoạn trên b bằng mảng đếm số dư cnt[0..k − 1]: O(n). '
        'Nhưng trước mỗi lần đếm phải **xóa** mảng cnt. `mid.cpp` xóa cả mảng: O(m^{2} · (n + k)). Với k ≤ 100 chạy ' + P.scores['mid.cpp']['detail'][1].split()[1] + ' (**' + S('mid.cpp') + ' điểm**).')
    D.box('red', 'ĐIỂM BẾ TẮC', ['k = 10^{6}: xóa mảng 80 200 lần là 8 · 10^{10} thao tác, trong khi phần tính toán thật chỉ 80 200 · 400 · 2 ≈ 6,4 · 10^{7}. '
                                  'Chi phí nằm ở việc dọn dẹp, không phải ở việc đếm!'])

    D.h('4. Phá bế tắc: Chỉ xóa những ô vừa dùng')
    D.fig(P.fig('clear'), 'Mỗi lượt chỉ chạm tới n + 1 ô của mảng đếm.', 15)
    D.p('Mỗi lượt đếm chỉ tăng cnt tại n + 1 vị trí P_{0}, ..., P_{n}. Đi lại dãy tiền tố một lần nữa và gán cnt[P_{j}] = 0 là mảng trở lại toàn 0: O(n) thay cho O(k).')
    D.box('blue', 'GIỮ MỌI SỐ TRONG [0, k)', ['Đưa a_{i,j} về số dư không âm ngay khi đọc. Sau đó b_{j} và P_{j} đều là tổng của hai số trong [0, k): '
                                              'cộng xong chỉ cần trừ k nếu ≥ k, không cần phép % (chậm hơn nhiều) trong vòng lặp 6,4 · 10^{7} lần. Mọi giá trị < 2 · 10^{6}: dùng int.'])
    D.p('Đáp số tới (400 · 401/2)^{2} ≈ 6,4 · 10^{9} > 2^{31}: long long.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối', 13.5)
    D.code('HCNCHIAHET.CPP', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(m^{2} · n) ≈ 3,2 · 10^{7} lượt cập nhật b và chừng ấy lượt đếm; chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '. Bộ nhớ: mảng cnt 4 MB.')
    D.box('blue', 'MỞ RỘNG', ['Nếu m > n, hãy cố định cặp **cột** thay vì cặp hàng: O(min(m, n)^{2} · max(m, n)).',
                              'Đếm hình chữ nhật có tổng bằng 0 (không theo mô-đun): thay mảng đếm bằng sắp xếp (bài 19.1) mỗi lượt, O(m^{2} n log n).',
                              'Kĩ thuật "xóa đúng những gì đã ghi" dùng rất nhiều: mảng đánh dấu trong DFS nhiều lần, bảng băm tự cài...'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Xóa cả mảng đếm** mỗi lượt.', '**Số dư âm** khi a_{i,j} < 0.', '**Quên cnt[0] = 1** (tiền tố rỗng).', '**Đáp số kiểu int.**',
               '**Dùng % trong vòng lặp trong cùng**: chậm hơn đáng kể.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
