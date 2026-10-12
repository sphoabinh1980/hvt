def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Đếm số nghiệm **tự nhiên** (x, y ≥ 0) của phương trình a · x + b · y = c. Trên mặt phẳng tọa độ, các nghiệm nguyên nằm cách đều nhau trên một đường thẳng, '
        'và ta chỉ đếm những điểm nằm trong góc phần tư thứ nhất.')
    D.fig(P.fig('line'), 'Các nghiệm nguyên của 3x + 5y = 30. Chỉ ba nghiệm (vàng) có x, y ≥ 0.', 13)

    D.h('2. Cách ngây thơ: Thử mọi x')
    D.p('Với mỗi số gói kẹo x = 0, 1, ..., ⌊c / a⌋, số tiền còn lại c − a · x phải chia hết cho b (khi đó y = (c − a · x) / b ≥ 0).')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử mọi x', 11)
    D.code('Cách ngây thơ: thử mọi x', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(c / a) mỗi câu hỏi: tới 10^{7} với c ≤ 10^{7} (subtask 1), nhưng tới 10^{18} với c = 10^{18}, a = 1.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (c ≤ 10^{7}): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               'Quan sát nửa vời: các x của nghiệm cách nhau đúng B = b / g. Chỉ cần tìm x nhỏ nhất bằng cách thử x trong [0, B), rồi đếm bằng một phép chia. '
               'Chương trình `mid.cpp` thử tới B ≤ 10^{6} lần, qua **subtask 2** (a, b ≤ 10^{6}): **' + S('mid.cpp') + ' điểm**.',
               '**Subtask 3**: B tới 10^{9}, Q = 10^{5}: tới 10^{14} phép thử: **0 điểm** ở subtask này.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Phải tìm được **x nhỏ nhất không âm** của một nghiệm mà không thử: đó là việc của thuật toán Euclid mở rộng.'])

    D.h('4. Phá bế tắc: Euclid mở rộng')
    D.sub('Bước 1. Điều kiện có nghiệm và rút gọn')
    D.p('Đặt g = gcd(a, b). Nếu g ∤ c thì vô nghiệm (đáp số 0). Ngược lại chia cả ba số cho g: A · x + B · y = C với A = a/g, B = b/g, C = c/g và gcd(A, B) = 1.')
    D.sub('Bước 2. x nhỏ nhất không âm')
    D.p('Lấy phương trình theo mô-đun B: A · x ≡ C (mod B). Euclid mở rộng cho u, v với a · u + b · v = g, tức A · u + B · v = 1, nên A · u ≡ 1 (mod B): '
        'u là nghịch đảo của A theo mô-đun B. Vậy')
    D.eq('**x ≡ C · u (mod B),   x_{min} = (C mod B) · (u mod B) mod B,**')
    D.p('với u mod B lấy theo nghĩa không âm. Ví dụ 3x + 5y = 30: g = 1, 3 · 2 + 5 · (−1) = 1 nên u = 2; x_{min} = (30 mod 5) · 2 mod 5 = 0.')
    D.sub('Bước 3. Đếm')
    D.p('Từ x_{min}, mọi nghiệm có x = x_{min} + B · t (t ≥ 0), y = (C − A · x) / B giảm A mỗi bước. Điều kiện y ≥ 0 tương đương A · x ≤ C. '
        'Nếu ngay A · x_{min} > C thì không có nghiệm tự nhiên; ngược lại số nghiệm là')
    D.eq('**⌊(C − A · x_{min}) / (A · B)⌋ + 1.**')
    D.fig(P.fig('xaxis'), 'Các x của nghiệm (bước B = 5) trên trục số; chỉ những x ≤ C/A = 10 cho y ≥ 0.', 15)
    D.box('purple', 'ƯỚC LƯỢNG ĐỂ KHÔNG TRÀN SỐ', [
        '- C mod B < B ≤ 10^{9} và u mod B < 10^{9}: tích < 10^{18}, vừa long long; lời giải dùng __int128 cho chắc vì không tốn gì.',
        '- A · x_{min} < A · B ≤ a · b ≤ 10^{18}: vừa long long.',
        '- Đáp số tới 10^{18} + 1 (a = b = 1, c = 10^{18}): vừa long long.',
        'Nếu lấy nghiệm riêng x_{0} = u · C (không lấy dư trước) thì u · C có thể tới 10^{9} · 10^{18} = 10^{27}: tràn.'])
    D.sub('Chạy tay')
    D.table(['a, b, c', 'g', 'A, B, C', 'u (A·u ≡ 1 mod B)', 'x_{min}', 'A·x_{min} ≤ C?', 'Đáp số'], [
        ['3, 5, 30', '1', '3, 5, 30', '2', '0', 'có', '⌊30/15⌋ + 1 = **3**'],
        ['6, 4, 7', '2', '–', '–', '–', '2 ∤ 7', '**0**'],
        ['3, 5, 7', '1', '3, 5, 7', '2', '7·2 mod 5 = 4', '12 > 7', '**0**'],
        ['10^{9}, 10^{9}, 10^{18}', '10^{9}', '1, 1, 10^{9}', '0', '0', 'có', '10^{9} + 1'],
    ], widths=[2, 0.9, 1.6, 1.8, 1.4, 1.4, 1.7])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12)
    D.code('MUAHANG.CPP: Euclid mở rộng, O(log) mỗi câu hỏi', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(log min(a, b)) mỗi câu hỏi cho Euclid mở rộng; cả bộ 10^{5} câu hỏi chạy trong '
        + P.scores['opt.cpp']['detail'][2].split()[1].replace('.', ',').replace('s', ' giây') + '.')
    D.box('blue', 'MỞ RỘNG: SỐ TIỀN LỚN NHẤT KHÔNG TIÊU HẾT ĐƯỢC', [
        'Với gcd(A, B) = 1, mọi C > A · B − A − B đều có nghiệm tự nhiên, và C = A · B − A − B thì không (định lí Sylvester). '
        'Câu hỏi thứ ba của ví dụ 1 chính là trường hợp này: 3 · 5 − 3 − 5 = 7.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**u âm:** Euclid mở rộng có thể trả về u < 0; phải đưa về [0, B) trước khi nhân.',
               '**Nhân trước, lấy dư sau:** u · C tràn số; lấy C mod B trước.',
               '**B = 1:** mọi x đều thỏa đồng dư, x_{min} = 0; công thức vẫn đúng nếu viết cẩn thận (mọi số mod 1 bằng 0).',
               '**Quên c = 0:** đáp số 1 (không mua gì), công thức cho ⌊0/(A·B)⌋ + 1 = 1.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
