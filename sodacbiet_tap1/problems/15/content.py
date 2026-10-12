def build(D, P):
    D.objectives([
        'Hiểu ý tưởng cốt lõi của **quy hoạch động chữ số**: dựng số từ trái sang, tách thành trạng thái "bám sát N" và "đã tự do".',
        'Đếm các số trong [L, R] (tới 10^{18}) có tổng chữ số bằng S trong vài nghìn phép tính, bằng công thức f(R) − f(L − 1).',
        'Nắm được **khuôn mẫu đệ quy có nhớ** go(pos, trạng thái, tight) dùng cho mọi bài đếm theo chữ số.',
        'Áp dụng cho số vui vẻ, số không có hai chữ số kề nhau bằng nhau, ...'])
    D.kbox('KHỞI ĐỘNG', [
        'Năm 2026 có tổng chữ số 2 + 0 + 2 + 6 = 10. Từ năm 1 đến năm 2026, có bao nhiêu năm có tổng chữ số bằng 10? Liệt kê thì được: 19, 28, 37, ..., 2008, 2017, 2026: tất cả **121** năm.',
        'Nhưng nếu hỏi từ 1 đến 10^{18} thì sao? Duyệt 10^{18} số mất hàng trăm năm. Vậy mà máy tính trả lời được trong một phần nghìn giây, nhờ một ý tưởng: '
        'đếm theo **chữ số**, không theo **số**.'])

    D.h('1. Đếm các số có k chữ số tự do')
    D.kbox('ĐỊNH NGHĨA', ['Gọi ways(k, t) là số cách điền k chữ số (mỗi chữ số từ 0 đến 9, cho phép 0 ở đầu) sao cho tổng bằng t. Ví dụ ways(2, 3) = 4: 03, 12, 21, 30.'])
    D.kbox('ĐỊNH LÍ (CÔNG THỨC TRUY HỒI)', ['$eq ways(0, t) = 1 nếu t = 0, ngược lại bằng 0',
                                           '$eq ways(k, t) = ways(k − 1, t) + ways(k − 1, t − 1) + ... + ways(k − 1, t − 9)'])
    D.kbox('VÌ SAO ĐÚNG?', ['Chia các cách điền theo chữ số đầu tiên d (0..9): phần còn lại là k − 1 chữ số có tổng t − d. Các nhóm rời nhau và phủ hết mọi cách. Với k ≤ 18, t ≤ 162, bảng chỉ có khoảng 3 000 ô.'])
    D.fig(P.fig('table'), 'Bảng ways(k, t) với k ≤ 3, t ≤ 11: mỗi ô bằng tổng 10 ô liền trước ở hàng trên.', 15.5)

    D.h('2. Bài toán TONGS')
    D.problem_box('TONGS', 'Cho ba số nguyên L, R, S. Hãy đếm số các số nguyên x với L ≤ x ≤ R mà tổng các chữ số của x bằng S.',
                  'Một dòng chứa L, R, S (1 ≤ L ≤ R ≤ 10^{18}, 1 ≤ S ≤ 162).', 'Số lượng các số thỏa mãn.')
    D.examples('TONGS', [('1 100 10', '9', '19, 28, 37, 46, 55, 64, 73, 82, 91.'), ('2000 2026 10', '3', '2008, 2017, 2026.'),
                         ('1 1000000000 1', '10', '1, 10, 100, ..., 10^{9}.')])
    D.p('Subtask 1 (30 điểm): R ≤ 10^{6}. Subtask 2 (70 điểm): R ≤ 10^{18}.')

    D.h('3. Ý tưởng ngây thơ: Duyệt mọi số')
    D.p('Duyệt x từ L đến R, tính tổng chữ số (như Bài 1) và đếm.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách duyệt.', 13)
    D.code('TONGS.CPP (ngây thơ): duyệt mọi số', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Khoảng (R − L + 1) · 19 phép chia. Đo thực tế: L = 1, R = 10^{9} mất **9,5 giây**. Với R = 10^{18} cần khoảng 300 năm. Cách này chỉ được 30 điểm.'])
    D.kbox('BẾ TẮC', ['Các số 1 000 000 – 1 999 999 và 3 000 000 – 3 999 999 có cùng "phần đuôi": sáu chữ số tùy ý. Số cách để đuôi có tổng t **không phụ thuộc** chữ số đầu. '
                      'Ta đang đếm đi đếm lại cùng một thứ hàng tỉ lần.'])

    D.h('4. Phá bế tắc: Quy hoạch động chữ số')
    D.step(1, 'Đổi đoạn thành tiền tố')
    D.p('Gọi f(N) là số các x trong [0, N] có tổng chữ số bằng S. Khi đó đáp số là **f(R) − f(L − 1)**: giống như tổng tiền tố. Chỉ cần đếm được các số **không vượt quá** N.')
    D.step(2, 'Số nhỏ hơn N "rời khỏi" N ở đâu?')
    D.p('Viết N có L chữ số, và mọi x ≤ N cũng viết đủ L chữ số (thêm 0 ở đầu). Nếu x < N thì có một vị trí **đầu tiên** i mà chữ số của x khác N: '
        'trước vị trí i, x **bám sát** N (giống hệt); tại i, x có chữ số d < c_{i}; sau i, các chữ số của x **tự do** (0..9 tùy ý), vì x đã chắc chắn nhỏ hơn N.')
    D.kbox('HÃY HÌNH DUNG', ['Như đi xuống một cây: ở mỗi tầng, nhánh "bằng chữ số của N" đi tiếp xuống tầng dưới (vẫn bám sát), còn mỗi nhánh "nhỏ hơn" rẽ ra thành một khối các số tự do '
                             'mà ta đếm **một lần** bằng ways(k, t). Cả cây chỉ có L tầng, mỗi tầng tối đa 9 nhánh rẽ.'])
    D.step(3, 'Công thức')
    D.p('Gọi need là tổng còn thiếu sau khi bám sát i chữ số đầu: need = S − (c_{0} + ... + c_{i−1}). Khi đó:')
    D.kbox('ĐỊNH LÍ (ĐẾM CÁC SỐ ≤ N)', ['$eq f(N) = Σ_{i} Σ_{d < c_{i}} ways(L − 1 − i, need_{i} − d) + [tổng chữ số của N = S]'])
    D.step(4, 'Chạy tay với N = 2026, S = 10')
    D.fig(P.fig('tree'), 'Các khối số được đếm khi N = 2026, S = 10.', 15.5)
    D.p('Kết quả 121 khớp với phép liệt kê ở phần Khởi động. Để trả lời ví dụ 2: f(2026) − f(1999) = 121 − 118 = 3.')
    D.step(5, 'Chương trình')
    D.p('Hàm ways được tính bằng đệ quy có nhớ (mảng memo, −1 nghĩa là chưa tính). Với L, R tới 10^{18} chỉ có 19 chữ số, nên cần L − 1 = 0 thì f(−1) = 0.')
    D.fig(P.fig('opt'), 'Sơ đồ khối của quy hoạch động chữ số.', 10.5)
    D.code('TONGS.CPP: quy hoạch động chữ số', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Bảng ways có 19 · 163 ô, mỗi ô tính bằng 10 phép cộng: khoảng 3 · 10^{4} phép tính; hàm f gọi ways không quá 19 · 9 lần. '
                               'Đo thực tế: R = 10^{18} chạy **0,005 giây**. Đáp số cho [1, 10^{18}] với S = 81 là 32 458 256 583 753 952: vẫn vừa long long. '
                               'Đã đối chiếu với cách duyệt trên 300 bộ dữ liệu nhỏ.'])
    D.kbox('LƯU Ý', ['Đáp số lớn nhất có thể vào khoảng 3,3 · 10^{16} (S = 81 là tổng "ở giữa", có nhiều số nhất): an toàn với long long. '
                     'Nhưng nếu đề hỏi tổng chữ số của mọi số tới 10^{18}, đáp số vượt 2^{63}: phải dùng __int128 hoặc lấy dư.'])

    D.h('5. Khuôn mẫu tổng quát')
    D.p('Cách ở mục 4 dùng được vì "tổng chữ số" cộng dồn đơn giản. Với điều kiện phức tạp hơn, ta viết một hàm đệ quy **go(pos, state, tight)**:')
    D.kbox('THUẬT TOÁN (KHUÔN QUY HOẠCH ĐỘNG CHỮ SỐ)', [
        '- pos: đang điền chữ số thứ mấy (từ trái sang).',
        '- state: những gì cần nhớ về phần đã điền (tổng, số dư, chữ số trước, đã bắt đầu chưa...).',
        '- tight: phần đã điền có đang **bám sát** N không; nếu có, chữ số tiếp theo chỉ được tới c_{pos}, ngược lại tới 9.',
        '- Chỉ nhớ (memo) kết quả khi tight = false: trạng thái tight chỉ xuất hiện đúng một lần trên mỗi tầng.',
        '- Độ phức tạp: (số vị trí) × (số trạng thái) × 10.'])

    D.h('6. Mở rộng')
    D.sub('Mở rộng 1: Đếm số không có hai chữ số kề nhau bằng nhau')
    D.p('Trạng thái là chữ số vừa điền (last), thêm giá trị đặc biệt 10 nghĩa là "chưa bắt đầu", để các chữ số 0 ở đầu không bị coi là chữ số thật (số 0012 thực chất là 12, không vi phạm). '
        'Đây đúng là khuôn mẫu ở mục 5.')
    D.code('Đếm x ≤ N không có hai chữ số kề nhau bằng nhau', P.src('ex_kele.cpp'))
    D.p('Kết quả: có 1 563 số như vậy trong [1, 2026] và 168 856 464 709 124 010 số trong [1, 10^{18}]. Đã đối chiếu với cách duyệt tới 2 · 10^{5}.')
    D.sub('Mở rộng 2: Đếm số vui vẻ tới 10^{18}')
    D.p('Số vui vẻ (Bài 11) là số mà lặp "tổng bình phương các chữ số" thì về 1. Sau **một bước**, mọi số ≤ 10^{18} trở thành một số ≤ 18 · 81 = 1 458. '
        'Vậy chỉ cần đếm, với mỗi q ≤ 1 458, có bao nhiêu x ≤ N có tổng bình phương chữ số bằng q (quy hoạch động như mục 4, thay d bằng d^{2}), rồi cộng các q vui vẻ.')
    D.code('Đếm số vui vẻ trong [1, N]', P.src('ex_happy.cpp'))
    D.p('Có 143 số vui vẻ ≤ 1 000, 302 số ≤ 2026 và 118 226 055 080 025 491 số ≤ 10^{18} (khoảng 11,8%). Đã đối chiếu với cách duyệt tới 2 · 10^{5}.')
    D.sub('Mở rộng 3: Số nhỏ nhất ≥ L có tổng chữ số S')
    D.p('Dùng f để **chặt nhị phân**: tìm x nhỏ nhất mà f(x) − f(L − 1) ≥ 1. Khoảng 60 lần gọi f. Cách này dùng được cho mọi câu hỏi "số thứ k thỏa mãn điều kiện" (Bài 16 sẽ dựng trực tiếp không cần chặt nhị phân).')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Quên đếm chính N:** vòng lặp chỉ đếm các số nhỏ hơn N; cộng thêm 1 nếu N thỏa mãn.',
        '- **Không dừng khi need < 0:** đi tiếp vẫn đúng nếu ways trả về 0 với t < 0, nhưng truy cập mảng với chỉ số âm thì sai.',
        '- **f(L − 1) với L = 1:** f(0) phải đúng (0 có tổng chữ số 0, không đếm khi S ≥ 1).',
        '- **Nhớ cả trạng thái tight:** kết quả khi bám sát phụ thuộc N; nếu dùng chung memo cho hai lần gọi f(R), f(L − 1) thì sai.',
        '- **Số 0 ở đầu** trong các điều kiện như "chữ số kề", "chữ số khác nhau": cần trạng thái "đã bắt đầu".'])
    D.kbox('GHI NHỚ', [
        '- Đoạn [L, R] → f(R) − f(L − 1). Đếm x ≤ N theo vị trí đầu tiên x rời khỏi N.',
        '- Phần sau khi rời khỏi N là tự do: đếm một lần bằng bảng quy hoạch động không phụ thuộc N.',
        '- Khuôn go(pos, state, tight): độ phức tạp = số vị trí × số trạng thái × 10.'])
    D.luyentap([('15.1', 'NĂM ĐẸP', 'Đếm các năm trong [L, R] có tổng chữ số bằng S (R ≤ 10^{18}): bài TONGS.'),
                ('15.2', 'SỐ VUI VẺ', 'Đếm số vui vẻ trong [L, R], R ≤ 10^{18}: Mở rộng 2.'),
                ('15.3', 'KHÔNG LẶP KỀ', 'Đếm số trong [L, R] không có hai chữ số kề nhau bằng nhau, và số có các chữ số tăng dần: khuôn mẫu mục 5.')])
    D.tukiemtra([('ways(2, 10) bằng bao nhiêu?', '9 (19, 28, ..., 91)'), ('Có bao nhiêu số có 3 chữ số (100..999) với tổng chữ số 1?', '1 (số 100)'),
                 ('Đếm x trong [1, 99] có tổng chữ số 9?', '10 (9, 18, ..., 90)'), ('Vì sao chỉ nhớ kết quả khi tight = false?', 'Khi tight, kết quả phụ thuộc N và mỗi tầng chỉ có một trạng thái tight')])
