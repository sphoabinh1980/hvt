def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Tháp a_{1}^{a_{2}^{...^{a_{k}}}} có giá trị khổng lồ (2 mũ 2 mũ 2 mũ 2 mũ 2 đã có gần 20 000 chữ số). Muốn tính theo mô-đun m, phải **rút gọn số mũ**. '
        'Nhưng số mũ của tầng 1 chính là tháp của các tầng trên, mà rút gọn số mũ theo mô-đun nào, và khi nào thì được phép?')
    D.fig(P.fig('seq'), 'Dãy 2^{e} mod 12: hai số hạng đầu chưa tuần hoàn, sau đó lặp với chu kì 2.', 15)
    D.p('Hình trên cho thấy cả hai cái bẫy: dãy lũy thừa theo mô-đun hợp số **không** tuần hoàn ngay từ đầu, và chu kì không nhất thiết là m − 1.')

    D.h('2. Cách ngây thơ: Giá trị thật')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách tính giá trị thật', 11)
    D.code('Cách ngây thơ: tính giá trị thật của tháp', P.src('naive.cpp'))
    D.p('Chỉ dùng được khi giá trị tháp ≤ 10^{18} (subtask 1). Ở các subtask khác, vòng nhân chạy hàng tỉ lần với số mũ lớn.')

    D.h('3. Bế tắc: hai cách rút gọn "gần đúng"')
    D.bullets(['**Giá trị thật:** subtask 1, **' + S('naive.cpp') + ' điểm**.',
               '**Fermat** (`fermat.cpp`): với k = 3, m nguyên tố, m ∤ a_{1} thì a_{1}^{E} ≡ a_{1}^{E mod (m − 1)}: qua đúng subtask 2, **' + S('fermat.cpp') + ' điểm**.',
               '**Euler thường, đệ quy** (`euler.cpp`): f(i, m) = a_{i}^{f(i + 1, φ(m))} mod m. Đúng khi mọi tầng có gcd(a_{i}, m) = 1; sai ngay với 2^{10^{18}} mod 12 (in 1 thay vì 4): **' + S('euler.cpp') + ' điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Định lí Euler a^{φ(m)} ≡ 1 chỉ đúng khi gcd(a, m) = 1. Với mô-đun bất kì cần **định lí Euler mở rộng**, và nó đòi hỏi biết số mũ thật có ≥ φ(m) hay không.'])

    D.h('4. Phá bế tắc: Euler mở rộng và giá trị chặn')
    D.sub('Định lí Euler mở rộng')
    D.eq('**Với mọi a, m và mọi E ≥ φ(m):   a^{E} ≡ a^{(E mod φ(m)) + φ(m)}   (mod m).**')
    D.p('Phần "+ φ(m)" chính là để "nhảy qua" đoạn chưa tuần hoàn ở đầu dãy (Hình ' + P.pid + '.1). Khi E < φ(m), không rút gọn gì, dùng thẳng a^{E}.')
    D.sub('Giá trị chặn của tháp con')
    D.p('Để biết E ≥ φ(m) hay không, tính trước cap[i] = min(tháp a_{i..k}, C) với C = 2 · 10^{9} > mọi φ(m). Tính từ trên xuống: cap[i] = min(a_{i}^{cap[i+1]}, C), '
        'với các quy tắc 0^{0} = 1, 0^{x} = 0 (x ≥ 1), 1^{x} = 1; khi a_{i} ≥ 2, chỉ cần tối đa 31 phép nhân là vượt C. Vì cap không phụ thuộc mô-đun, tính một lần cho cả bộ dữ liệu.')
    D.sub('Đệ quy')
    D.nums(['solve(i, m) = 0 nếu m = 1.', 'solve(k, m) = a_{k} mod m.',
            'Ngược lại, E = cap[i + 1]: nếu E < φ(m) thì trả về a_{i}^{E} mod m; nếu không, trả về a_{i}^{solve(i + 1, φ(m)) + φ(m)} mod m.'])
    D.fig(P.fig('chain'), 'Chạy tay ví dụ 1, bộ thứ hai: tháp 2, 10, 18 theo mô-đun 12.', 15)
    D.box('purple', 'VÌ SAO NHANH?', ['Dãy m, φ(m), φ(φ(m)), ... về 1 sau O(log m) bước (với m ≤ 10^{9}, chưa tới 32 bước), và khi mô-đun bằng 1 thì đệ quy dừng. '
        'Mỗi bước tính φ bằng thử chia tới √m ≈ 31 623: tổng cộng chưa tới 10^{6} phép chia mỗi bộ, cộng O(k) để tính mảng cap.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối hàm solve(i, m)', 12)
    D.code('THAPLT.CPP: Euler mở rộng + giá trị chặn', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(k + log m · √m) mỗi bộ dữ liệu.')
    D.box('blue', 'MỞ RỘNG: KIỂM TRA BẰNG PYTHON', ['Với tháp nhỏ, Python tính được giá trị thật của các tầng trên (số nguyên lớn) rồi gọi pow(a, E, m): đó chính là chương trình "trâu" '
        'đã dùng để đối chiếu lời giải này trên hàng trăm bộ dữ liệu ngẫu nhiên.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Bỏ "+ φ(m)":** sai khi gcd(a_{i}, m) > 1.', '**Luôn cộng φ(m)** kể cả khi E < φ(m): sai, ví dụ 2^{1} mod 12 thành 2^{1 + 4} = 32 ≡ 8.',
               '**Số 0 và 1 trong tháp:** 2, 0, 0, 5 có giá trị 2^{0^{0^{5}}} = 2^{0^{0}} = 2^{1} = 2.', '**Tràn khi tính cap:** chặn ngay khi vượt C.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'fermat.cpp', 'euler.cpp', 'opt.cpp'])
