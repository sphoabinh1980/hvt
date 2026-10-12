def build(D, P):
    D.objectives([
        'Kiểm tra số chính phương **chính xác** bằng hàm isqrt (không tin vào sqrt của số thực).',
        'Phát biểu và hiểu **định lí hai bình phương** của Fermat: n là tổng hai bình phương khi nào, và có bao nhiêu cách.',
        'Trả lời 10^{6} truy vấn với n ≤ 10^{7} bằng **sàng ước nguyên tố nhỏ nhất** (spf) để phân tích thừa số trong O(log n).',
        'Sinh mọi bộ ba Pythagoras bằng công thức Euclid; biết định lí ba bình phương và bốn bình phương.'])
    D.kbox('KHỞI ĐỘNG', [
        'Năm 2025 = 45^{2} là năm chính phương cuối cùng trước năm 2116 = 46^{2}. Năm 2026 thì sao? 2026 = 45^{2} + 1^{2}: một **tổng của hai bình phương**. '
        'Còn 2027 thì không thể viết như vậy, dù em thử bao nhiêu cặp đi nữa.',
        'Vì sao? Câu trả lời của Fermat (1640) là một trong những định lí đẹp nhất của số học: nó chỉ phụ thuộc vào **các ước nguyên tố** của n chia cho 4 dư mấy.'])

    D.h('1. Số chính phương và hàm isqrt')
    D.kbox('ĐỊNH NGHĨA', ['n là **số chính phương** nếu n = k^{2} với k nguyên. isqrt(n) = ⌊√n⌋ là số nguyên k lớn nhất có k^{2} ≤ n. n chính phương khi và chỉ khi isqrt(n)^{2} = n.'])
    D.p('Kiểm tra bằng (long long)sqrt(n) rồi bình phương lại là **không an toàn** khi n lớn: kiểu double chỉ có 53 bit, không phân biệt được 10^{18} − 1 với 10^{18}. '
        'Thực tế sqrt(10^{18} − 1) tính bằng double trả về đúng 10^{9}, trong khi isqrt(10^{18} − 1) = 999 999 999. Cách an toàn: lấy xấp xỉ rồi **chỉnh lại** bằng số nguyên:')
    D.kbox('THUẬT TOÁN (ISQRT)', ['$code r = sqrtl(x);  while (r * r > x) r--;  while ((r + 1) * (r + 1) <= x) r++;',
                                  'Với x ≤ 10^{18}, sai số của sqrtl chỉ vài đơn vị nên hai vòng while chạy rất ít lần; (r + 1)^{2} không tràn long long.'])
    D.kbox('LƯU Ý', ['Số chính phương chỉ có thể tận cùng bằng 0, 1, 4, 5, 6, 9 và chia 4 dư 0 hoặc 1, chia 8 dư 0, 1, 4. Dùng các điều kiện này để loại nhanh trước khi gọi isqrt.'])

    D.h('2. Định lí hai bình phương')
    D.p('Trong Hình 19.1: các số nguyên tố 5, 13, 17, 29, 37, 41 (chia 4 dư 1) đều viết được; 3, 7, 11, 19, 23, 31, 43, 47 (chia 4 dư 3) đều không. Hợp số thì phụ thuộc vào ước nguyên tố: 21 = 3 · 7 không được, nhưng 45 = 3^{2} · 5 = 36 + 9 lại được.')
    D.fig(P.fig('grid'), 'Các số 1..50 viết được thành tổng hai bình phương (tô màu), kể cả 0^{2}.', 13)
    D.kbox('ĐỊNH LÍ (FERMAT, HAI BÌNH PHƯƠNG)', [
        'Viết n = 2^{a} · Π p_{i}^{e_{i}} · Π q_{j}^{f_{j}}, với p_{i} ≡ 1 và q_{j} ≡ 3 (mod 4). Khi đó n là tổng hai bình phương **khi và chỉ khi mọi f_{j} đều chẵn**. Khi đó, đặt B = Π (e_{i} + 1):',
        '$eq số cặp (a, b) với 0 ≤ a ≤ b, a² + b² = n  =  (B + [n chính phương] + [n = 2h²]) / 2'])
    D.kbox('VÌ SAO ĐÚNG?', [
        '- **Chiều "không được":** bình phương chia 4 dư 0 hoặc 1, nên a^{2} + b^{2} không bao giờ chia 4 dư 3. Tổng quát hơn: nếu q ≡ 3 (mod 4) chia hết a^{2} + b^{2} thì q chia hết cả a và b, nên q xuất hiện với số mũ chẵn.',
        '- **Chiều "được":** đẳng thức Brahmagupta (a^{2} + b^{2})(c^{2} + d^{2}) = (ac − bd)^{2} + (ad + bc)^{2} cho phép nhân các biểu diễn; phần khó (do Fermat phát biểu, Euler chứng minh) là mọi p ≡ 1 (mod 4) đều là tổng hai bình phương.',
        '- **Công thức đếm:** số cách viết có thứ tự và có dấu là r_{2}(n) = 4B (Jacobi). Mỗi cặp 0 < a < b ứng với 8 cách có dấu và thứ tự; cặp (0, b) và cặp (h, h) mỗi loại ứng với 4 cách. Đếm ngược lại được công thức trên.'])
    D.fig(P.fig('circle'), 'Các điểm nguyên trên đường tròn x² + y² = 325 trong góc phần tư thứ nhất.', 13)

    D.h('3. Bài toán HAIBP')
    D.problem_box('HAIBP', 'Cho Q số nguyên n. Với mỗi số, hãy đếm số cặp số nguyên (a, b) với 0 ≤ a ≤ b và a^{2} + b^{2} = n.',
                  'Dòng đầu chứa Q (1 ≤ Q ≤ 10^{6}); Q dòng tiếp theo, mỗi dòng một số n (1 ≤ n ≤ 10^{7}).', 'Q dòng, dòng thứ i là đáp số cho truy vấn thứ i.')
    D.examples('HAIBP', [('5 / 25 / 2026 / 3 / 50 / 325', '2 / 1 / 0 / 2 / 3', '25 = 0² + 5² = 3² + 4²; 2026 = 1² + 45²; 50 = 1² + 7² = 5² + 5².')])
    D.p('Subtask 1 (30 điểm): Q ≤ 1 000. Subtask 2 (70 điểm): Q ≤ 10^{6}.')

    D.h('4. Ý tưởng ngây thơ: Thử mọi a')
    D.p('Với mỗi truy vấn, thử a = 0, 1, 2, ... sao cho a ≤ b, tức 2a^{2} ≤ n; kiểm tra n − a^{2} có chính phương không bằng isqrt.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử mọi a.', 11.5)
    D.code('HAIBP.CPP (ngây thơ): thử mọi a', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi truy vấn khoảng √(n/2) ≈ 2 236 lần thử, mỗi lần một phép sqrtl. Đo thực tế: 10^{6} truy vấn ngẫu nhiên mất **10,9 giây**. Đủ cho subtask 1, không đủ cho subtask 2.'])
    D.kbox('BẾ TẮC', ['Ta không cần **tìm** các cặp, chỉ cần **đếm**. Định lí hai bình phương cho đáp số từ phân tích thừa số nguyên tố. Nhưng phân tích n ≤ 10^{7} bằng thử chia tốn tới √n ≈ 3 162 phép chia: chưa nhanh hơn bao nhiêu.'])

    D.h('5. Phá bế tắc: Sàng ước nguyên tố nhỏ nhất')
    D.step(1, 'Sàng spf một lần')
    D.p('Với mỗi m ≤ 10^{7}, lưu spf[m] = ước nguyên tố nhỏ nhất của m: chạy sàng Eratosthenes, khi gặp số nguyên tố i thì ghi i vào mọi bội chưa có giá trị. Tốn khoảng N log log N phép tính và 40 MB bộ nhớ.')
    D.step(2, 'Phân tích trong O(log n)')
    D.p('Lặp: p = spf[m], chia m cho p tới hết, đếm số mũ e; rồi tiếp tục với m mới. Mỗi bước chia làm m giảm ít nhất một nửa, nên chỉ tối đa log_{2} n ≈ 23 phép chia.')
    D.step(3, 'Áp dụng định lí')
    D.p('Trong khi phân tích: p ≡ 1 (mod 4) thì nhân B với e + 1; p ≡ 3 (mod 4) với e lẻ thì đáp số là 0; p = 2 không ảnh hưởng. Cuối cùng cộng thêm hai số hạng hiệu chỉnh và chia đôi. '
        'Ví dụ 325 = 5^{2} · 13: B = 3 · 2 = 6; 325 không chính phương, không có dạng 2h^{2}: đáp số 6 / 2 = **3** (khớp Hình 19.2).')
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của cách dùng sàng spf.', 12)
    D.code('HAIBP.CPP: sàng spf và định lí hai bình phương', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Sàng tới 10^{7}: khoảng **0,18 giây**. Mỗi truy vấn tối đa 23 phép chia. Đo thực tế với 10^{6} truy vấn: **0,72 giây** (gồm cả đọc ghi bằng scanf, printf). '
                               'Công thức đếm đã được đối chiếu với cách thử mọi a trên 300 bộ dữ liệu.'])

    D.h('6. Mở rộng')
    D.sub('Mở rộng 1: Bộ ba Pythagoras')
    D.p('Bộ ba Pythagoras (a, b, c) với a^{2} + b^{2} = c^{2} là **nguyên thủy** nếu ƯCLN(a, b) = 1. Công thức Euclid: mọi bộ ba nguyên thủy có dạng '
        'a = m^{2} − n^{2}, b = 2mn, c = m^{2} + n^{2} với m > n > 0, ƯCLN(m, n) = 1 và m − n lẻ, mỗi bộ đúng một lần. Mọi bộ ba khác là bội k · (a, b, c) của một bộ nguyên thủy.')
    D.code('Đếm bộ ba Pythagoras với c ≤ N', P.src('ex_pytago.cpp'))
    D.p('Kết quả: với N = 100 có 16 bộ nguyên thủy và 52 bộ tất cả; N = 2026: 322 và 2 009; N = 10^{6}: 159 139 và 1 980 642. N = 10^{8} chạy 1,2 giây. Đã đối chiếu với cách duyệt trên 46 giá trị N ≤ 2026.')
    D.sub('Mở rộng 2: Ba bình phương, bốn bình phương')
    D.kbox('ĐỊNH LÍ (LAGRANGE VÀ LEGENDRE)', ['- **Lagrange (1770):** mọi số tự nhiên là tổng của **bốn** bình phương.',
                                             '- **Legendre:** n là tổng của **ba** bình phương khi và chỉ khi n không có dạng 4^{a}(8b + 7). Các số không viết được: 7, 15, 23, 28, 31, 39, ...'])
    D.p('Hệ quả cho bài "số bình phương ít nhất có tổng bằng n" (rất hay gặp): đáp số là 1 nếu n chính phương, 2 nếu định lí hai bình phương cho phép, 4 nếu n = 4^{a}(8b + 7), còn lại là 3. Mỗi truy vấn O(√n) hoặc O(log n) với sàng spf.')
    D.sub('Mở rộng 3: Đếm số chính phương trong đoạn')
    D.p('Số các số chính phương trong [L, R] là isqrt(R) − isqrt(L − 1): một công thức, không cần duyệt. Tương tự, số các lập phương là icbrt(R) − icbrt(L − 1), với icbrt viết theo cùng kiểu "xấp xỉ rồi chỉnh".')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Tin vào sqrt:** (long long)sqrt(10^{18} − 1) = 10^{9}, sai. Luôn chỉnh lại bằng số nguyên.',
        '- **Quên số mũ chẵn:** 9 = 0^{2} + 3^{2} được, dù 3 ≡ 3 (mod 4).',
        '- **Đếm trùng/thiếu** khi a = 0 hoặc a = b: chính là hai số hạng hiệu chỉnh trong công thức.',
        '- **Sàng spf với vector<int> 10^{7}** phần tử: 40 MB, cẩn thận giới hạn bộ nhớ; đọc ghi 10^{6} dòng phải dùng scanf/printf hoặc tắt đồng bộ cin.'])
    D.kbox('GHI NHỚ', [
        '- isqrt: xấp xỉ bằng sqrtl, rồi chỉnh bằng hai vòng while.',
        '- n là tổng hai bình phương ⇔ mọi ước nguyên tố dạng 4k + 3 có số mũ chẵn.',
        '- Nhiều truy vấn phân tích thừa số với n ≤ 10^{7}: sàng spf, mỗi truy vấn O(log n).'])
    D.luyentap([('19.1', 'HAI BÌNH PHƯƠNG', 'Đếm số cách viết n thành tổng hai bình phương cho 10^{6} truy vấn: bài HAIBP.'),
                ('19.2', 'ÍT BÌNH PHƯƠNG NHẤT', 'Số bình phương ít nhất có tổng bằng n (n ≤ 10^{12}): Mở rộng 2.'),
                ('19.3', 'PYTHAGORAS', 'Đếm bộ ba Pythagoras với c ≤ N, và liệt kê các bộ có cạnh huyền c cho trước: Mở rộng 1 kết hợp định lí hai bình phương.')])
    D.tukiemtra([('2027 có phải tổng hai bình phương không?', 'Không: 2027 chia 4 dư 3'), ('Có bao nhiêu cặp 0 ≤ a ≤ b với a² + b² = 65?', '2 (1 + 64, 16 + 49)'),
                 ('Số bình phương ít nhất có tổng bằng 7?', '4 (7 = 4 + 1 + 1 + 1)'), ('Bộ ba Pythagoras nguyên thủy ứng với m = 2, n = 1?', '(3, 4, 5)')])
