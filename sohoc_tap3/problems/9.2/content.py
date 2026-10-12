def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Tính a^{b} mod m với số mũ b dài tới 10^{5} chữ số và m **bất kì** (có thể hợp số, có thể có ước chung với a). '
        'Không đọc được b vào kiểu số; câu hỏi là có cách nào "đọc dần" b như khi tính số dư của một xâu dài (sơ đồ Horner, Bài 1) không.')

    D.h('2. Cách ngây thơ: b kiểu long long')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ', 8)
    D.code('Cách ngây thơ: đọc b vào long long', P.src('naive.cpp'))
    D.p('Đúng khi b ≤ 10^{18} (lũy thừa nhanh 60 lượt); sai khi b dài hơn 19 chữ số.')

    D.h('3. Bế tắc, và cách của Hùng')
    D.bullets(['**Subtask 1** (b ≤ 10^{18}): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.'])
    D.p('Đề bài nhắc tới đề xuất của bạn Hùng: tính e = b mod (m − 1) (dễ, bằng Horner trên xâu) rồi lấy a^{e}. Theo định lí Fermat, cách này **đúng khi m nguyên tố và m ∤ a** '
        '(subtask 2). Nhưng với m hợp số thì sai, kể cả với b nhỏ:')
    D.table(['a, b, m', 'Đúng', 'Cách của Hùng', 'Theo φ(m)'], [
        ['2, 100, 12', '2^{100} mod 12 = **4**', 'e = 100 mod 11 = 1 → 2', 'φ(12) = 4: e = 0 → 1'],
        ['10, 10^{18}, 100', '**0**', 'e = 10^{18} mod 99 = 1 → 10', 'φ(100) = 40: e = 0 → 1'],
        ['3, 10^{18}, 10', '**1**', 'e = 10^{18} mod 9 = 1 → 3', 'φ(10) = 4: e = 0 → **1** (đúng vì gcd(3, 10) = 1)'],
    ], widths=[2, 2.3, 3.2, 2.3])
    D.p('Chương trình `fermat.cpp` cài đặt đúng cách của Hùng: qua subtask 2 nhưng mất cả subtask 1 (có m hợp số) và subtask 3: **' + S('fermat.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Rút gọn số mũ chỉ hợp lệ trong những điều kiện chặt chẽ (Fermat, Euler; Bài 11 sẽ có dạng mở rộng). '
                                 'Ta cần một cách **không rút gọn số mũ** mà vẫn xử lí được số mũ dài 10^{5} chữ số.'])

    D.h('4. Phá bế tắc: Horner trên số mũ')
    D.p('Đọc b từ trái sang phải. Nếu x là phần đầu đã đọc và d là chữ số tiếp theo thì phần đầu mới là 10x + d, và')
    D.eq('**a^{10x + d} = (a^{x})^{10} · a^{d}.**')
    D.p('Vậy giữ r = a^{x} mod m; mỗi chữ số d cập nhật r ← r^{10} · a^{d} mod m. Chỉ dùng phép nhân theo mô-đun: đúng với **mọi** m, kể cả hợp số, kể cả m = 1.')
    D.fig(P.fig('horner'), 'Chạy tay ví dụ 1, bộ thứ nhất: 2^{12345} mod 1000.', 15)
    D.box('purple', 'BAO NHIÊU PHÉP NHÂN?', ['Tính sẵn a^{0}, ..., a^{9}. Mỗi chữ số: r^{10} bằng lũy thừa nhanh (10 = 1010₂: 4 lần bình phương, 2 lần nhân) cộng một phép nhân với a^{d}: '
                                             'khoảng 7 phép nhân. 10^{5} chữ số × 10 bộ: khoảng 7 · 10^{6} phép nhân.'])
    D.p('Với m ≤ 10^{9}, mọi số dư < 10^{9} và tích < 10^{18}: vừa long long. Nhớ lấy a mod m trước (a tới 10^{18}), và khởi tạo r = 1 % m (bộ "7 0 1" phải in 0).')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 10)
    D.code('SOMULON.CPP: lũy thừa với số mũ là xâu', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(|b|) phép nhân theo mô-đun, không phụ thuộc m.')
    D.box('blue', 'MỞ RỘNG: TỪ PHẢI SANG TRÁI', ['Cũng có thể đọc b từ phải sang trái: giữ P = a^{10^{i}} (P ← P^{10} sau mỗi chữ số) và nhân r với P^{d_{i}}. '
        'Hai cách cùng độ phức tạp; cách Horner (trái sang phải) không cần đảo xâu.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Rút gọn số mũ theo m − 1 hoặc φ(m)** khi điều kiện không thỏa.', '**r = 1 thay vì 1 % m:** sai khi m = 1.',
               '**Quên a %= m:** a tới 10^{18}, tràn ngay ở phép nhân đầu.', '**b = "0":** vòng lặp cho r = (1)^{10} · a^{0} = 1: đúng (a^{0} = 1).'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'fermat.cpp', 'opt.cpp'])
