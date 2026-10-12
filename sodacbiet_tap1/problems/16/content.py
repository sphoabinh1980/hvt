def build(D, P):
    D.objectives([
        'Xử lý điều kiện phụ thuộc vào **chính tổng chữ số** (như "x chia hết cho tổng chữ số của x") bằng cách **cố định** đại lượng chưa biết rồi quy hoạch động.',
        'Ghép nhiều thông tin vào trạng thái: tổng chữ số, số dư theo mô-đun, trạng thái máy so khớp mẫu.',
        'Dựng trực tiếp **số thứ k** thỏa mãn điều kiện, không cần chặt nhị phân.',
        'Đếm các số không chứa một mẫu chữ số cho trước bằng máy KMP.'])
    D.kbox('KHỞI ĐỘNG', [
        'Số 2026 có tổng chữ số 10, và 2026 không chia hết cho 10. Nhưng 2025 có tổng chữ số 9 và 2025 = 9 · 225: 2025 là một **số Harshad** (tiếng Phạn: "niềm vui lớn"), '
        'tức là số chia hết cho tổng các chữ số của nó. Năm 2024 cũng vậy (tổng 8, 2024 = 8 · 253).',
        'Từ 1 đến 10^{18} có bao nhiêu số Harshad? Khó khăn mới so với Bài 15: điều kiện "chia hết cho tổng chữ số" dính tới tổng chữ số, mà tổng chữ số chỉ biết khi đã điền **xong** mọi chữ số.'])

    D.h('1. Số Harshad')
    D.kbox('ĐỊNH NGHĨA', ['Số nguyên dương x là **số Harshad** (hay số Niven) nếu x chia hết cho tổng các chữ số S(x) của nó. Ví dụ: 1..9, 10, 12, 18, 20, 21, 24, 27, 30, ..., 2024, 2025.'])
    D.p('Mọi số có một chữ số đều là số Harshad. Số dạng 10^{k} cũng vậy (tổng chữ số 1). Số **n!** với n nhỏ thường là số Harshad. Có đúng **33** số Harshad không vượt quá 100:')
    D.fig(P.fig('groups'), 'Các số Harshad ≤ 100, xếp theo tổng chữ số.', 11.5)
    D.kbox('LƯU Ý', ['Nhóm theo tổng chữ số s chính là chìa khóa của bài toán: **trong một nhóm**, điều kiện "x chia hết cho S(x)" trở thành "x chia hết cho s", với s là một hằng số cố định.'])

    D.h('2. Bài toán HARSHAD')
    D.problem_box('HARSHAD', 'Cho số nguyên dương N. Hãy đếm số các số Harshad trong đoạn [1, N].', 'Một số nguyên N (1 ≤ N ≤ 10^{18}).', 'Số các số Harshad không vượt quá N.')
    D.examples('HARSHAD', [('100', '33', 'Xem Hình 16.1.'), ('2026', '410', ''), ('1000000', '95428', 'Khoảng 9,5% các số.')])
    D.p('Subtask 1 (30 điểm): N ≤ 10^{6}. Subtask 2 (70 điểm): N ≤ 10^{18}.')

    D.h('3. Ý tưởng ngây thơ: Kiểm tra từng số')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách kiểm tra từng số.', 13.5)
    D.code('HARSHAD.CPP (ngây thơ): kiểm tra từng số', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['N số, mỗi số khoảng 19 phép chia. Đo thực tế: N = 10^{8} mất **1,0 giây**, N = 10^{9} khoảng 10 giây; N = 10^{18} cần hơn 300 năm. Cách này được 30 điểm.'])
    D.kbox('BẾ TẮC', ['Thử dùng quy hoạch động chữ số như Bài 15: điền từ trái sang, nhớ (tổng chữ số, x mod ?). Nhưng mod **cái gì**? Mô-đun là tổng chữ số, mà tổng ấy chưa biết khi đang điền dở. '
                      'Nhớ x nguyên vẹn thì có 10^{18} trạng thái.'])

    D.h('4. Phá bế tắc: Đoán trước tổng chữ số')
    D.step(1, 'Cố định tổng chữ số s')
    D.p('Tổng chữ số của một số ≤ 10^{18} không vượt quá 9 · 19 = 171. Ta **thử mọi giá trị s** từ 1 đến 9L, và với mỗi s chỉ đếm các x ≤ N thỏa mãn **hai** điều kiện: '
        'tổng chữ số của x đúng bằng s, và x chia hết cho s. Mỗi số Harshad được đếm đúng một lần, ở đúng giá trị s = S(x) của nó.')
    D.step(2, 'Trạng thái (t, r)')
    D.p('Với s cố định, khi điền chữ số từ trái sang, chỉ cần nhớ t = tổng các chữ số đã điền (không quá s, vượt thì bỏ) và r = giá trị tiền tố mod s. Thêm chữ số x:')
    D.kbox('ĐỊNH LÍ (CHUYỂN TRẠNG THÁI)', ['$eq (t, r) + chữ số x → (t + x, (10 · r + x) mod s)'])
    D.fig(P.fig('trans'), 'Chuyển trạng thái với s = 9: từ tiền tố 4 sang tiền tố 45.', 14.5)
    D.kbox('VÌ SAO ĐÚNG?', ['Tiền tố mới bằng 10 · (tiền tố cũ) + x, nên số dư mới chỉ phụ thuộc số dư cũ (tính chất số dư của tổng và tích, Bài 5). Cuối cùng x là số Harshad ứng với s khi và chỉ khi t = s và r = 0.'])
    D.step(3, 'Xử lý giới hạn N')
    D.p('Như Bài 15, ta giữ riêng **một** đường "bám sát N" (tổng ts, số dư tr), và mảng cnt[t][r] đếm các tiền tố đã nhỏ hơn N (phần sau tự do). Ở vị trí i có chữ số c của N: '
        'mọi trạng thái trong cnt được thêm chữ số 0..9; đường bám sát sinh ra các trạng thái mới khi đặt chữ số x < c (từ đó trở đi tự do), rồi tiếp tục bám sát với chữ số c.')
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối: vòng ngoài thử tổng s, vòng trong quy hoạch động chữ số.', 11)
    D.code('HARSHAD.CPP: quy hoạch động chữ số cho từng tổng s', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Với mỗi s: L vị trí × (s + 1) giá trị t × s giá trị r × 10 chữ số. Cộng theo s = 1..171: khoảng 19 · 10 · 171^{3} / 3 ≈ 3 · 10^{8} phép tính, '
                               'nhưng nhiều trạng thái bằng 0 được bỏ qua. Đo thực tế: N = 10^{18} chạy **0,32 giây**, đáp số 29 410 615 796 612 778 (khoảng 2,9%). Đã đối chiếu với cách duyệt trên 300 bộ dữ liệu.'])
    D.kbox('LƯU Ý', ['Kĩ thuật "cố định đại lượng chưa biết, rồi kiểm tra ở cuối" dùng được rất rộng: đếm số chia hết cho tích chữ số, cho chữ số cuối, cho số chữ số khác 0... '
                     'Miễn là đại lượng ấy chỉ nhận **ít** giá trị.'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Số thứ k có tổng chữ số S')
    D.p('Thay vì chặt nhị phân (Bài 15, Mở rộng 3), ta **dựng trực tiếp**: viết đáp số với đúng 18 chữ số (cho phép 0 ở đầu: với cùng độ dài, thứ tự xâu chính là thứ tự số). '
        'Tại mỗi vị trí, thử chữ số d = 0, 1, 2, ...: khối các số bắt đầu bằng d có ways(còn lại, need − d) phần tử. Nếu k nằm trong khối thì chọn d, ngược lại trừ k đi kích thước khối và thử d tiếp theo.')
    D.code('Số nguyên dương thứ k có tổng chữ số S', P.src('ex_kth.cpp'))
    D.p('Ví dụ: số thứ 2026 có tổng chữ số 10 là **221 014**; số thứ 10^{15} có tổng chữ số 81 là 36 637 804 683 492 651. Đã đối chiếu với cách liệt kê trên 200 bộ dữ liệu.')
    D.sub('Mở rộng 2: Số không chứa một mẫu')
    D.p('Đếm các số ≤ N mà xâu chữ số **không chứa** một xâu mẫu P (ví dụ "13", số xui xẻo ở nhiều nước). Trạng thái là **độ dài phần đầu của P đang khớp** với đuôi của phần đã điền; '
        'khi điền thêm chữ số, độ dài khớp mới được tính bằng máy KMP (hàm tiền tố). Gặp khớp đủ |P| thì loại. Cần thêm cờ "đã bắt đầu" để các chữ số 0 ở đầu không tham gia khớp mẫu.')
    D.code('Đếm x ≤ N không chứa mẫu P', P.src('ex_mau.cpp'))
    D.p('Kết quả: có 1 886 số ≤ 2026 không chứa "13"; 841 554 882 220 704 499 số ≤ 10^{18} không chứa "13"; 150 094 635 296 999 121 = 9^{18} số ≤ 10^{18} không chứa chữ số 4. '
        'Đã đối chiếu với cách duyệt trên 300 bộ dữ liệu (mẫu dài 1..3, có cả chữ số 0).')
    D.sub('Mở rộng 3: Nhiều điều kiện cùng lúc')
    D.p('Các trạng thái ghép được với nhau: "chia hết cho K **và** tổng chữ số bằng S" dùng trạng thái (tổng, số dư mod K); "số đối xứng" thì không làm theo cách này được (cần nhìn cả hai đầu), '
        'phải dựng nửa đầu như Bài 9. Trước khi viết, luôn ước lượng: **số vị trí × số trạng thái × 10** có nhỏ không?')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Chọn sai giới hạn s:** 10^{18} có 19 chữ số; tổng chữ số tới 171 chứ không phải 162 (mảng [163] gây lỗi truy cập bộ nhớ).',
        '- **Đếm trùng:** mỗi số chỉ được đếm ở giá trị s bằng đúng tổng chữ số của nó, nên điều kiện cuối phải là t = s, không phải t ≤ s.',
        '- **Số 0 ở đầu** khi khớp mẫu: "0013" là 13, nhưng "013" không được khớp mẫu "01".',
        '- **Dùng chung memo** giữa các giá trị s hay các mẫu khác nhau mà quên xóa.'])
    D.kbox('GHI NHỚ', [
        '- Đại lượng chưa biết nhưng ít giá trị (tổng chữ số ≤ 171): cố định nó ở vòng ngoài, kiểm tra ở cuối.',
        '- Trạng thái số dư: (r, x) → (10r + x) mod m.',
        '- Số thứ k: dựng từ trái sang, trừ dần kích thước các khối.',
        '- Không chứa mẫu: trạng thái là độ dài khớp KMP.'])
    D.luyentap([('16.1', 'HARSHAD', 'Đếm số Harshad trong [L, R], R ≤ 10^{18}: bài HARSHAD với f(R) − f(L − 1).'),
                ('16.2', 'SỐ THỨ K', 'Số thứ k có tổng chữ số S, và số thứ k chia hết cho tổng chữ số của nó: Mở rộng 1 kết hợp mục 4.'),
                ('16.3', 'SỐ XUI XẺO', 'Đếm số trong [L, R] không chứa "13" và không chứa chữ số 4: Mở rộng 2 với nhiều mẫu.')])
    D.tukiemtra([('2026 có phải số Harshad không?', 'Không (tổng 10, 2026 không chia hết cho 10)'), ('Số Harshad lớn nhất ≤ 100?', '100'),
                 ('Từ (t, r) = (4, 4) với s = 9, thêm chữ số 5 được trạng thái nào?', '(9, 0)'), ('Có bao nhiêu số có 2 chữ số không chứa chữ số 4?', '72 = 8 · 9')])
