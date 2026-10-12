def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Đây là bài "tổng hợp" của phương trình đồng dư bậc nhất: mô-đun tới 10^{18}, hệ số có thể âm, có thể không nguyên tố cùng nhau với mô-đun, và đoạn [L, R] có thể chứa số âm. '
        'Tập nghiệm của a · x ≡ c (mod m), nếu khác rỗng, luôn là **một lớp đồng dư** x ≡ x_{0} (mod M), tức một cấp số cộng vô hạn hai phía. '
        'Bài toán quy về: tìm x_{0}, M rồi đếm phần tử của cấp số cộng trong [L, R].')
    D.fig(P.fig('line'), 'Ví dụ 1, câu hỏi 1: các nghiệm cách đều 5; tô vàng nghiệm nhỏ nhất trong đoạn, tô xám nghiệm ngoài đoạn.', 15)

    D.h('2. Cách ngây thơ: Thử mọi x')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử mọi x', 13)
    D.code('Cách ngây thơ: thử mọi x trong [L, R]', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(R − L) mỗi câu hỏi, tới 2 · 10^{18}.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (|L|, |R| ≤ 10^{6}): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.', '**Subtask 2, 3**: đoạn tới 2 · 10^{18} số.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Không cần thử: Euclid mở rộng cho ngay lớp nghiệm, và số phần tử của một cấp số cộng trong một đoạn là **một phép chia**.'])

    D.h('4. Phá bế tắc: Giải tổng quát')
    D.fig(P.fig('chain'), 'Các bước giải phương trình đồng dư tổng quát.', 15.5)
    D.nums(['**Chuẩn hóa:** a ← a mod m, c ← c mod m về [0, m).',
            '**Điều kiện có nghiệm:** g = gcd(a, m) phải chia hết c (Bézout: a · x + m · y = c).',
            '**Rút gọn:** a\' = a/g, c\' = c/g, M = m/g, gcd(a\', M) = 1. Euclid mở rộng a · u + m · v = g cho a\' · u ≡ 1 (mod M), nên x_{0} = c\' · u mod M.',
            '**Nghiệm nhỏ nhất ≥ L:** first = L + ((x_{0} − L) mod M) với phép lấy dư không âm. Nếu first > R thì không có nghiệm; ngược lại số nghiệm là ⌊(R − first)/M⌋ + 1.'])
    D.box('purple', 'TRƯỜNG HỢP a ≡ 0', ['Khi a ≡ 0 (mod m) thì g = gcd(0, m) = m: có nghiệm khi và chỉ khi m | c, và khi đó **mọi** x là nghiệm (M = 1, x_{0} = 0). '
        'Số nghiệm có thể tới 2 · 10^{18} + 1 (đoạn [−10^{18}, 10^{18}]): vẫn vừa long long (tới 9,2 · 10^{18}). Hàm Euclid mở rộng xử lí đúng trường hợp này.'])
    D.sub('Ước lượng độ lớn')
    D.table(['Đại lượng', 'Lớn nhất', 'Kiểu'], [['a, c, m, M, x₀ (sau chuẩn hóa)', '< 10^{18}', 'long long'], ['(c\' mod M) · (u mod M)', '< 10^{36}', '__int128'],
                                            ['x₀ − L', '< 2 · 10^{18}', 'long long'], ['R − first, số nghiệm', '≤ 2 · 10^{18} + 1', 'long long']], widths=[3.6, 2, 1.6])
    D.p('Chương trình `mid.cpp` giống hệt lời giải mẫu nhưng nhân hai số dư bằng long long: đúng khi m ≤ 10^{9}, sai ở subtask 3: **' + S('mid.cpp') + ' điểm**.')
    D.sub('Chạy tay ví dụ 2, câu hỏi 3')
    D.p('a = −3 → a mod 10^{18} = 10^{18} − 3; c = 1; g = 1, M = 10^{18}. Nghịch đảo của −3 theo 10^{18} là −666 666 666 666 666 667 ≡ 333 333 333 333 333 333, nên '
        'x_{0} = 333 333 333 333 333 333. Đoạn [−10^{18}, 0]: first = −10^{18} + ((x_{0} + 10^{18}) mod 10^{18}) = −666 666 666 666 666 667 ≤ 0, và chỉ có 1 nghiệm.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12)
    D.code('PTDONGDU.CPP: phương trình đồng dư tổng quát', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(log m) mỗi câu hỏi.')
    D.box('blue', 'MỞ RỘNG', ['Ba bài 4.2, 4.3 và 10.3 dùng chung một khung: "giải đồng dư bậc nhất → lớp x₀ mod M → đếm trên đoạn". Bài 12 (định lí Trung Hoa) sẽ ghép nhiều lớp như vậy lại với nhau.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Số dư âm** của a, c, x₀ − L.', '**Đi từng bước M từ x₀** tới L: có thể tới 10^{18} bước.', '**Tràn khi nhân** c\' · u.', '**Nhầm M với m:** các nghiệm cách nhau m/g, không phải m.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
