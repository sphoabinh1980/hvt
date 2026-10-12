def build(D, P):
    D.objectives([
        'Đếm số chữ số của một số khổng lồ (như 2^{2026} hay 10^{6}!) mà không cần viết số ấy ra, nhờ **logarit thập phân**.',
        'Hiểu **phần nguyên** và **phần lẻ** của log_{10} n nói gì: phần nguyên cho số chữ số, phần lẻ cho các chữ số đầu.',
        'Tìm k chữ số đầu và k chữ số cuối của a^{b} với a, b tới 10^{9} trong O(log b).',
        'Biết giới hạn độ chính xác của số thực, và vì sao chữ số đầu "thích" là chữ số 1 (định luật Benford).'])
    D.kbox('KHỞI ĐỘNG', [
        'Số 2^{2026} lớn đến mức nếu in ra giấy với cỡ chữ thường thì dài gần hai trang. Nhưng không cần in, em vẫn có thể trả lời ngay: nó có **610** chữ số, '
        'bắt đầu bằng **770...** và kết thúc bằng **...864**.',
        'Chữ số cuối thì quen thuộc: chỉ cần lấy dư cho 1000. Còn chữ số đầu và số chữ số? Phép chia lấy dư không giúp được gì, vì chữ số đầu nằm "ở đầu kia" của con số. '
        'Bài học này dùng một công cụ khác: logarit.'])

    D.h('1. Số chữ số và logarit thập phân')
    D.p('Logarit thập phân của một số dương n, kí hiệu log_{10} n, là số mũ x sao cho 10^{x} = n: log_{10} 1000 = 3, log_{10} 2 ≈ 0,30103. '
        'Logarit biến phép nhân thành phép cộng và lũy thừa thành phép nhân: log_{10}(a · b) = log_{10} a + log_{10} b và log_{10}(a^{b}) = b · log_{10} a.')
    D.kbox('ĐỊNH LÍ (SỐ CHỮ SỐ)', [
        'Với mọi số nguyên n ≥ 1:',
        '$eq **len(n) = ⌊log_{10} n⌋ + 1**',
        'Hệ quả: len(a^{b}) = ⌊b · log_{10} a⌋ + 1 và len(n!) = ⌊log_{10} 1 + log_{10} 2 + ... + log_{10} n⌋ + 1.'])
    D.kbox('VÌ SAO ĐÚNG?', ['n có k chữ số khi và chỉ khi 10^{k−1} ≤ n < 10^{k}. Lấy log_{10} ba vế (hàm log_{10} đồng biến): k − 1 ≤ log_{10} n < k, tức ⌊log_{10} n⌋ = k − 1.'])
    D.kbox('VÍ DỤ', ['- 2^{100}: 100 · log_{10} 2 = 30,103 nên 2^{100} có 31 chữ số.',
                     '- 25! = 15 511 210 043 330 985 984 000 000: tổng log_{10} của 2..25 bằng 25,19 nên 25! có 26 chữ số.',
                     '- 10^{6}! có 5 565 709 chữ số, 10^{7}! có 65 657 060 chữ số (chương trình dưới đây, đã đối chiếu với phép tính chính xác).'])
    D.code('Số chữ số của n! bằng tổng logarit', P.src('ex_fact.cpp'))
    D.table(['n', '10', '100', '1000', '10⁶', '10⁷'], [['len(n!)', '7', '158', '2568', '5 565 709', '65 657 060']], widths=[1.2, 1, 1, 1, 1.6, 1.6], sz=20)
    D.kbox('LƯU Ý: SỐ THỰC KHÔNG CHÍNH XÁC TUYỆT ĐỐI', [
        'log10 trả về số thực, có sai số làm tròn rất nhỏ. Với n = 1000, log10(1000) có thể là 2,9999999999999996 và ⌊...⌋ cho 2 thay vì 3. '
        'Vì vậy: với số nguyên vừa long long, hãy đếm chữ số bằng vòng chia 10 (Bài 1); chỉ dùng logarit cho những số **không viết ra được** như a^{b}, n!. '
        'Dùng long double (khoảng 19 chữ số có nghĩa) thay cho double (khoảng 16).'])

    D.h('2. Chữ số đầu nằm trong phần lẻ')
    D.p('Viết x = log_{10} n = ⌊x⌋ + {x}, với {x} = x − ⌊x⌋ ∈ [0, 1) là **phần lẻ**. Khi đó')
    D.eq('n = 10^{x} = 10^{⌊x⌋} · 10^{{x}},    1 ≤ 10^{{x}} < 10')
    D.p('Thừa số 10^{⌊x⌋} chỉ dời dấu phẩy, không đổi chữ số nào. Mọi chữ số của n nằm trong số thực 10^{{x}} ∈ [1, 10): đó chính là n viết dưới dạng "một chữ số, dấu phẩy, các chữ số còn lại".')
    D.kbox('ĐỊNH LÍ (k CHỮ SỐ ĐẦU)', ['Nếu n có ít nhất k chữ số thì số tạo bởi k chữ số đầu của n là', '$eq **⌊10^{{x} + k − 1}⌋**,   x = log_{10} n.'])
    D.fig(P.fig('mantissa'), '2¹⁰⁰: phần nguyên của x cho số chữ số, phần lẻ cho các chữ số đầu.', 15.2)

    D.h('3. Bài toán DAUCUOI')
    D.problem_box('DAUCUOI', 'Cho T cặp số a, b. Với mỗi cặp, hãy in 3 chữ số đầu và 3 chữ số cuối của a^{b}.',
                  'Dòng đầu chứa T (T ≤ 1000). Mỗi dòng tiếp theo chứa a, b (2 ≤ a ≤ 10^{9}, 1 ≤ b ≤ 10^{9}); bảo đảm a^{b} có ít nhất 6 chữ số.',
                  'T dòng, mỗi dòng hai số: 3 chữ số đầu và 3 chữ số cuối (in đủ 3 chữ số, kể cả số 0 ở đầu).')
    D.examples('DAUCUOI', [('3\n2 100\n10 6\n123456789 1000000000', '126 376\n100 000\n147 001',
                            '2^{100} = 1267650600...205376. 10^{6} = 1000000: ba chữ số cuối là 000 (in đủ 3 chữ số). a^{b} thứ ba có 8 091 514 978 chữ số, không thể viết ra.')])

    D.h('4. Ý tưởng ngây thơ: Tính chính xác aᵇ')
    D.p('Dùng số lớn (mỗi ô 9 chữ số, như bài LUYTHUALON của bộ Số học), nhân b lần với a, đổi ra xâu rồi cắt 3 kí tự đầu, 3 kí tự cuối.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách tính chính xác.', 11)
    D.code('DAUCUOI.CPP (ngây thơ): số lớn', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['a^{b} có khoảng b · log_{10} a chữ số, tức tới 9 · 10^{9} chữ số: chỉ riêng việc lưu đã cần 4 GB. Lần nhân thứ k làm việc trên khoảng k · log_{10} a / 9 ô, '
                               'tổng cộng O(b^{2}). Đo thực tế với a = 999 999 999: b = 10^{4} mất **0,14 giây**, b = 3 · 10^{4} mất **1,16 giây**, b = 10^{5} mất **12,9 giây**. '
                               'Với b = 10^{9}, gấp 10^{8} lần số phép tính của b = 10^{5}: hàng chục năm.'])
    D.kbox('BẾ TẮC', ['Ta tính tất cả 8 tỉ chữ số chỉ để dùng 6 chữ số. Ba chữ số cuối không phụ thuộc vào các chữ số khác (chúng là số dư cho 1000). '
                      'Còn ba chữ số đầu, có cách nào "nhìn" vào đầu số mà không tính phần còn lại không?'])

    D.h('5. Phá bế tắc: Hai đầu, hai công cụ')
    D.step(1, 'Ba chữ số cuối: lấy dư cho 1000')
    D.p('Ba chữ số cuối của a^{b} là a^{b} mod 1000. Theo tính chất đồng dư, ta lấy dư sau mỗi phép nhân, và dùng **lũy thừa nhanh** (bình phương liên tiếp) để chỉ cần khoảng 2 log_{2} b ≈ 60 phép nhân. '
        'Khi in, nhớ in đủ 3 chữ số: 10^{6} mod 1000 = 0 phải in là 000.')
    D.step(2, 'Ba chữ số đầu: phần lẻ của b · log₁₀ a')
    D.p('Theo định lí ở mục 2 với k = 3: ba chữ số đầu là ⌊10^{f + 2}⌋ với f là phần lẻ của x = b · log_{10} a. Không cần biết a^{b}, chỉ cần một phép nhân số thực.')
    D.step(3, 'Chạy tay với a = 2, b = 100')
    D.table(['Đại lượng', 'Giá trị', 'Ý nghĩa'], [
        ['x = 100 · log₁₀ 2', '30,1029995664', ''], ['⌊x⌋', '30', '2^{100} có 31 chữ số'], ['f = x − ⌊x⌋', '0,1029995664', ''],
        ['10^{f + 2}', '126,765060...', 'ba chữ số đầu: **126**'], ['2^{100} mod 1000', '376', 'ba chữ số cuối: **376**']],
        widths=[2.6, 2.4, 3.4], align=['left', 'center', 'left'], sz=20)
    D.p('Đối chiếu: 2^{100} = 1 267 650 600 228 229 401 496 703 205 376.')
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối: hai đầu của aᵇ được tính độc lập.', 13.5)
    D.code('DAUCUOI.CPP: logarit + lũy thừa nhanh', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi cặp (a, b): một phép logarit, một phép lũy thừa số thực, và khoảng 60 phép nhân lấy dư: O(log b). 1000 cặp với b = 10^{9} chạy trong khoảng **0,01 giây**.'])
    D.kbox('VÌ SAO ĐỦ CHÍNH XÁC?', [
        'x = b · log_{10} a tới khoảng 9 · 10^{9}. long double giữ khoảng 19 chữ số có nghĩa, nên phần lẻ f vẫn đúng tới khoảng 10^{−9}, dư sức cho 3 chữ số đầu. '
        'Chương trình đã được đối chiếu với phép tính logarit 80 chữ số (thư viện decimal của Python) trên hàng trăm bộ (a, b) ngẫu nhiên tới 10^{9}.',
        'Chỉ khi 10^{f + 2} rơi **cực sát** một số nguyên (chẳng hạn a^{b} = 1 259 999 999 999...) mới có nguy cơ sai. Muốn lấy nhiều chữ số đầu hơn (k ≥ 10) thì double/long double không còn đủ.'])

    D.h('6. Mở rộng')
    D.sub('Mở rộng 1: Định luật Benford')
    D.p('Trong 1000 số 2^{1}, 2^{2}, ..., 2^{1000}, có 301 số bắt đầu bằng chữ số 1 nhưng chỉ 45 số bắt đầu bằng chữ số 9. Lí do: chữ số đầu là d khi phần lẻ f rơi vào đoạn [log_{10} d, log_{10}(d + 1)), '
        'và các phần lẻ của n · log_{10} 2 rải đều trên [0, 1). Đoạn ứng với chữ số 1 dài log_{10} 2 ≈ 0,301, đoạn ứng với chữ số 9 chỉ dài log_{10}(10/9) ≈ 0,046.')
    D.fig(P.fig('benford'), 'Chữ số đầu của 2¹..2¹⁰⁰⁰ khớp với dự đoán log₁₀(1 + 1/d).', 14)
    D.sub('Mở rộng 2: Chữ số đầu của n! và của số Fibonacci')
    D.p('Với n!, cộng dồn log_{10} i (hoặc dùng hàm lgammal(n + 1) / ln 10). Với số Fibonacci, công thức Binet cho log_{10} F_{n} ≈ n · log_{10} φ − log_{10} √5 với φ = (1 + √5)/2, '
        'sai số giảm rất nhanh khi n tăng. Nhờ đó tìm được số Fibonacci đầu tiên có 1000 chữ số là F_{4782} mà không cần số lớn.')
    D.sub('Mở rộng 3: k chữ số cuối với k lớn')
    D.p('k chữ số cuối là a^{b} mod 10^{k}. Với k ≤ 9, tích hai số dư < 10^{18} vừa long long; với k tới 18 phải nhân bằng __int128. '
        'Cẩn thận: nếu a^{b} có ít hơn k chữ số thì "k chữ số cuối" chính là cả số, không được thêm số 0 vào đầu. Đề bài DAUCUOI tránh trường hợp này bằng cam kết a^{b} có ít nhất 6 chữ số.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Quên in đủ chữ số cuối:** 10^{6} mod 1000 = 0 phải in 000 (printf("%03lld")).',
        '- **Dùng double cho x lớn:** x tới 9 · 10^{9} chiếm hết phần lớn độ chính xác của double, phần lẻ sai từ chữ số thứ 6–7.',
        '- **Dùng logarit để đếm chữ số của số nhỏ:** log10(1000) có thể cho 2,999999...; hãy dùng vòng chia 10.',
        '- **Lũy thừa mod 1000 không lấy dư a trước:** a tới 10^{9}, a · a tới 10^{18} vẫn vừa long long nhưng chỉ vừa sát; lấy a %= 1000 trước cho an toàn.'])
    D.kbox('GHI NHỚ', [
        '- len(n) = ⌊log_{10} n⌋ + 1; len(a^{b}) = ⌊b · log_{10} a⌋ + 1; len(n!) = ⌊Σ log_{10} i⌋ + 1.',
        '- k chữ số đầu = ⌊10^{{x} + k − 1}⌋ với x = log_{10} n: phần lẻ quyết định chữ số đầu.',
        '- k chữ số cuối = n mod 10^{k}: dùng lũy thừa nhanh, in đủ k chữ số.',
        '- Số thực chỉ đủ tin cậy cho khoảng 15–18 chữ số có nghĩa: tính toán bằng long double và kiểm tra trường hợp sát biên.'])
    D.luyentap([('2.1', 'ĐỘ DÀI GIAI THỪA', 'Q truy vấn số chữ số của n! (n ≤ 10^{7}): tính sẵn tổng tiền tố của log_{10} i.'),
                ('2.2', 'ĐẦU VÀ CUỐI', 'k chữ số đầu và k chữ số cuối của a^{b} với k ≤ 9; xử lí trường hợp a^{b} có ít hơn 2k chữ số.'),
                ('2.3', 'FIBONACCI DÀI', 'Chỉ số của số Fibonacci đầu tiên có ít nhất k chữ số (k ≤ 10^{6}): công thức Binet và logarit.')])
    D.tukiemtra([('3^{2026} có bao nhiêu chữ số? Ba chữ số đầu và ba chữ số cuối là gì?', '967 chữ số, bắt đầu bằng 444, kết thúc bằng 329'),
                 ('7^{77} có bao nhiêu chữ số?', '⌊77 · 0,845098⌋ + 1 = 66'),
                 ('Vì sao chữ số đầu của 2^{n} không bao giờ "đứng yên" ở một giá trị khi n tăng?', 'mỗi lần nhân 2, phần lẻ tăng thêm log_{10} 2 ≈ 0,301 (lấy phần lẻ), không bao giờ lặp lại vì log_{10} 2 là số vô tỉ'),
                 ('Trong 2^{1}, ..., 2^{1000} có bao nhiêu số bắt đầu bằng chữ số 1?', '301')])
