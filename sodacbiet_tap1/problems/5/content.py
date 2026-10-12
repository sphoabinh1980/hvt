def build(D, P):
    D.objectives([
        'Hiểu **vì sao** các dấu hiệu chia hết cho 2, 3, 4, 5, 8, 9, 11 đúng, và tự xây dấu hiệu chia hết cho 7, 13, 37 hay một số m bất kì.',
        'Nắm định lí: một số đồng dư với tổng các chữ số nhân với 10^{k} mod m, và dãy 10^{k} mod m luôn tuần hoàn.',
        'Trả lời 10^{6} câu hỏi "đoạn chữ số từ l tới r chia m dư bao nhiêu?" mỗi câu trong O(1), nhờ **tiền tố số dư**.',
        'Đếm số đoạn con chia hết cho m bằng cách đếm cặp hậu tố cùng số dư.'])
    D.kbox('KHỞI ĐỘNG', [
        'Không cần máy tính, em biết ngay 123 456 789 chia hết cho 9 (tổng chữ số 45) và 918 082 chia hết cho 11 (2 − 8 + 0 − 8 + 1 − 9 = −22). '
        'Nhưng 2 026 202 620 có chia hết cho 7 không? Có "dấu hiệu chia hết cho 7" không?',
        'Câu trả lời là có, và mọi dấu hiệu chia hết đều sinh ra từ **một** định lí duy nhất. Hiểu được định lí ấy, em sẽ biến dấu hiệu chia hết thành một công cụ lập trình rất mạnh.'])

    D.h('1. Một định lí cho mọi dấu hiệu chia hết')
    D.p('Viết n = d_{k} · 10^{k} + ... + d_{1} · 10 + d_{0}. Theo tính chất đồng dư, ta được thay mỗi lũy thừa 10^{i} bằng số dư của nó khi chia cho m mà không làm đổi số dư của cả tổng.')
    D.kbox('ĐỊNH LÍ (SỐ DƯ QUA CÁC CHỮ SỐ)', ['Với mọi số nguyên dương m:',
                                              '$eq **n ≡ d_{0} · w_{0} + d_{1} · w_{1} + ... + d_{k} · w_{k}  (mod m)**,   với w_{i} = 10^{i} mod m.',
                                              'Các "trọng số" w_{i} tạo thành một dãy tuần hoàn (có thể có một đoạn đầu không lặp khi m có ước 2 hoặc 5).'])
    D.fig(P.fig('pow'), 'Trọng số 10ᵏ mod m của sáu số chia quen thuộc.', 15.2)
    D.p('Mỗi dấu hiệu chia hết quen thuộc là một trường hợp riêng:')
    D.table(['Chia cho', 'Trọng số w_{0}, w_{1}, w_{2}, ...', 'Dấu hiệu'], [
        ['2, 5', '1, 0, 0, ...', 'chỉ chữ số hàng đơn vị quyết định'], ['4, 25', '1, 10, 0, 0, ...', 'hai chữ số cuối'], ['8, 125', '1, 10, 100, 0, ...', 'ba chữ số cuối'],
        ['3, 9', '1, 1, 1, ...', 'tổng các chữ số'], ['11', '1, −1, 1, −1, ...  (vì 10 ≡ −1)', 'tổng đan dấu, tính từ hàng đơn vị'],
        ['7, 11, 13', '1001 = 7 · 11 · 13 nên 1000 ≡ −1', 'tổng đan dấu của các nhóm 3 chữ số'], ['27, 37', '999 = 27 · 37 nên 1000 ≡ 1', 'tổng các nhóm 3 chữ số']],
        widths=[1.3, 3.2, 3.6], align=['center', 'left', 'left'], sz=20)
    D.kbox('VÍ DỤ: CHIA HẾT CHO 7', ['2 026 202 620 chia thành các nhóm 3 chữ số từ phải: 2 | 026 | 202 | 620. Tổng đan dấu từ phải: 620 − 202 + 26 − 2 = 442. '
                                     '442 = 7 · 63 + 1, nên 2 026 202 620 chia 7 dư 1, không chia hết cho 7. Kiểm tra bằng máy: đúng như vậy.'])
    D.kbox('VÌ SAO ĐÚNG?', ['Vì 1001 = 7 · 11 · 13 nên 1000 ≡ −1 (mod 7), suy ra 1000^{j} ≡ (−1)^{j}. Viết n = Σ g_{j} · 1000^{j} với g_{j} là các nhóm 3 chữ số, ta được n ≡ Σ (−1)^{j} g_{j} (mod 7). '
                            'Lập luận y hệt cho 11 và 13; với 27 và 37 thì 1000 ≡ 1 nên không cần đan dấu.'])

    D.h('2. Bài toán DOANDU')
    D.problem_box('DOANDU', 'Cho một xâu chữ số S dài n và số nguyên dương m. Có q câu hỏi, câu hỏi thứ i cho hai chỉ số l ≤ r: hãy tính số dư khi chia cho m của số được tạo bởi các chữ số S[l], S[l+1], ..., S[r] (có thể có chữ số 0 ở đầu).',
                  'Dòng đầu là S (1 ≤ n ≤ 10^{6}). Dòng thứ hai chứa m, q (1 ≤ m ≤ 10^{9}, 1 ≤ q ≤ 10^{6}). Mỗi dòng trong q dòng tiếp theo chứa l, r (1 ≤ l ≤ r ≤ n).',
                  'q dòng, mỗi dòng một số dư.')
    D.examples('DOANDU', [('2026202620\n7 4\n1 4\n2 5\n1 10\n5 5', '3\n3\n1\n2', '2026 mod 7 = 3; "0262" = 262 = 7 · 37 + 3; cả xâu chia 7 dư 1 (ví dụ ở mục 1); "2" dư 2.')])

    D.h('3. Ý tưởng ngây thơ: Horner trên từng đoạn')
    D.p('Với mỗi câu hỏi, đọc các chữ số từ l tới r theo sơ đồ Horner: res ← (10 · res + S[i]) mod m. Đây chính là cách tính số dư của số lớn ở bộ Số học (Bài 1).')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách tính lại từng đoạn.', 11.5)
    D.code('DOANDU.CPP (ngây thơ): Horner trên từng đoạn', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi câu hỏi tốn O(r − l + 1), tổng O(q · n) trong trường hợp xấu nhất = 10^{12}. Đo thực tế: 1000 câu hỏi trên cả xâu 10^{6} chữ số mất **8,4 giây**; '
                               '10^{6} câu hỏi như vậy cần khoảng **2,3 giờ**.'])
    D.kbox('BẾ TẮC', ['Các đoạn [l, r] của những câu hỏi khác nhau chồng lên nhau rất nhiều, nhưng mỗi câu hỏi lại tính lại từ đầu. Với tổng của một đoạn, em đã biết mẹo **tổng tiền tố**: '
                      'S[l..r] = T[r] − T[l − 1]. Liệu có "số dư tiền tố" tương tự cho một đoạn chữ số không? Cẩn thận: ghép chữ số không phải là phép cộng.'])

    D.h('4. Phá bế tắc: Tiền tố số dư')
    D.step(1, 'Quan hệ giữa tiền tố và đoạn')
    D.p('Gọi N(l, r) là số tạo bởi S[l..r]. Ghép số N(1, l − 1) với số N(l, r) có r − l + 1 chữ số chính là dịch số đầu sang trái r − l + 1 chữ số rồi cộng:')
    D.eq('**N(1, r) = N(1, l − 1) · 10^{r − l + 1} + N(l, r)**')
    D.step(2, 'Lấy dư hai vế')
    D.p('Đặt P[i] = N(1, i) mod m (P[0] = 0) và pw[k] = 10^{k} mod m, tính sẵn trong một lượt duyệt. Khi đó')
    D.kbox('ĐỊNH LÍ (SỐ DƯ CỦA MỘT ĐOẠN)', ['$eq **N(l, r) mod m = (P[r] − P[l − 1] · pw[r − l + 1]) mod m**', 'Phép trừ có thể ra số âm: cộng thêm m trước khi lấy dư.'])
    D.step(3, 'Chạy tay với S = 2026202620, m = 7')
    D.fig(P.fig('prefix'), 'Tiền tố số dư P[i] và câu hỏi (2, 5).', 15.2)
    D.p('Bảng 10^{k} mod 7 = 1, 3, 2, 6, 4, 5, 1, ... cho pw[4] = 4. Câu hỏi (1, 10): P[10] − P[0] · pw[10] = 1. Câu hỏi (5, 5): P[5] − P[4] · pw[1] = 4 − 3 · 3 = −5 ≡ 2. Khớp với ví dụ.')
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối: chuẩn bị O(n), mỗi câu hỏi O(1).', 13)
    D.code('DOANDU.CPP: tiền tố số dư', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Chuẩn bị O(n), mỗi câu hỏi O(1): tổng O(n + q). 1000 câu hỏi trên cả xâu 10^{6} chữ số chạy **0,03 giây** (so với 8,4 giây); bộ 10^{6} câu hỏi chạy dưới nửa giây, '
                               'chủ yếu là thời gian đọc dữ liệu. Tích P[l − 1] · pw[...] < m^{2} ≤ 10^{18}: vừa long long.'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Đếm đoạn con chia hết cho m')
    D.p('Có bao nhiêu cặp (l, r) mà N(l, r) chia hết cho m? Nếu gcd(m, 10) = 1 thì 10 khả nghịch theo mô-đun m, và có một mẹo đẹp với **hậu tố**: gọi T[i] = N(i, n) mod m. '
        'Ta có N(l, n) = N(l, r) · 10^{n − r} + N(r + 1, n), nên N(l, r) ≡ 0 khi và chỉ khi **T[l] ≡ T[r + 1]** (vì 10^{n − r} không có ước chung với m). Bài toán trở thành đếm cặp hậu tố cùng số dư.')
    D.code('Đếm đoạn con chia hết cho m (gcd(m, 10) = 1)', P.src('ex_count.cpp'))
    D.p('Với S = 2026202620 và m = 7, chương trình cho 4 đoạn: "0" (hai lần ở vị trí 2 và 6, một lần ở vị trí 10) và "6202" = 7 · 886. Chương trình đã được đối chiếu với cách thử mọi đoạn trên 300 xâu ngẫu nhiên.')
    D.sub('Mở rộng 2: Khi m có ước 2 hoặc 5')
    D.p('Với m = 2, 4, 5, 8, 25..., trọng số w_{i} bằng 0 từ một chỗ nào đó trở đi: chỉ vài chữ số cuối quyết định. Ví dụ đếm đoạn chia hết cho 4: đoạn [l, r] hợp lệ khi số tạo bởi hai chữ số cuối S[r − 1]S[r] chia hết cho 4 '
        '(khi đó mọi l ≤ r − 1 đều được, đóng góp r − 1 đoạn), cộng thêm đoạn một chữ số S[r] nếu S[r] chia hết cho 4. Với m tổng quát, tách m = 2^{a} · 5^{b} · m\' và kết hợp hai cách.')
    D.sub('Mở rộng 3: Băm xâu chữ số')
    D.p('Công thức P[r] − P[l − 1] · pw[r − l + 1] chính là **hàm băm đa thức** dùng để so sánh hai đoạn xâu trong O(1). Chọn m là số nguyên tố lớn (chẳng hạn 10^{9} + 7) và cơ số khác 10 '
        'là có ngay công cụ so sánh xâu con, tìm xâu đối xứng... mà em sẽ gặp nhiều ở các bài xử lí xâu.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Quên nhân P[l − 1] với 10^{độ dài}:** P[r] − P[l − 1] là hiệu hai tiền tố, không phải số dư của đoạn.',
        '- **Số dư âm** sau phép trừ: cộng m.',
        '- **pw[0] = 1 khi m = 1:** phải là 1 % m = 0, nếu không có thể in ra 1 thay vì 0.',
        '- **Đọc 10^{6} câu hỏi bằng cin chưa tắt đồng bộ:** chậm gấp nhiều lần.',
        '- **Áp dụng mẹo hậu tố khi gcd(m, 10) ≠ 1:** sai, vì không chia được cho 10^{n − r}.'])
    D.kbox('GHI NHỚ', [
        '- n ≡ Σ d_{i} · (10^{i} mod m) (mod m): mọi dấu hiệu chia hết đều từ đây. 1001 = 7 · 11 · 13, 999 = 27 · 37.',
        '- N(1, r) = N(1, l − 1) · 10^{r − l + 1} + N(l, r): số dư của đoạn = P[r] − P[l − 1] · 10^{r − l + 1}.',
        '- Khi gcd(m, 10) = 1: đoạn chia hết cho m ⇔ hai hậu tố cùng số dư.'])
    D.luyentap([('5.1', 'CHIA HẾT CHO 11', 'Q truy vấn: số tạo bởi đoạn [l, r] có chia hết cho 11 không? Dùng tổng đan dấu tiền tố, không cần lũy thừa.'),
                ('5.2', 'ĐOẠN CHIA HẾT', 'Đếm đoạn con của xâu 10^{6} chữ số chia hết cho m (m ≤ 10^{9} bất kì): Mở rộng 1 và 2.'),
                ('5.3', 'XÂU GIỐNG NHAU', 'So sánh nhiều cặp đoạn con của một xâu bằng băm: Mở rộng 3.')])
    D.tukiemtra([('Tìm số dư của 2026 khi chia cho 11 bằng tổng đan dấu.', '6 − 2 + 0 − 2 = 2'),
                 ('Dãy 10^{k} mod 41 có chu kì bao nhiêu?', '5, vì 10^{5} = 100 000 = 41 · 2439 + 1'),
                 ('Số 123 123 123 chia 37 dư bao nhiêu?', 'tổng các nhóm 123 + 123 + 123 = 369 = 37 · 9 + 36, dư 36'),
                 ('Với S = 2026, m = 7, tính P[1..4].', '2, 6, 6, 3')])
