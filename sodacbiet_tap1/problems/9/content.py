def build(D, P):
    D.objectives([
        'Kiểm tra một số có đối xứng không, bằng số đảo ngược hoặc bằng xâu.',
        'Hiểu rằng một số đối xứng được **quyết định bởi nửa đầu** của nó, từ đó đếm được: có 9 · 10^{⌈L/2⌉−1} số đối xứng L chữ số.',
        'Đếm số đối xứng trên đoạn [L, R] tới 10^{18} trong O(18), và tìm số đối xứng thứ k.',
        'Chứng minh mọi số đối xứng có số chữ số chẵn đều chia hết cho 11, và làm quen với bài toán "đảo và cộng".'])
    D.kbox('KHỞI ĐỘNG', [
        'Ngày 02/02/2020 viết thành 02022020: đọc xuôi hay đọc ngược đều như nhau. Những con số như 121, 2002, 12321 gọi là **số đối xứng** (palindrome).',
        'Từ 1 tới 10^{18} có bao nhiêu số đối xứng? Trông thì "rất nhiều", nhưng thực ra chỉ có 1 999 999 998: ít hơn một phần năm trăm triệu số các số. '
        'Đếm chúng không cần duyệt: một số đối xứng chỉ có "một nửa thông tin".'])

    D.h('1. Số đối xứng và nửa đầu')
    D.kbox('ĐỊNH NGHĨA', ['Số nguyên dương n là **số đối xứng** nếu đọc các chữ số của n từ phải sang trái được chính n, tức rev(n) = n. Các số một chữ số đều đối xứng.'])
    D.p('Để kiểm tra, so sánh n với số đảo ngược (Bài 1), hoặc đổi n thành xâu rồi so sánh hai đầu. Cả hai đều O(số chữ số).')
    D.kbox('ĐỊNH LÍ (NỬA ĐẦU QUYẾT ĐỊNH TẤT CẢ)', [
        'Một số đối xứng L chữ số được xác định duy nhất bởi h = ⌈L/2⌉ chữ số đầu của nó (gọi là **nửa đầu**). Ngược lại, mọi số h chữ số (chữ số đầu khác 0) đều là nửa đầu của đúng một số đối xứng L chữ số. Do đó:',
        '$eq **có 9 · 10^{⌈L/2⌉ − 1} số đối xứng có L chữ số**.'])
    D.fig(P.fig('mirror'), 'Sinh số đối xứng từ nửa đầu 202.', 14.5)
    D.table(['L', '1', '2', '3', '4', '5', '6', '...', '17', '18'], [['Số lượng', '9', '9', '90', '90', '900', '900', '...', '9 · 10⁸', '9 · 10⁸']],
            widths=[1.3, 0.6, 0.6, 0.6, 0.6, 0.7, 0.7, 0.5, 1.0, 1.0], sz=19)
    D.p('Cộng 18 cột: 2 · (9 + 90 + ... + 9 · 10^{8}) = 2 · (10^{9} − 1) = 1 999 999 998 số đối xứng dưới 10^{18}.')
    D.kbox('ĐỊNH LÍ (SỐ ĐỐI XỨNG CÓ SỐ CHỮ SỐ CHẴN)', ['Mọi số đối xứng có số chữ số **chẵn** đều chia hết cho 11. Hệ quả: số nguyên tố đối xứng duy nhất có số chữ số chẵn là 11.'])
    D.kbox('VÌ SAO ĐÚNG?', ['Theo dấu hiệu chia hết cho 11 (Bài 5), n ≡ d_{0} − d_{1} + d_{2} − ... (mod 11). Với L chẵn, hai chữ số đối xứng nhau d_{i} = d_{L−1−i} nằm ở hai vị trí khác tính chẵn lẻ '
                            '(i + (L − 1 − i) = L − 1 lẻ), nên chúng mang dấu ngược nhau và triệt tiêu. Tổng đan dấu bằng 0. Ví dụ 2002: 2 − 0 + 0 − 2 = 0, và 2002 = 11 · 182.'])

    D.h('2. Bài toán DEMDX')
    D.problem_box('DEMDX', 'Cho Q đoạn [L, R]. Với mỗi đoạn, hãy đếm số đối xứng thuộc đoạn đó.',
                  'Dòng đầu chứa Q (Q ≤ 10^{5}). Mỗi dòng tiếp theo chứa L, R (1 ≤ L ≤ R ≤ 10^{18}).', 'Q dòng, mỗi dòng một số nguyên.')
    D.examples('DEMDX', [('3\n1 100\n100 2026\n1 1000000000000000000', '18\n101\n1999999998', '1..9 và 11, 22, ..., 99. Đoạn thứ hai được tính tay ở mục 4. Đoạn thứ ba: mọi số đối xứng có ≤ 18 chữ số.')])

    D.h('3. Ý tưởng ngây thơ: Kiểm tra từng số')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách kiểm tra từng số.', 10.5)
    D.code('DEMDX.CPP (ngây thơ): kiểm tra từng số', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['O((R − L) · số chữ số). Đo thực tế: đoạn [1, 10^{8}] mất **0,93 giây**, [1, 10^{9}] mất **11 giây** (và chỉ tìm được 109 998 số đối xứng). Đoạn dài 10^{18} cần hàng trăm năm.'])
    D.kbox('BẾ TẮC', ['Gần như mọi số được kiểm tra đều **không** đối xứng: trong 10^{9} số chỉ có khoảng 10^{5} số đối xứng. Ta đang tốn thời gian cho những số chắc chắn bị loại. '
                      'Theo định lí ở mục 1, số đối xứng tương ứng một-một với nửa đầu: đếm số đối xứng chính là **đếm nửa đầu**.'])

    D.h('4. Phá bế tắc: Đếm nửa đầu')
    D.step(1, 'Đếm trên [1, n] rồi lấy hiệu')
    D.p('Gọi dem(n) là số số đối xứng trong [1, n]. Đáp số là dem(R) − dem(L − 1).')
    D.step(2, 'Các số đối xứng ngắn hơn n')
    D.p('Nếu n có len chữ số thì mọi số đối xứng có ít hơn len chữ số đều < n: cộng 9 · 10^{⌈L/2⌉−1} với L = 1, ..., len − 1.')
    D.step(3, 'Các số đối xứng có đúng len chữ số')
    D.p('Đặt h = ⌈len/2⌉ và half = h chữ số đầu của n. Một số đối xứng len chữ số với nửa đầu x:')
    D.bullets(['nếu x < half thì nó nhỏ hơn n (khác nhau ngay trong h chữ số đầu): có half − 10^{h−1} số như vậy;',
               'nếu x > half thì nó lớn hơn n;', 'nếu x = half thì phải so sánh trực tiếp **gương(half)** với n.'])
    D.step(4, 'Chạy tay với dem(2026) và dem(99)')
    D.fig(P.fig('count'), 'Đếm các số đối xứng không vượt quá 2026.', 15.2)
    D.p('dem(99): len = 2, các số một chữ số: 9; half = 9, có 9 − 1 = 8 nửa đầu nhỏ hơn (11, ..., 88), gương(9) = 99 ≤ 99 nên +1: tổng 18. Vậy đoạn [100, 2026] có 119 − 18 = **101** số đối xứng.')
    D.step(5, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của hàm dem(n).', 13)
    D.code('DEMDX.CPP: đếm theo độ dài và nửa đầu', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi lần gọi dem tốn khoảng 20 phép tính: O(số chữ số). 10^{5} đoạn chạy trong khoảng **0,26 giây** (chủ yếu là đọc ghi). '
                               'Hàm guong với n tới 10^{18} cho số tới 10^{18} + 1: vừa long long.'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Số đối xứng thứ k')
    D.p('Cùng tư tưởng: nhảy qua các nhóm độ dài (như Bài 4), trong nhóm L thì nửa đầu thứ k là 10^{h−1} + k − 1, lật lại là xong. Ví dụ số đối xứng thứ 2026 là 1 027 201, thứ 10^{9} là 90 000 000 100 000 009.')
    D.code('Số đối xứng thứ k', P.src('ex_kth.cpp'))
    D.sub('Mở rộng 2: Số đối xứng kế tiếp')
    D.p('Số đối xứng nhỏ nhất lớn hơn n: lấy nửa đầu của n và lật; nếu kết quả ≤ n thì tăng nửa đầu thêm 1 rồi lật. Trường hợp đặc biệt n = 99...9: đáp số là 10...01 (dài hơn một chữ số). '
        'Với n là xâu dài 10^{5} chữ số, phép "tăng nửa đầu thêm 1" làm trên xâu, có xử lí nhớ.')
    D.sub('Mở rộng 3: Đảo và cộng, số đối xứng ở nhiều cơ số')
    D.p('Lấy một số, cộng với số đảo ngược của nó, lặp lại: 89 cần 24 bước để thành số đối xứng 8 813 200 023 188. Riêng 196 thì đến nay **chưa ai biết** có bao giờ thành số đối xứng không '
        '(những số như vậy gọi là số Lychrel). Một biến thể khác: số đối xứng ở cả cơ số 10 lẫn cơ số 2, như 585 = (1001001001)_{2}; dưới 1000 có 1, 3, 5, 7, 9, 33, 99, 313, 585, 717. '
        'Cách tìm nhanh: **sinh** số đối xứng cơ số 10 (ít hơn nhiều) rồi kiểm tra cơ số 2.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Quên chữ số giữa** khi lật nửa đầu độ dài lẻ: 202 → 20202, không phải 202202.',
        '- **dem(0)** phải bằng 0 khi L = 1.',
        '- **Tràn khi lật nửa đầu của số 19 chữ số:** n ≤ 10^{18} an toàn, nhưng nếu đề cho n tới 9 · 10^{18} thì nên làm với xâu.',
        '- **Coi số có chữ số 0 ở cuối là đối xứng:** 120 đảo thành 21, không đối xứng (số không có chữ số 0 ở đầu).'])
    D.kbox('GHI NHỚ', [
        '- Số đối xứng được quyết định bởi nửa đầu: có 9 · 10^{⌈L/2⌉−1} số đối xứng L chữ số.',
        '- Đếm trên [1, n]: các độ dài nhỏ hơn + (half − 10^{h−1}) + [gương(half) ≤ n].',
        '- Số đối xứng có số chữ số chẵn chia hết cho 11.',
        '- Muốn tìm số đối xứng có thêm tính chất (nguyên tố, đối xứng cơ số 2...): **sinh** chúng từ nửa đầu rồi kiểm tra.'])
    D.luyentap([('9.1', 'ĐỐI XỨNG THỨ K', 'Số đối xứng thứ k và vị trí của một số đối xứng cho trước trong dãy: Mở rộng 1.'),
                ('9.2', 'ĐỐI XỨNG KẾ TIẾP', 'Số đối xứng nhỏ nhất lớn hơn n, n là xâu tới 10^{5} chữ số: Mở rộng 2.'),
                ('9.3', 'NGUYÊN TỐ ĐỐI XỨNG', 'Đếm số nguyên tố đối xứng trong [L, R] với R ≤ 10^{9}: sinh từ nửa đầu, chỉ xét độ dài lẻ, kiểm tra nguyên tố.')])
    D.tukiemtra([('Có bao nhiêu số đối xứng có 7 chữ số?', '9 · 10^{3} = 9000'), ('Số đối xứng thứ 100 là số nào?', '919 (9 + 9 = 18 số trước, nửa đầu thứ 82 là 91)'),
                 ('Vì sao 123 321 chia hết cho 11?', 'số đối xứng 6 chữ số; tổng đan dấu 1 − 2 + 3 − 3 + 2 − 1 = 0'), ('dem(1000) bằng bao nhiêu?', '9 + 9 + 90 = 108')])
