def build(D, P):
    D.objectives([
        'Hiểu một số tự nhiên được ghép từ các chữ số như thế nào: **giá trị theo vị trí**.',
        'Tách chữ số bằng hai phép `% 10` và `/ 10`; tính số chữ số, tổng, tích chữ số, số đảo ngược.',
        'Biết vì sao "cộng theo cột" nhanh hơn "cộng theo hàng" hàng tỉ lần, và tính tổng chữ số của mọi số từ 1 tới 10^{15} trong nháy mắt.',
        'Tránh các bẫy kinh điển: số 0, số âm, tràn số khi đảo ngược, tràn số khi nhân p với 10.'])
    D.kbox('KHỞI ĐỘNG', [
        'Một cuốn sách dày 2026 trang. Người thợ in cần bao nhiêu kí tự số để in hết số trang? Và nếu cộng tất cả các chữ số đã in lại thì được bao nhiêu?',
        'Với 2026 trang, em có thể ngồi cộng cả buổi chiều. Nhưng nếu là 10^{15} "trang" thì sao? Một máy tính cộng từng chữ số cần khoảng ba tháng. '
        'Bài học này chỉ ra rằng chỉ cần **16 lượt tính** là đủ, nhờ một cách nhìn mới: thay vì cộng theo từng **số**, hãy cộng theo từng **cột chữ số**.'])

    D.h('1. Giá trị theo vị trí')
    D.p('Trong hệ thập phân, mỗi chữ số mang một giá trị phụ thuộc vào **vị trí** của nó: chữ số 2 trong 2026 đứng ở hàng nghìn nên mang giá trị 2000, còn chữ số 2 thứ hai đứng ở hàng chục nên chỉ mang giá trị 20.')
    D.kbox('ĐỊNH NGHĨA (BIỂU DIỄN THẬP PHÂN)', [
        'Mỗi số tự nhiên n > 0 viết được duy nhất dưới dạng',
        '$eq **n = d_{k−1} · 10^{k−1} + ... + d_{1} · 10^{1} + d_{0} · 10^{0}**',
        'trong đó các **chữ số** d_{i} thuộc {0, 1, ..., 9} và chữ số đầu d_{k−1} ≠ 0. Số k gọi là **số chữ số** của n; d_{0} là chữ số hàng đơn vị, d_{1} hàng chục, ... '
        'Ta viết gọn n = (d_{k−1} ... d_{1} d_{0})_{10}. Riêng số 0 được viết bằng một chữ số 0.'])
    D.fig(P.fig('place'), 'Bốn chữ số của 2026 và giá trị theo vị trí của chúng.', 14)
    D.p('Từ định nghĩa, mọi số hạng trừ d_{0} đều chia hết cho 10, nên **d_{0} = n mod 10**. Phần còn lại, chia cho 10, là số (d_{k−1} ... d_{1})_{10}: bỏ đi chữ số cuối chính là **⌊n / 10⌋**. Hai phép tính này là "con dao" để tách mọi chữ số.')

    D.h('2. Tách chữ số bằng % 10 và / 10')
    D.kbox('THUẬT TOÁN (TÁCH CHỮ SỐ)', [
        '$n 1|Lấy chữ số hàng đơn vị: d = n % 10.',
        '$n 2|Xử lí d (cộng vào tổng, nhân vào tích, đếm...).',
        '$n 3|Bỏ chữ số hàng đơn vị: n = n / 10. Nếu n > 0, quay lại bước 1.',
        'Các chữ số lấy ra theo thứ tự **từ phải sang trái**. Số lượt lặp đúng bằng số chữ số k ≈ log_{10} n + 1, nên n tới 10^{18} chỉ mất 19 lượt.'])
    D.fig(P.fig('tach'), 'Tách 2026: mỗi lượt lấy một chữ số bằng % 10, rồi bỏ nó đi bằng / 10.', 15)
    D.p('Bốn hàm dưới đây là "bộ đồ nghề" sẽ dùng trong cả cuốn sách. Hãy để ý hàm **soChuSo** và **tichChuSo** dùng `do ... while` chứ không dùng `while`: với n = 0, vòng `while (n > 0)` không chạy lần nào và cho số chữ số bằng 0, trong khi số 0 có một chữ số.')
    D.code('Bộ đồ nghề tách chữ số', P.src('ex_digits.cpp'))
    D.table(['n', 'Số chữ số', 'Tổng chữ số', 'Tích chữ số', 'Số đảo ngược'], [
        ['0', '1', '0', '0', '0'], ['7', '1', '7', '7', '7'], ['2026', '4', '10', '0', '6202'], ['1200', '4', '3', '0', '21'],
        ['987654321', '9', '45', '362880', '123456789']], widths=[2, 1.4, 1.4, 1.4, 1.8], sz=20)
    D.p('Bảng trên là kết quả chạy chương trình. Hãy để ý số đảo ngược của 1200 là 21 chứ không phải 0021: các chữ số 0 ở đầu tự biến mất. '
        'Nếu đề bài coi "0021" là kết quả đúng, phải làm việc với **xâu** chứ không phải với số.')
    D.kbox('LƯU Ý: SỐ ÂM VÀ TRÀN SỐ', [
        '- Với n âm, `n % 10` trong C++ cũng âm (−2026 % 10 = −6). Hãy tách dấu ra trước: làm việc với |n|.',
        '- Số đảo ngược có thể **lớn hơn** số ban đầu: n = 1 999 999 999 vừa kiểu int nhưng số đảo ngược 9 999 999 991 thì không. '
        'Với long long, n = 1 999 999 999 999 999 999 (≈ 2 · 10^{18}) có số đảo ngược ≈ 10^{19}, vượt 9,2 · 10^{18}. Luôn ước lượng độ lớn của kết quả trước khi chọn kiểu.'])

    D.h('3. Bài toán TONGCS')
    D.problem_box('TONGCS', 'Viết liên tiếp các số tự nhiên 1, 2, 3, ..., n. Hãy tính tổng tất cả các chữ số đã viết.',
                  'Một số nguyên n (1 ≤ n ≤ 10^{15}).', 'Một số nguyên là tổng các chữ số của mọi số từ 1 tới n.')
    D.examples('TONGCS', [('12', '51', '1 + 2 + ... + 9 = 45; 10, 11, 12 có tổng chữ số 1, 2, 3. Tổng 45 + 6 = 51.'),
                          ('100', '901', 'Mỗi chữ số 1..9 xuất hiện 10 lần ở hàng đơn vị và 10 lần ở hàng chục: 20 · 45 = 900; thêm 1 của số 100.'),
                          ('2026', '28189', 'Được tính tay ở mục 5, bước 3.')])

    D.h('4. Ý tưởng ngây thơ: Cộng chữ số của từng số')
    D.p('Đề bài nói "cộng tất cả các chữ số", vậy cứ làm đúng như thế: với mỗi x từ 1 tới n, tách các chữ số của x bằng thuật toán ở mục 2 và cộng dồn.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách cộng từng số.', 11)
    D.code('TONGCS.CPP (ngây thơ): tách chữ số của từng x', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Có n số, mỗi số tách tối đa 16 chữ số: khoảng 16n phép chia. Đo thực tế: n = 10^{8} mất **0,85 giây**, n = 10^{9} mất **9,4 giây**. '
                               'Với n = 10^{15} lớn gấp một triệu lần, chương trình cần khoảng **9 · 10^{6} giây, tức hơn 100 ngày**.'])
    D.kbox('BẾ TẮC', ['Chương trình làm đúng nhưng làm **quá nhiều việc lặp lại**: chữ số hàng đơn vị chạy 0, 1, 2, ..., 9 rồi lại 0, 1, 2, ... '
                      'hàng trăm nghìn tỉ lần, và lần nào ta cũng cộng lại từ đầu. Có cách nào cộng một lần cho cả một "chu kì" không?'])

    D.h('5. Phá bế tắc: Đếm theo cột')
    D.step(1, 'Đổi thứ tự cộng: theo cột thay vì theo hàng')
    D.p('Viết các số 0, 1, 2, ..., n thẳng hàng theo cột (thêm chữ số 0 vào đầu cho đủ độ dài; các chữ số 0 thêm vào không làm thay đổi tổng). '
        'Tổng mọi chữ số trong bảng không đổi dù ta cộng theo **hàng** (từng số) hay theo **cột** (từng vị trí). Cộng theo cột có lợi vì mỗi cột có một quy luật rất đơn giản.')
    D.kbox('HÃY HÌNH DUNG', ['Bảng các số xếp dọc giống như đồng hồ đo quãng đường của xe máy: bánh xe hàng đơn vị quay nhanh nhất, 0 → 9 rồi quay về 0; '
                             'mỗi lần nó quay hết một vòng thì bánh xe hàng chục nhích lên một nấc. Mỗi bánh xe quay **đều đặn**, chỉ có tốc độ khác nhau.'])
    D.fig(P.fig('cot'), 'Các số 0..29 viết thành hai cột: mỗi cột lặp lại theo một chu kì riêng.', 15.2)
    D.step(2, 'Quy luật của một cột')
    D.p('Xét cột có giá trị vị trí p (p = 1 là cột đơn vị, p = 10 là cột chục, ...). Khi x chạy 0, 1, 2, ..., chữ số ở cột này là ⌊x / p⌋ mod 10: '
        'đầu tiên **p số 0**, rồi p số 1, ..., p số 9, rồi lặp lại. Một chu kì dài 10p và có tổng (0 + 1 + ... + 9) · p = 45p.')
    D.kbox('ĐỊNH LÍ (TỔNG MỘT CỘT)', [
        'Với n ≥ 0 và cột p, đặt high = ⌊n / 10p⌋ (số chu kì trọn vẹn), cur = ⌊n / p⌋ mod 10 (chữ số của n ở cột này), low = n mod p (phần bên phải cột). '
        'Tổng các chữ số ở cột p của mọi số 0, 1, ..., n là',
        '$eq **T_{p} = 45 · high · p  +  p · cur(cur − 1)/2  +  cur · (low + 1)**',
        'và đáp số của bài toán là tổng T_{p} theo mọi p = 1, 10, 100, ... không vượt quá n.'])
    D.kbox('VÌ SAO ĐÚNG?', [
        'Các số 0..n chia làm hai phần: high · 10p số đầu tạo thành high chu kì trọn vẹn, góp 45p mỗi chu kì. Phần còn lại là các số từ high · 10p tới n. '
        'Ở phần này chữ số cột p lần lượt là 0 (p lần), 1 (p lần), ..., cur − 1 (p lần): góp p · (0 + 1 + ... + (cur − 1)) = p · cur(cur − 1)/2; '
        'cuối cùng là chữ số cur, xuất hiện ở các số từ high · 10p + cur · p tới n, tức low + 1 số, góp cur · (low + 1).'])
    D.step(3, 'Chạy tay với n = 2026')
    D.table(['Cột p', 'high', 'cur', 'low', '45 · high · p', 'p · cur(cur−1)/2', 'cur · (low+1)', 'T_p'], [
        ['1', '202', '6', '0', '9090', '15', '6', '9111'], ['10', '20', '2', '6', '9000', '10', '14', '9024'],
        ['100', '2', '0', '26', '9000', '0', '0', '9000'], ['1000', '0', '2', '26', '0', '1000', '54', '1054'],
        ['', '', '', '', '', '', '**Tổng**', '**28189**']], widths=[0.9, 0.8, 0.6, 0.7, 1.3, 1.5, 1.3, 0.9], sz=19, hl=[4])
    D.p('Bốn lượt tính thay cho việc tách 2026 số. Kiểm tra cột nghìn: các số 1000..1999 có chữ số nghìn bằng 1 (1000 lần), các số 2000..2026 có chữ số nghìn bằng 2 (27 lần): '
        '1000 + 54 = 1054, khớp với bảng.')
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của cách đếm theo cột.', 13)
    D.code('TONGCS.CPP: đếm theo cột', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Vòng lặp chạy một lần cho mỗi cột: 16 lượt với n = 10^{15}, mỗi lượt vài phép tính. Từ "hơn 100 ngày" xuống **dưới một phần triệu giây**. '
                               'Đáp số với n = 10^{15} là 67 500 000 000 000 001 ≈ 6,75 · 10^{16}: vẫn vừa long long.'])

    D.h('6. Mở rộng')
    D.sub('Mở rộng 1: Chữ số d xuất hiện bao nhiêu lần?')
    D.p('Câu hỏi của người thợ in: khi đánh số trang 1..n, chữ số d được in bao nhiêu lần? Cùng cách đếm theo cột: ở cột p, chữ số d xuất hiện high · p lần trong các chu kì trọn vẹn, '
        'thêm p lần nếu cur > d, hoặc low + 1 lần nếu cur = d. Riêng **chữ số 0** phải trừ đi một chu kì, vì không ai viết số 0 ở đầu (trang 7 không in thành 0007).')
    D.code('Đếm số lần xuất hiện của chữ số d trong 1..n', P.src('ex_count.cpp'))
    D.p('Kiểm tra bằng cách đếm trực tiếp trên hàng trăm giá trị n ≤ 3000: hàm cho kết quả đúng ở mọi trường hợp. Với n = 2026: chữ số 0 được in 529 lần, chữ số 2 được in 637 lần.')
    D.sub('Mở rộng 2: Tổng chữ số trên một đoạn')
    D.p('Gọi F(n) là đáp số của TONGCS. Tổng các chữ số của mọi số từ L tới R là **F(R) − F(L − 1)**, giống hệt tổng đoạn bằng hiệu hai tổng tiền tố. Nhớ F(0) = 0.')
    D.sub('Mở rộng 3: Khi n tới 10¹⁸')
    D.p('F(10^{18} − 1) = 18 · 45 · 10^{17} = 8,1 · 10^{19}: vượt cả unsigned long long (≈ 1,8 · 10^{19}). Phải cộng bằng __int128 và tự viết hàm in. '
        'Thêm một cái bẫy: khi p = 10^{18}, biểu thức p * 10 tràn long long; hãy dừng vòng lặp trước khi nhân, hoặc dùng __int128 cho p.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Số 0:** `while (n > 0)` không chạy lần nào khi n = 0. Số chữ số của 0 là 1.',
        '- **Số âm:** `-7 % 10` bằng −7 trong C++. Tách dấu trước khi tách chữ số.',
        '- **Tràn khi đảo ngược** hoặc khi nhân p với 10 ở cột cuối.',
        '- **Quên chữ số 0 đứng đầu** khi đếm chữ số 0: phải trừ đi các số 0 "tưởng tượng" ở đầu.',
        '- **Dùng int** cho tổng: tổng chữ số của 1..10^{9} đã là 4,05 · 10^{10}.'])
    D.kbox('GHI NHỚ', [
        '- Chữ số hàng đơn vị là n % 10, bỏ nó đi là n / 10. Số chữ số của n là số lần chia cho 10 tới khi bằng 0 (nhưng số 0 có 1 chữ số).',
        '- Khi phải cộng/đếm chữ số của **rất nhiều số liên tiếp**, hãy cộng **theo cột**: cột p lặp chu kì 10p.',
        '- Công thức một cột dùng ba đại lượng high = n / 10p, cur = (n / p) % 10, low = n % p.',
        '- Đáp số trên đoạn [L, R] = F(R) − F(L − 1).'])
    D.luyentap([('1.1', 'ĐÁNH SỐ TRANG', 'Đếm số chữ số cần dùng và số lần xuất hiện mỗi chữ số 0..9 khi đánh số trang 1..n (n ≤ 10^{18}): Mở rộng 1, cẩn thận chữ số 0.'),
                ('1.2', 'TỔNG CHỮ SỐ ĐOẠN', 'Q truy vấn tổng chữ số của mọi số trong [L, R]: F(R) − F(L − 1), n tới 10^{18} cần __int128.'),
                ('1.3', 'SỐ ĐẢO', 'Đếm các x ≤ n có số đảo ngược lớn hơn chính nó; xử lí số tận cùng bằng 0.')])
    D.tukiemtra([('Số 10^{18} có bao nhiêu chữ số? Vòng lặp tách chữ số chạy bao nhiêu lượt?', '19 chữ số, 19 lượt'),
                 ('Tính tổng chữ số của mọi số từ 1 tới 99 bằng cách đếm theo cột.', 'mỗi cột góp 10 · 45 = 450, tổng 900'),
                 ('Khi đánh số trang một cuốn sách 100 trang, chữ số 0 được in bao nhiêu lần?', '11 lần: 10, 20, ..., 90 và hai chữ số 0 của 100'),
                 ('Số đảo ngược của 1 000 000 007 là bao nhiêu? Có vừa kiểu int không?', '7 000 000 001 > 2^{31} − 1, không vừa int')])
