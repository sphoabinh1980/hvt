def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Viết n = p + q với p ≤ q nguyên tố, p nhỏ nhất. Cách tìm hiển nhiên: thử p = 2, 3, 5, ... tăng dần, dừng ở p đầu tiên mà q = n − p cũng nguyên tố. '
        'Câu hỏi là: phải thử bao nhiêu p, và mỗi lần kiểm tra tốn bao nhiêu?')
    D.fig(P.fig('tries'), 'Ví dụ 1, n = 98: các q = 98 − p bị loại (ô xám ghi một ước) cho tới p = 19.', 15)

    D.h('2. Cách ngây thơ: Sàng tới n')
    D.p('Sàng Eratosthenes trên [0, n] rồi duyệt p. Với n ≤ 10^{6}, sàng chỉ mất vài mili giây.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách sàng tới n', 12)
    D.code('Cách ngây thơ: sàng Eratosthenes tới n', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n log log n) thời gian và O(n) bộ nhớ mỗi câu hỏi. Với n = 10^{12}, mảng sàng cần 10^{12} bit ≈ 125 GB.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (n ≤ 10^{6}, chẵn): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               '**Subtask 2, 3**: không cấp phát nổi mảng sàng (chương trình bị dừng ngay): **0 điểm**.'])
    D.p('Thay sàng bằng kiểm tra nguyên tố thử chia 6k ± 1 (bài 5.1): `mid.cpp` thử p tăng dần, mỗi p kiểm tra cả p và n − p. Với n chẵn, p cần thử rất nhỏ '
        '(giả thuyết Goldbach "dư dả"), nên chương trình qua **subtask 2**. Nhưng với **n lẻ** mà n − 2 là hợp số, không có p nào thỏa mãn và vòng lặp chạy tới tận n/2 ≈ 5 · 10^{11}: '
        '**' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Với n lẻ, vòng thử p không bao giờ tìm được gì ngoài p = 2, nhưng không biết khi nào nên dừng. Cần một lập luận để **cắt bỏ** cả vòng lặp.'])

    D.h('4. Phá bế tắc: Tính chẵn lẻ')
    D.fig(P.fig('parity'), 'Tổng hai số nguyên tố theo tính chẵn lẻ. 2 là số nguyên tố chẵn duy nhất.', 13)
    D.p('Nếu n lẻ thì p và q phải khác tính chẵn lẻ, nên một trong hai số là số chẵn, tức là **bằng 2**. Vì p ≤ q, ta có p = 2: '
        'đáp số là "2 n−2" nếu n − 2 nguyên tố, ngược lại là −1. Chỉ **một** lần kiểm tra nguyên tố!')
    D.p('Với n chẵn, thử p tăng dần. Hai mẹo nhỏ giúp chạy nhanh:')
    D.nums(['**Kiểm tra p trước:** p nhỏ (vài nghìn) nên kiểm tra rất rẻ; chỉ khi p nguyên tố mới kiểm tra n − p (cỡ 10^{12}, đắt). Toán tử `&&` tự bỏ qua vế phải khi vế trái sai.',
            '**Hầu hết n − p bị loại sớm:** một số ngẫu nhiên có xác suất 2/3 chia hết cho 2 hoặc 3, 4/5 chia hết cho 2, 3 hoặc 5... nên hàm kiểm tra thường dừng sau vài phép chia. '
            'Chỉ lần cuối cùng (n − p nguyên tố) mới chạy đủ √n / 3 ≈ 333 334 vòng.'])
    D.box('purple', 'BAO NHIÊU p LÀ ĐỦ?', ['Chưa ai chứng minh được giả thuyết Goldbach, nhưng thực nghiệm cho thấy p cần thử rất nhỏ: với mọi số chẵn trong [10^{12} − 2 · 10^{6}, 10^{12}], '
                                           'p lớn nhất là 1669 (số 999 999 634 148 ở ví dụ 2), tức chỉ 263 số nguyên tố đầu tiên. '
                                           'Đó là lí do lời giải "thử p tăng dần" chạy nhanh, dù về lí thuyết ta không chặn được số bước.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12)
    D.code('GOLDBACH.CPP: xét chẵn lẻ, kiểm tra rẻ trước, đắt sau', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** n lẻ: một lần kiểm tra O(√n). n chẵn: vài trăm lần kiểm tra rẻ cộng một lần kiểm tra đầy đủ. 100 câu hỏi chạy trong ' + tm('opt.cpp', 3) + '.')
    D.box('blue', 'MỞ RỘNG: GOLDBACH "YẾU"', ['Năm 2013, Harald Helfgott chứng minh mọi số lẻ lớn hơn 5 là tổng của **ba** số nguyên tố (giả thuyết Goldbach yếu). '
                                              'Lời giải kiểu bài này: lấy p = 3 (hoặc một số nguyên tố nhỏ) rồi viết n − p (chẵn) thành tổng hai số nguyên tố.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Bỏ qua n lẻ:** vòng lặp tới n/2 với n ≈ 10^{12} không bao giờ xong.',
               '**n = 2 và n = 3:** đều in −1 (1 không nguyên tố). **n = 4:** in "2 2", p được phép bằng q.',
               '**Kiểm tra n − p trước:** vẫn đúng nhưng chậm hơn nhiều, vì phải kiểm tra cả những n − p ứng với p hợp số.',
               '**Dùng sàng cho n lớn:** mảng 10^{12} phần tử không thể cấp phát.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
