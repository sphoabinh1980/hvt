def build(D, P):
    D.objectives([
        'Biết đếm có bao nhiêu số có đúng L chữ số (9 · 10^{L−1}) và chúng chiếm bao nhiêu chữ số khi viết liền.',
        'Tìm chữ số thứ k của dãy 123456789101112... với k tới 10^{18} bằng kĩ thuật **nhóm theo số chữ số**.',
        'Tính tổng số chữ số khi viết 1..n, và dùng nó (kết hợp tìm kiếm nhị phân) cho các dãy viết liền phức tạp hơn.',
        'Tránh lỗi "lệch một" khi chuyển giữa đánh số từ 1 và từ 0.'])
    D.kbox('KHỞI ĐỘNG', [
        'Bạn Minh viết liền các số tự nhiên lên một băng giấy rất dài: 1234567891011121314... Bạn Lan đứng ở ô thứ 2026 và hỏi: "Ở đây là chữ số mấy?"',
        'Minh có thể đếm lại từ đầu. Nhưng nếu băng giấy dài 10^{18} ô (gấp hàng triệu lần khoảng cách từ Trái Đất tới Mặt Trời, nếu mỗi ô dài 1 mm) thì không ai đếm nổi. '
        'Bài học này cho em cách "nhảy cóc": nhảy qua cả nghìn, cả triệu, cả tỉ số trong một bước.'])

    D.h('1. Có bao nhiêu số có L chữ số?')
    D.kbox('ĐỊNH LÍ (NHÓM CÁC SỐ CÓ L CHỮ SỐ)', [
        'Các số có đúng L chữ số là các số từ 10^{L−1} tới 10^{L} − 1. Có **9 · 10^{L−1}** số như vậy, và viết liền chúng cần **9 · 10^{L−1} · L** chữ số.'])
    D.table(['L', 'Các số', 'Số lượng', 'Số chữ số', 'Tổng tích lũy'], [
        ['1', '1..9', '9', '9', '9'], ['2', '10..99', '90', '180', '189'], ['3', '100..999', '900', '2 700', '2 889'], ['4', '1000..9999', '9 000', '36 000', '38 889'],
        ['...', '', '', '', ''], ['17', '10^{16}..10^{17} − 1', '9 · 10^{16}', '1,53 · 10^{18}', '1 688 888 888 888 888 889']],
        widths=[0.6, 2.2, 1.4, 1.6, 2.6], sz=20)
    D.p('Cột cuối có một hình mẫu đẹp: tổng các chữ số dùng để viết mọi số có không quá L chữ số là (L − 1) chữ số 8 kẹp giữa chữ số 1 và chữ số 9 (189, 2889, 38889...), '
        'cụ thể bằng ((9L − 1) · 10^{L} + 1) / 9. Dòng cuối cho thấy 17 nhóm đầu đã vượt 10^{18} chữ số: chữ số thứ k ≤ 10^{18} luôn nằm trong một số có không quá 17 chữ số.')
    D.fig(P.fig('groups'), 'Băng giấy chia thành các nhóm theo số chữ số; nhóm sau dài gấp hơn 10 lần nhóm trước.', 15.2)

    D.h('2. Bài toán CHUSOK')
    D.problem_box('CHUSOK', 'Dãy vô hạn S = 123456789101112131415... được tạo bằng cách viết liền các số nguyên dương. Cho Q số k, hãy cho biết chữ số thứ k của S (đánh số từ 1).',
                  'Dòng đầu chứa Q (Q ≤ 10^{5}); mỗi dòng tiếp theo chứa một số k (1 ≤ k ≤ 10^{18}).', 'Q dòng, mỗi dòng một chữ số.')
    D.examples('CHUSOK', [('3\n11\n2026\n1000000000000000000', '0\n7\n3',
                           'Chữ số thứ 10, 11 là "1", "0" của số 10. Chữ số thứ 2026 là chữ số đầu của 712. Chữ số thứ 10^{18} nằm trong số 59 477 124 183 006 535.')])

    D.h('3. Ý tưởng ngây thơ: Đi qua từng số')
    D.p('Đi lần lượt qua x = 1, 2, 3, ...: nếu k không vượt quá số chữ số của x thì chữ số cần tìm nằm trong x; ngược lại trừ k đi số chữ số của x và sang số tiếp theo.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách đi qua từng số.', 11)
    D.code('CHUSOK.CPP (ngây thơ): đi qua từng số', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Số vòng lặp xấp xỉ số các số được đi qua, khoảng k / (độ dài trung bình). Đo thực tế: k = 10^{8} mất **0,22 giây**, k = 10^{9} mất **1,85 giây**. '
                               'Với k = 10^{18} cần khoảng 1,85 · 10^{9} giây, tức **gần 60 năm**, cho mỗi truy vấn.'])
    D.kbox('BẾ TẮC', ['Chương trình đi qua từng số trong khi các số có cùng số chữ số chiếm những đoạn băng giấy **dài bằng nhau** (L ô mỗi số). '
                      'Đã biết trước độ dài của cả nhóm, sao không nhảy qua cả nhóm trong một bước? Và trong nhóm, sao không dùng phép chia thay cho việc đếm từng số?'])

    D.h('4. Phá bế tắc: Nhóm theo số chữ số')
    D.step(1, 'Nhảy qua cả nhóm')
    D.p('Bắt đầu với nhóm L = 1 (9 số, 9 chữ số). Nếu k lớn hơn số chữ số của cả nhóm (L · cnt với cnt = 9 · 10^{L−1}) thì chữ số cần tìm nằm ở các nhóm sau: trừ k đi L · cnt và sang nhóm L + 1. '
        'Tối đa 17 lần nhảy với k ≤ 10^{18}.')
    D.step(2, 'Tìm số và vị trí trong nhóm')
    D.p('Bây giờ k là vị trí (đánh số từ 1) trong nhóm L, bắt đầu từ số start = 10^{L−1}. Mỗi số chiếm đúng L ô, nên đổi sang đánh số từ 0 cho dễ chia: k − 1 = L · q + r. '
        'Số cần tìm là **start + q** và chữ số cần tìm là chữ số thứ **r** (đánh số từ 0, tính từ trái) của nó.')
    D.kbox('VÌ SAO ĐÚNG?', ['Trong nhóm L, số start + j chiếm các ô L · j + 1, ..., L · j + L (đánh số từ 1), tức các ô L · j, ..., L · j + L − 1 nếu đánh số từ 0. '
                            'Ô thứ k − 1 (đánh số từ 0) thuộc số có j = ⌊(k − 1)/L⌋ và là ô thứ (k − 1) mod L trong số đó.'])
    D.step(3, 'Chạy tay với k = 2026')
    D.table(['Nhóm L', 'Số chữ số của nhóm', 'k > L · cnt ?', 'k sau bước này'], [
        ['1', '9', 'có', '2026 − 9 = 2017'], ['2', '180', 'có', '2017 − 180 = 1837'], ['3', '2 700', '**không**: dừng', '1837']],
        widths=[1.1, 2.1, 1.8, 2.6], sz=20, hl=[2])
    D.p('Trong nhóm 3: k − 1 = 1836 = 3 · 612 + 0. Số cần tìm là 100 + 612 = **712**, chữ số thứ 0 của nó là **7**.')
    D.fig(P.fig('inside'), 'Vị trí 1837 của nhóm ba chữ số rơi vào chữ số đầu của 712.', 15.2)
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của cách nhóm theo số chữ số.', 13)
    D.code('CHUSOK.CPP: nhóm theo số chữ số', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Tối đa 17 vòng lặp và một phép đổi số thành xâu cho mỗi truy vấn: O(log k). 10^{5} truy vấn chạy trong khoảng **0,14 giây**, và gần như toàn bộ thời gian là đọc ghi.'])
    D.kbox('LƯU Ý: TRÀN SỐ', ['L · cnt với L = 18 là 18 · 9 · 10^{17} = 1,62 · 10^{19}: tràn long long. Chương trình an toàn vì với k ≤ 10^{18} vòng lặp luôn dừng ở L ≤ 17 '
                             '(17 nhóm đầu đã chứa 1,69 · 10^{18} chữ số), và L · cnt = 1,53 · 10^{18} vẫn vừa long long. Nếu đề cho k lớn hơn, phải so sánh bằng __int128 hoặc bằng phép chia.'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Tổng số chữ số khi viết 1..n')
    D.p('Bài toán ngược: viết liền 1..n cần bao nhiêu chữ số? Cộng theo nhóm, nhóm cuối bị cắt tại n.')
    D.code('Số chữ số khi viết liền 1, 2, ..., n', P.src('ex_len.cpp'))
    D.p('Ví dụ: n = 99 cho 189, n = 2026 cho 6997 (khớp với việc đếm trực tiếp). Đây chính là câu hỏi của người thợ in ở Bài 1.')
    D.sub('Mở rộng 2: Dãy 1 12 123 1234 12345 ...')
    D.p('Một biến thể nổi tiếng: viết liền các khối "1", "12", "123", ..., "123...i", ... thành 1121231234123451234561234567... Tìm chữ số thứ k (k ≤ 10^{18}). '
        'Khối thứ i dài đúng tongDoDai(i) chữ số. Tổng độ dài của i khối đầu tăng rất nhanh nên **tìm kiếm nhị phân** khối chứa chữ số thứ k, rồi trong khối đó (là dãy 1..i viết liền) dùng lại đúng thuật toán của CHUSOK. '
        'Ví dụ: chữ số thứ 56 của dãy này là 0 (chữ số cuối của số 10 trong khối thứ 10).')
    D.sub('Mở rộng 3: Dãy viết liền các số chính phương, các số nguyên tố...')
    D.p('Với dãy 149162536496481100121... (viết liền các bình phương), nhóm theo số chữ số của **giá trị** i^{2}: các i có i^{2} gồm L chữ số tạo thành một đoạn liên tiếp ⌈√(10^{L−1})⌉ ≤ i ≤ ⌊√(10^{L} − 1)⌋. '
        'Kĩ thuật y hệt, chỉ khác cách tính số lượng mỗi nhóm. Với số nguyên tố thì không có công thức đếm đơn giản, phải sàng.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Lệch một:** quên đổi k sang đánh số từ 0 trước khi chia, (k / L) thay cho (k − 1) / L.',
        '- **cnt và start bằng int:** 9 · 10^{9} đã tràn int.',
        '- **Tràn L · cnt** khi đề cho k lớn hơn 10^{18}.',
        '- **Quên rằng nhóm 1 có 9 số chứ không phải 10:** số 0 không được viết.'])
    D.kbox('GHI NHỚ', [
        '- Có 9 · 10^{L−1} số có L chữ số, chiếm 9 · 10^{L−1} · L chữ số khi viết liền.',
        '- Nhảy qua cả nhóm bằng phép trừ, trong nhóm dùng phép chia: k − 1 = L · q + r.',
        '- Khi độ dài các khối không đều nhưng tăng dần: tìm kiếm nhị phân trên tổng tích lũy.'])
    D.luyentap([('4.1', 'BĂNG GIẤY', 'Chữ số thứ k của dãy viết liền các số từ A trở đi (A ≤ 10^{18}): tính độ dài phần bị bỏ qua bằng tongDoDai(A − 1).'),
                ('4.2', 'KHỐI SỐ', 'Chữ số thứ k của dãy 1 12 123 1234 ... (k ≤ 10^{18}): Mở rộng 2.'),
                ('4.3', 'VIẾT LIỀN BÌNH PHƯƠNG', 'Chữ số thứ k của dãy viết liền 1, 4, 9, 16, 25, ...: Mở rộng 3, căn bậc hai nguyên.')])
    D.tukiemtra([('Chữ số thứ 190 và thứ 192 của S là gì?', '1 và 0 (ba chữ số của 100 nằm ở vị trí 190, 191, 192)'),
                 ('Chữ số thứ 1000 của S là gì?', '3 (thuộc số 370)'),
                 ('Viết liền các số từ 1 tới 2026 cần bao nhiêu chữ số?', '9 + 180 + 2700 + 4 · 1027 = 6997'),
                 ('Chữ số thứ 100 của dãy 149162536496481100121...?', '9')])
