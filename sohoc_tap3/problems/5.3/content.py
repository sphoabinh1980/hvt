def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Kiểm tra 10^{5} số, mỗi số tới 2^{64} − 1 ≈ 1,8 · 10^{19}. Thử chia tới √n cần tới √n / 3 ≈ 1,4 · 10^{9} phép chia cho **một** số nguyên tố cỡ 2^{64}: '
        'không thể. Công cụ đúng là phép kiểm tra **Miller–Rabin** (Tập 1, Bài 5, Mở rộng 1), với ba yêu cầu: đúng thuật toán, '
        'đủ cơ số để không bị lừa, và nhân theo mô-đun không tràn số.')

    D.h('2. Cách ngây thơ: Thử chia 6k ± 1')
    D.fig(P.fig('naive'), 'Sơ đồ khối hàm kiểm tra bằng thử chia', 9)
    D.code('Cách ngây thơ: thử chia 6k ± 1 tới √n', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(√n) mỗi số. Với Q = 100 và n ≤ 10^{12}: 3,3 · 10^{7} phép chia, kịp. Với Q = 10^{5} số nguyên tố cỡ 10^{18}: 3 · 10^{13} phép chia.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1**: **' + str(P.pts('naive.cpp', 1)) + ' điểm**.', '**Subtask 2, 3**: quá giới hạn: **0 điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Thử chia đi tìm **một ước** của n; trong khi để kết luận "hợp số" chỉ cần một **nhân chứng** bất kì, '
                                 'và với số nguyên tố thì một tính chất đại số (định lí Fermat) luôn đúng. Miller–Rabin kiểm tra tính chất ấy trong O(log n) phép nhân.'])

    D.h('4. Phá bế tắc: Miller–Rabin tất định')
    D.sub('Ý tưởng')
    D.p('Viết n − 1 = d · 2^{s} với d lẻ. Nếu n nguyên tố và a không chia hết cho n thì a^{n−1} ≡ 1 (mod n) (Fermat), và vì trong mô-đun nguyên tố, '
        'x^{2} ≡ 1 chỉ có hai nghiệm x ≡ ±1, dãy')
    D.eq('**a^{d}, a^{2d}, a^{4d}, ..., a^{2^{s}·d} = a^{n−1}   (mod n)**')
    D.p('hoặc bắt đầu bằng 1, hoặc có một số hạng bằng n − 1 ở trước số 1 đầu tiên. Nếu dãy **không** như vậy thì a là **nhân chứng**: n chắc chắn là hợp số.')
    D.fig(P.fig('mrseq'), 'Ví dụ 2: dãy bình phương liên tiếp của bốn cơ số với n = 25 326 001 = 2251 · 11 251. Ba cơ số đầu "cho qua"; cơ số 7 vạch mặt n.', 15.5)
    D.sub('Bao nhiêu cơ số là đủ?')
    D.p('Một hợp số có thể "qua mặt" một vài cơ số (gọi là **số giả nguyên tố mạnh**). Bảng dưới liệt kê số nhỏ nhất qua mặt được k cơ số nguyên tố đầu tiên:')
    D.table(['Các cơ số', 'Số nhỏ nhất qua mặt được', 'Độ lớn'], [
        ['2', '2047 = 23 · 89', '≈ 2 · 10^{3}'],
        ['2, 3, 5', '25 326 001', '≈ 2,5 · 10^{7}'],
        ['2, 3, ..., 17 (7 cơ số)', '341 550 071 728 321', '≈ 3,4 · 10^{14}'],
        ['2, 3, ..., 31 (11 cơ số)', '3 825 123 056 546 413 051', '≈ 3,8 · 10^{18}'],
        ['2, 3, ..., 37 (12 cơ số)', '318 665 857 834 031 151 167 461', '> 2^{64}'],
    ], widths=[2.4, 3.6, 1.6])
    D.p('Vậy **12 cơ số 2, 3, ..., 37** cho kết quả chính xác tuyệt đối với mọi n < 2^{64}. Chương trình `mr11.cpp` bớt cơ số 37 "cho nhanh": '
        'nó đúng với mọi n ≤ 10^{18} (qua subtask 1, 2) nhưng trả lời YES với 3 825 123 056 546 413 051 ở subtask 3: **' + S('mr11.cpp') + ' điểm**. '
        'Tiết kiệm được chưa tới 10% thời gian, mất 30 điểm.')
    D.sub('Nhân theo mô-đun không tràn số')
    D.fig(P.fig('bits'), 'Tích hai số dư 64 bit cần 128 bit.', 12)
    D.p('Mọi phép nhân x · y mod n phải ép một thừa số sang `unsigned __int128` trước khi nhân. Ngoài ra n có thể lớn hơn 2^{63} − 1, '
        'nên phải đọc bằng `unsigned long long` (`%llu`).')
    D.box('purple', 'TRƯỜNG HỢP n CHIA HẾT CHO MỘT CƠ SỞ', ['Nếu a chia hết n thì a^{d} ≡ 0 (mod n), dãy toàn số 0 và kết luận "hợp số", sai khi n = a. '
                                                          'Vì vậy trước tiên xét n chia hết cho cơ số p nào: khi đó n nguyên tố khi và chỉ khi n = p.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối hàm Miller–Rabin', 12)
    D.code('NT64.CPP: Miller–Rabin 12 cơ số, nhân __int128', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** mỗi số tối đa 12 · (64 + 64) phép nhân theo mô-đun 128 bit, tức khoảng 1500 phép nhân. 10^{5} số nguyên tố cỡ 2^{64} chạy trong ' + tm('opt.cpp', 3) + '.')
    D.box('blue', 'MỞ RỘNG: ÍT CƠ SỞ HƠN MÀ VẪN ĐÚNG', ['Người ta đã tìm được bộ 7 cơ số {2, 325, 9375, 28178, 450775, 9780504, 1795265022} đúng với mọi n < 2^{64} '
                                                      '(Jim Sinclair, 2011). Khi dùng bộ này phải lấy a mod n và bỏ qua a ≡ 0.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Bớt cơ số:** mất subtask 3 vì một hợp số qua mặt 11 cơ số đầu.',
               '**Nhân 64 bit:** `a * b % n` tràn số mà không báo lỗi; kết quả sai với hầu hết n > 2^{32}.',
               '**Đọc bằng %lld:** n > 2^{63} − 1 bị đọc sai.',
               '**Quên n = 1, n = 2, n = cơ số:** xử lí riêng trước vòng Miller–Rabin.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mr11.cpp', 'opt.cpp'])
