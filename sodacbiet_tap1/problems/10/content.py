def build(D, P):
    D.objectives([
        'Hiểu các họ số được định nghĩa bằng "tổng lũy thừa các chữ số": số tự luân (Armstrong), Disarium, factorion, Dudeney.',
        'Chứng minh mỗi họ chỉ có **hữu hạn** số, bằng cách so sánh tổng lớn nhất có thể với số nhỏ nhất cùng độ dài.',
        'Nắm kĩ thuật **duyệt theo tập chữ số**: thay vì 10^{18} số, chỉ duyệt khoảng 1,3 · 10^{7} tập chữ số.',
        'Biết tự đặt chặn trên cho một cuộc tìm kiếm trước khi viết vòng lặp.'])
    D.kbox('KHỞI ĐỘNG', [
        '153 = 1^{3} + 5^{3} + 3^{3}. 9474 = 9^{4} + 4^{4} + 7^{4} + 4^{4}. Những số bằng tổng các chữ số của chính nó, mỗi chữ số lũy thừa số chữ số, gọi là **số tự luân** (narcissistic number, hay số Armstrong).',
        'Có bao nhiêu số như vậy? Liệu có số tự luân dài 100 chữ số? Và làm thế nào để tìm hết các số tự luân dưới 10^{18} khi không thể duyệt 10^{18} số?'])
    D.fig(P.fig('n153'), '153 là số tự luân ba chữ số.', 13)

    D.h('1. Số tự luân và chặn trên')
    D.kbox('ĐỊNH NGHĨA', ['Số n có L chữ số d_{1}, ..., d_{L} là **số tự luân** nếu n = d_{1}^{L} + d_{2}^{L} + ... + d_{L}^{L}. Các số 1..9 hiển nhiên là số tự luân (L = 1).'])
    D.kbox('ĐỊNH LÍ (CHỈ CÓ HỮU HẠN SỐ TỰ LUÂN)', ['Số tự luân có không quá 60 chữ số. Hệ quả: chỉ có hữu hạn số tự luân (người ta đã tìm ra đúng 88 số, số lớn nhất có 39 chữ số).'])
    D.kbox('VÌ SAO ĐÚNG?', ['Với L chữ số, tổng các lũy thừa không vượt quá L · 9^{L}, còn số nhỏ nhất có L chữ số là 10^{L−1}. Vế phải tăng gấp 10 mỗi khi L tăng 1, vế trái chỉ tăng khoảng 9 lần, '
                            'nên đến lúc nào đó L · 9^{L} < 10^{L−1}: khi ấy không số L chữ số nào bằng tổng của nó được. Tính trực tiếp cho thấy điều đó xảy ra từ L = 61.'])
    D.fig(P.fig('bound'), 'Tỉ số giữa tổng lớn nhất L · 9ᴸ và số nhỏ nhất 10ᴸ⁻¹ (thang logarit).', 14.5)

    D.h('2. Bài toán TULUAN')
    D.problem_box('TULUAN', 'Cho số nguyên K. Hãy in theo thứ tự tăng dần mọi số tự luân nhỏ hơn 10^{K}.',
                  'Một số nguyên K (1 ≤ K ≤ 18).', 'Mỗi dòng một số tự luân, theo thứ tự tăng dần.')
    D.examples('TULUAN', [('3', '1 2 ... 9\n153\n370\n371\n407', 'Mười ba số (in mỗi số một dòng). 370 = 3^{3} + 7^{3} + 0^{3}; 407 = 4^{3} + 0^{3} + 7^{3}.')])

    D.h('3. Ý tưởng ngây thơ: Kiểm tra từng số')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách kiểm tra từng số.', 12)
    D.code('TULUAN.CPP (ngây thơ): kiểm tra mọi n < 10ᴷ', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['10^{K} số, mỗi số O(L^{2}) phép nhân (có thể tính sẵn d^{L} để còn O(L)). Đo thực tế: K = 8 mất **3,1 giây**, K = 9 mất **35 giây**. '
                               'Với K = 18 cần khoảng 3,5 · 10^{10} giây: hơn **một nghìn năm**.'])
    D.kbox('BẾ TẮC', ['Tổng d_{1}^{L} + ... + d_{L}^{L} **không phụ thuộc thứ tự** các chữ số: 135, 153, 315, 351, 513, 531 đều cho cùng tổng 153. '
                      'Ta đang tính đi tính lại cùng một tổng cho mọi hoán vị. Nếu chỉ tính một lần cho mỗi **tập chữ số** thì sao? Có bao nhiêu tập như vậy?'])

    D.h('4. Phá bế tắc: Duyệt theo tập chữ số')
    D.step(1, 'Mỗi tập chữ số cho đúng một tổng')
    D.p('Một "tập chữ số" độ dài L (cho phép lặp, không kể thứ tự) được mô tả bởi cnt[0], ..., cnt[9] ≥ 0 với tổng L. Tổng tương ứng là s = Σ cnt[d] · d^{L}. '
        'Nếu có số tự luân nào với tập chữ số này thì số đó **bắt buộc** bằng s. Vậy chỉ cần kiểm tra: s có đúng L chữ số và tập chữ số của s có đúng là cnt không.')
    D.fig(P.fig('multiset'), 'Ba tập chữ số độ dài 3 và kết quả kiểm tra.', 15)
    D.step(2, 'Có bao nhiêu tập chữ số?')
    D.kbox('ĐỊNH LÍ (CHIA KẸO)', ['Số cách chọn cnt[0], ..., cnt[9] ≥ 0 có tổng L là C(L + 9, 9). Với L = 18 là C(27, 9) = 4 686 825; cộng mọi L từ 1 tới 18 được **13 123 109** tập, '
                                  'so với 10^{18} số: nhỏ hơn khoảng 7,6 · 10^{10} lần.'])
    D.step(3, 'Liệt kê tập chữ số bằng đệ quy')
    D.p('Hàm chon(d, left, s) quyết định chữ số d xuất hiện bao nhiêu lần (từ 0 tới left), rồi gọi tiếp cho chữ số d + 1; chữ số 9 nhận nốt phần còn lại. Tổng s được cộng dồn trong lúc đệ quy.')
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của cách duyệt theo tập chữ số.', 12.5)
    D.code('TULUAN.CPP: duyệt theo tập chữ số', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['13 123 109 tập chữ số, mỗi tập một lần kiểm tra O(L): chương trình in đủ 46 số tự luân dưới 10^{18} trong khoảng **0,5 giây** (so với hơn một nghìn năm). '
                               'Tổng lớn nhất 18 · 9^{18} ≈ 2,7 · 10^{18} vừa long long. Kết quả trùng khớp cách kiểm tra từng số với mọi K ≤ 7.'])
    D.table(['Số chữ số', 'Các số tự luân'], [
        ['1', '1, 2, ..., 9'], ['3', '153, 370, 371, 407'], ['4', '1634, 8208, 9474'], ['5', '54748, 92727, 93084'], ['6', '548834'], ['7', '1741725, 4210818, 9800817, 9926315'],
        ['8', '24678050, 24678051, 88593477'], ['9', '146511208, 472335975, 534494836, 912985153'], ['10', '4679307774'],
        ['11', '32164049650, 32164049651, 40028394225, 42678290603, 44708635679, 49388550606, 82693916578, 94204591914'],
        ['14', '28116440335967'], ['16', '4338281769391370, 4338281769391371'], ['17', '21897142587612075, 35641594208964132, 35875699062250035']],
        widths=[1.2, 7.0], align=['center', 'left'], sz=19)
    D.p('Không có số tự luân nào có 2, 12, 13, 15 hay 18 chữ số.')

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Factorion')
    D.p('Số bằng tổng **giai thừa** các chữ số: 145 = 1! + 4! + 5!, 40585 = 4! + 0! + 5! + 8! + 5!. Chặn trên: số có L ≥ 8 chữ số có tổng không quá L · 9! < 10^{L−1}, nên chỉ cần xét n < 10^{7}. '
        'Chỉ có bốn factorion: 1, 2, 145, 40585.')
    D.code('Tìm mọi factorion', P.src('ex_factorion.cpp'))
    D.sub('Mở rộng 2: Disarium và Münchhausen')
    D.p('**Disarium**: chữ số thứ i (tính từ trái, từ 1) lũy thừa i: 89 = 8^{1} + 9^{2}, 135 = 1^{1} + 3^{2} + 5^{3}; dưới 10^{6} có 1..9, 89, 135, 175, 518, 598, 1306, 1676, 2427. '
        'Vì số mũ phụ thuộc vị trí nên không duyệt theo tập được; nhưng chặn trên vẫn cho thấy chỉ có hữu hạn số. '
        '**Münchhausen**: mỗi chữ số lũy thừa chính nó: 3435 = 3^{3} + 4^{4} + 3^{3} + 5^{5}; lại duyệt theo tập được vì tổng không phụ thuộc thứ tự.')
    D.sub('Mở rộng 3: Số Dudeney')
    D.p('Số bằng **lập phương của tổng chữ số**: 512 = (5 + 1 + 2)^{3}, 4913, 5832, 17576, 19683. Lần này duyệt theo **tổng chữ số** s (≤ 9 · 18 = 162) thay vì theo số: n phải bằng s^{3}, '
        'chỉ cần kiểm tra 162 giá trị. Đổi đại lượng được duyệt từ "số" sang "đặc trưng của số" là ý tưởng chung của cả bài.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Quên kiểm tra số chữ số của s:** tập {1, 2, 3} cho 36, có 2 chữ số chứ không phải 3.',
        '- **Quên chữ số 0** trong tập (370, 407 có chữ số 0).',
        '- **Trùng lặp:** các số như 1..9 có thể được tìm thấy từ nhiều cách đếm; sắp xếp rồi bỏ trùng trước khi in.',
        '- **Tràn số:** với K > 19, 9^{L} · L vượt long long; khi đó cần __int128 hoặc số lớn.'])
    D.kbox('GHI NHỚ', [
        '- Chặn trên từ so sánh "tổng lớn nhất" với "số nhỏ nhất cùng độ dài" biến bài tìm kiếm vô hạn thành hữu hạn.',
        '- Nếu đại lượng cần tính không phụ thuộc thứ tự chữ số, hãy **duyệt theo tập chữ số**: C(L + 9, 9) tập thay vì 10^{L} số.',
        '- Hoặc duyệt theo một đặc trưng nhỏ hơn (tổng chữ số, số chữ số) rồi dựng lại số.'])
    D.luyentap([('10.1', 'TỰ LUÂN', 'Đếm số tự luân trong [L, R] với R ≤ 10^{18}: tìm hết bằng cách duyệt theo tập rồi đếm.'),
                ('10.2', 'TỔNG LŨY THỪA', 'Tìm mọi n < 10^{K} bằng tổng các chữ số lũy thừa p cho trước (p ≤ 9): cùng kĩ thuật, chặn trên phụ thuộc p.'),
                ('10.3', 'DUDENEY', 'Tìm mọi n bằng (tổng chữ số)^{k} với k ≤ 10: duyệt theo tổng chữ số, cần __int128.')])
    D.tukiemtra([('Kiểm tra 9474 là số tự luân.', '6561 + 256 + 2401 + 256 = 9474'), ('Có bao nhiêu tập chữ số độ dài 3?', 'C(12, 9) = 220'),
                 ('Vì sao factorion không thể có 8 chữ số?', 'tổng lớn nhất 8 · 9! = 2 903 040 có 7 chữ số'), ('Số Dudeney nào bằng (tổng chữ số)^{3} với tổng 17?', '17^{3} = 4913, tổng chữ số 4 + 9 + 1 + 3 = 17')])
