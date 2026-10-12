def build(D, P):
    D.objectives([
        'Biết các khái niệm: tổng các ước σ(n), tổng các ước thực sự s(n) = σ(n) − n; số hoàn hảo, số dư, số thiếu, số thân thiết, số kì dị.',
        'Tính σ(n) từ phân tích thừa số nguyên tố, và tính s(n) cho **mọi** n ≤ 10^{7} cùng lúc bằng **sàng tổng ước** O(N log N).',
        'Hiểu định lí Euclid–Euler: mọi số hoàn hảo chẵn đều có dạng 2^{p−1}(2^{p} − 1).',
        'Tìm các cặp số thân thiết và chuỗi số "hòa đồng" bằng mảng s đã sàng.'])
    D.kbox('KHỞI ĐỘNG', [
        'Pythagoras được hỏi: "Bạn là gì?", ông đáp: "Là một **cái tôi khác**, như 220 và 284." Các ước thực sự của 220 cộng lại bằng 284, và các ước thực sự của 284 cộng lại bằng 220. '
        'Hai số "đúng là của nhau" như thế được gọi là **cặp số thân thiết**.',
        'Hơn hai nghìn năm, người ta chỉ biết cặp này. Năm 1636 Fermat tìm ra cặp thứ hai (17 296, 18 416), Euler sau đó tìm thêm hàng chục cặp. Bằng máy tính, em sẽ tìm được **100 cặp** trong một giây.'])

    D.h('1. Tổng các ước')
    D.kbox('ĐỊNH NGHĨA', ['σ(n) là tổng mọi ước dương của n; s(n) = σ(n) − n là tổng các **ước thực sự** (ước nhỏ hơn n). Số n được gọi là:',
                          '- **hoàn hảo** nếu s(n) = n (6 = 1 + 2 + 3, 28, 496, 8128, ...);',
                          '- **dư** nếu s(n) > n (12, 18, 20, 24, ...), **thiếu** nếu s(n) < n (mọi số nguyên tố);',
                          '- hai số a ≠ b là **thân thiết** nếu s(a) = b và s(b) = a.'])
    D.fig(P.fig('pair'), 'Cặp số thân thiết nhỏ nhất: 220 và 284.', 15)
    D.kbox('ĐỊNH LÍ (CÔNG THỨC TỔNG ƯỚC)', ['Nếu n = p_{1}^{a_{1}} · p_{2}^{a_{2}} · ... · p_{k}^{a_{k}} thì',
                                           '$eq σ(n) = (1 + p_{1} + ... + p_{1}^{a_{1}}) · ... · (1 + p_{k} + ... + p_{k}^{a_{k}}) = Π (p_{i}^{a_{i}+1} − 1) / (p_{i} − 1)'])
    D.kbox('VÌ SAO ĐÚNG?', ['Khai triển tích, mỗi số hạng là p_{1}^{b_{1}} · ... · p_{k}^{b_{k}} với 0 ≤ b_{i} ≤ a_{i}: mỗi ước của n xuất hiện **đúng một lần** (phân tích thừa số nguyên tố là duy nhất). '
                            'Ví dụ 220 = 2^{2} · 5 · 11: σ(220) = 7 · 6 · 12 = 504, s(220) = 504 − 220 = 284.'])

    D.h('2. Bài toán THANTHIET')
    D.problem_box('THANTHIET', 'Cho số nguyên N. Hãy liệt kê mọi cặp số thân thiết (a, b) với a < b ≤ N.',
                  'Một số nguyên N (1 ≤ N ≤ 10^{7}).', 'Dòng đầu là số cặp K; K dòng tiếp theo, mỗi dòng một cặp a b, theo thứ tự a tăng dần.')
    D.examples('THANTHIET', [('300', '1 / 220 284', 'Mỗi dấu "/" là một lần xuống dòng.'), ('2000', '2 / 220 284 / 1184 1210', '1184 và 1210 do Paganini (16 tuổi) tìm ra năm 1866.'),
                             ('100', '0', 'Không có cặp nào.')])
    D.p('Subtask 1 (30 điểm): N ≤ 10^{5}. Subtask 2 (70 điểm): N ≤ 10^{7}.')

    D.h('3. Ý tưởng ngây thơ: Tính s(a) cho từng số')
    D.p('Với mỗi a, tính b = s(a) bằng cách thử chia tới √a (gặp ước d thì cộng cả d và a/d); nếu a < b ≤ N thì tính tiếp s(b) và so với a. Điều kiện a < b giúp mỗi cặp chỉ in một lần và loại số hoàn hảo (a = b).')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách tính s(a) từng số.', 10.5)
    D.code('THANTHIET.CPP (ngây thơ): thử chia tới căn', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi số tốn √a phép chia, cả thảy khoảng (2/3) · N^{1,5} phép chia. Đo thực tế: N = 10^{6} mất **2,95 giây**; N = 10^{7} cần khoảng 30 lần như thế, **1,5 phút**.'])
    D.kbox('BẾ TẮC', ['Khi tính s(a) cho từng a, ta "hỏi" mỗi số d có phải ước của a không: phần lớn câu trả lời là **không**. Có cách nào chỉ đi qua các cặp (d, a) mà d **thật sự** là ước của a?'])

    D.h('4. Phá bế tắc: Sàng tổng ước')
    D.step(1, 'Đảo vai trò: ước đi tìm bội')
    D.p('Thay vì với mỗi a đi tìm các ước d, ta cho mỗi d đi tới các **bội** của nó: 2d, 3d, 4d, ... (bỏ chính d, vì chỉ cộng ước thực sự), và cộng d vào s của các bội đó. '
        'Giống hệt sàng Eratosthenes, nhưng mỗi số "ghi" vào bội của nó thay vì gạch bỏ.')
    D.step(2, 'Chạy tay với N = 12')
    D.fig(P.fig('sieve'), 'Sàng tổng ước với N = 12: mỗi ô hồng là một lần cộng.', 15.5)
    D.step(3, 'Độ phức tạp')
    D.kbox('VÌ SAO NHANH?', ['Số d đi qua N/d − 1 bội. Tổng là N/1 + N/2 + ... + N/N − N ≈ N · ln N (tổng điều hòa, như sàng Eratosthenes). Với N = 10^{7}: khoảng 1,5 · 10^{8} phép cộng, '
                             'và **mỗi phép cộng là một ước thật**: không phép tính nào bị phí.'])
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của sàng tổng ước.', 11.5)
    D.code('THANTHIET.CPP: sàng tổng ước', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Đo thực tế: N = 10^{7} chạy **0,68 giây**, tìm được **100 cặp**. Đã đối chiếu với cách ngây thơ trên 100 bộ dữ liệu. '
                               'Mảng s dùng int đủ: s(n) < 4,5 · 10^{7} với n ≤ 10^{7}; nhưng s(b) có thể vượt N nên phải kiểm tra b ≤ N **trước** khi đọc s[b].'])
    D.kbox('LƯU Ý', ['Có thể tính σ trong O(N) bằng sàng tuyến tính và công thức nhân tính ở mục 1, nhưng sàng tổng ước đơn giản hơn nhiều và đã đủ nhanh. '
                     'Đổi "s[m] += d" thành "cnt[m]++" ta được **sàng số ước**; đổi thành "s[m] += d * d" được tổng bình phương các ước...'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Số hoàn hảo và định lí Euclid–Euler')
    D.kbox('ĐỊNH LÍ (EUCLID–EULER)', ['Số chẵn n là số hoàn hảo **khi và chỉ khi** n = 2^{p−1} · (2^{p} − 1) với 2^{p} − 1 là số nguyên tố (số nguyên tố Mersenne).'])
    D.kbox('VÌ SAO ĐÚNG?', ['Chiều thuận (Euclid): với q = 2^{p} − 1 nguyên tố, σ(n) = σ(2^{p−1}) · σ(q) = (2^{p} − 1) · 2^{p} = 2n, tức s(n) = n. '
                            'Chiều ngược (Euler) dùng tính nhân tính của σ: viết n = 2^{k} · m (m lẻ), từ σ(n) = 2n suy ra m phải là số nguyên tố dạng 2^{k+1} − 1.'])
    D.p('Vậy chỉ cần thử các số mũ p: không cần sàng tới 10^{18}.')
    D.code('Liệt kê các số hoàn hảo chẵn', P.src('ex_hoanhao.cpp'))
    D.p('Kết quả: 6, 28, 496, 8 128, 33 550 336, 8 589 869 056, 137 438 691 328, 2 305 843 008 139 952 128 (p = 2, 3, 5, 7, 13, 17, 19, 31). '
        'Chưa ai biết có số hoàn hảo **lẻ** hay không: một bài toán mở hơn hai nghìn năm.')
    D.sub('Mở rộng 2: Số dư, số kì dị và chuỗi hòa đồng')
    D.p('Với mảng s đã sàng, nhiều câu hỏi trở thành một vòng lặp: có 246 số dư ≤ 1000 và 3 số hoàn hảo ≤ 1000; số dư lẻ nhỏ nhất là **945**. '
        'Số **kì dị** là số dư nhưng không viết được thành tổng của một vài ước thực sự khác nhau của nó; nhỏ nhất là **70** (ước 1, 2, 5, 7, 10, 14, 35 có tổng 74 > 70, nhưng không tập con nào có tổng 70). '
        'Lặp n → s(n) có thể tạo chu trình dài hơn 2: chuỗi **hòa đồng** 12 496 → 14 288 → 15 472 → 14 536 → 14 264 → 12 496 (độ dài 5). Phát hiện chu trình như Bài 11.')
    D.sub('Mở rộng 3: Số có nhiều ước nhất')
    D.p('Thay s[m] += d bằng cnt[m]++ để có số ước của mọi số ≤ N. Số ≤ 10^{6} có nhiều ước nhất là **720 720** = 2^{4} · 3^{2} · 5 · 7 · 11 · 13, với 240 ước. '
        'Những số "kỉ lục" như vậy (số **siêu hợp**) luôn có số mũ giảm dần theo các số nguyên tố nhỏ nhất: dựa vào đó có thể tìm bằng quay lui tới 10^{18} mà không cần sàng.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Đọc s[b] khi b > N:** s(a) có thể lớn gấp vài lần a (s(720 720) > 2 · 720 720); truy cập ngoài mảng.',
        '- **In mỗi cặp hai lần** hoặc in số hoàn hảo như một cặp: dùng điều kiện a < b.',
        '- **Cộng cả chính số đó** khi sàng (bắt đầu từ d chứ không phải 2d), ra σ thay vì s.',
        '- **Thử chia đếm trùng** ước √a khi a là số chính phương.'])
    D.kbox('GHI NHỚ', [
        '- σ(n) = Π (p^{a+1} − 1)/(p − 1); s(n) = σ(n) − n.',
        '- Sàng tổng ước: mỗi d cộng vào các bội 2d, 3d, ...: O(N log N), mọi phép cộng đều có ích.',
        '- Số hoàn hảo chẵn = 2^{p−1}(2^{p} − 1) với 2^{p} − 1 nguyên tố.'])
    D.luyentap([('18.1', 'THÂN THIẾT', 'Liệt kê các cặp số thân thiết a < b ≤ N, N ≤ 10^{7}: bài THANTHIET.'),
                ('18.2', 'HOÀN HẢO', 'Phân loại các số trong [L, R] thành hoàn hảo, dư, thiếu (R ≤ 10^{7}); liệt kê số hoàn hảo ≤ 10^{18}: Mở rộng 1.'),
                ('18.3', 'NHIỀU ƯỚC NHẤT', 'Tìm số ≤ N có nhiều ước nhất (N ≤ 10^{7} bằng sàng, N ≤ 10^{18} bằng quay lui): Mở rộng 3.')])
    D.tukiemtra([('s(28) bằng bao nhiêu?', '28 = 1 + 2 + 4 + 7 + 14: số hoàn hảo'), ('σ(12) bằng bao nhiêu?', '28 (= 7 · 4)'),
                 ('Vì sao mọi số nguyên tố là số thiếu?', 's(p) = 1 < p'), ('Với p = 11, 2^{11} − 1 = 2047 = 23 · 89: có cho số hoàn hảo không?', 'Không, 2047 không nguyên tố')])
