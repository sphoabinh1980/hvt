def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Đèn i nháy ở các bội của t_{i}; các đèn l..r cùng nháy ở các bội chung của t_{l}, ..., t_{r}, lần đầu tiên ở **BCNN** của chúng. '
        'Vậy mỗi kịch bản hỏi lcm(t_{l..r}), và in −1 nếu nó vượt 10^{18}.')
    D.fig(P.fig('blink'), 'Ba đèn với chu kì 2, 3, 4 cùng nháy lần đầu ở giây 12.', 15)
    D.p('Hai khó khăn: (1) BCNN của hai số ≤ 10^{18} có thể tới gần 10^{36}, phải phát hiện "vượt 10^{18}" mà không tràn số; '
        '(2) có tới 2 · 10^{5} kịch bản trên dãy 2 · 10^{5} đèn.')
    D.sub('Công cụ: BCNN có chặn trên')
    D.p('Ta quy ước một giá trị đặc biệt INF = 10^{18} + 1 nghĩa là "đã vượt 10^{18}". Hàm lcm(a, b): nếu một trong hai là INF thì trả về INF; '
        'ngược lại x = a / gcd(a, b) (chia trước), và nếu x > ⌊10^{18} / b⌋ thì x · b > 10^{18}: trả về INF; còn lại trả về x · b. '
        'Mọi phép tính đều nằm trong long long. Một khi BCNN đã vượt 10^{18}, thêm đèn nào cũng vẫn vượt: INF "hút" mọi thứ.')

    D.h('2. Cách ngây thơ: Tính lại cho mỗi kịch bản')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ', 12)
    D.code('Cách ngây thơ: O(n) lần gọi lcm cho mỗi kịch bản', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n · Q · log) trường hợp xấu nhất: 4 · 10^{10} lần gọi lcm khi n = Q = 2 · 10^{5}. Dừng sớm khi gặp INF giúp được '
        'những test có số lớn, nhưng với các đèn chu kì nhỏ (1, 2, 3, 4, 6, 12...) BCNN không bao giờ vượt ngưỡng và vòng lặp phải chạy hết.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (n, Q ≤ 2000): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               '**Subtask 2** (l = 1): BCNN tiền tố pre[r] = lcm(pre[r − 1], t_{r}) trả lời mỗi kịch bản trong O(1). '
               'Chương trình `mid.cpp` thêm đúng nhánh này: **' + S('mid.cpp') + ' điểm**.',
               '**Subtask 3**: không có phép "trừ" cho BCNN (không thể suy lcm(t_{l..r}) từ pre[r] và pre[l − 1]), nên mẹo tiền tố không dùng được.'])
    D.box('red', 'ĐIỂM BẾ TẮC', [
        'Có tới n(n + 1)/2 ≈ 2 · 10^{10} đoạn [l, r], nhưng với mỗi r cố định, các giá trị lcm(t_{l..r}) **rất ít khác nhau**. '
        'Nếu biết nén chúng lại, ta trả lời được mọi kịch bản có cùng r một lúc.'])

    D.h('4. Phá bế tắc: Ít giá trị khác nhau')
    D.sub('Quan sát then chốt')
    D.p('Cố định r và cho l giảm dần từ r về 1. Đoạn [l, r] chứa đoạn [l + 1, r], nên lcm(t_{l..r}) là **bội** của lcm(t_{l+1..r}). '
        'Hoặc hai giá trị bằng nhau, hoặc giá trị mới là một bội thật sự, tức **ít nhất gấp đôi**. Vì 2^{60} > 10^{18}, chỉ có không quá 61 giá trị khác nhau '
        'không vượt 10^{18}, cộng thêm giá trị INF.')
    D.fig(P.fig('segs'), 'Dãy t = 6, 4, 3, 10, 2, 9, 5, 8 và bảng lcm(t[l..r]) với r = 5, 6, 8. Mỗi hàng chỉ có vài khối cùng giá trị.', 15)
    D.sub('Duy trì danh sách khối khi r tăng')
    D.p('Lưu danh sách seg các cặp (giá trị, lo), xếp theo lo giảm dần: cặp (v, lo) nghĩa là với mọi l từ lo tới (lo của cặp đứng trước) − 1, lcm(t_{l..r}) = v. '
        'Khi chuyển từ r − 1 sang r:')
    D.nums(['Khối mới nhất là (t_{r}, r): đoạn chỉ gồm đèn r.',
            'Mỗi cặp cũ (v, lo) trở thành (lcm(v, t_{r}), lo), vì thêm đèn r vào mọi đoạn [l, r − 1].',
            'Hai khối liền nhau có cùng giá trị thì **gộp** lại (giữ lo nhỏ hơn). Nhờ đó danh sách luôn ngắn (≤ 62 cặp).'])
    D.p('Để trả lời kịch bản (l, r), ta đọc hết kịch bản trước, gom theo r (**xử lí ngoại tuyến**); ngay sau khi cập nhật danh sách cho r, '
        'mỗi kịch bản (l, r) lấy giá trị của cặp đầu tiên có lo ≤ l.')
    D.box('purple', 'VÌ SAO DANH SÁCH NGẮN?', [
        'Các giá trị trong danh sách (theo thứ tự lo giảm dần) là một dãy mà mỗi số là bội thật sự của số trước, nên tăng ít nhất gấp đôi: '
        'v_{1} ≥ 1, v_{2} ≥ 2, ..., v_{k} ≥ 2^{k − 1}. Nếu v_{k} ≤ 10^{18} thì k ≤ 60 + 1. Mọi giá trị vượt 10^{18} đều bị gộp vào một khối INF.'])
    D.sub('Chạy tay')
    D.p('Với t = 6, 4, 3, 10, 2 (r = 5) danh sách là (2, 5), (10, 4), (30, 3), (60, 1): giá trị 60 của l = 1 và l = 2 đã được gộp. '
        'Thêm đèn 6 với t_{6} = 9: (9, 6), lcm(2, 9) = 18 → (18, 5), lcm(10, 9) = 90 → (90, 4), lcm(30, 9) = 90 trùng → gộp thành (90, 3), '
        'lcm(60, 9) = 180 → (180, 1). Kịch bản (2, 6) lấy cặp đầu tiên có lo ≤ 2: (180, 1), đáp số 180 = lcm(4, 3, 10, 2, 9).')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 13)
    D.code('DENNHAY.CPP: quét r, nén các khối cùng BCNN', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** mỗi r cập nhật ≤ 62 cặp (mỗi cặp một lần gcd), mỗi kịch bản duyệt ≤ 62 cặp: tổng O((n + Q) · 62 · log), '
        'khoảng 1,2 · 10^{7} lần gọi gcd. Bộ nhớ O(n + Q).')
    D.box('blue', 'MỞ RỘNG: BẢNG THƯA (SPARSE TABLE)', [
        'BCNN có hai tính chất: kết hợp và **lũy đẳng** (lcm(x, x) = x), nên lcm(t_{l..r}) = lcm(A, B) với A, B là BCNN của hai đoạn độ dài 2^{k} phủ [l, r] '
        '(có thể chồng lên nhau). Dựng bảng st[k][i] = lcm của 2^{k} phần tử từ i trong O(n log n), mỗi kịch bản trả lời trực tuyến trong O(1). '
        'Cách này dùng được cho gcd, min, max; không dùng được cho tổng (vì phần chồng bị cộng hai lần).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Tràn số khi nhân:** kiểm tra x > LIM / b **trước** khi nhân. Viết x * b > LIM là đã tràn rồi mới so sánh.',
               '**Quên INF là "hút":** lcm(INF, b) phải là INF; nếu để INF tham gia vào gcd, giá trị thu được vô nghĩa.',
               '**Giá trị đúng bằng 10^{18}:** vẫn in ra (ví dụ 2, kịch bản 4). Điều kiện vượt là "> 10^{18}", không phải "≥".',
               '**Trả lời sai thứ tự:** xử lí ngoại tuyến xong phải in theo thứ tự ban đầu; lưu số thứ tự của từng kịch bản.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
