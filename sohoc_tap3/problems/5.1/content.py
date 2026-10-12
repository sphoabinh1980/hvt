def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Cần tìm số nguyên tố p làm |p − n| nhỏ nhất, khi hòa thì lấy số nhỏ hơn. Cách tìm tự nhiên là **loang ra hai phía**: '
        'xét khoảng cách d = 0, 1, 2, ...; với mỗi d xét n − d **trước** n + d. Số nguyên tố đầu tiên gặp được chính là đáp số, '
        'và thứ tự "trái trước phải sau" tự động xử lí luật hòa.')
    D.fig(P.fig('loang'), 'Loang ra hai phía từ n = 26; số trong vòng tròn là thứ tự kiểm tra.', 15)
    D.p('Bài toán vì thế chỉ còn một câu hỏi: **kiểm tra một số tới 10^{12} có nguyên tố không, đủ nhanh**. '
        'Quanh 10^{12}, khoảng cách giữa hai số nguyên tố liên tiếp chỉ vài trăm, nên số lần kiểm tra mỗi lượt chơi rất ít; '
        'phần lớn số bị loại ngay ở phép chia cho 2, 3, 5, 7. Lần kiểm tra **đắt nhất** là lần cuối cùng, khi số đang xét thực sự là số nguyên tố.')

    D.h('2. Cách ngây thơ: Thử chia tới n − 1')
    D.fig(P.fig('naive'), 'Sơ đồ khối phần loang ra hai phía (giống nhau ở mọi cách làm)', 9)
    D.code('Cách ngây thơ: kiểm tra nguyên tố bằng thử chia tới x − 1', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** kiểm tra một số nguyên tố p tốn p − 2 phép chia: 10^{9} phép chia với p ≈ 10^{9}, nhân thêm 100 lượt chơi.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (n ≤ 1000): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               'Chỉ thử chia tới √x (hợp số luôn có ước ≤ √x): chương trình `mid.cpp` qua **subtask 2** (10^{9}: 31 623 phép chia mỗi số nguyên tố). '
               'Nhưng với n ≈ 10^{12}, mỗi số nguyên tố tốn 10^{6} phép chia 64 bit, 100 lượt là 10^{8} phép chia: test lớn nhất mất '
               + tm('mid.cpp', 3) + ', vượt giới hạn. Tổng **' + S('mid.cpp') + ' điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Thử chia cho **mọi** i ≤ √x là lãng phí: nếu x không chia hết cho 2 thì cũng không chia hết cho 4, 6, 8, ...; '
                                 'không chia hết cho 3 thì cũng không chia hết cho 9, 15, ... Chỉ cần thử các ước có thể là **số nguyên tố**.'])

    D.h('4. Phá bế tắc: Chỉ thử 6k ± 1')
    D.p('Xếp các số tự nhiên thành bảng 6 cột theo số dư khi chia cho 6: các cột 6k, 6k + 2, 6k + 4 chứa toàn số chẵn, cột 6k + 3 chứa toàn bội của 3. '
        'Vậy mọi số nguyên tố lớn hơn 3 đều nằm ở cột **6k + 1** hoặc **6k + 5 = 6(k + 1) − 1**.')
    D.fig(P.fig('wheel'), 'Các số 1..41 xếp theo số dư khi chia cho 6. Ô vàng: số nguyên tố; chúng (trừ 2, 3) chỉ nằm ở hai cột.', 15)
    D.p('Do đó, sau khi loại các số chia hết cho 2 hoặc 3, ta chỉ cần thử chia cho các cặp i, i + 2 với i = 5, 11, 17, ... (i = 6k − 1, i + 2 = 6k + 1) '
        'trong khi i · i ≤ x: khoảng √x / 3 phép chia, ít hơn ba lần so với thử mọi i.')
    D.box('purple', 'VÌ SAO ĐÚNG?', ['Nếu x là hợp số thì x có một ước nguyên tố p ≤ √x. Nếu p = 2 hoặc 3 thì đã bị loại ở bước đầu; nếu p > 3 thì p có dạng 6k ± 1, '
                                     'và vòng lặp thử đúng mọi số dạng này (kể cả một số hợp số như 25, 35: thừa nhưng vô hại).'])
    D.sub('Chạy tay ví dụ 2')
    D.table(['n', 'd', 'Số được kiểm tra', 'Kết quả'], [
        ['1', '0; 1', '1 (không nguyên tố); 0 (không), 2 (nguyên tố)', '**2**'],
        ['12', '0; 1', '12 (chẵn); 11 (nguyên tố)', '**11**'],
        ['999 999 549 106', '0..153', '306 số, phần lớn bị loại bởi 2, 3, 5, 7', '**999 999 548 953**'],
        ['10^{12}', '0..11', '10^{12} − 11 = 999 999 999 989 nguyên tố', '**999 999 999 989**'],
    ], widths=[2, 1, 4.3, 2.2], align=['center', 'center', 'left', 'center'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối hàm kiểm tra nguyên tố tối ưu', 10)
    D.code('NTGANNHAT.CPP: loang hai phía + thử chia 6k ± 1', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** mỗi lượt chơi khoảng √n / 3 ≈ 333 334 phép chia cho lần kiểm tra thành công, cộng vài trăm lần kiểm tra thất bại rất rẻ. '
        '100 lượt: khoảng 3,3 · 10^{7} phép chia, test lớn nhất mất ' + tm('opt.cpp', 3) + '.')
    D.box('blue', 'MỞ RỘNG: KHI n TỚI 10^{18}', ['Thử chia tới √n = 10^{9} không còn khả thi. Khi đó dùng kiểm tra Miller–Rabin (bài NT64, 5.3): '
                                                 'mỗi lần kiểm tra chỉ khoảng 12 · 64 phép nhân theo mô-đun.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**n = 1:** 0 và 1 không nguyên tố; hàm kiểm tra phải trả về "sai" với x < 2, nếu không sẽ in 1 hoặc 0.',
               '**Biến i kiểu int:** i * i tràn khi i > 46 340; với x ≈ 10^{12} vòng lặp không dừng đúng chỗ.',
               '**Xét n + d trước n − d:** sai luật hòa (ví dụ n = 12 phải in 11, không phải 13).',
               '**Gọi sqrt mỗi vòng lặp:** chậm và có thể lệch ±1; dùng i * i <= x.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
