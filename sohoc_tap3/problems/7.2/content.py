def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Số chữ số 0 tận cùng của n! trong hệ cơ số b là số k lớn nhất mà b^{k} | n!. Phân tích b = q_{1}^{k_{1}} ··· q_{m}^{k_{m}}: b^{t} | n! khi và chỉ khi '
        '**với mọi i**, n! chứa ít nhất t · k_{i} thừa số q_{i}. Gọi e_{q}(n!) là số mũ của q trong n!, ta được')
    D.eq('**đáp số = min_{i} ⌊ e_{q_{i}}(n!) / k_{i} ⌋.**')
    D.fig(P.fig('dots'), 'Đếm thừa số 2 và 3 trong 10! (mỗi chấm là một thừa số).', 15)

    D.h('2. Cách ngây thơ: Tính n!')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách tính thẳng n!', 11)
    D.code('Cách ngây thơ: tính n! rồi chia dần cho b', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n) phép nhân; nhưng 21! đã vượt 2^{64}, nên cách này chỉ đúng khi n ≤ 20.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (n ≤ 20): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               '**Subtask 2** (b = 10): số chữ số 0 thập phân của n! là số thừa số 5 (luôn ít hơn thừa số 2). Ghép hai trường hợp, `mid.cpp` được **' + S('mid.cpp') + ' điểm**.',
               '**Subtask 3** (b bất kì): cần một cách tổng quát.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['n! có hàng tỉ tỉ chữ số; ta không cần n!, chỉ cần **số mũ** của vài số nguyên tố trong n!. Và cần biết **số nguyên tố nào** quyết định đáp số.'])

    D.h('4. Phá bế tắc: Công thức Legendre')
    D.sub('Số mũ của p trong n!')
    D.p('Trong 1, 2, ..., n có ⌊n/p⌋ bội của p (mỗi số góp ít nhất một thừa số p), ⌊n/p²⌋ bội của p² (góp thêm một), ⌊n/p³⌋ bội của p³... Vậy')
    D.eq('**e_{p}(n!) = ⌊n/p⌋ + ⌊n/p^{2}⌋ + ⌊n/p^{3}⌋ + ...**')
    D.fig(P.fig('legendre'), 'Công thức Legendre với n = 2026, p = 3.', 15)
    D.p('Mỗi số hạng là số hạng trước chia cho p (⌊⌊n/p⌋/p⌋ = ⌊n/p²⌋), nên cài đặt `while (n) { n /= p; s += n; }` vừa gọn vừa không bao giờ tính p^{k} (với p ≈ 10^{12}, p² đã tràn).')
    D.sub('Không có số nguyên tố "quyết định"')
    D.p('Một lối tắt hấp dẫn: "chỉ cần xét ước nguyên tố **lớn nhất** của b, vì nó hiếm nhất trong n!". Sai! Với b = 12 = 2² · 3:')
    D.table(['n!', 'e_{2}', '⌊e_{2}/2⌋', 'e_{3}', '⌊e_{3}/1⌋', 'Đáp số', 'Quyết định bởi'], [
        ['8! = 2^{7} · 3^{2} · 5 · 7', '7', '3', '2', '2', '**2**', 'số 3'],
        ['9! = 2^{7} · 3^{4} · 5 · 7', '7', '3', '4', '4', '**3**', 'số 2'],
    ], widths=[2.6, 0.7, 1, 0.7, 1, 1, 1.4])
    D.p('Chương trình `bay.cpp` chỉ xét ước nguyên tố lớn nhất: đúng ở subtask 2 (với b = 10 thì 5 quả thật quyết định) nhưng sai cả subtask 1 lẫn 3: '
        '**' + S('bay.cpp') + ' điểm**. Phải lấy **min trên mọi** ước nguyên tố của b.')
    D.sub('Phân tích b')
    D.p('b ≤ 10^{12}: thử chia tới √b = 10^{6}; phần còn lại > 1 là một số nguyên tố (số mũ 1). T = 100 nên 10^{8} phép chia là chấp nhận được.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12)
    D.code('CHUSO0.CPP: Legendre cho mọi ước nguyên tố của b', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(√b) để phân tích b, mỗi lần gọi Legendre O(log_{p} n) ≤ 60 bước.')
    D.box('blue', 'MỞ RỘNG: SỐ MŨ CỦA 2 TRONG n!', ['e_{2}(n!) = n − s_{2}(n), với s_{2}(n) là số chữ số 1 trong biểu diễn nhị phân của n. '
        'Tổng quát: e_{p}(n!) = (n − s_{p}(n)) / (p − 1), s_{p} là tổng chữ số trong cơ số p. Ví dụ 2: 10^{18} có 24 chữ số 1 nên e_{2} = 10^{18} − 24.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Chỉ xét một ước nguyên tố** của b (lớn nhất, hoặc nhỏ nhất): sai với b = 12.',
               '**Quên chia cho k:** b = 12 chứa 2², nên mỗi chữ số 0 "tiêu" hai thừa số 2.',
               '**Tính p^{k} trực tiếp:** tràn số khi p lớn.',
               '**n = 0:** 0! = 1, không có chữ số 0 nào; vòng Legendre cho 0, đúng.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'bay.cpp', 'opt.cpp'])
