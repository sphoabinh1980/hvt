def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Đây là bài 20.2 cho tam giác, với Pick: **I = (2S − B + 2)/2**, trong đó 2S = |u_{x} v_{y} − v_{x} u_{y}| với u = P_{2} − P_{1}, v = P_{3} − P_{1}, '
        'và B là tổng gcd ba cạnh. Công thức không có gì mới; cái khó nằm ở **độ lớn** của các đại lượng khi tọa độ tới 10^{18}.')
    D.fig(P.fig('tri'), 'Ví dụ 1, tam giác thứ hai: 12 điểm trên biên, 37 điểm bên trong.', 15.2)

    D.h('2. Cách ngây thơ: Thử từng điểm')
    D.code('Cách ngây thơ: kiểm tra mọi điểm trong hình chữ nhật bao', P.src('naive.cpp'))
    D.p('Một điểm nằm hẳn bên trong khi ba tích chéo với ba cạnh khác 0 và cùng dấu. Nhưng ngay ở subtask 1, Q = 10^{5} tam giác, mỗi tam giác có hình chữ nhật bao tới 201 × 201 điểm: '
        '4 · 10^{9} lần kiểm tra. Cách ngây thơ được **' + S('naive.cpp') + ' điểm**: bài này buộc phải dùng công thức ngay từ đầu.')

    D.h('3. Bế tắc')
    D.p('Pick với long long (`mid.cpp`) đúng khi |x|, |y| ≤ 10^{9}: hiệu tới 2 · 10^{9}, tích tới 4 · 10^{18}, |2S| ≤ 8 · 10^{18} < 9,2 · 10^{18}. **' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Tọa độ 10^{18}: tích hai hiệu tới 4 · 10^{36}, vượt xa long long. Ví dụ 2, tam giác thứ hai: 2S = |10^{18} · (10^{18} − 1) − 10^{18} · 10^{18}| = 10^{18} '
                                  'vừa long long, nhưng hai tích ở giữa thì không: kết quả cuối nhỏ không có nghĩa là phép tính trung gian an toàn.'])

    D.h('4. Phá bế tắc: Ước lượng từng đại lượng, dùng __int128')
    D.fig(P.fig('sizes'), 'Độ lớn của các đại lượng khi tọa độ tới 10¹⁸.', 14)
    D.box('purple', 'BẪY: ÉP KIỂU SAU KHI NHÂN', ['$lll S2 = (lll)(ux * vy) - (lll)(vx * uy);',
                                                  'ux * vy được tính trên 64 bit và tràn **trước khi** ép kiểu; ép kiểu một kết quả đã sai không cứu được gì. '
                                                  'Phải ép một thừa số: (lll)ux * vy, khi đó phép nhân diễn ra trên 128 bit.'])
    D.p('Ba gcd đều ≤ 2 · 10^{18}, tổng B ≤ 6 · 10^{18} vẫn vừa long long nhưng đã sát trần; cộng chúng vào biến __int128 cho an toàn. '
        'Đáp số tới khoảng 4 · 10^{36} (ví dụ 2 có 36 chữ số): printf không in được __int128, phải tự tách từng chữ số như bài 18.2.')
    D.box('blue', 'ĐỪNG DÙNG SỐ THỰC', ['double giữ khoảng 15–16 chữ số có nghĩa, long double khoảng 18–19. Đáp số 36 chữ số không thể chính xác; '
                                        'tam giác "mỏng" như ví dụ 2 còn mất hết ý nghĩa vì phép trừ hai số gần bằng nhau.'])
    D.sub('Chạy tay ví dụ 2, tam giác thứ nhất')
    D.p('u = (10^{18}, 0), v = (0, 10^{18}): 2S = 10^{36}. B = gcd(10^{18}, 0) + gcd(0, 10^{18}) + gcd(10^{18}, 10^{18}) = 3 · 10^{18}. '
        'I = (10^{36} − 3 · 10^{18} + 2)/2 = 499 999 999 999 999 998 500 000 000 000 000 001.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của một tam giác', 12)
    D.code('TAMGIAC.CPP: Pick với __int128', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(log C) mỗi tam giác (ba lần gcd); 10^{5} tam giác chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Đếm điểm nguyên trên biên và bên trong: I + B = (2S + B + 2)/2.',
                              'Thói quen tốt cho mọi bài có số lớn: viết ra giới hạn của **từng** đại lượng trung gian (như bảng ở mục 4) trước khi chọn kiểu dữ liệu.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**(lll)(a * b)** thay vì (lll)a * b.', '**In __int128 bằng printf("%lld")**: sai hoặc lỗi biên dịch.', '**Dùng double/long double.**',
               '**Hàm abs cho long long** (abs nhận int): dùng llabs hoặc tự viết.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
