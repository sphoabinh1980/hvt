def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Đèn i nháy ở các thời điểm a_{i} + k·p_{i} (k ≥ 0). Thời điểm t là lần nháy chung khi và chỉ khi **ba** điều kiện cùng đúng:')
    D.eq('**t ≡ a_{1} (mod p_{1}),   t ≡ a_{2} (mod p_{2}),   t ≥ max(a_{1}, a_{2}).**')
    D.p('Hai điều kiện đầu là một hệ đồng dư với hai mô-đun **có thể có ước chung**; điều kiện thứ ba nằm ngoài thế giới đồng dư và rất dễ bị quên.')
    D.fig(P.fig('lights'), 'Câu hỏi 1 và 3 của ví dụ 1. Ở câu 3, giây 6 thỏa cả hai đồng dư nhưng đèn 1 chưa bật.', 15)

    D.h('2. Cách ngây thơ: Mô phỏng')
    D.p('Giữ thời điểm nháy kế tiếp của mỗi đèn, luôn tăng thời điểm nhỏ hơn, dừng khi hai thời điểm bằng nhau. Sau mốc max(a_{1}, a_{2}) + p_{1}p_{2} thì mọi thứ lặp lại, nên nếu vượt mốc ấy mà chưa gặp thì in −1.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách mô phỏng', 13)
    D.code('Cách ngây thơ: mô phỏng hai dãy thời điểm', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** khoảng |a_{1} − a_{2}|/min(p_{1}, p_{2}) bước để "đuổi kịp", cộng tới (p_{1} + p_{2})/g bước trong một chu kì lcm: ổn với các số ≤ 1000, quá chậm khi p tới 10^{9} hay a tới 10^{18}.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (≤ 1000): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.'])
    D.p('Giải hệ đồng dư bằng cách gộp (Bài 12) cho r ∈ [0, lcm) rồi in r: chương trình `nogate.cpp`. Ở subtask 2 (a_{i} < p_{i}) điều này đúng vì r ≡ a_{i} và r ≥ 0 kéo theo r ≥ a_{i}. '
        'Nhưng khi a_{i} lớn (subtask 1, 3), r có thể nhỏ hơn thời điểm bật đèn, như giây 6 ở câu 3: **' + S('nogate.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Cần (1) gộp hai phương trình khi mô-đun có ước chung, và (2) chọn đúng nghiệm thỏa điều kiện "đã bật".'])

    D.h('4. Phá bế tắc')
    D.sub('Gộp hai phương trình tổng quát')
    D.p('Đặt r_{i} = a_{i} mod p_{i}, g = gcd(p_{1}, p_{2}). t = r_{1} + p_{1}·s thỏa phương trình thứ hai khi p_{1}·s ≡ r_{2} − r_{1} (mod p_{2}): '
        'có nghiệm ⇔ **g | (r_{2} − r_{1})** (ở câu 2: g = 2, r_{2} − r_{1} = 1, vô nghiệm, giống như "giây lẻ" và "giây chẵn"). Khi có nghiệm, '
        's ≡ (r_{2} − r_{1})/g · (p_{1}/g)^{−1} (mod p_{2}/g), và t ≡ r (mod L) với r = r_{1} + p_{1}·s, L = lcm(p_{1}, p_{2}) = p_{1}/g · p_{2}.')
    D.sub('Điều kiện "đã bật"')
    D.p('Đặt A = max(a_{1}, a_{2}). Nghiệm nhỏ nhất ≥ A của lớp r (mod L) là **A + ((r − A) mod L)**, giống bài 12.1.')
    D.table(['Câu', 'r₁, r₂', 'g', 'r (mod L)', 'A', 'Đáp số'], [['1', '2, 3', '1', '8 (mod 15)', '3', '**8**'], ['2', '1, 2', '2', 'vô nghiệm', '–', '**−1**'], ['3', '2, 0', '2', '6 (mod 12)', '10', '10 + (−4 mod 12) = **18**']],
            widths=[0.6, 1, 0.6, 1.5, 0.6, 2.4])
    D.box('purple', 'ƯỚC LƯỢNG', ['L = lcm ≤ p_{1}p_{2} ≤ 10^{18}; r < L; đáp số < A + L ≤ 2 · 10^{18}: vừa long long. Không được cộng thêm gì "cho chắc" vì A đã tới 10^{18}.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 14)
    D.code('HAIDEN.CPP: gộp hai đồng dư tổng quát', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(log p) mỗi câu hỏi.')
    D.box('blue', 'MỞ RỘNG', ['Hàm "gộp (r₁, m₁) với (r₂, m₂)" ở đây là phiên bản tổng quát (mô-đun có ước chung). Gộp lần lượt nhiều phương trình bằng hàm này là lời giải của bài LỊCH CAN CHI (12.3).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Quên điều kiện t ≥ max(a₁, a₂).**', '**Không lấy a mod p trước:** a tới 10^{18}, r₁ + p₁·s có thể tràn.', '**Dùng tích p₁·p₂ thay cho lcm:** bỏ sót nghiệm khi p₁, p₂ có ước chung.', '**Quên trường hợp vô nghiệm.**'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'nogate.cpp', 'opt.cpp'])
