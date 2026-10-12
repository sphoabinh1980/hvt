def build(D, P):
    D.objectives([
        'Chứng minh rằng mọi số nguyên dương n đều có một bội chỉ gồm chữ số 0 và 1, dài không quá n chữ số (**nguyên lí Dirichlet**).',
        'Hiểu vì sao để tìm một số có tính chất về số dư, ta chỉ cần nhớ **số dư** chứ không cần nhớ cả số.',
        'Tìm bội nhỏ nhất của n chỉ gồm chữ số 0 và 1 bằng **tìm kiếm theo chiều rộng (BFS) trên đồ thị số dư**, trong O(n).',
        'Mở rộng cho tập chữ số bất kì, và cho các ràng buộc thêm như tổng chữ số.'])
    D.kbox('KHỞI ĐỘNG', [
        'Một chiếc máy tính đời cũ chỉ in được hai chữ số 0 và 1. Thầy giáo đố: "Hãy in ra một bội của 2026." Số 2026 · 1 = 2026 không in được, 2026 · 5 = 10 130 có chữ số 3...',
        'Có chắc là luôn tìm được không? Và bội **nhỏ nhất** như vậy là bao nhiêu? Với 2026 đáp số là 100 001 101 010 = 2026 · 49 358 885. Với n = 999 999, đáp số có 54 chữ số. '
        'Bài học này giới thiệu một cách nghĩ rất mạnh: **đi tìm một số bằng cách đi trên các số dư của nó**.'])

    D.h('1. Luôn tồn tại một bội như vậy')
    D.kbox('ĐỊNH LÍ', ['Với mọi số nguyên dương n, tồn tại một bội dương của n chỉ gồm chữ số 0 và 1, có không quá n chữ số.'])
    D.kbox('VÌ SAO ĐÚNG?', [
        'Xét n số 1, 11, 111, ..., 11...1 (n chữ số 1). Nếu có số chia hết cho n, xong. Nếu không, n số này chỉ nhận n − 1 số dư khác 0, nên theo **nguyên lí Dirichlet** (n con chim, n − 1 cái lồng) '
        'có hai số cùng số dư, chẳng hạn số có i chữ số 1 và số có j chữ số 1 (i > j). Hiệu của chúng là 11...100...0 (i − j chữ số 1, j chữ số 0): chia hết cho n và chỉ gồm 0, 1.'])
    D.fig(P.fig('pigeon'), 'Với n = 7: số dư của 1, 11, 111, ... cho 7; ở đây 111111 chia hết cho 7 luôn.', 15)

    D.h('2. Bài toán BOI01')
    D.problem_box('BOI01', 'Cho số nguyên dương n. Hãy tìm bội dương nhỏ nhất của n mà mọi chữ số đều là 0 hoặc 1.',
                  'Một số nguyên n (1 ≤ n ≤ 10^{6}).', 'Bội tìm được, viết trong hệ thập phân (có thể dài tới hàng chục, hàng trăm chữ số).')
    D.examples('BOI01', [('3', '111', '10 không chia hết cho 3; 11 cũng không; 111 = 3 · 37.'), ('12', '11100', '= 12 · 925. Được chạy tay ở mục 4.'),
                         ('2026', '100001101010', '= 2026 · 49 358 885.')])

    D.h('3. Ý tưởng ngây thơ: Thử các số 0/1 theo thứ tự tăng dần')
    D.p('Các số chỉ gồm chữ số 0 và 1, xếp tăng dần, là 1, 10, 11, 100, 101, 110, 111, ...: chính là biểu diễn **nhị phân** của k = 1, 2, 3, ... nhưng đọc như số thập phân. '
        'Vậy cứ thử k = 1, 2, 3, ...; với mỗi k tính số dư của "số thập phân có chữ số là các bit của k" bằng sơ đồ Horner, dừng ở k đầu tiên cho số dư 0.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử lần lượt.', 12)
    D.code('BOI01.CPP (ngây thơ): duyệt k theo thứ tự tăng', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Nếu đáp số có L chữ số thì phải thử khoảng 2^{L} giá trị k. Với n = 99 đáp số có 18 chữ số (2^{18} ≈ 2,6 · 10^{5} lần thử: 0,05 giây); '
                               'với n = 999 đáp số là 27 chữ số 1 (2^{27} ≈ 1,3 · 10^{8} lần thử: **28 giây**); với n = 999 999 đáp số có 54 chữ số: 2^{54} lần thử, hàng trăm năm.'])
    D.kbox('BẾ TẮC', ['Số lần thử tăng theo hàm mũ của độ dài đáp số. Nhưng hãy để ý: chỉ có n số dư khác nhau. Hai số 0/1 có cùng số dư thì khi viết thêm cùng một dãy chữ số vào sau, '
                      'chúng vẫn cùng số dư. Vậy với mỗi số dư, ta chỉ cần giữ lại **một** đại diện: số nhỏ nhất đạt tới số dư đó.'])

    D.h('4. Phá bế tắc: Tìm kiếm theo chiều rộng trên số dư')
    D.step(1, 'Đồ thị số dư')
    D.p('Mỗi số dư r ∈ {0, 1, ..., n − 1} là một đỉnh. Viết thêm chữ số d vào cuối một số có số dư r cho số có số dư (10r + d) mod n: đó là một cạnh r → (10r + d) mod n mang nhãn d. '
        'Bắt đầu ở đỉnh 1 mod n (số "1"), ta cần đi tới đỉnh 0 bằng đường đi mà dãy nhãn tạo thành số nhỏ nhất.')
    D.step(2, 'BFS cho số nhỏ nhất')
    D.kbox('THUẬT TOÁN (BFS TRÊN SỐ DƯ)', [
        '$n 1|Đưa số dư của "1" vào hàng đợi, đánh dấu đã gặp.',
        '$n 2|Lấy r ở đầu hàng đợi. Nếu r = 0: dừng.',
        '$n 3|Với d = 0 rồi d = 1: t = (10r + d) mod n. Nếu t chưa gặp, ghi nhớ par[t] = r, dig[t] = d, đánh dấu và đưa t vào cuối hàng đợi. Quay lại bước 2.',
        '$n 4|Lần ngược par từ 0 về đỉnh xuất phát, đọc các nhãn dig theo thứ tự ngược lại: đó là đáp số.'])
    D.kbox('VÌ SAO NHỎ NHẤT?', [
        'BFS đi theo từng "tầng": tầng L gồm các số dư đạt được bằng số có L chữ số. Số ít chữ số hơn thì nhỏ hơn, nên đáp số ở tầng thấp nhất có thể. '
        'Trong cùng một tầng, các số được đưa vào hàng đợi theo **thứ tự tăng dần**: điều này đúng ở tầng 1, và nếu đúng ở tầng L thì ở tầng L + 1, con của số nhỏ hơn đứng trước, '
        'và với cùng một cha thì con thêm chữ số 0 đứng trước con thêm chữ số 1. Vì vậy lần đầu một số dư được gặp, nó được gặp bởi số nhỏ nhất có số dư ấy; bỏ qua các lần gặp sau là an toàn.'])
    D.step(3, 'Chạy tay với n = 12')
    D.fig(P.fig('tree'), 'Cây BFS với n = 12: mỗi số dư chỉ được giữ một lần.', 15.2)
    D.p('Tầng 4 có 8 số nhưng 1000, 1001, 1010, 1011 cho các số dư 4, 5, 2, 3 đã gặp ở tầng 3, nên bị cắt. Ở tầng 5, số 11100 đến số dư 0: đáp số là **11100** = 12 · 925. '
        'Chỉ có 12 số dư nên BFS không bao giờ phải giữ quá 12 "đại diện", dù số các số 0/1 có 5 chữ số là 16, có 50 chữ số là 2^{49}.')
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của BFS trên số dư.', 13.5)
    D.code('BOI01.CPP: BFS trên số dư', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi số dư vào hàng đợi tối đa một lần và sinh hai cạnh: O(n) thời gian và bộ nhớ. Với n = 10^{6}, chương trình chạy khoảng **0,03 giây**. '
                               'Đáp số dài tối đa n chữ số (theo định lí ở mục 1), nên việc lần ngược cũng O(n). Chương trình đã được đối chiếu với cách thử lần lượt cho mọi n ≤ 150.'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Tập chữ số bất kì')
    D.p('Bội nhỏ nhất của n chỉ dùng các chữ số trong một tập cho trước (ví dụ {4, 7}, các "số may mắn"): giữ nguyên BFS, chỉ đổi vòng lặp d chạy qua tập chữ số theo thứ tự tăng, '
        'và các đỉnh xuất phát là các chữ số khác 0 của tập. Khác với {0, 1}, lần này có thể **không có nghiệm** (ví dụ n = 2 với tập {1, 3}, n = 5 với tập {4, 7}): BFS kết thúc mà không gặp số dư 0.')
    D.sub('Mở rộng 2: Thêm ràng buộc về tổng chữ số')
    D.p('Tìm số nhỏ nhất chia hết cho d và có tổng chữ số bằng s (d ≤ 500, s ≤ 5000): mỗi đỉnh bây giờ là **cặp** (số dư, tổng chữ số đã dùng), có d · s đỉnh. '
        'BFS (thêm chữ số 0..9 theo thứ tự tăng) vẫn cho số nhỏ nhất vì cùng lí do: ít chữ số hơn thì nhỏ hơn, cùng độ dài thì thứ tự hàng đợi là thứ tự tăng.')
    D.sub('Mở rộng 3: Sinh các số may mắn')
    D.p('Bài toán ngược "liệt kê mọi số chỉ gồm chữ số 4 và 7 không vượt quá 10^{9}" không cần số dư: có 2 + 4 + ... + 2^{9} = 1022 số, sinh bằng BFS/đệ quy (thêm 4 hoặc 7 vào cuối). '
        'Sinh trực tiếp các số có cấu trúc thay vì duyệt 10^{9} số là ý tưởng sẽ gặp lại ở các bài sau.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Lưu cả số vào hàng đợi:** đáp số có thể dài 54 chữ số, không vừa kiểu số nào. Chỉ lưu số dư và lần ngược.',
        '- **Thêm chữ số 1 trước chữ số 0:** BFS vẫn tìm được bội, nhưng không phải bội **nhỏ nhất**.',
        '- **Quên n = 1:** số dư xuất phát đã là 0, đáp số là "1".',
        '- **Tính 10 · r bằng int khi n gần 2 · 10^{8}:** tràn; dùng long long cho phép nhân.'])
    D.kbox('GHI NHỚ', [
        '- Tìm một số theo tính chất về số dư: **đi trên đồ thị số dư**, mỗi số dư một đại diện.',
        '- BFS với chữ số thêm theo thứ tự tăng cho số nhỏ nhất (ít chữ số nhất, rồi nhỏ nhất theo thứ tự từ điển).',
        '- Lần ngược bằng mảng cha để in đáp số dài; độ phức tạp O(n · số chữ số được dùng).',
        '- Nguyên lí Dirichlet bảo đảm luôn có bội gồm 0 và 1 với không quá n chữ số.'])
    D.luyentap([('7.1', 'SỐ MAY MẮN', 'Bội nhỏ nhất của n chỉ gồm chữ số 4 và 7, hoặc in −1: Mở rộng 1.'),
                ('7.2', 'TỔNG VÀ BỘI', 'Số nhỏ nhất chia hết cho d và có tổng chữ số s: BFS trên cặp (số dư, tổng), Mở rộng 2.'),
                ('7.3', 'ĐẾM SỐ MAY MẮN', 'Đếm số may mắn trong [L, R] (R ≤ 10^{18}) và tìm số may mắn thứ k: sinh trực tiếp, Mở rộng 3.')])
    D.tukiemtra([('Bội nhỏ nhất của 9 chỉ gồm 0 và 1?', '111 111 111 (cần tổng chữ số chia hết cho 9)'), ('Bội nhỏ nhất của 5 chỉ gồm 0 và 1?', '10'),
                 ('Bội nhỏ nhất của 7 chỉ gồm 0 và 1?', '1001 = 7 · 143'),
                 ('Có bao nhiêu số may mắn (chỉ gồm 4, 7) có đúng 5 chữ số?', '2^{5} = 32')])
