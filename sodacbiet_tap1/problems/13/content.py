def build(D, P):
    D.objectives([
        'Ghép các chữ số cho trước thành số lớn nhất, số nhỏ nhất (không có chữ số 0 ở đầu).',
        'Hiểu vì sao với cùng số chữ số, so sánh số chính là so sánh **thứ tự từ điển** của xâu chữ số.',
        'Tìm số nhỏ nhất lớn hơn n có cùng các chữ số với n (**hoán vị kế tiếp**) trong O(L), kể cả khi n dài 10^{6} chữ số, và chứng minh vì sao đúng.',
        'Dựng số nhỏ nhất có tổng chữ số cho trước bằng tham lam.'])
    D.kbox('KHỞI ĐỘNG', [
        'Biển số xe của bố là 2026. Bé Na thích các số "na ná" biển số bố: dùng đúng các chữ số 2, 0, 2, 6. Số lớn nhất như vậy là 6220, số nhỏ nhất là 2026 (không được bắt đầu bằng 0). '
        'Và số **ngay sau** 2026 trong dãy các số như vậy là 2062.',
        'Với 4 chữ số, em có thể liệt kê hết. Nhưng nếu n dài một triệu chữ số thì sao? Bài học này cho em một thuật toán ba bước chạy trong một lượt quét.'])

    D.h('1. Số lớn nhất, số nhỏ nhất từ các chữ số')
    D.kbox('ĐỊNH LÍ (SO SÁNH HAI SỐ CÙNG ĐỘ DÀI)', ['Với hai số có cùng số chữ số, số nào có chữ số đầu tiên khác nhau lớn hơn thì lớn hơn. Nói cách khác, **so sánh số = so sánh xâu theo thứ tự từ điển** khi hai xâu dài bằng nhau.'])
    D.kbox('VÌ SAO ĐÚNG?', ['Nếu hai số giống nhau ở các chữ số đầu và khác nhau lần đầu ở vị trí có giá trị 10^{i}, chênh lệch ở vị trí đó ít nhất 10^{i}, '
                            'trong khi mọi chữ số phía sau cộng lại chênh lệch không quá 9 · (10^{i−1} + ... + 1) = 10^{i} − 1. Chữ số bên trái "thắng" mọi chữ số bên phải.'])
    D.p('Hệ quả: số lớn nhất ghép từ một tập chữ số là các chữ số **xếp giảm dần**; số nhỏ nhất là các chữ số xếp tăng dần, nhưng nếu có chữ số 0 thì đổi chữ số khác 0 nhỏ nhất lên đầu '
        '(2, 0, 2, 6 → 0226 → **2026**). Đây cũng là bước "sắp giảm − sắp tăng" của dãy Kaprekar ở Bài 11.')

    D.h('2. Bài toán KETIEP')
    D.problem_box('KETIEP', 'Cho số nguyên dương n. Hãy tìm số nhỏ nhất **lớn hơn n** được viết bằng đúng các chữ số của n (mỗi chữ số dùng đúng số lần nó xuất hiện trong n). In −1 nếu không có số nào như vậy.',
                  'Một dòng chứa n, có không quá 10^{6} chữ số, không có chữ số 0 ở đầu.', 'Số tìm được, hoặc −1.')
    D.examples('KETIEP', [('2026', '2062', 'Các số dùng {0, 2, 2, 6} theo thứ tự: 2026, 2062, 2206, ...'), ('4321', '-1', 'Các chữ số đã xếp giảm dần: 4321 là số lớn nhất.'),
                          ('1987654320', '2013456789', 'Đáp số lớn hơn n tới hơn 2,6 · 10^{7}.')])

    D.h('3. Ý tưởng ngây thơ: Tăng dần và so sánh')
    D.p('Thử x = n + 1, n + 2, ...: với mỗi x, sắp xếp các chữ số của x và so với các chữ số (đã sắp xếp) của n. Số đầu tiên khớp là đáp số. Nếu đã vượt sang số có nhiều chữ số hơn mà chưa gặp thì in −1.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách tăng dần.', 12.5)
    D.code('KETIEP.CPP (ngây thơ): tăng n và so sánh tập chữ số', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Số lần thử bằng khoảng cách từ n tới đáp số, có thể rất lớn: với n = 1 987 654 320 cần 2,6 · 10^{7} lần thử (**1,4 giây**); với n = 1 999 999 999 đáp số là 9 199 999 999, '
                               'cách 7,2 · 10^{9}: khoảng **6 phút**. Còn n dài 10^{6} chữ số thì không đọc nổi vào long long.'])
    D.kbox('BẾ TẮC', ['Ta đi qua hàng tỉ số trong khi chỉ cần thay đổi **vài chữ số cuối** của n. Câu hỏi đúng là: phải thay đổi ở vị trí nào, và thay đổi thế nào để số mới lớn hơn n nhưng "lớn hơn ít nhất"?'])

    D.h('4. Phá bế tắc: Hoán vị kế tiếp')
    D.step(1, 'Chữ số nào phải tăng?')
    D.p('Muốn số mới lớn hơn n ít nhất, phải giữ nguyên **phần đầu dài nhất có thể** và chỉ thay đổi phần cuối. Nếu một đoạn cuối của n đã xếp **không tăng** (như 976 trong 534976), '
        'thì đoạn ấy đã là cách xếp lớn nhất của các chữ số của nó: không thể làm số lớn hơn nếu chỉ sắp xếp lại đoạn đó. Vì vậy phải chạm tới chữ số **ngay trước** đuôi không tăng dài nhất: vị trí i.')
    D.step(2, 'Tăng s[i] ít nhất có thể')
    D.p('Thay s[i] bằng chữ số **nhỏ nhất lớn hơn s[i]** trong đuôi (vị trí j, tìm từ phải sang vì đuôi không tăng), rồi đổi chỗ s[i] và s[j]. Đuôi sau khi đổi vẫn không tăng.')
    D.step(3, 'Làm đuôi nhỏ nhất')
    D.p('Phần từ i trở về trước đã lớn hơn n; phần đuôi giờ phải nhỏ nhất có thể: xếp tăng dần. Vì đuôi đang không tăng, chỉ cần **đảo ngược** nó.')
    D.fig(P.fig('steps'), 'Bốn bước tìm hoán vị kế tiếp của 534976.', 15.2)
    D.kbox('VÌ SAO ĐÚNG?', [
        'Mọi số lớn hơn n dùng cùng chữ số phải khác n ở một vị trí ≤ i (đuôi sau i đã lớn nhất). Muốn nhỏ nhất, vị trí khác đầu tiên phải là **đúng i** (càng về phải càng tốt), '
        'chữ số mới ở i phải là chữ số nhỏ nhất > s[i] lấy được từ đuôi, và phần sau phải xếp tăng dần. Thuật toán làm đúng ba điều đó. Nếu không có i (cả xâu không tăng) thì n đã lớn nhất: in −1.',
        'Chữ số 0 không gây phiền: i luôn có s[i] < s[i + 1] nên chữ số mới ở vị trí i lớn hơn chữ số cũ, chữ số đầu của số không bao giờ thành 0.'])
    D.step(4, 'Chạy tay với n = 2026')
    D.p('Đuôi không tăng dài nhất là "6" (vì 2 < 6): i chỉ vào chữ số 2 thứ hai. Chữ số nhỏ nhất > 2 trong đuôi là 6: đổi chỗ được 2062; đuôi "2" đảo ngược vẫn là "2". Đáp số **2062**.')
    D.step(5, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của thuật toán hoán vị kế tiếp.', 12)
    D.code('KETIEP.CPP: hoán vị kế tiếp', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Ba lượt quét xâu: O(L). Với L = 10^{6}, chương trình chạy khoảng **0,03 giây**, chủ yếu là đọc ghi. Đã đối chiếu với cách liệt kê mọi hoán vị trên các số tới 7 chữ số. '
                               'Thư viện C++ có sẵn hàm next_permutation làm đúng việc này.'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Số nhỏ nhất có k chữ số và tổng chữ số S')
    D.p('Tham lam từ hàng đơn vị: đặt vào mỗi vị trí phía phải chữ số lớn nhất có thể (tối đa 9), nhưng luôn chừa lại ít nhất 1 cho chữ số đầu. Chữ số đầu nhận phần còn lại. '
        'Ví dụ k = 4, S = 10 cho 1009. Không có nghiệm khi S < 1 hoặc S > 9k.')
    D.code('Số nhỏ nhất có k chữ số và tổng chữ số S', P.src('ex_minsum.cpp'))
    D.sub('Mở rộng 2: Số nhỏ nhất có tích chữ số bằng P')
    D.p('Tách P thành các thừa số từ 9 xuống 2 (chia cho 9 nhiều nhất có thể, rồi 8, ..., rồi 2); nếu còn dư thừa số nguyên tố > 7 thì vô nghiệm. Xếp các chữ số tăng dần. '
        'Ví dụ P = 100 = 4 · 5 · 5 → 455. Chia cho số lớn trước để có **ít chữ số nhất** (số ít chữ số hơn thì nhỏ hơn).')
    D.sub('Mở rộng 3: Hoán vị thứ k')
    D.p('Có bao nhiêu số dùng đúng một tập chữ số? Với tập có c_{d} chữ số d, số hoán vị là L! / (c_{0}! · c_{1}! · ... · c_{9}!) (trừ đi các hoán vị bắt đầu bằng 0). '
        'Để tìm hoán vị thứ k theo thứ tự tăng, dựng từng chữ số từ trái: thử lần lượt các chữ số, đếm số hoán vị của phần còn lại, trừ dần k: đúng kĩ thuật "dựng số thứ k" sẽ gặp lại ở Bài 15, 16.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **So sánh số dạng xâu khác độ dài** bằng toán tử <: "9" > "10". Ở bài này mọi hoán vị cùng độ dài nên an toàn.',
        '- **Dùng ≤ / ≥ sai** khi tìm i và j: phải bỏ qua cả các chữ số **bằng nhau** (s[i] >= s[i+1], s[j] <= s[i]).',
        '- **Sắp xếp đuôi** thay vì đảo ngược: vẫn đúng nhưng O(L log L).',
        '- **Số nhỏ nhất có chữ số 0:** đừng để 0 đứng đầu.'])
    D.kbox('GHI NHỚ', [
        '- Cùng độ dài: so sánh số = so sánh xâu. Chữ số bên trái quan trọng hơn mọi chữ số bên phải cộng lại.',
        '- Hoán vị kế tiếp: tìm i trước đuôi không tăng; đổi với chữ số nhỏ nhất lớn hơn trong đuôi; đảo đuôi. O(L).',
        '- Dựng số nhỏ nhất/lớn nhất theo ràng buộc: tham lam từng vị trí, ưu tiên vị trí bên trái.'])
    D.luyentap([('13.1', 'BIỂN SỐ', 'Số lớn nhất và nhỏ nhất ghép từ các chữ số của n, và hiệu của chúng: sắp xếp, cẩn thận chữ số 0.'),
                ('13.2', 'KẾ TRƯỚC', 'Số lớn nhất nhỏ hơn n có cùng các chữ số (không có chữ số 0 ở đầu): hoán vị kế trước, kiểm tra chữ số đầu.'),
                ('13.3', 'TỔNG VÀ TÍCH', 'Số nhỏ nhất có k chữ số với tổng S, và số nhỏ nhất có tích chữ số P (P ≤ 10^{18}): Mở rộng 1, 2.')])
    D.tukiemtra([('Hoán vị kế tiếp của 115?', '151'), ('Hoán vị kế tiếp của 12 543?', '13 245'), ('Số nhỏ nhất có 3 chữ số, tổng chữ số 27?', '999'),
                 ('Số nhỏ nhất có tích chữ số 36?', '49 (36 = 9 · 4)')])
