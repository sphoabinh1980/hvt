def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Hai loại truy vấn là hai câu hỏi "ngược nhau" về cùng một dãy các số nguyên tố 2, 3, 5, 7, 11, ...: '
        'loại 1 hỏi **có bao nhiêu** số nguyên tố ≤ n, loại 2 hỏi số nguyên tố **ở vị trí** k. '
        'Mọi số trong bài đều ≤ 10^{7}, nhưng có tới **10^{6} truy vấn**: mỗi truy vấn phải được trả lời trong O(1).')
    D.fig(P.fig('arrays'), 'Hai mảng trả lời hai loại truy vấn (minh họa tới 20).', 15)

    D.h('2. Cách ngây thơ: Tính lại cho mỗi truy vấn')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ', 11)
    D.code('Cách ngây thơ: thử chia cho mỗi truy vấn', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** một truy vấn loại 1 tốn O(n√n) phép chia (khoảng 2 · 10^{10} với n = 10^{7}).')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (Q ≤ 100, số nhỏ): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               'Sàng một lần rồi dựng mảng đếm c[x] = π(x): loại 1 thành O(1). Nếu loại 2 vẫn "đếm dần trên mảng" thì mỗi truy vấn tốn tới 10^{7} bước: '
               'chương trình `mid.cpp` qua **subtask 2** (chỉ loại 1) nhưng không qua subtask 3: **' + S('mid.cpp') + ' điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Cả hai câu hỏi đều chỉ phụ thuộc vào **một** tập hợp cố định (các số nguyên tố ≤ 10^{7}). Hãy tính trước mọi câu trả lời có thể: '
                                 '10^{7} giá trị π(x) và 664 579 giá trị p_{k}.'])

    D.h('4. Phá bế tắc: Sàng một lần, hai mảng tra cứu')
    D.sub('Sàng Eratosthenes')
    D.fig(P.fig('sieve'), 'Sàng tới 30. Ô xanh đậm: số nguyên tố; mỗi hợp số ghi số nguyên tố đầu tiên gạch nó.', 15)
    D.p('Với mỗi p chưa bị gạch mà p · p ≤ N, gạch p², p² + p, p² + 2p, ... Tổng số phép gạch khoảng N · ln ln N ≈ 2,4 · 10^{7} với N = 10^{7}.')
    D.sub('Hai mảng')
    D.nums(['**c[x] = c[x − 1] + [x nguyên tố]** (c[0] = 0): trả lời loại 1 bằng c[n].',
            '**Danh sách pr**: duyệt x tăng dần, gặp số nguyên tố thì đẩy vào cuối; danh sách tự động tăng dần, trả lời loại 2 bằng pr[k − 1] (đánh số từ 0).'])
    D.box('purple', 'HAI MẢNG LÀ "NGHỊCH ĐẢO" CỦA NHAU', ['c[pr[k − 1]] = k với mọi k: số nguyên tố thứ k có đúng k số nguyên tố không vượt quá nó. '
                                                       'Ngược lại, pr[c[n] − 1] là số nguyên tố lớn nhất ≤ n.'])
    D.sub('Bộ nhớ')
    D.table(['Mảng', 'Kiểu', 'Số phần tử', 'Bộ nhớ'], [['comp (sàng)', 'char', '10^{7}', '10 MB'], ['c', 'int', '10^{7}', '40 MB'], ['pr', 'int', '664 579', '2,7 MB']],
            widths=[2, 1.2, 1.5, 1.3])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 13)
    D.code('DEMNGUYENTO.CPP: sàng + mảng đếm + danh sách', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(N log log N) để sàng, O(N) để dựng mảng, O(1) mỗi truy vấn. Phần lớn thời gian (' + tm('opt.cpp', 3) + ') là sàng và đọc ghi 10^{6} dòng.')
    D.box('blue', 'MỞ RỘNG: KHÔNG CẦN MẢNG c', ['Có thể bỏ mảng c (40 MB): π(n) là số phần tử ≤ n trong danh sách pr, tìm bằng `upper_bound(pr.begin(), pr.end(), n) - pr.begin()` '
                                              'trong O(log 664 579) = 20 bước. Đổi một chút thời gian lấy nhiều bộ nhớ.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Quên gạch số 1:** mọi π(n) lớn hơn đáp số đúng 1, danh sách lệch một vị trí.',
               '**Đánh số danh sách:** số nguyên tố thứ k là pr[k − 1].',
               '**Mảng lớn trong main:** khai báo toàn cục để không tràn ngăn xếp.',
               '**Đọc ghi chậm:** 10^{6} dòng vào, 10^{6} dòng ra: dùng scanf/printf.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
