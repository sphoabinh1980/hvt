def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Đếm số cặp (p, p + 2) cùng nguyên tố nằm **trọn** trong [a, b], cho 10^{6} truy vấn. Bài DEMNGUYENTO (6.1) dạy ta "đếm trong đoạn" bằng hiệu hai tiền tố; '
        'cái mới ở đây là đối tượng được đếm là một **cặp** số, không phải một số.')
    D.p('Mẹo then chốt: **ghi danh mỗi cặp tại số nhỏ p của nó**. Đặt s[p] = 1 nếu p và p + 2 đều nguyên tố. Cặp nằm trọn trong [a, b] khi và chỉ khi a ≤ p và p + 2 ≤ b, '
        'tức **p ∈ [a, b − 2]**.')
    D.fig(P.fig('register'), 'Dấu hiệu s[x] tới 20 (cung đỏ: các cặp sinh đôi). Truy vấn [6, 20] chỉ đếm p trong [6, 18].', 15.5)

    D.h('2. Cách ngây thơ: Duyệt p trong đoạn')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ cho một truy vấn', 13)
    D.code('Cách ngây thơ: thử chia cho mỗi p', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O((b − a)√b) mỗi truy vấn.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (b ≤ 10^{4}, Q ≤ 100): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               'Sàng trước rồi duyệt dấu hiệu s[p] trên đoạn: O(b − a) mỗi truy vấn. Chương trình `mid.cpp` qua **subtask 2** (Q ≤ 100: 10^{9} phép cộng đơn giản, '
               + tm('mid.cpp', 2) + '), nhưng với Q = 10^{6} thì không: **' + S('mid.cpp') + ' điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Mỗi truy vấn vẫn đếm lại từ đầu trên đoạn của nó. Như bài 6.1, cần một mảng **tiền tố** để trả lời O(1); nhưng tiền tố của cái gì, và hiệu nào?'])

    D.h('4. Phá bế tắc: Tiền tố trên dấu hiệu tự chọn')
    D.p('Đặt t[x] = s[1] + s[2] + ... + s[x]. Số cặp nằm trọn trong [a, b] là tổng s[p] với p ∈ [a, b − 2]:')
    D.eq('**đáp số = t[b − 2] − t[a − 1]   (và bằng 0 nếu b − 2 < a).**')
    D.sub('Cái bẫy "trông như đúng"')
    D.p('Viết theo thói quen từ bài 6.1, t[b] − t[a − 1], là đếm mọi p ∈ [a, b], kể cả p = b − 1, b mà p + 2 đã vượt b. Chương trình `bay.cpp` sai ngay ở ví dụ 1:')
    D.fig(P.fig('trap'), 'Đoạn [6, 12] không chứa trọn cặp nào, nhưng t[12] − t[5] đếm cặp (11, 13).', 14)
    D.box('purple', 'BIÊN CỦA ĐOẠN', ['- Cần biết p + 2 có nguyên tố không với p tới 10^{7}: sàng tới 10^{7} + 2.',
                                      '- Khi b − a < 2 (đoạn có 1 hoặc 2 số), b − 2 < a: in 0 ngay, tránh hiệu âm hoặc truy cập t[−1].'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12)
    D.code('SINHDOI.CPP: sàng + tiền tố trên dấu hiệu cặp', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(N log log N) chuẩn bị, O(1) mỗi truy vấn. 10^{6} truy vấn chạy trong ' + tm('opt.cpp', 3) + '.')
    D.box('blue', 'MỞ RỘNG: "BỘ BA" HAY "CẶP CÁCH k"', ['Mẹo ghi danh tại phần tử nhỏ nhất dùng được cho mọi cấu hình có độ rộng cố định w: '
        'đếm các p ∈ [a, b − w]. Chẳng hạn cặp "anh em họ" (p, p + 4), hay bộ ba (p, p + 2, p + 6).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**t[b] − t[a − 1]:** đếm thừa cặp thò ra bên phải.', '**Sàng chỉ tới 10^{7}:** cần biết 10^{7} + 1, 10^{7} + 2 có nguyên tố không (hoặc chỉ ghi danh p ≤ 10^{7} − 2).',
               '**Đoạn quá ngắn:** b − 2 < a cho chỉ số âm.', '**Đọc ghi chậm** với 10^{6} truy vấn.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'bay.cpp', 'opt.cpp'])
