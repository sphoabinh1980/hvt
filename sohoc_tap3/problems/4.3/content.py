def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Ở giây t, kim A ở nấc (p + a·t) mod m, kim B ở nấc (q + b·t) mod m. Hai kim trùng nhau khi hai số dư bằng nhau, tức m chia hết hiệu của chúng:')
    D.eq('**(a − b) · t ≡ q − p (mod m).**')
    D.p('Đây là một **phương trình đồng dư bậc nhất** ẩn t (Tập 1, Bài 4, Mở rộng 3). Cần tìm nghiệm t ≥ 0 nhỏ nhất và đếm số nghiệm trong [0, T].')
    D.fig(P.fig('clock'), 'Ví dụ 1, đồng hồ thứ nhất (m = 12): hai kim trùng nhau ở các giây 1, 5, 9, ...', 15)

    D.h('2. Cách ngây thơ: Mô phỏng từng giây')
    D.p('Sau m giây, cả hai kim đều quay về vị trí ban đầu (a·m ≡ 0 mod m), nên dãy vị trí tuần hoàn với chu kì m. '
        'Mô phỏng các giây 0..max(T, m − 1): đủ để vừa đếm trong [0, T], vừa chắc chắn tìm thấy lần trùng đầu tiên nếu có.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách mô phỏng', 11)
    D.code('Cách ngây thơ: mô phỏng từng giây', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(max(T, m)) mỗi đồng hồ: 10^{6} trong subtask 1, nhưng tới 10^{18} trong các subtask sau.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (m ≤ 1000, T ≤ 10^{6}): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               '**Subtask 2, 3**: m, T tới 10^{9} và 10^{18}: **0 điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Các giây trùng nhau tạo thành một **cấp số cộng**. Biết số hạng đầu và công sai là đếm được bằng một phép chia, không cần mô phỏng.'])

    D.h('4. Phá bế tắc: Phương trình đồng dư')
    D.fig(P.fig('reduce'), 'Chuỗi biến đổi từ "hai kim trùng nhau" tới một lớp đồng dư của t.', 15)
    D.nums([
        '**Đưa về số dư không âm:** d = (a − b) mod m, e = (q − p) mod m, dùng ((x % m) + m) % m vì a − b, q − p có thể âm.',
        '**Điều kiện có nghiệm:** d·t ≡ e (mod m) ⇔ d·t + m·y = e có nghiệm nguyên ⇔ g = gcd(d, m) chia hết e (Bézout). Không chia hết: in "-1 0".',
        '**Nghiệm:** chia cho g: (d/g)·t ≡ e/g (mod M) với M = m/g và gcd(d/g, M) = 1. Euclid mở rộng d·u + m·v = g cho (d/g)·u ≡ 1 (mod M), nên '
        't ≡ (e/g)·u (mod M). Nghiệm nhỏ nhất không âm t_{0} = (e/g mod M) · (u mod M) mod M.',
        '**Đếm:** các giây trùng nhau là t_{0}, t_{0} + M, t_{0} + 2M, ...; trong [0, T] có 0 giây nếu t_{0} > T, ngược lại ⌊(T − t_{0}) / M⌋ + 1 giây.'])
    D.box('purple', 'TRƯỜNG HỢP a = b', [
        'Khi d = 0, gcd(0, m) = m. Phương trình có nghiệm khi và chỉ khi m | e, tức e = 0 (p = q): hai kim luôn trùng nhau, M = 1, t_{0} = 0, '
        'số giây là T + 1. Euclid mở rộng với (0, m) vẫn chạy đúng: extgcd(0, m) gọi extgcd(m, 0), trả về g = m và u = 0. Không cần if riêng.'])
    D.sub('Chạy tay')
    D.table(['m, p, a, q, b', 'd', 'e', 'g', 'M', 't₀', 'Số giây trong [0, T]'], [
        ['12, 0, 5, 3, 2', '3', '3', '3', '4', '1·u = 1 (u = 1)', '⌊(10 − 1)/4⌋ + 1 = **3**'],
        ['12, 0, 4, 1, 0', '4', '1', '4', '–', '4 ∤ 1', '**−1 0**'],
        ['60, 7, 13, 7, 13', '0', '0', '60', '1', '0', '⌊5/1⌋ + 1 = **6**'],
        ['10^{18}, 0, 3, 1, 0', '3', '1', '1', '10^{18}', '666...667', '1'],
    ], widths=[2, 0.6, 0.6, 0.7, 0.8, 2.2, 2.6])
    D.sub('Tràn số với m tới 10^{18}')
    D.p('t_{0} là tích của hai số dư theo mô-đun M ≤ 10^{18}: tích tới 10^{36}, phải nhân bằng `__int128`. Chương trình `mid.cpp` giống hệt lời giải mẫu '
        'nhưng nhân trong long long: đúng khi m ≤ 10^{9} (tích < 10^{18}), sai ở subtask 3: **' + S('mid.cpp') + ' điểm**.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 13)
    D.code('DONGHO.CPP: phương trình đồng dư, __int128', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(log m) mỗi đồng hồ (Euclid mở rộng, ≤ 90 tầng đệ quy). 10^{5} đồng hồ chạy trong '
        + P.scores['opt.cpp']['detail'][2].split()[1].replace('.', ',').replace('s', ' giây') + '.')
    D.box('blue', 'MỞ RỘNG: HÀM GIẢI ĐỒNG DƯ DÙNG LẠI', [
        'Hàm "giải a·x ≡ c (mod m), trả về (x₀, M) hoặc báo vô nghiệm" sẽ xuất hiện lại ở bài PHƯƠNG TRÌNH ĐỒNG DƯ (10.3) và là bước then chốt khi gộp hai '
        'phương trình trong định lí số dư Trung Hoa (Bài 12). Hãy viết nó một lần, thật cẩn thận, và lưu vào thư viện của em (Phụ lục B).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Số dư âm:** a − b và q − p có thể âm; `%` của C++ trả về số âm.',
               '**u âm hoặc lớn:** đưa u về [0, M) trước khi nhân.',
               '**t₀ > T:** vẫn in t₀ (giây đầu tiên tồn tại, chỉ là nằm ngoài [0, T]) và số giây là 0.',
               '**Số giây tới 10^{18} + 1:** m = 1 hoặc a = b, p = q. Vừa long long, nhưng đừng cộng thêm gì.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
