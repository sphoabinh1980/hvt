def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Mỗi cách xếp n học sinh thành r hàng, mỗi hàng c bạn (r · c = n) ứng với đúng **một ước r của n**. Hai ước bị loại là r = 1 (một hàng ngang) '
        'và r = n (một hàng dọc), vì đề yêu cầu r ≥ 2 và c ≥ 2. Vậy:')
    D.bullets(['**Số cách xếp** k = d(n) − 2, với d(n) là số ước của n (nếu kết quả ≤ 0 thì in 0).',
               '**Cách cân đối nhất** (r ≤ c, c − r nhỏ nhất) có r là ước lớn nhất của n không vượt quá √n, và c = n / r.'])
    D.fig(P.fig('grids'), 'Bốn cách xếp 12 học sinh; 12 có 6 ước, bỏ hai cách 1 × 12 và 12 × 1.', 15)
    D.p('Vì sao r lớn nhất ≤ √n cho hiệu c − r nhỏ nhất? Với r ≤ √n, khi r tăng thì c = n / r giảm, nên hiệu c − r giảm. '
        'Vậy trong các ước r ≤ √n, ước lớn nhất cho hiệu nhỏ nhất.')

    D.h('2. Cách ngây thơ: Thử mọi d từ 1 tới n')
    D.p('Thử từng d = 1, 2, ..., n; nếu d chia hết n thì đếm (khi 2 ≤ d ≤ n/2) và ghi nhận d làm r (khi d · d ≤ n).')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử mọi d', 11)
    D.code('Cách ngây thơ: thử mọi d từ 1 tới n', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n) phép chia mỗi số. Với T = 10 và n = 10^{7}: 10^{8} phép chia lấy dư, mất khoảng '
        + P.scores['naive.cpp']['detail'][1].split()[1].replace('.', ',').replace('s', ' giây') + ' trên máy chấm. Với n = 10^{12}: 10^{13} phép chia, cả giờ đồng hồ.')

    D.h('3. Bế tắc')
    D.bullets([
        '**Subtask 1, 2** (n ≤ 10^{7}): chạy kịp: **' + str(P.pts('naive.cpp', 1) + P.pts('naive.cpp', 2)) + ' điểm**.',
        '**Subtask 3** (n ≤ 10^{12}): quá giới hạn thời gian: **0 điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', [
        'Ước của n đi thành **cặp** (d, n / d). Thử mọi d tới n là tìm mỗi cặp hai lần, và tốn công vô ích cho nửa trên rất dài [√n, n]: '
        'với n = 10^{12}, nửa dưới chỉ có 10^{6} số, nửa trên có gần 10^{12} số.'])

    D.h('4. Phá bế tắc: Cặp ước')
    D.fig(P.fig('pairs'), 'Các ước của 36 xếp tăng dần; mỗi cung nối một cặp (d, 36 / d). Chỉ cần duyệt nửa trái d ≤ √36 = 6.', 15)
    D.nums([
        '**Mỗi ước d ≤ √n cho thêm ước n / d ≥ √n.** Duyệt d từ 1 tới √n, mỗi lần gặp ước thì cộng 2 vào số ước.',
        '**Số chính phương:** nếu d · d = n thì d và n / d là cùng một số, chỉ cộng 1. Với n = 36, ước 6 chỉ được đếm một lần: 9 ước, 7 cách xếp.',
        '**Cách cân đối nhất:** d duyệt tăng dần tới √n nên ước **cuối cùng** gặp được chính là r cần tìm. Không cần mảng, không cần sắp xếp.',
        '**Trường hợp suy biến:** n = 1 có 1 ước, n nguyên tố có 2 ước: d(n) − 2 ≤ 0, in 0.'])
    D.box('purple', 'VÌ SAO CHỈ CẦN TỚI √n?', [
        'Nếu d · e = n và cả d, e đều lớn hơn √n thì d · e > √n · √n = n: vô lí. Vậy trong mỗi cặp ước luôn có một số ≤ √n. '
        'Duyệt hết các d ≤ √n là "nhìn thấy" mọi cặp.'])
    D.sub('Bẫy tràn số ở điều kiện d · d ≤ n')
    D.p('Chương trình `intd.cpp` làm đúng như trên nhưng khai báo `int d`. Với n ≤ 10^{7} không sao, nhưng với n cỡ 10^{12}, khi d vượt 46 341 thì '
        'd · d (tính bằng int) vượt 2^{31} − 1 ≈ 2,1 · 10^{9} và bị tràn thành số âm, điều kiện `d * d <= n` vẫn đúng, vòng lặp không dừng đúng chỗ. '
        'Kết quả: **' + S('intd.cpp') + ' điểm**, mất trọn subtask 3.')
    D.sub('Chạy tay với n = 36')
    D.table(['d', '1', '2', '3', '4', '5', '6'], [
        ['36 mod d', '0', '0', '0', '0', '1', '0'],
        ['cộng vào cnt', '+2 (1, 36)', '+2 (2, 18)', '+2 (3, 12)', '+2 (4, 9)', '–', '+1 (6 · 6 = 36)'],
        ['r', '1', '2', '3', '4', '4', '**6**'],
    ], widths=[1.5, 1.1, 1.1, 1.1, 1.1, 0.7, 1.5])
    D.p('cnt = 9, k = 9 − 2 = 7, cách cân đối nhất 6 × 6: in "7 6 6".')

    D.h('5. Cách tối ưu: Duyệt cặp ước tới √n')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12)
    D.code('XEPHANG.CPP: duyệt cặp ước, O(√n)', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(√n) mỗi số: với n = 10^{12} là 10^{6} phép chia; T = 10 số chỉ 10^{7} phép chia, khoảng '
        + P.scores['opt.cpp']['detail'][2].split()[1].replace('.', ',').replace('s', ' giây') + '.')
    D.box('blue', 'MỞ RỘNG: NHIỀU SỐ HƠN', [
        'Nếu T lên tới 10^{4}, O(T√n) = 10^{10} là quá chậm. Khi đó nên sàng các số nguyên tố tới 10^{6} một lần, rồi phân tích n bằng cách chỉ thử chia cho số nguyên tố '
        '(78 498 số) và dùng công thức d(n) = (e_{1} + 1) ··· (e_{k} + 1) (Bài 7). Riêng ước lớn nhất ≤ √n thì phải sinh mọi ước từ phân tích.'])

    D.h('6. Bẫy thường gặp')
    D.bullets([
        '**n = 1:** công thức d(n) − 2 cho −1. Phải in 0.',
        '**Số chính phương:** đếm √n hai lần làm sai cả số cách lẫn kết quả "7 6 6" của n = 36.',
        '**Biến chạy kiểu int:** `d * d` tràn khi n vượt khoảng 2,1 · 10^{9}. Dùng `long long d`.',
        '**Dùng sqrt số thực:** `for (d = 1; d <= sqrt(n); d++)` gọi sqrt mỗi vòng (chậm) và có thể sai ±1 với số lớn. Điều kiện `d * d <= n` vừa nhanh vừa chính xác.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'intd.cpp', 'opt.cpp'])
