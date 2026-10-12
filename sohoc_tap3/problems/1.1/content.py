def build(D, P):
    D.h('1. Hiểu bài toán')
    D.p('Mỗi câu hỏi cho "hôm nay là thứ t" và một số nguyên k, hỏi k ngày sau (hoặc |k| ngày trước) là thứ mấy. '
        'Các ngày trong tuần lặp lại theo vòng tròn 7 ngăn, nên bài toán thực chất là: **đi k bước trên một vòng tròn 7 ngăn** '
        '(k âm thì đi ngược chiều). Đây đúng là phép chia có dư cho 7 của Tập 1, Bài 1.')
    D.p('Mẹo đầu tiên là **đánh số lại cho đẹp**: các thứ 2, 3, ..., 8 không bắt đầu từ 0 nên rất khó làm việc với phép chia có dư. '
        'Đặt d = t − 2 thì thứ Hai ứng với d = 0, thứ Ba d = 1, ..., Chủ nhật d = 6: đúng bảy số dư có thể có khi chia cho 7.')
    D.fig(P.fig('vong'), 'Bảy ngày trên vòng tròn; mỗi ngày mang thêm "số dư" d = t − 2. Đi k bước theo chiều kim đồng hồ là cộng k rồi lấy dư cho 7.', 14.5)
    D.p('Ví dụ 1, câu hỏi thứ nhất: thứ Hai (d = 0), k = 1000. Vì 1000 = 7 · 142 + 6, đi 1000 bước là đi đúng 142 vòng trọn vẹn '
        '(quay về chỗ cũ) rồi thêm 6 bước: tới d = 6, tức Chủ nhật, in ra 8.')

    D.h('2. Cách ngây thơ: Đếm từng ngày')
    D.p('Cách tự nhiên nhất là mô phỏng đúng như ta lật lịch: tiến (hoặc lùi) từng ngày một, mỗi lần cập nhật d, khi d vượt quá 6 thì quay về 0 '
        '(khi d nhỏ hơn 0 thì quay về 6).')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách đếm từng ngày cho một câu hỏi', 11.5)
    D.code('Cách ngây thơ: đếm từng ngày', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(|k|) cho mỗi câu hỏi, tổng cộng O(Q · max|k|). Với Q = 10^{5} và |k| = 10^{6} đã là 10^{11} bước; '
        'với |k| = 10^{18} thì một câu hỏi thôi cũng cần 10^{18} bước, tức chạy khoảng ba mươi năm.')

    D.h('3. Bế tắc')
    D.bullets([
        '**Subtask 1** (0 ≤ k ≤ 10^{6}): nghe như dễ, nhưng Q vẫn tới 10^{5}. Bộ test có các test Q = 10^{5}, k ≈ 10^{6}: '
        'khoảng 10^{11} bước, chạy quá giới hạn: **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
        '**Subtask 2, 3** (k tới 10^{18}): không bao giờ chạy xong: **0 điểm**.'])
    D.p('Một học sinh khác nhận ra ngay cần chia lấy dư và viết một dòng: `printf("%lld\\n", (t - 2 + k) % 7 + 2);`. '
        'Chương trình chạy tức thì, đúng hết hai subtask đầu (k ≥ 0) nhưng **sai** ở subtask 3: với t = 2, k = −100 nó in ra 0, '
        'một "thứ" không tồn tại. Tổng cộng **' + str(P.total('modam.cpp')) + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', [
        'Có tới 10^{18} ngày cần "đi qua", nhưng chỉ có **7 kết quả** có thể xảy ra. Đếm từng ngày là làm đi làm lại cùng một vòng tròn.',
        'Còn khi dùng phép %, toán tử % của C++ **không** cho số dư theo nghĩa toán học khi số bị chia âm.'])

    D.h('4. Phá bế tắc: Phép chia có dư')
    D.sub('Bước 1. Bỏ các vòng tròn trọn vẹn')
    D.p('Đi 7 bước trên vòng 7 ngăn là quay về chỗ cũ. Vậy đi k bước cũng như đi r bước, với r là số dư của k khi chia cho 7. '
        'Tổng quát hơn, vị trí sau khi đi là số dư của d + k khi chia cho 7:')
    D.eq('**d\' = (d + k) mod 7,   đáp số = d\' + 2,   với d = t − 2.**')
    D.box('purple', 'VÌ SAO ĐÚNG?', [
        'Viết k = 7q + r với 0 ≤ r < 7 (q có thể âm khi k âm). Đi 7q bước là đi |q| vòng trọn (xuôi hoặc ngược chiều), '
        'không thay đổi vị trí. Phần còn lại là r bước xuôi chiều. Hai số có cùng số dư khi chia cho 7 thì chỉ cùng một ngày: '
        'đó chính là đồng dư theo mô-đun 7 (Tập 1, Bài 1).',
        'Đặc biệt, **đi lùi |k| ngày** cũng là đi xuôi một số bước r ∈ [0, 7): lùi 1 ngày = tiến 6 ngày, lùi 100 ngày = tiến 5 ngày.'])
    D.sub('Bước 2. Lấy số dư không âm trong C++')
    D.p('Trong toán học, số dư của −100 khi chia cho 7 là 5, vì −100 = 7 · (−15) + 5. Nhưng C++ làm tròn thương **về phía 0** '
        '(thương là −14), nên `-100 % 7` bằng −2: kết quả mang dấu của số bị chia.')
    D.fig(P.fig('numline'), 'Trên trục số, −100 nằm giữa hai bội của 7 là −105 và −98. Số dư toán học đo từ bội bên trái (5); C++ đo từ bội gần 0 hơn (−2).', 15)
    D.p('Cách sửa quen thuộc: `x % 7` luôn nằm trong (−7, 7), nên cộng thêm 7 được một số trong (0, 14), lấy dư thêm một lần nữa là về [0, 7):')
    D.eq('`((x % 7) + 7) % 7`')
    D.sub('Chạy tay các ví dụ')
    D.table(['t', 'k', 'x = t − 2 + k', 'x % 7 (C++)', '((x % 7) + 7) % 7', 'In ra'], [
        ['2', '1000', '1000', '6', '6', '8'],
        ['2', '−100', '−100', '−2', '5', '7'],
        ['2', '10^{18}', '10^{18}', '1', '1', '3'],
        ['8', '0', '6', '6', '6', '8'],
        ['5', '−7', '−4', '−4', '3', '5'],
    ], widths=[0.7, 1.1, 1.6, 1.4, 1.9, 0.9], bold_cols=(5,))
    D.p('Dòng thứ hai chính là chỗ cách "một dòng" ở mục 3 sai: nó in −2 + 2 = 0. Dòng cuối là một bẫy khác: x = −4 âm dù k = −7 chia hết cho 7.')

    D.h('5. Cách tối ưu: O(1) mỗi câu hỏi')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 8.5)
    D.code('NGAYTHU.CPP: số dư không âm, O(1) mỗi câu hỏi', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(1) cho mỗi câu hỏi, O(Q) cho cả bài; bộ nhớ O(1). Phần lớn thời gian là đọc và in 10^{5} dòng, '
        'nên dùng scanf/printf.')
    D.box('blue', 'MỞ RỘNG: KHÔNG CẦN PHÉP % THỨ HAI', [
        'Có thể viết `long long d = x % 7; if (d < 0) d += 7;`. Cách này dễ đọc và nhanh hơn một chút. '
        'Khi lập trình, nên viết sẵn một hàm `mod(x, m)` trả về số dư không âm và dùng lại ở mọi bài của chương.'])

    D.h('6. Bẫy thường gặp')
    D.bullets([
        '**Quên số âm:** `(t - 2 + k) % 7 + 2` cho kết quả 0, −1, ..., −4 khi t − 2 + k < 0. Mất trọn subtask 3.',
        '**"Cộng cho chắc dương":** viết `(t - 2 + k + 7 * 1000000000000000000LL) % 7`: số 7 · 10^{18} đã vượt long long (≈ 9,2 · 10^{18}), tràn số. '
        'Nếu muốn cộng một bội của 7, chỉ cộng 7 sau khi đã lấy % 7.',
        '**Dùng int:** k tới 10^{18} phải đọc bằng `%lld` vào `long long`.',
        '**Quên đánh số lại:** lấy `t % 7` trực tiếp thì Chủ nhật (8) cho 1, thứ Bảy (7) cho 0: rất dễ nhầm. Đưa về d = t − 2 trước rồi mới tính.'])

    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'modam.cpp', 'opt.cpp'])
