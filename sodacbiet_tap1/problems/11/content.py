def build(D, P):
    D.objectives([
        'Làm quen với các **dãy lặp trên chữ số**: tổng bình phương chữ số (số hạnh phúc), phép biến đổi Kaprekar, dãy Collatz.',
        'Hiểu vì sao một dãy x_{i+1} = f(x_{i}) nhận hữu hạn giá trị thì luôn có dạng **đuôi + chu trình** (hình ρ).',
        'Tìm phần tử thứ K của dãy với K tới 10^{18}: tìm đuôi μ và chu trình λ rồi nhảy bằng phép chia lấy dư.',
        'Biết thuật toán **rùa và thỏ** của Floyd để tìm chu trình chỉ với O(1) bộ nhớ.'])
    D.kbox('KHỞI ĐỘNG', [
        'Lấy số 7. Bình phương từng chữ số rồi cộng: 7^{2} = 49. Làm tiếp: 4^{2} + 9^{2} = 97, rồi 9^{2} + 7^{2} = 130, rồi 1 + 9 + 0 = 10, rồi 1. Từ đó mãi mãi là 1. Số 7 được gọi là **số hạnh phúc**.',
        'Thử với 2025: 33, 18, 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, ... và quay vòng mãi trong 8 số. Vậy sau **10^{18}** bước, dãy bắt đầu từ 2025 dừng ở đâu? Không ai đi nổi 10^{18} bước, nhưng ta không cần đi.'])
    D.fig(P.fig('happy'), 'Dãy tổng bình phương chữ số bắt đầu từ 7.', 14)

    D.h('1. Dãy lặp và hình chữ ρ')
    D.kbox('ĐỊNH NGHĨA', ['Cho hàm f và giá trị đầu x_{0}. **Dãy lặp** là x_{1} = f(x_{0}), x_{2} = f(x_{1}), ... Trong bài này f(x) là tổng bình phương các chữ số của x. '
                          'Số x là **số hạnh phúc** nếu dãy bắt đầu từ x đi tới 1.'])
    D.kbox('ĐỊNH LÍ (ĐUÔI VÀ CHU TRÌNH)', [
        'Nếu dãy lặp chỉ nhận giá trị trong một tập hữu hạn thì tồn tại μ ≥ 0, λ ≥ 1 sao cho x_{0}, ..., x_{μ−1} đôi một khác nhau và không lặp lại (**đuôi**), '
        'còn từ x_{μ} trở đi dãy tuần hoàn với chu kì λ (**chu trình**): x_{i+λ} = x_{i} với mọi i ≥ μ.'])
    D.kbox('VÌ SAO ĐÚNG?', ['Có hữu hạn giá trị nên phải có hai chỉ số i < j với x_{i} = x_{j}; lấy cặp có j nhỏ nhất, đặt μ = i, λ = j − i. Vì x_{i+1} = f(x_{i}) chỉ phụ thuộc x_{i}, '
                            'từ x_{i} = x_{j} suy ra x_{i+1} = x_{j+1}, và cứ thế: dãy lặp lại mãi với chu kì λ.'])
    D.kbox('VÍ DỤ: TỔNG BÌNH PHƯƠNG CHỮ SỐ CHỈ NHẬN GIÁ TRỊ NHỎ', ['Số có L chữ số cho f(x) ≤ 81L. Với x ≤ 10^{18}, sau **một** bước f(x) ≤ 18 · 81 = 1458; và mọi số ≤ 1458 lại cho f ≤ 1 + 81 · 3 = 244. '
                                                                 'Dãy rơi rất nhanh vào một tập nhỏ, nên chắc chắn có dạng ρ. Người ta đã kiểm tra: mọi dãy hoặc về điểm dừng 1, '
                                                                 'hoặc rơi vào **đúng một** chu trình 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4.'])
    D.fig(P.fig('rho'), 'Dãy bắt đầu từ 2025: đuôi 5 số, chu trình 8 số.', 15.2)

    D.h('2. Bài toán DAYLAP')
    D.problem_box('DAYLAP', 'Cho Q câu hỏi, mỗi câu gồm x và K. Đặt x_{0} = x và x_{i+1} = tổng bình phương các chữ số của x_{i}. Hãy in x_{K}.',
                  'Dòng đầu chứa Q (Q ≤ 10^{5}). Mỗi dòng tiếp theo chứa x, K (1 ≤ x ≤ 10^{18}, 0 ≤ K ≤ 10^{18}).', 'Q dòng, mỗi dòng giá trị x_{K}.')
    D.examples('DAYLAP', [('3\n7 5\n4 3\n2025 1000000000000000000', '1\n58\n145', '7 → 49 → 97 → 130 → 10 → 1. 4 → 16 → 37 → 58. Câu thứ ba được tính ở mục 4.')])

    D.h('3. Ý tưởng ngây thơ: Đi đúng K bước')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách mô phỏng.', 11)
    D.code('DAYLAP.CPP (ngây thơ): mô phỏng K bước', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['K bước, mỗi bước vài phép chia: O(K). Đo thực tế với x = 2025: K = 10^{8} mất **0,68 giây**, K = 10^{9} mất **6,8 giây**; K = 10^{18} cần khoảng **200 năm**, cho mỗi câu hỏi.'])
    D.kbox('BẾ TẮC', ['Sau vài bước dãy đã quay vòng trong 8 số, nhưng chương trình vẫn đi tiếp hàng tỉ tỉ vòng. Nếu biết dãy vào vòng ở bước nào và vòng dài bao nhiêu, '
                      'ta có thể "đi tắt" như khi tính thứ trong tuần sau 10^{18} ngày: chỉ cần một phép chia lấy dư.'])

    D.h('4. Phá bế tắc: Tìm ρ rồi nhảy')
    D.step(1, 'Ghi lại lần đầu gặp mỗi giá trị')
    D.p('Đi từng bước, lưu dãy seq và mảng first[v] = chỉ số đầu tiên giá trị v xuất hiện. Lần đầu gặp một giá trị đã có first, ta biết ngay μ = first[v] và λ = (số phần tử đã lưu) − μ. '
        'Để mảng first nhỏ, đi trước **một** bước: sau bước đó mọi giá trị ≤ 1458 (cẩn thận: khi đó K giảm 1 và chỉ số tính từ x_{1}).')
    D.step(2, 'Nhảy bằng phép chia lấy dư')
    D.kbox('ĐỊNH LÍ (PHẦN TỬ THỨ K)', ['Nếu K < μ thì x_{K} nằm trên đuôi, lấy trực tiếp. Nếu K ≥ μ:', '$eq **x_{K} = x_{μ + (K − μ) mod λ}**'])
    D.step(3, 'Chạy tay với x = 2025, K = 10^{18}')
    D.table(['i', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'], [
        ['x_{i}', '2025', '33', '18', '65', '61', '37', '58', '89', '145', '42', '20', '4', '16', '**37**']],
        widths=[0.6] + [0.62] * 14, sz=18)
    D.p('x_{13} = 37 đã gặp ở chỉ số 5: μ = 5, λ = 13 − 5 = 8. Vì 10^{18} chia hết cho 8 nên (10^{18} − 5) mod 8 = 3, và x_{10^{18}} = x_{5+3} = x_{8} = **145**.')
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của cách tìm ρ.', 13)
    D.code('DAYLAP.CPP: tìm đuôi và chu trình', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi câu hỏi đi tối đa vài trăm bước (đuôi + chu trình trong tập ≤ 1458 giá trị), thực tế chỉ vài chục: 10^{5} câu hỏi chạy khoảng **0,35 giây**. '
                               'Đã đối chiếu với mô phỏng trực tiếp trên hàng nghìn câu hỏi có K ≤ 60.'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Rùa và thỏ (Floyd)')
    D.p('Khi tập giá trị quá lớn để dùng mảng first (ví dụ x tới 10^{18} và f phức tạp), dùng hai con trỏ: rùa đi 1 bước, thỏ đi 2 bước mỗi lượt. Trong chu trình, thỏ sẽ đuổi kịp rùa. '
        'Sau đó đặt rùa về x_{0}, cho cả hai cùng đi 1 bước: chỗ gặp nhau chính là x_{μ}. Cuối cùng đi một vòng để đo λ. Bộ nhớ O(1), thời gian O(μ + λ).')
    D.code('Thuật toán Floyd tìm μ và λ', P.src('ex_floyd.cpp'))
    D.p('Chạy thử: x = 2025 cho μ = 5, λ = 8; x = 7 cho μ = 5, λ = 1 (điểm dừng 1); x = 4 cho μ = 0, λ = 8.')
    D.sub('Mở rộng 2: Hằng số Kaprekar 6174')
    D.p('Với số 4 chữ số (không phải bốn chữ số giống nhau): lấy số lớn nhất ghép từ các chữ số trừ số nhỏ nhất (giữ đủ 4 chữ số, kể cả số 0 ở đầu). Lặp lại, dãy **luôn** về 6174 sau không quá 7 bước.')
    D.fig(P.fig('kaprekar'), 'Dãy Kaprekar bắt đầu từ 2026.', 15.2)
    D.code('Đếm số bước về 6174 của mọi số 4 chữ số', P.src('ex_kaprekar.cpp'))
    D.p('Kết quả chạy: 356 số cần 1 bước, 519 số cần 2 bước, ..., 1980 số cần đủ 7 bước (cộng với chính 6174 là 8991 số, đúng bằng 9000 trừ 9 số dạng aaaa). '
        'Với 3 chữ số, điểm dừng là 495; với nhiều chữ số hơn, dãy rơi vào các chu trình: lại là hình ρ.')
    D.sub('Mở rộng 3: Dãy Collatz')
    D.p('x chẵn thì chia 2, x lẻ thì nhân 3 cộng 1. Người ta tin rằng mọi dãy đều về 1 (giả thuyết Collatz) nhưng chưa ai chứng minh được. Khác với dãy tổng bình phương chữ số, giá trị có thể tăng rất cao '
        '(27 lên tới 9232 rồi mới về 1 sau 111 bước), nên khi mô phỏng phải dùng long long và đặt giới hạn số bước.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Lệch một khi đi trước một bước:** nhớ trừ K đi 1, và xử lí riêng K = 0.',
        '- **Dùng (K mod λ) thay cho (K − μ) mod λ:** sai khi μ > 0.',
        '- **Mảng first quá nhỏ:** phải đủ cho mọi giá trị có thể sau bước đầu (≤ 1458 với x ≤ 10^{18}).',
        '- **K < μ:** phần tử nằm trên đuôi, không được dùng công thức chu kì.'])
    D.kbox('GHI NHỚ', [
        '- Dãy lặp trên tập hữu hạn luôn có dạng ρ: đuôi μ, chu trình λ.',
        '- x_{K} = x_{μ + (K − μ) mod λ} với K ≥ μ.',
        '- Tìm ρ bằng mảng "lần đầu gặp" (khi tập giá trị nhỏ) hoặc bằng rùa và thỏ (bộ nhớ O(1)).',
        '- Số hạnh phúc: dãy tổng bình phương chữ số về 1; các số còn lại rơi vào vòng 4 → 16 → ... → 20 → 4.'])
    D.luyentap([('11.1', 'SỐ HẠNH PHÚC', 'Đếm số hạnh phúc trong [1, N] với N ≤ 10^{7}: tính sẵn cho các giá trị ≤ 567 rồi tra bảng (với N tới 10^{18} cần quy hoạch động chữ số, Bài 15).'),
                ('11.2', 'KAPREKAR', 'Số bước để dãy Kaprekar k chữ số (k ≤ 9) bắt đầu từ x đi vào chu trình, và độ dài chu trình: Mở rộng 1, 2.'),
                ('11.3', 'COLLATZ', 'Trong [1, N] (N ≤ 10^{6}), số nào có dãy Collatz dài nhất? Ghi nhớ kết quả của các số nhỏ để tránh tính lại.')])
    D.tukiemtra([('Số 2026 có phải số hạnh phúc không?', 'có: 2026 → 44 → 32 → 13 → 10 → 1'), ('Dãy bắt đầu từ 4: x_{10^{18}} bằng bao nhiêu?', 'μ = 0, λ = 8, 10^{18} mod 8 = 0: x = 4'),
                 ('Dãy Kaprekar bắt đầu từ 3524?', '3524 → 3087 → 8352 → 6174'), ('Vì sao chỉ cần mảng first cỡ 2000?', 'sau một bước, mọi giá trị không vượt quá 18 · 81 = 1458')])
