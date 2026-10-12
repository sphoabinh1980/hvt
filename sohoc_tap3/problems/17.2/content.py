def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('a^{b} với a = 10^{9}, b = 10^{4} có 90 001 chữ số: phải dùng **số lớn**. Ta chỉ cần một phép toán: **nhân số lớn với số nhỏ** a (Tập 1, Bài 17), '
        'lặp lại b lần bắt đầu từ số lớn 1. Câu hỏi then chốt là **lưu mỗi ô bao nhiêu chữ số**.')

    D.h('2. Cách ngây thơ: long long')
    D.code('Cách ngây thơ', P.src('naive.cpp'))
    D.p('Đúng khi a^{b} ≤ 10^{18}: **' + S('naive.cpp') + ' điểm**.')

    D.h('3. Bế tắc')
    D.p('Số lớn cơ số 10 (mỗi ô một chữ số, `mid.cpp`) cho kết quả đúng ở mọi trường hợp, nhưng hãy đếm số phép tính. '
        'Lần nhân thứ k làm việc trên khoảng 9k chữ số (a^{k} có khoảng 9k chữ số khi a = 10^{9}); tổng cộng 9 · (1 + 2 + ... + 10^{4}) ≈ 4,5 · 10^{8} lượt, '
        'mỗi lượt một phép nhân, một phép chia và một phép lấy dư 64 bit.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Subtask 2 (a ≤ 1000, b ≤ 3000) chỉ khoảng 1,4 · 10^{7} lượt, chạy ' + P.scores['mid.cpp']['detail'][1].split()[1] + '. '
                                  'Subtask 3 thì quá thời gian: **' + S('mid.cpp') + ' điểm**. Mỗi ô chỉ chứa một chữ số là quá lãng phí: long long chứa được tới 18 chữ số.'])

    D.h('4. Phá bế tắc: Cơ số 10⁹')
    D.p('Lưu mỗi ô **9 chữ số** (cơ số BASE = 10^{9}): số ô giảm 9 lần, số lượt giảm còn khoảng 5 · 10^{7}. Vì sao không nhiều hơn 9?')
    D.bullets(['Trong phép nhân, t = d[i] · a + c với d[i] < 10^{9}, a ≤ 10^{9}, c < a: t < 10^{18} + 10^{9} < 9,2 · 10^{18}, vừa long long. '
               'Cơ số 10^{10} sẽ cho t tới 10^{19}: tràn.',
               'Số nhớ c = ⌊t / 10^{9}⌋ < a ≤ 10^{9} nhỏ hơn BASE, nên sau mỗi lần nhân chỉ thêm **nhiều nhất một ô**.'])
    D.fig(P.fig('steps'), 'Hai lần nhân với 10⁹; ô vàng là ô vừa được thêm.', 15.2)
    D.sub('In kết quả')
    D.fig(P.fig('print'), 'Mọi ô sau ô cao nhất phải in đủ 9 chữ số.', 15.2)
    D.box('purple', 'BẪY: IN MỖI Ô BẰNG %lld', ['$printf("%lld", d[i]);',
                                                 'Ô 056928801 bị in thành 56928801, ô 000000000 bị in thành 0. Ví dụ 1 ra 19 chữ số, ví dụ 2 ra 100. '
                                                 'Chương trình `trap.cpp` sai gần như mọi test: **' + S('trap.cpp') + ' điểm**, dù phần tính toán hoàn toàn đúng.'])
    D.sub('Trường hợp a = 0')
    D.p('Sau lần nhân đầu tiên mọi ô bằng 0; xóa các ô 0 ở đầu nhưng giữ một ô: kết quả 0. Với b = 0 vòng lặp không chạy, kết quả là 1 (quy ước 0^{0} = 1).')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối', 13)
    D.code('LUYTHUALON.CPP: cơ số 10⁹', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(b^{2} · log a / 9): khoảng 5 · 10^{7} lượt, chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Lũy thừa nhanh không giúp nhiều ở đây: nó cần nhân **hai số lớn** với nhau (bài 17.3), mà hai lần bình phương cuối đã tốn bằng cả quá trình nhân dần.',
                              'Với a nhỏ (a ≤ 9), có thể gộp nhiều lần nhân: nhân với a^{k} sao cho a^{k} ≤ 10^{9}, giảm số vòng lặp k lần.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**In thiếu số 0 đầu ô.**', '**Dùng int cho d[i]** rồi nhân với a: tràn.', '**Cơ số 10^{10} trở lên:** t tràn long long.',
               '**a = 0:** phải in 0 (b > 0) hoặc 1 (b = 0), không phải một dãy số 0.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'trap.cpp', 'opt.cpp'])
