def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Đếm số nghiệm nguyên của x_{1} + ... + x_{k} = n với mọi x_{i} ≥ t. Hai bước biến đổi đưa về **một** hệ số nhị thức:')
    D.nums(['**Phát trước:** cho mỗi bạn t cái (cần n ≥ k·t, nếu không thì đáp số 0). Đặt y_{i} = x_{i} − t ≥ 0: y_{1} + ... + y_{k} = m với m = n − k·t.',
            '**Chia kẹo Euler (sao và vạch):** mỗi nghiệm không âm ứng với một cách đặt k − 1 vạch ngăn xen giữa m viên kẹo, tức chọn k − 1 vị trí trong m + k − 1 ô.'])
    D.eq('**Đáp số = C(n − k·t + k − 1, k − 1)  (hoặc 0 nếu k·t > n).**')
    D.fig(P.fig('stars'), 'Ví dụ 1, câu hỏi thứ hai: n = 10, k = 3, t = 1.', 15)

    D.h('2. Cách ngây thơ: Liệt kê')
    D.fig(P.fig('naive'), 'Sơ đồ khối hàm đệ quy liệt kê', 12)
    D.code('Cách ngây thơ: đệ quy thử số kẹo của từng bạn', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** tỉ lệ với chính đáp số, tức C(n + k − 1, k − 1): nhỏ khi n ≤ 10, k ≤ 5, khổng lồ khi n, k tới hàng nghìn.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1**: **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               'Có công thức rồi, tính C(a, b) bằng **tam giác Pascal** tới 4000 (`pascal.cpp`, mảng 64 MB): qua subtask 2, nhưng chỉ số tới 2 · 10^{6} thì không có bảng nào 2 · 10^{6} × 2 · 10^{6}: **' + S('pascal.cpp') + ' điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Cần C(a, b) theo mô-đun nguyên tố cho a tới 2 · 10^{6} và 10^{5} câu hỏi: mỗi câu O(1) sau một lần chuẩn bị O(a).'])

    D.h('4. Phá bế tắc: Bảng giai thừa và nghịch đảo giai thừa')
    D.p('Với p = 10^{9} + 7 nguyên tố lớn hơn mọi chỉ số, C(a, b) ≡ fact[a] · ifact[b] · ifact[a − b] (mod p), với ifact[i] = (i!)^{−1}. Chuẩn bị (Tập 1, Bài 13):')
    D.nums(['fact[i] = fact[i − 1] · i mod p;', 'ifact[N] = fact[N]^{p − 2} mod p (**một** lần lũy thừa);', 'ifact[i − 1] = ifact[i] · i mod p, đi từ N về 1.'])
    D.box('purple', 'BẢNG PHẢI ĐỦ LỚN', ['Chỉ số lớn nhất là n − k·t + k − 1, đạt gần 2 · 10^{6} khi t = 0, n = k = 10^{6}. Chương trình `bay.cpp` chỉ lập bảng tới 10^{6} '
        '("vì n ≤ 10^{6}"): truy cập ngoài mảng ở subtask 3, chương trình bị dừng: **' + S('bay.cpp') + ' điểm**.',
        'Ngoài ra k·t tới 10^{12}: so sánh k·t > n phải dùng long long (với int, tích tràn thành số âm, như ví dụ 2 đã cảnh báo).'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 13)
    D.code('CHIAKEO.CPP: bảng giai thừa tới 2·10^6', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(N + log p) chuẩn bị, O(1) mỗi câu hỏi. Hai mảng long long 2 · 10^{6} phần tử: 32 MB.')
    D.box('blue', 'MỞ RỘNG: GIỚI HẠN TRÊN', ['Nếu thêm điều kiện x_{i} ≤ u, đếm bằng bù trừ: Σ_{j} (−1)^{j} C(k, j) · C(n − j(u + 1) + k − 1, k − 1) (bỏ dần các bạn "nhận quá u"). Xem Bài 14.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Bảng giai thừa quá nhỏ** (tới 10^{6} thay vì 2 · 10^{6}).', '**k·t tràn int.**', '**Nhân ba số không lấy dư giữa chừng:** fact · ifact · ifact tràn long long.', '**n = 0:** đáp số 1 (mọi bạn nhận 0, khi t = 0).'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'pascal.cpp', 'bay.cpp', 'opt.cpp'])
