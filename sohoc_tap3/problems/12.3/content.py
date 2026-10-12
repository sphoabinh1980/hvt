def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Năm x mang tên (x mod m_{1}, ..., x mod m_{k}). Hai câu hỏi:')
    D.nums(['**Có bao nhiêu tên khác nhau?** Tên lặp lại với chu kì M = lcm(m_{1}, ..., m_{k}) và trong một chu kì không có hai năm trùng tên (nếu x ≡ y theo mọi m_{i} thì lcm | x − y). '
            'Vậy số tên **bằng lcm**, có thể tới khoảng 10^{120}, in theo mô-đun 10^{9} + 7.',
            '**Những năm nào mang tên (c_{1}, ..., c_{k}) trong [L, R]?** Đó là nghiệm của hệ x ≡ c_{i} (mod m_{i}) với các mô-đun có ước chung: gộp từng cặp như bài 12.2.'])
    D.fig(P.fig('table'), 'Bảng 10 × 12 tên Can Chi; ô ghi x là năm thứ x trong vòng 60 năm.', 15.5)

    D.h('2. Cách ngây thơ: Liệt kê')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách liệt kê', 12)
    D.code('Cách ngây thơ: liệt kê các năm', P.src('naive.cpp'))
    D.p('Chỉ dùng được khi m_{1}m_{2} và R nhỏ (subtask 1).')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1**: **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               'Gộp đồng dư bằng long long và tính lcm bằng gcd (`mid.cpp`) đúng khi tích các m_{i} ≤ 10^{18} (subtask 2): **' + S('mid.cpp') + ' điểm**. '
               'Ở subtask 3, lcm và mô-đun M khi gộp vượt xa 10^{18}: tràn số.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['(1) lcm không "đi qua" phép lấy dư (bài 7.3): phải tính qua phân tích thừa số. (2) Khi gộp, M có thể vượt mọi kiểu số; cần nhận ra lúc nào **không cần gộp tiếp**.'])

    D.h('4. Phá bế tắc')
    D.sub('Số tên: lcm theo mô-đun qua bảng số mũ')
    D.p('Phân tích từng m_{i} ≤ 10^{6} bằng sàng spf, giữ số mũ lớn nhất của mỗi số nguyên tố p; số tên là Π p^{M(p)} mod (10^{9} + 7) (giống hệt bài BCNN CỦA DÃY, 7.3).')
    D.sub('Câu hỏi: gộp và dừng đúng lúc')
    D.p('Gộp lần lượt các phương trình vào (r, M) như bài 12.2; gặp g ∤ (c − r) thì in 0. Quan sát then chốt:')
    D.fig(P.fig('big'), 'Khi M > R, chỉ còn đúng một ứng viên trong [0, R].', 15)
    D.p('Một khi M > R (R ≤ 10^{18}), từ đó về sau mọi phương trình chỉ cần **kiểm tra** r mod m_{i} = c_{i}, không gộp nữa. Kết luận: nếu r thỏa hết và L ≤ r ≤ R thì in "1 r", ngược lại in 0. '
        'Nếu gộp xong mà M ≤ R thì đếm cấp số cộng trong [L, R] như bài 10.3.')
    D.box('purple', 'ƯỚC LƯỢNG', ['Lúc còn gộp thì M ≤ R ≤ 10^{18}; sau một lần gộp M mới ≤ 10^{18} · 10^{6} = 10^{24} và r < M: lưu r, M bằng __int128. '
        'Ngay sau đó M > R nên không bao giờ phải nhân tiếp.'])
    D.sub('Chạy tay ví dụ 2, câu hỏi 1')
    D.p('m = 4, 6, 9; tên (1, 3, 3). Gộp x ≡ 1 (mod 4) với x ≡ 3 (mod 6): g = 2 | 2, được x ≡ 9 (mod 12). Gộp với x ≡ 3 (mod 9): g = 3 | (3 − 9), được x ≡ 21 (mod 36). '
        'Trong [0, 100]: 21, 57, 93 – ba năm, sớm nhất là 21.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 14)
    D.code('CANCHI.CPP: lcm qua thừa số, gộp có dừng sớm', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(MX log log MX) sàng, O(k log m) mỗi câu hỏi.')
    D.box('blue', 'MỞ RỘNG', ['Ý tưởng "đại lượng vượt ngưỡng thì chỉ còn tối đa một ứng viên" gặp lại ở nhiều nơi: BCNN có chặn (bài 3.3), giá trị chặn của tháp (bài 11.3). '
        'Khi một số lớn tới mức "vô nghĩa" đối với câu hỏi, hãy dừng tính nó.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Tính lcm bằng gcd rồi lấy dư:** sai (bài 7.3).', '**Tràn khi gộp:** M · t tới 10^{24}.', '**Đếm năm tới 10^{18} + 1:** khi mọi m_{i} = 1.', '**Quên kiểm tra các phương trình còn lại** sau khi dừng gộp.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
