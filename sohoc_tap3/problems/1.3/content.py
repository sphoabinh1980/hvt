def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Bé Na viết liền 1, 2, ..., n thành một số rất dài N và ta cần N mod m. Với n = 10^{7}, N có gần 69 triệu chữ số: '
        'không kiểu số nào chứa nổi, và như sẽ thấy, ngay cả một xâu chứa nó cũng không vừa bộ nhớ.')
    D.p('Bài toán là "anh em" của bài SODU ở Tập 1, Bài 1: tính số dư của một số rất dài bằng **sơ đồ Horner**, đọc từ trái sang phải, '
        'mỗi bước "thêm một chữ số vào bên phải": r ← r · 10 + c. Ở đây mỗi bước ta thêm **cả một số i**, và số i có thể có nhiều chữ số.')
    D.fig(P.fig('shift'), 'Viết thêm số i vào bên phải là "dịch trái" phần đã viết đi số chữ số của i rồi cộng i.', 15)

    D.h('2. Cách ngây thơ: Ghép thành một số')
    D.p('Giữ giá trị thật x của số bé Na đang viết; viết thêm i thì x ← x · 10^{k} + i, với k là số chữ số của i. Cuối cùng in x mod m.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ghép thành một số', 9.5)
    D.code('Cách ngây thơ: ghép thành số long long', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n log n) phép tính, nhưng x tràn long long ngay khi có hơn 18 chữ số, tức từ n = 14 '
        '(số 123456789101112131415 với n = 15 đã có 21 chữ số).')

    D.h('3. Bế tắc')
    D.bullets([
        '**Subtask 1** (n ≤ 9): x có tối đa 9 chữ số, vừa long long: **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
        '**Subtask 2, 3**: x tràn số, kết quả sai: **0 điểm**.'])
    D.p('Cải tiến tự nhiên: dựng hẳn xâu `s = "123456789101112..."` rồi áp dụng Horner cho từng chữ số. Chương trình `mid.cpp` đúng với mọi n, '
        'qua subtask 2 (n ≤ 1000, xâu chỉ 2893 kí tự). Nhưng ở subtask 3, xâu dài tới 68 888 897 kí tự:')
    D.fig(P.fig('memory'), 'Số kí tự của xâu theo nhóm số có cùng số chữ số, với n = 10^{7}.', 15)
    D.p('Riêng xâu đã chiếm gần 69 MB, chưa kể bộ nhớ dự phòng khi xâu tự nới rộng: chương trình bị dừng vì vượt giới hạn 64 MB. '
        'Tổng cộng **' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', [
        'Ta không cần nhớ những gì đã viết. Sơ đồ Horner chỉ cần **số dư của phần đã viết**; cái cần biết thêm là "dịch trái" bao nhiêu chữ số, '
        'tức 10^{k} mod m với k là số chữ số của i.'])

    D.h('4. Phá bế tắc: Horner theo từng khối')
    D.sub('Công thức')
    D.p('Gọi r_{i} là số dư (theo m) của số viết được sau khi viết xong 1, 2, ..., i, và k_{i} là số chữ số của i. Khi đó')
    D.eq('**r_{i} = (r_{i−1} · 10^{k_{i}} + i) mod m,   r_{0} = 0.**')
    D.box('purple', 'VÌ SAO ĐÚNG?', [
        'Gọi X_{i} là số thật bé Na viết được sau bước i. Viết thêm i (có k chữ số) vào bên phải nghĩa là X_{i} = X_{i−1} · 10^{k} + i. '
        'Phép lấy dư "đi xuyên qua" phép nhân và phép cộng (Tập 1, Bài 1), nên ta được thay X_{i−1} bằng số dư r_{i−1} của nó, '
        'và thay 10^{k} bằng 10^{k} mod m.'])
    D.sub('Lũy thừa của 10 chỉ thay đổi 7 lần')
    D.p('k_{i} chỉ tăng khi i chạm 10, 100, 1000, ..., 10^{7}. Vậy ta giữ p = 10^{k} mod m và biến `next` là lũy thừa của 10 kế tiếp; '
        'khi i = next thì p ← p · 10 mod m. Không cần hàm `pow` (số thực, dễ sai) và không cần đếm chữ số của từng i.')
    D.sub('Chạy tay với n = 12, m = 1000 (ví dụ 1)')
    D.table(['i', 'p = 10^{k} mod 1000', 'r_{i} = (r_{i−1} · p + i) mod 1000'], [
        ['1..9', '10', 'r_{9} = 123456789 mod 1000 = 789'],
        ['10', '100 (i = next = 10)', '(789 · 100 + 10) mod 1000 = 78 910 mod 1000 = 910'],
        ['11', '100', '(910 · 100 + 11) mod 1000 = 91 011 mod 1000 = 11'],
        ['12', '100', '(11 · 100 + 12) mod 1000 = 1 112 mod 1000 = **112**'],
    ], widths=[1, 2.2, 5], align=['center', 'center', 'left'])
    D.p('Đáp số 112 khớp với 123456789101112 = 1000 · 123456789101 + 112.')

    D.h('5. Cách tối ưu: Horner theo từng số i')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 11)
    D.code('VIETLIEN.CPP: Horner theo khối, bộ nhớ O(1)', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(n) thời gian, mỗi bước một phép nhân và một phép chia lấy dư; O(1) bộ nhớ. Với n = 10^{7}, chương trình chạy khoảng '
        '0,1 giây trên máy chấm của sách.')
    D.box('blue', 'MỞ RỘNG: n TỚI 10^{18}', [
        'Trong mỗi nhóm số có cùng k chữ số, phép biến đổi r ← r · P + i (P = 10^{k}) là một phép biến đổi tuyến tính của vectơ (r, i, 1): '
        'r\' = P · r + i, i\' = i + 1. Lũy thừa ma trận 3 × 3 (Bài 15) cho phép "nhảy" qua cả nhóm trong O(log n), và cả bài chạy trong O(18 · 27 · log n).'])

    D.h('6. Bẫy thường gặp')
    D.bullets([
        '**Tràn số trong r · p:** r < m ≤ 10^{9} và p < m, nên tích tới 10^{18}: phải dùng long long, không được dùng int.',
        '**Quên lấy dư i:** với m nhỏ hơn i, cộng i mà không lấy dư vẫn đúng nhờ phép % ở cuối, nhưng chỉ vì r · p + i vẫn vừa long long; '
        'thói quen tốt là lấy dư mọi số hạng.',
        '**m = 1:** mọi số dư là 0; khởi tạo p = 10 % m (bằng 0) chứ không phải 10 thì mọi giá trị trung gian đều đúng.',
        '**Dùng pow(10, k):** hàm số thực; với k lớn cho kết quả không chính xác hoặc tràn. Hãy nhân dần.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
