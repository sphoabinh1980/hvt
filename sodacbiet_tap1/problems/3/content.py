def build(D, P):
    S = lambda f: str(sum(P.scores[f]['pts']))
    D.objectives([
        'Hiểu vì sao n! có rất nhiều chữ số 0 ở cuối, và đếm chúng bằng **công thức Legendre**.',
        'Thấy rõ vì sao "chỉ giữ chữ số cuối" là sai khi đi tìm chữ số khác 0 cuối cùng.',
        'Tính chữ số khác 0 cuối cùng của n! với n tới 10^{18} bằng một công thức đệ quy chỉ có khoảng 26 tầng, và chứng minh được nó.',
        'Ôn lại tính tuần hoàn của chữ số tận cùng: 2^{k} mod 10 lặp 2, 4, 8, 6.'])
    D.kbox('KHỞI ĐỘNG', [
        '10! = 3 628 800 có 2 chữ số 0 ở cuối, 25! = 15 511 210 043 330 985 984 000 000 có 6 chữ số 0 ở cuối. 2026! có bao nhiêu chữ số 0 ở cuối? Và **ngay trước** dãy số 0 ấy là chữ số nào?',
        'Câu hỏi thứ nhất có đáp án gọn trong một dòng. Câu hỏi thứ hai khó hơn nhiều: nó đã làm mất điểm của rất nhiều học sinh, vì cách làm "hiển nhiên" lại sai.'])

    D.h('1. Chữ số 0 tận cùng')
    D.p('Mỗi chữ số 0 ở cuối n! là một thừa số 10 = 2 · 5. Vậy số chữ số 0 tận cùng bằng số cặp (2, 5) ghép được từ các thừa số nguyên tố của n!, tức min(số thừa số 2, số thừa số 5).')
    D.fig(P.fig('pairs'), 'Thừa số 2 và thừa số 5 của 1, 2, ..., 10.', 15.2)
    D.p('Thừa số 2 luôn nhiều hơn thừa số 5 (cứ hai số có một số chẵn, năm số mới có một bội của 5), nên **số chữ số 0 tận cùng của n! bằng số thừa số 5 của n!**.')
    D.kbox('ĐỊNH LÍ (LEGENDRE)', ['Số mũ của số nguyên tố p trong phân tích n! là', '$eq **v_{p}(n!) = ⌊n/p⌋ + ⌊n/p^{2}⌋ + ⌊n/p^{3}⌋ + ...**',
                                   'Với p = 5, đây là số chữ số 0 tận cùng của n!. Tổng dừng khi p^{i} > n, nên chỉ có khoảng log_{5} n số hạng (26 số hạng với n = 10^{18}).'])
    D.kbox('VÌ SAO ĐÚNG?', ['Một số m ≤ n chứa đúng v_{p}(m) thừa số p. Đếm theo "tầng": ⌊n/p⌋ số chia hết cho p góp mỗi số một thừa số; ⌊n/p^{2}⌋ số chia hết cho p^{2} góp **thêm** một thừa số nữa; '
                            'và cứ thế. Số m được đếm đúng v_{p}(m) lần, ở các tầng p, p^{2}, ..., p^{v_{p}(m)}.'])
    D.fig(P.fig('legendre'), 'Đếm thừa số 5 của 60! theo tầng.', 15)
    D.kbox('VÍ DỤ', ['2026! có ⌊2026/5⌋ + ⌊2026/25⌋ + ⌊2026/125⌋ + ⌊2026/625⌋ = 405 + 81 + 16 + 3 = **505** chữ số 0 tận cùng.'])

    D.h('2. Bài toán GIAITHUA')
    D.problem_box('GIAITHUA', 'Cho Q số n. Với mỗi n, hãy cho biết n! có bao nhiêu chữ số 0 tận cùng và chữ số khác 0 cuối cùng của n! là chữ số nào.',
                  'Dòng đầu chứa Q (Q ≤ 10^{5}); mỗi dòng tiếp theo chứa một số n (0 ≤ n ≤ 10^{18}).',
                  'Q dòng, mỗi dòng hai số: số chữ số 0 tận cùng và chữ số khác 0 cuối cùng của n!.')
    D.examples('GIAITHUA', [('3\n10\n15\n2026', '2 8\n3 8\n505 2', '10! = 3628800. 15! = 1307674368000. Kết quả của 2026! được tính tay ở mục 5.')])

    D.h('3. Một cách làm "trông như đúng"')
    D.p('Ý tưởng tự nhiên nhất: nhân dần 1 · 2 · 3 · ... · n; mỗi khi tích tận cùng bằng 0 thì bỏ số 0 ấy đi (và đếm); để khỏi tràn số thì chỉ **giữ lại chữ số cuối**.')
    D.code('GIAITHUA.CPP (sai): chỉ giữ chữ số cuối', P.src('trap.cpp'))
    D.p('Chương trình cho đúng 10! nhưng sai ngay ở 15!: in "3 3" thay vì "3 8". Trên bộ test chương trình được **' + S('trap.cpp') + ' điểm**.')
    D.fig(P.fig('trap'), 'Vì sao chỉ giữ chữ số cuối là sai.', 15.2)
    D.kbox('BẪY THƯỜNG GẶP', ['Phép nhân với một bội của 5 sinh ra số 0 mới; bỏ số 0 ấy đi tức là "kéo" chữ số hàng chục xuống hàng đơn vị. Chữ số hàng chục là chữ số ta đã vứt đi, nên kết quả sai. '
                              'Giữ nhiều chữ số hơn (chẳng hạn 5 chữ số cuối) chỉ đẩy lùi chỗ sai chứ không chữa được: khi n chứa nhiều thừa số 5, số chữ số 0 sinh ra liên tiếp có thể vượt số chữ số ta giữ.'])

    D.h('4. Ý tưởng ngây thơ (đúng): Tách riêng thừa số 2 và 5')
    D.p('Chữ số khác 0 cuối cùng của n! là (n! / 10^{z}) mod 10 với z là số chữ số 0 tận cùng. Viết n! = 2^{c2} · 5^{c5} · rest, trong đó rest không chia hết cho 2 và 5. '
        'Mọi số 0 đến từ các cặp (2, 5), nên n! / 10^{c5} = 2^{c2 − c5} · rest. Hai thừa số này tính được theo mô-đun 10 mà không mất thông tin, vì việc chia cho 10 đã được làm "trên giấy" bằng cách đếm.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách tách thừa số 2 và 5.', 13)
    D.code('GIAITHUA.CPP (ngây thơ): tách thừa số 2, 5 của từng số', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi số i tốn vài phép chia: O(n) mỗi truy vấn (cộng thêm vòng nhân 2 lặp c2 − c5 lần, cũng O(n)). Đo thực tế: n = 10^{7} mất **0,08 giây**, n = 10^{8} mất **0,78 giây**. '
                               'Với n = 10^{18} cần khoảng 7,8 · 10^{9} giây, tức **hơn 240 năm**, chưa kể Q = 10^{5} truy vấn. Chương trình được **' + S('naive.cpp') + ' điểm**.'])
    D.kbox('BẾ TẮC', ['Số chữ số 0 thì đã có công thức Legendre O(log n). Nhưng chữ số khác 0 cuối cùng vẫn đòi đi qua từng số 1, 2, ..., n. '
                      'Có cách nào "nhảy" qua cả khối số như Legendre đã làm không? Gợi ý: Legendre tách riêng các bội của 5; bội của 5 là 5 · 1, 5 · 2, ..., 5 · k, và 1 · 2 · ... · k lại là một giai thừa.'])

    D.h('5. Phá bế tắc: Đệ quy theo n / 5')
    D.step(1, 'Tách n! thành hai phần')
    D.p('Đặt k = ⌊n / 5⌋ và r = n mod 5. Các bội của 5 trong 1..n là 5 · 1, 5 · 2, ..., 5 · k, tích của chúng là 5^{k} · k!. Các số còn lại (không chia hết cho 5) có tích P. Vậy n! = 5^{k} · k! · P.')
    D.step(2, 'Công thức')
    D.kbox('ĐỊNH LÍ (CHỮ SỐ KHÁC 0 CUỐI CÙNG CỦA n!)', ['Gọi D(n) là chữ số khác 0 cuối cùng của n!. Với n ≥ 5, k = ⌊n/5⌋, r = n mod 5:',
                                                       '$eq **D(n) = (2^{k} mod 10) · D(k) · D(r)  mod 10**',
                                                       'trong đó D(0..4) = 1, 1, 2, 6, 4 và 2^{k} mod 10 (k ≥ 1) lặp lại 2, 4, 8, 6 theo k mod 4.'])
    D.kbox('VÌ SAO ĐÚNG?', [
        'Một chữ số được xác định hoàn toàn nếu biết nó **chẵn hay lẻ** và **số dư khi chia cho 5** (định lí Trung Hoa cho 10 = 2 · 5). Ta chứng minh hai vế giống nhau ở cả hai điều đó.',
        '- **Tính chẵn lẻ:** với n ≥ 2, n! có nhiều thừa số 2 hơn thừa số 5, nên n! / 10^{z} còn ít nhất một thừa số 2: D(n) chẵn. Vế phải cũng chẵn vì k ≥ 1 nên 2^{k} mod 10 chẵn.',
        '- **Số dư cho 5:** n! / 10^{z} = (5^{k} · k! · P) / 10^{k + v_{5}(k!)} = (k! / 10^{v_{5}(k!)}) · P / 2^{k}. Mỗi khối năm số liên tiếp không chia hết cho 5 có tích ≡ 1 · 2 · 3 · 4 = 24 ≡ −1 (mod 5), '
        'nên P ≡ (−1)^{k} · r! (mod 5). Chia cho 2^{k} theo mô-đun 5 là nhân với 3^{k} (vì 2 · 3 ≡ 1), nên P / 2^{k} ≡ (−3)^{k} · r! ≡ 2^{k} · r! (mod 5). '
        'Do đó D(n) ≡ D(k) · 2^{k} · r! ≡ 2^{k} · D(k) · D(r) (mod 5), vì D(r) ≡ r! (mod 5) với r ≤ 4.'])
    D.step(3, 'Chạy tay với n = 2026')
    D.fig(P.fig('chain'), 'Mỗi tầng chia n cho 5; năm tầng là đủ cho 2026.', 15.2)
    D.table(['n', 'k = ⌊n/5⌋', 'r', '2^{k} mod 10', 'D(k)', 'D(r)', 'D(n)'], [
        ['3', '', '', '', '', '', '6 (3! = 6)'], ['16', '3', '1', '8', '6', '1', '8 · 6 · 1 = 48 → **8**'], ['81', '16', '1', '6', '8', '1', '6 · 8 · 1 = 48 → **8**'],
        ['405', '81', '0', '2', '8', '1', '2 · 8 · 1 = 16 → **6**'], ['2026', '405', '1', '2', '6', '1', '2 · 6 · 1 = 12 → **2**']],
        widths=[0.9, 1.1, 0.5, 1.3, 0.8, 0.8, 2.6], sz=20, hl=[4])
    D.p('Đối chiếu bằng phép tính chính xác: 2026! (5822 chữ số) có 505 chữ số 0 tận cùng và chữ số ngay trước chúng là 2.')
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của hàm đệ quy D(n).', 11)
    D.code('GIAITHUA.CPP: Legendre + đệ quy', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi tầng đệ quy chia n cho 5: với n = 10^{18} chỉ có 26 tầng; Legendre cũng 26 phép chia. 10^{5} truy vấn chạy trong khoảng **0,16 giây**. '
                               'Chương trình được đối chiếu với giai thừa chính xác (Python) cho mọi n ≤ 3000.'])

    D.h('6. Mở rộng')
    D.sub('Mở rộng 1: Chữ số tận cùng có chu kì')
    D.p('Dãy chữ số tận cùng của a, a^{2}, a^{3}, ... luôn tuần hoàn với chu kì chia hết 4 (vì chỉ có 10 chữ số và mỗi chữ số chỉ phụ thuộc chữ số trước): 2 → 2, 4, 8, 6; 3 → 3, 9, 7, 1; 7 → 7, 9, 3, 1; '
        '4 → 4, 6; 9 → 9, 1; 0, 1, 5, 6 không đổi. Bảng 2^{k} mod 10 trong bài chính là một trường hợp.')
    D.sub('Mở rộng 2: Số mũ của p trong C(n, k) và các bài "chia hết cho p^{e}"')
    D.p('Từ Legendre: v_{p}(C(n, k)) = v_{p}(n!) − v_{p}(k!) − v_{p}((n − k)!). Định lí Kummer còn cho cách đếm đẹp hơn: con số này bằng **số lần nhớ** khi cộng k với n − k trong cơ số p. '
        'Ví dụ: số chữ số 0 tận cùng của C(n, k) là min(v_{2}, v_{5}) của nó.')
    D.sub('Mở rộng 3: Số chữ số 0 tận cùng trong cơ số b')
    D.p('Trong cơ số b = p_{1}^{e1} · ... · p_{t}^{et}, n! có min_{i} ⌊v_{pi}(n!) / e_{i}⌋ chữ số 0 tận cùng. Ví dụ trong cơ số 12 = 2^{2} · 3: lấy min(⌊v_{2}(n!)/2⌋, v_{3}(n!)).')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Chỉ giữ một vài chữ số cuối** rồi bỏ số 0: sai, như mục 3.',
        '- **Quên trường hợp n < 5** (0! = 1! = 1) hoặc dùng bảng 2^{k} cho k = 0 (2^{0} = 1, không phải 6).',
        '- **Lặp 5^{i} ≤ n bằng phép nhân:** 5^{i} có thể tràn khi n gần 10^{18}; hãy chia n cho 5 liên tục như trong chương trình.',
        '- **Đếm thừa số 2:** số chữ số 0 là v_{5}, không phải v_{2}, càng không phải ⌊n/10⌋.'])
    D.kbox('GHI NHỚ', [
        '- Số chữ số 0 tận cùng của n! = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ... (Legendre với p = 5).',
        '- Chữ số khác 0 cuối cùng **không** tính được bằng cách giữ vài chữ số cuối.',
        '- D(n) = 2^{k} · D(k) · D(n mod 5) mod 10 với k = ⌊n/5⌋: O(log n). Chứng minh bằng "chẵn lẻ + đồng dư mod 5".',
        '- Chữ số tận cùng của lũy thừa tuần hoàn với chu kì chia hết 4.'])
    D.luyentap([('3.1', 'SỐ KHÔNG', 'Tìm n nhỏ nhất sao cho n! có ít nhất k chữ số 0 tận cùng (k ≤ 10^{18}): tìm kiếm nhị phân trên Legendre.'),
                ('3.2', 'CHỮ SỐ KHÁC 0', 'Chữ số khác 0 cuối cùng của n! với n cho dưới dạng xâu 10^{5} chữ số: cùng công thức, chia số lớn cho 5.'),
                ('3.3', 'CƠ SỐ B', 'Số chữ số 0 tận cùng của n! khi viết trong cơ số b (b ≤ 10^{12}): phân tích b, Legendre cho từng ước nguyên tố.')])
    D.tukiemtra([('100! có bao nhiêu chữ số 0 tận cùng?', '20 + 4 = 24'), ('Có n nào để n! có đúng 5 chữ số 0 tận cùng không?', 'không: 24! có 4, 25! có 6'),
                 ('Chữ số khác 0 cuối cùng của 30! là gì? (dùng công thức)', 'k = 6, r = 0: 4 · D(6) · 1 = 4 · 2 = 8'),
                 ('Chữ số tận cùng của 7^{2026}?', '2026 mod 4 = 2, giống 7^{2} = 49: chữ số 9')])
