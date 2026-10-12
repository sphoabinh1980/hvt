def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Chữ số tận cùng của một số chính là số dư của nó khi chia cho 10. Vậy câu hỏi là: tính **a^{b} mod 10** với a, b có tới 10^{5} chữ số. '
        'Hai quan sát của Tập 1, Bài 1 sẽ biến một con số "không máy tính nào tính nổi" thành một phép tính trên vài chữ số:')
    D.bullets([
        '**Chỉ chữ số cuối của a là quan trọng:** đồng dư giữ nguyên qua phép nhân, nên a^{b} ≡ d^{b} (mod 10) với d = a mod 10.',
        '**Dãy chữ số cuối của d^{1}, d^{2}, d^{3}, ... lặp lại tuần hoàn:** mỗi số hạng chỉ phụ thuộc vào số hạng trước, mà chỉ có 10 chữ số.'])
    D.fig(P.fig('cycles'), 'Chữ số cuối của d^{b} với d = 0..9 và b = 1..8. Ô vàng là một chu kì; chu kì chỉ có thể là 1, 2 hoặc 4.', 15)
    D.p('Bảng cho thấy mọi chu kì đều là **ước của 4**: d = 2, 3, 7, 8 có chu kì 4; d = 4, 9 có chu kì 2; d = 0, 1, 5, 6 có chu kì 1. '
        'Vì vậy khi b ≥ 1, chữ số cuối của d^{b} chỉ phụ thuộc vào **b mod 4**.')

    D.h('2. Cách ngây thơ: Nhân b lần')
    D.p('Đọc a, b vào long long, giữ r = 1 rồi nhân b lần với d = a mod 10, mỗi lần lấy dư cho 10. Chương trình đúng về ý tưởng (vì đã chỉ giữ chữ số cuối), '
        'nhưng phải đi đủ b bước.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách nhân b lần', 9)
    D.code('Cách ngây thơ: nhân b lần', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(b) mỗi câu hỏi. Với b ≤ 10^{6} và T ≤ 10 chỉ 10^{7} phép nhân, rất nhanh. Với b = 10^{18} thì không thể chạy xong; '
        'còn với b có 10^{5} chữ số thì ngay việc đọc b vào long long đã sai.')

    D.h('3. Bế tắc')
    D.bullets([
        '**Subtask 1** (a, b ≤ 10^{6}): nhân b lần chạy tức thì: **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
        '**Subtask 2** (a, b ≤ 10^{18}): thay vòng lặp bằng **lũy thừa nhanh** (Bài 9) chỉ còn 60 bước. Chương trình `mid.cpp` (cùng ý tưởng, '
        'thay vòng lặp) đạt **' + S('mid.cpp') + ' điểm**.',
        '**Subtask 3** (10^{5} chữ số): `scanf("%lld")` với một xâu 10^{5} chữ số cho ra một số rác. Cả hai chương trình trên đều **0 điểm** ở đây.'])
    D.box('red', 'ĐIỂM BẾ TẮC', [
        'Số mũ b quá lớn để lưu, chứ chưa nói tới việc lặp. Nhưng ta không cần b: theo bảng ở Hình ' + P.pid + '.1, ta chỉ cần **b mod 4**, '
        'và số dư của một xâu chữ số rất dài thì tính được mà không cần "đổi ra số".'])

    D.h('4. Phá bế tắc: Chu kì 4 và số dư của xâu')
    D.sub('Bước 1. Tính b mod 4 từ xâu')
    D.p('Có hai cách, đều O(độ dài xâu):')
    D.fig(P.fig('mod4'), 'Số dư của b khi chia cho 4: sơ đồ Horner, hoặc chỉ cần hai chữ số cuối.', 15)
    D.sub('Bước 2. Cẩn thận với b chia hết cho 4')
    D.p('Đây là cái bẫy lớn nhất của bài. Khi b ≡ 0 (mod 4) và b > 0, số mũ tương ứng trong một chu kì **không phải 0 mà là 4**: '
        '2^{4} = 16 tận cùng là 6, trong khi 2^{0} = 1. Chu kì của bảng bắt đầu từ b = 1, không phải từ b = 0.')
    D.box('purple', 'VÌ SAO DÙNG ĐƯỢC SỐ MŨ 4 THAY CHO MỌI b ⋮ 4?', [
        'Với mọi chữ số d, d^{5} ≡ d (mod 10) (kiểm tra trực tiếp bảng: cột b = 5 trùng cột b = 1). Nhân hai vế với d^{k − 1} được '
        'd^{k + 4} ≡ d^{k} (mod 10) với mọi k ≥ 1. Vậy với b ≥ 1, ta có thể trừ dần 4 khỏi b cho tới khi b ∈ {1, 2, 3, 4}: đó chính là '
        '"(b mod 4), nhưng thay 0 bằng 4".',
        'Chỉ riêng b = 0 thì không trừ được (vì k ≥ 1): đáp số là 1 theo quy ước, kể cả với a = 0.'])
    D.p('Chương trình `bay4.cpp` dùng thẳng số mũ b mod 4 (nhân e lần) mắc đúng lỗi này. Nó qua được cả ba ví dụ của đề bài (2026 mod 4 = 2, 3 mod 4 = 3, b = 0), '
        'nhưng mỗi subtask đều có test với b chia hết cho 4: **' + S('bay4.cpp') + ' điểm**. Một ví dụ "đẹp" không thay được việc tự thử các trường hợp biên!')
    D.sub('Chạy tay')
    D.table(['a', 'b', 'd = a mod 10', 'b mod 4', 'Số mũ e', 'd^{e}', 'Đáp số'], [
        ['2', '2026', '2', '2', '2', '4', '4'],
        ['7', '3', '7', '3', '3', '343', '3'],
        ['0', '0', '0', '–', '(b = 0)', '–', '1'],
        ['...789', '...3210', '9', '2', '2', '81', '1'],
        ['2', '4', '2', '0', '4', '16', '6'],
        ['10', '5', '0', '1', '1', '0', '0'],
    ], widths=[1.1, 1.1, 1.3, 1, 1.1, 0.9, 1], bold_cols=(6,))

    D.h('5. Cách tối ưu: Xâu, chu kì 4')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu cho một cặp (a, b)', 9)
    D.code('CHUSOCUOI.CPP: chu kì 4, O(độ dài xâu)', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(|a| + |b|) cho việc đọc xâu và tính b mod 4; phần lũy thừa nhiều nhất 4 phép nhân. Với T = 10 và mỗi xâu 10^{5} '
        'chữ số, tổng cộng chỉ 2 · 10^{6} kí tự.')
    D.box('blue', 'MỞ RỘNG: CHỮ SỐ CUỐI TRONG HỆ CƠ SỐ KHÁC, HOẶC HAI CHỮ SỐ CUỐI', [
        'Muốn hai chữ số cuối (a^{b} mod 100) thì chu kì không còn là 4. Cách tổng quát là lũy thừa với số mũ dạng xâu theo sơ đồ Horner '
        '(bài SỐ MŨ KHỔNG LỒ, 9.2): r ← r^{10} · a^{c} (mod m) với mỗi chữ số c của b. Cách này không cần biết chu kì và đúng với mọi mô-đun m.'])

    D.h('6. Bẫy thường gặp')
    D.bullets([
        '**b chia hết cho 4:** dùng số mũ 0 thay vì 4. Thử ngay 2^{4}: phải ra 6.',
        '**b = 0:** đáp số là 1, kể cả khi a = 0 (quy ước 0^{0} = 1); và đừng nhầm với trường hợp a = 0, b > 0 (đáp số 0).',
        '**Đọc vào kiểu số:** a, b có 10^{5} chữ số, phải đọc vào `string`.',
        '**Lấy b mod 4 bằng chữ số cuối:** b mod 4 phụ thuộc **hai** chữ số cuối (12 ⋮ 4 nhưng 22 không ⋮ 4); chỉ mod 2 và mod 5 mới chỉ cần chữ số cuối.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'bay4.cpp', 'opt.cpp'])
