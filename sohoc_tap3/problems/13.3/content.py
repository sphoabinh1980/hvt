def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Tính C(n, k) mod m với n tới 10^{18} và m là tích các số nguyên tố **khác nhau**, mỗi số ≤ 10^{5}. Công thức fact[n] · ifact[k] · ifact[n − k] không dùng được: '
        'không lập được bảng tới 10^{18}, và theo mô-đun hợp số thì k! thường không có nghịch đảo. Hai công cụ ghép lại thành lời giải:')
    D.nums(['**Định lí Lucas** (Tập 1, Bài 13): với p nguyên tố, C(n, k) ≡ Π C(n_{i}, k_{i}) (mod p), n_{i}, k_{i} là các chữ số của n, k trong cơ số p.',
            '**Định lí số dư Trung Hoa** (Tập 1, Bài 12): biết C(n, k) mod p_{i} với mọi ước nguyên tố p_{i} của m (đôi một nguyên tố cùng nhau) thì xác định duy nhất C(n, k) mod m.'])
    D.fig(P.fig('lucas'), 'Hai bước của lời giải trên ví dụ 1 và ví dụ 2.', 15.5)

    D.h('2. Cách ngây thơ: Tam giác Pascal')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách dùng tam giác Pascal', 13)
    D.code('Cách ngây thơ: tam giác Pascal theo mô-đun m', P.src('naive.cpp'))
    D.p('Hằng đẳng thức Pascal chỉ dùng phép cộng nên đúng với **mọi** mô-đun; nhưng bảng chỉ lập được tới n ≈ 2000.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (n ≤ 2000): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               'Coi m là số nguyên tố và dùng thẳng Lucas (`lucas1.cpp`): đúng ở **subtask 2**. Khi m là hợp số tới 10^{10}, chương trình phải lập bảng giai thừa tới m − 1 (10^{10} phần tử!) '
               'và dùng Fermat với mô-đun không nguyên tố: **' + S('lucas1.cpp') + ' điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Lucas chỉ đúng với mô-đun **nguyên tố**, và cần bảng giai thừa tới p − 1. Với m = p_{1}···p_{r}, hãy dùng Lucas **riêng cho từng** p_{i} (mỗi p_{i} ≤ 10^{5}), rồi ghép lại.'])

    D.h('4. Phá bế tắc')
    D.sub('Lucas theo từng ước nguyên tố')
    D.p('Với mỗi p_{i}, chuẩn bị giai thừa và nghịch đảo giai thừa cho 0..p_{i} − 1. Mỗi truy vấn: tách n, k theo cơ số p_{i}; mỗi cặp chữ số cho một C(n_{j}, k_{j}) với n_{j}, k_{j} < p_{i} '
        '(bằng 0 nếu k_{j} > n_{j}). Số chữ số ≤ log_{2} 10^{18} ≈ 60.')
    D.sub('Ghép bằng định lí Trung Hoa')
    D.p('Đặt M_{i} = m/p_{i} và e_{i} = M_{i} · (M_{i}^{−1} mod p_{i}): e_{i} ≡ 1 (mod p_{i}) và e_{i} ≡ 0 (mod p_{j}) với j ≠ i. Khi đó')
    D.eq('**C(n, k) ≡ Σ_{i} r_{i} · e_{i}  (mod m),   r_{i} = C(n, k) mod p_{i}.**')
    D.p('Các e_{i} chỉ phụ thuộc m, tính **một lần** cho mọi truy vấn. Mỗi tích r_{i} · e_{i} < 10^{5} · 10^{10} = 10^{15}: vừa long long.')
    D.box('purple', 'VÌ SAO m PHẢI LÀ TÍCH CÁC SỐ NGUYÊN TỐ KHÁC NHAU?', ['Lucas cho C(n, k) mod p, không cho mod p^{2}. Nếu m chứa p^{2} (như 12 = 2² · 3), cần định lí Lucas mở rộng (Granville) phức tạp hơn nhiều. '
        'Đề bài đã chọn dạng m để hai công cụ cơ bản là đủ.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 14)
    D.code('TOHOPLON.CPP: Lucas + Trung Hoa', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** chuẩn bị O(Σ p_{i}) ≤ 10^{6}; mỗi truy vấn O(Σ log_{p_{i}} n) ≤ 10 · 60 phép tính.')
    D.box('blue', 'MỞ RỘNG', ['m ≤ 10^{10} có nhiều nhất 10 ước nguyên tố (tích 11 số nguyên tố đầu tiên đã vượt 2 · 10^{11}). Kĩ thuật "tách mô-đun thành các thừa số nguyên tố rồi ghép" '
        'dùng được cho mọi bài tính theo mô-đun hợp số không có lũy thừa.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Dùng Fermat với mô-đun hợp số.**', '**k > n:** phải in 0 (Lucas tự cho 0 khi một chữ số k_{j} > n_{j}).', '**m = 1:** mọi đáp số 0.', '**Tích r_{i}·e_{i} trong int:** tràn.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'lucas1.cpp', 'opt.cpp'])
