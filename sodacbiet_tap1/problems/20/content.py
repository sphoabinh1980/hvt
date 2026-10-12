def build(D, P):
    D.objectives([
        'Nhận biết các **số hình học** (số tam giác, số chính phương, số ngũ giác...) và kiểm tra một số có phải số tam giác trong O(1).',
        'Sinh theo thứ tự tăng dần các số chỉ có ước nguyên tố 2, 3, 5 (**số Hamming**) bằng kĩ thuật **ba con trỏ**, không sinh trùng, không cần sắp xếp.',
        'Biểu diễn mọi số thành tổng các số Fibonacci không kề nhau (**định lí Zeckendorf**) bằng tham lam.',
        'Biết thêm các dãy kinh điển: Catalan, Collatz; và nhìn lại cả cuốn sách qua những "con số đáng nhớ".'])
    D.kbox('KHỞI ĐỘNG', [
        'Xếp bi thành hình tam giác: 1, 3, 6, 10, 15, ... viên. Xếp thành hình vuông: 1, 4, 9, 16, ... viên. Từ thời Pythagoras, người ta đã gọi đó là các **số hình học**. '
        'Em có biết 2016 là một số tam giác (hàng 63), còn 2026 thì không?',
        'Bài cuối của cuốn sách là một chuyến dạo qua những dãy số đặc biệt nổi tiếng nhất, và một kĩ thuật lập trình nhỏ mà đẹp: sinh dãy số theo thứ tự bằng **nhiều con trỏ**.'])

    D.h('1. Số hình học')
    D.fig(P.fig('dots'), 'Số tam giác và số chính phương: số viên bi xếp thành hình.', 15.5)
    D.kbox('ĐỊNH NGHĨA', ['- **Số tam giác** T_{n} = 1 + 2 + ... + n = n(n + 1)/2: 1, 3, 6, 10, 15, 21, ...',
                          '- **Số ngũ giác** P_{n} = n(3n − 1)/2: 1, 5, 12, 22, 35, ...',
                          '- Tổng quát, **số k-giác** thứ n bằng ((k − 2)n^{2} − (k − 4)n)/2; với k = 4 được n^{2}.'])
    D.kbox('ĐỊNH LÍ (KIỂM TRA SỐ TAM GIÁC)', ['x là số tam giác khi và chỉ khi **8x + 1 là số chính phương**; khi đó x = T_{n} với n = (√(8x + 1) − 1)/2.'])
    D.kbox('VÌ SAO ĐÚNG?', ['x = n(n + 1)/2 ⇔ 8x + 1 = 4n^{2} + 4n + 1 = (2n + 1)^{2}. Ngược lại, nếu 8x + 1 = m^{2} thì m lẻ, đặt m = 2n + 1 là xong. '
                            'Ví dụ 8 · 2016 + 1 = 16 129 = 127^{2}: 2016 = T_{63}. Còn 8 · 2026 + 1 = 16 209 nằm giữa 127^{2} và 128^{2}: 2026 không phải số tam giác. Dùng isqrt (Bài 19) để kiểm tra.'])
    D.p('Năm 1796, Gauss ghi trong nhật kí: "EYPHKA! num = Δ + Δ + Δ", nghĩa là mọi số tự nhiên là tổng của **ba** số tam giác (cho phép T_{0} = 0). '
        'Ví dụ 2026 = 946 + 780 + 300 = T_{43} + T_{39} + T_{24}. Đây là "anh em" của định lí bốn bình phương ở Bài 19.')
    D.h('2. Bài toán HAMMING')
    D.p('Số **Hamming** (còn gọi là số "xấu xí" hay số 5-trơn) là số nguyên dương không có ước nguyên tố nào khác 2, 3, 5: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, ... '
        'Chúng là những số dạng 2^{a} · 3^{b} · 5^{c}, rất hay gặp khi chọn kích thước mảng cho phép biến đổi Fourier nhanh.')
    D.problem_box('HAMMING', 'Cho số nguyên dương n. Hãy tìm số Hamming thứ n (số 1 là số thứ nhất).', 'Một số nguyên n (1 ≤ n ≤ 10^{4}).', 'Số Hamming thứ n.')
    D.examples('HAMMING', [('10', '12', '1, 2, 3, 4, 5, 6, 8, 9, 10, 12.'), ('15', '24', ''), ('1500', '859963392', '= 2^{17} · 3^{8}.')])
    D.p('Subtask 1 (30 điểm): n ≤ 500. Subtask 2 (70 điểm): n ≤ 10^{4}. Số thứ 10^{4} là 288 325 195 312 500 000 ≈ 2,9 · 10^{17}: vẫn vừa long long.')

    D.h('3. Ý tưởng ngây thơ: Kiểm tra từng số')
    D.p('Duyệt x = 1, 2, 3, ...: chia x cho 2, 3, 5 tới hết; nếu còn lại 1 thì x là số Hamming. Dừng khi gặp số thứ n.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách kiểm tra từng số.', 11.5)
    D.code('HAMMING.CPP (ngây thơ): kiểm tra từng số', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Số lần lặp bằng **giá trị** của đáp số, không phải n. Đo thực tế: n = 500 (đáp số 937 500) mất 0,05 giây; n = 1000 (51 200 000) mất **1,5 giây**; '
                               'n = 1500 (859 963 392) mất **25,6 giây**; n = 10^{4} cần 2,9 · 10^{17} lần lặp: hàng nghìn năm.'])
    D.kbox('BẾ TẮC', ['Số Hamming càng về sau càng **thưa**: trong 10^{17} số đầu tiên chỉ có vài nghìn số Hamming. Duyệt mọi số là lãng phí khủng khiếp. Ta cần **sinh** trực tiếp số Hamming tiếp theo từ các số Hamming đã có.'])

    D.h('4. Phá bế tắc: Ba con trỏ')
    D.step(1, 'Số Hamming sinh ra số Hamming')
    D.p('Mọi số Hamming x > 1 đều bằng 2, 3 hoặc 5 nhân với một số Hamming **nhỏ hơn** (x/2, x/3 hoặc x/5). Vậy dãy h được tạo thành từ ba dãy: 2 · h, 3 · h, 5 · h, mỗi dãy đều **tăng**. '
        'Bài toán trở thành **trộn** ba dãy tăng (như bước trộn của sắp xếp trộn), bỏ các phần tử trùng.')
    D.step(2, 'Ba con trỏ')
    D.p('Giữ ba chỉ số i2, i3, i5: phần tử tiếp theo của dãy "2 · h" chưa dùng là 2 · h[i2], tương tự với 3 và 5. h[k] là số nhỏ nhất trong ba ứng viên; '
        'sau đó tăng **mọi** con trỏ có ứng viên bằng h[k]. Tăng cả khi bằng nhau là cách loại trùng: 6 = 2 · 3 = 3 · 2 chỉ được ghi một lần.')
    D.step(3, 'Chạy tay')
    D.fig(P.fig('ptr'), 'Ba con trỏ sinh 11 số Hamming sau số 1.', 13.5)
    D.kbox('VÌ SAO ĐÚNG?', ['Bất biến: h[0..k−1] là k số Hamming nhỏ nhất, theo thứ tự tăng, và với mỗi p ∈ {2, 3, 5}, p · h[i_{p}] là bội p **nhỏ nhất** chưa vượt qua h[k − 1]. '
                            'Số Hamming tiếp theo x có dạng p · y với y nhỏ hơn x, nên y đã có trong h, và x chính là min của ba ứng viên. Mỗi con trỏ chỉ tiến, nên tổng số bước là O(n).'])
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của kĩ thuật ba con trỏ.', 11)
    D.code('HAMMING.CPP: ba con trỏ', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['n bước, mỗi bước 3 phép nhân và 3 phép so sánh: O(n). n = 10^{4} chạy chưa tới **0,01 giây**. Đã đối chiếu với cách kiểm tra từng số trên 150 bộ dữ liệu. '
                               'Một kết quả vui: số Hamming thứ 2026 là 9 000 000 000 = 2^{9} · 3^{2} · 5^{9}.'])
    D.kbox('LƯU Ý', ['Với k số nguyên tố bất kì (số "siêu xấu xí"), dùng k con trỏ: mỗi bước O(k), hoặc một hàng đợi ưu tiên chứa k ứng viên: O(log k). '
                     'Cách "đẩy x · 2, x · 3, x · 5 vào hàng đợi ưu tiên, dùng set để loại trùng" cũng đúng nhưng chậm hơn và tốn bộ nhớ hơn.'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Fibonacci và định lí Zeckendorf')
    D.kbox('ĐỊNH LÍ (ZECKENDORF)', ['Mọi số nguyên dương viết được **duy nhất** thành tổng các số Fibonacci (1, 2, 3, 5, 8, 13, ...) đôi một **không kề nhau** trong dãy. Cách viết tìm được bằng tham lam: lấy số Fibonacci lớn nhất không vượt quá n, rồi lặp lại với phần còn lại.'])
    D.kbox('VÌ SAO ĐÚNG?', ['Nếu F_{k} ≤ n < F_{k+1} thì phần còn lại n − F_{k} < F_{k+1} − F_{k} = F_{k−1}, nên số tiếp theo được lấy có chỉ số ≤ k − 2: không kề nhau. '
                            'Tính duy nhất: tổng các số Fibonacci không kề nhau có chỉ số < k luôn nhỏ hơn F_{k} (chứng minh bằng quy nạp).'])
    D.code('Biểu diễn Zeckendorf', P.src('ex_zeck.cpp'))
    D.p('Ví dụ: 100 = 89 + 8 + 3; 2026 = 1597 + 377 + 34 + 13 + 5. Với n = 10^{18}, biểu diễn có 27 số hạng. Đã kiểm tra tổng và tính "không kề nhau" cho mọi n < 3000 và 300 số ngẫu nhiên tới 10^{18}. '
        'Chú ý điều kiện vòng while viết dạng F.back() ≤ n − F[...] để không tràn số khi n gần 10^{18}.')
    D.sub('Mở rộng 2: Số Catalan')
    D.p('C_{n} = (2n)! / ((n + 1)! n!): 1, 1, 2, 5, 14, 42, 132, ... đếm số cách đặt n cặp ngoặc đúng, số cây nhị phân n nút, số cách chia đa giác n + 2 cạnh thành tam giác. '
        'Tính bằng truy hồi C_{n+1} = Σ C_{i} C_{n−i}, hoặc theo mô-đun bằng giai thừa và nghịch đảo.')
    D.sub('Mở rộng 3: Dãy Collatz')
    D.p('Từ n: chẵn thì chia 2, lẻ thì thành 3n + 1. Giả thuyết Collatz (chưa ai chứng minh): mọi n đều về 1. Từ 27 cần 111 bước và đi lên tới 9 232. '
        'Bài "số nhỏ hơn N có dãy Collatz dài nhất" giải bằng **nhớ kết quả** (memo) cho các số nhỏ, giống tư tưởng ghi nhớ trong phát hiện chu trình (Bài 11).')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Chỉ tăng một con trỏ** khi có hai ứng viên bằng nhau: dãy bị lặp 6, 6, 10, 10, ...',
        '- **Tràn số** khi n lớn: số Hamming thứ 10^{5} khoảng 2,9 · 10^{37}, vượt long long; số Fibonacci thứ 93 vượt 2^{63}.',
        '- **Kiểm tra số tam giác bằng sqrt** của số thực khi x lớn: dùng isqrt.',
        '- **Dùng double cho C_{n}:** từ n = 31, C_{n} vượt 2^{53} và không còn biểu diễn chính xác; dùng số nguyên hoặc mô-đun.'])
    D.kbox('GHI NHỚ', [
        '- x là số tam giác ⇔ 8x + 1 chính phương.',
        '- Sinh dãy tăng các số dạng 2^{a}3^{b}5^{c}: ba con trỏ, tăng mọi con trỏ trùng. O(n).',
        '- Zeckendorf: tham lam lấy số Fibonacci lớn nhất; các số hạng không bao giờ kề nhau.'])
    D.luyentap([('20.1', 'SỐ HAMMING', 'Tìm số Hamming thứ n, và số Hamming nhỏ nhất ≥ X: bài HAMMING, kết hợp chặt nhị phân.'),
                ('20.2', 'SỐ TAM GIÁC', 'Kiểm tra 10^{5} số x ≤ 10^{18} có phải số tam giác không; đếm số tam giác trong [L, R]: định lí ở mục 1.'),
                ('20.3', 'FIBONACCI', 'Biểu diễn Zeckendorf của n ≤ 10^{18}, và số cách viết n thành tổng các số Fibonacci khác nhau: Mở rộng 1.')])
    D.tukiemtra([('210 có phải số tam giác không?', 'Có: 8 · 210 + 1 = 1681 = 41², 210 = T₂₀'), ('Số Hamming thứ 20?', '36'),
                 ('Biểu diễn Zeckendorf của 50?', '34 + 13 + 3'), ('Vì sao 14 không phải số Hamming?', '14 = 2 · 7 có ước nguyên tố 7')])
