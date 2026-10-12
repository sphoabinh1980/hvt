def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Mỗi túi độc lập nên xác suất "mọi viên đều đỏ" là tích các xác suất x_{i}/(x_{i} + y_{i}); "ít nhất một viên đỏ" là phần bù của "mọi viên đều xanh":')
    D.eq('**P_{1} = Π x_{i} / Π (x_{i} + y_{i}),     P_{2} = 1 − Π y_{i} / Π (x_{i} + y_{i}).**')
    D.fig(P.fig('bags'), 'Ví dụ 1: hai túi.', 14)
    D.p('Kết quả phải in **theo mô-đun** p = 10^{9} + 7: số R với Q · R ≡ P (mod p). Đó không phải xác suất thực, mà là "ảnh" của phân số P/Q trong thế giới số dư (Tập 1, Bài 10).')
    D.fig(P.fig('modfrac'), 'Phân số theo mô-đun 10^{9} + 7 của ví dụ 1.', 15)

    D.h('2. Cách ngây thơ: Phân số chính xác')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ', 12)
    D.code('Cách ngây thơ: tử và mẫu chính xác bằng long long', P.src('naive.cpp'))
    D.p('Đúng khi các tích còn vừa long long: n ≤ 10 túi với x + y ≤ 10 (tích ≤ 10^{10}), hoặc một túi. Với 10^{5} túi, tích có tới 900 000 chữ số.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1, 2**: **' + S('naive.cpp') + ' điểm**.', '**Subtask 3**: các tích tràn số, thậm chí thành 0 khiến chương trình chia cho 0 và bị dừng: **0 điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Phân số thật quá lớn để lưu. Nhưng ta không cần phân số thật: chỉ cần ảnh của nó theo mô-đun, và ảnh ấy tính được từ **tử theo mô-đun** và **mẫu theo mô-đun**.'])

    D.h('4. Phá bế tắc: Làm việc hoàn toàn theo mô-đun')
    D.nums(['Tính X = Π x_{i}, Y = Π y_{i}, Z = Π (x_{i} + y_{i}) theo mô-đun, lấy dư sau **mỗi** phép nhân.',
            'Nghịch đảo của Z: inv = Z^{p − 2} mod p (định lí Fermat). Cả bài chỉ cần **một** lần nghịch đảo.',
            'P_{1} = X · inv, P_{2} = (1 − Y · inv) mod p, nhớ **cộng thêm p** trước khi lấy dư vì phép trừ có thể ra số âm.'])
    D.box('purple', 'VÌ SAO KHÔNG CẦN RÚT GỌN TRƯỚC?', ['Nếu P/Q = P\'/Q\' (dạng tối giản) thì P · Q\' = P\' · Q, nên P · Q^{−1} ≡ P\' · Q\'^{−1} (mod p) miễn là Q, Q\' không chia hết cho p. '
        'Ở đây mỗi x_{i} + y_{i} ≤ 10^{9} < p nên Z không bao giờ chia hết cho p: nghịch đảo luôn tồn tại, và kết quả không phụ thuộc cách viết phân số.'])
    D.p('Chương trình `bay.cpp` đúng mọi thứ, trừ một chi tiết: viết `(1 - Y * inv % MOD) % MOD`. Khi Y · inv mod p > 1 (gần như luôn luôn), kết quả là số âm. '
        'Ngay ví dụ 1 đã in ra −333 333 335 thay vì 666 666 672: **' + S('bay.cpp') + ' điểm**.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 13)
    D.code('XACSUAT.CPP: tích theo mô-đun + một lần nghịch đảo', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(n + log p).')
    D.box('blue', 'MỞ RỘNG: KIỂM TRA ĐÁP SỐ', ['Muốn chắc chắn số in ra đúng là P/Q, nhân ngược lại: Q · R mod p phải bằng P mod p. '
        'Với ví dụ 1: 6 · 166 666 668 mod (10^{9} + 7) = 1. Đây cũng là cách nhanh để "đoán" xem một số in ra theo mô-đun ứng với phân số nào khi Q nhỏ.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Tính bằng double rồi đổi sang mô-đun:** vô nghĩa, phân số theo mô-đun không phải số thực.',
               '**Phép trừ ra số âm:** cộng thêm p trước khi lấy dư.', '**Quên lấy dư sau mỗi phép nhân.**',
               '**Nghịch đảo của từng mẫu:** đúng nhưng tốn 10^{5} lần lũy thừa nhanh; một lần là đủ.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'bay.cpp', 'opt.cpp'])
