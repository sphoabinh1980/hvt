def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Bài có hai phần: (1) liệt kê mọi ước của n theo thứ tự tăng dần; (2) với mỗi khách, tìm **ước nhỏ nhất không nhỏ hơn x** '
        '(hoặc −1 nếu x > n, vì n là ước lớn nhất). Phần (2) là câu hỏi quen thuộc "phần tử đầu tiên ≥ x trên một dãy tăng".')
    D.p('Kích thước: n ≤ 10^{12} nên chỉ được duyệt tới √n = 10^{6}; một số ≤ 10^{12} có nhiều nhất 6720 ước (đạt tại 963 761 198 400); '
        'và có tới Q = 10^{5} khách.')

    D.h('2. Cách ngây thơ: Thử mọi d, duyệt dãy cho mỗi khách')
    D.p('Thử d = 1, 2, ..., n: các ước tự động xuất hiện theo thứ tự tăng. Với mỗi khách, duyệt dãy ước từ đầu tới phần tử đầu tiên ≥ x.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ', 10)
    D.code('Cách ngây thơ: thử mọi d ≤ n', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n) để tìm ước, cộng O(Q · d(n)) cho các khách. Phần tìm ước đã là 10^{12} phép chia với n = 10^{12}.')

    D.h('3. Bế tắc')
    D.bullets([
        '**Subtask 1** (n ≤ 10^{6}, Q ≤ 100): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
        '**Subtask 2, 3** (n tới 10^{12}): vòng thử ước không chạy xong: **0 điểm**.'])
    D.p('Sửa phần tìm ước bằng cặp ước (bài 2.1) rồi sắp xếp, nhưng vẫn duyệt tuần tự cho mỗi khách, ta được `mid.cpp`. '
        'Phần duyệt khách giờ mới là phần nặng: trường hợp xấu nhất mỗi khách đi hết 6720 ước, Q = 10^{5} khách là **6,7 · 10^{8} phép so sánh**. '
        'Trên máy chấm của sách, test xấu nhất mất ' + tm('mid.cpp', 3) + ': vẫn kịp (' + S('mid.cpp') + ' điểm) vì mỗi phép so sánh rất rẻ, '
        'nhưng đã dùng gần một nửa thời gian cho phép; trên máy chấm chậm hơn hai lần là mất 50 điểm.')
    D.box('red', 'ĐIỂM BẾ TẮC', [
        'Dãy ước đã **tăng dần**, nhưng cách duyệt tuần tự không tận dụng điều đó: nó so sánh x với từng phần tử một. '
        'Trên dãy tăng, "phần tử đầu tiên ≥ x" tìm được bằng **tìm kiếm nhị phân** trong ⌈log_{2} 6720⌉ = 13 bước.'])

    D.h('4. Phá bế tắc: Ghép hai dãy, tìm kiếm nhị phân')
    D.sub('Bước 1. Dãy ước tăng dần không cần sắp xếp')
    D.p('Khi duyệt d tăng dần tới √n, các ước nhỏ d xuất hiện **tăng dần**, các ước lớn n / d xuất hiện **giảm dần**. Ghi chúng vào hai mảng riêng, '
        'rồi nối mảng thứ hai theo chiều ngược lại vào sau mảng thứ nhất.')
    D.fig(P.fig('merge'), 'Dãy ước của 36: nối ước nhỏ (tăng) với ước lớn đảo ngược. Ước 6 = √36 chỉ xuất hiện một lần.', 15)
    D.box('purple', 'VÌ SAO DÃY GHÉP TĂNG DẦN?', [
        'Mọi ước nhỏ đều ≤ √n, mọi ước lớn đều ≥ √n; trong mỗi nửa thứ tự đã đúng. Chỗ nối giữa hai nửa cũng đúng: '
        'ước nhỏ cuối cùng d_{max} ≤ √n ≤ n / d_{max}, đúng bằng phần tử đầu của nửa sau. Nếu d_{max} = √n (số chính phương) '
        'thì ta đã không cho n / d vào mảng lớn, nên không có phần tử lặp.'])
    D.sub('Bước 2. Tìm kiếm nhị phân')
    D.p('Hàm `lower_bound(ds.begin(), ds.end(), x)` của C++ trả về vị trí phần tử đầu tiên ≥ x (hoặc `ds.end()` nếu không có). '
        'Hình dưới chạy tay với x = 10 trên dãy ước của 36:')
    D.fig(P.fig('bsearch'), 'Tìm kiếm nhị phân: mỗi bước so sánh với phần tử giữa và bỏ đi một nửa khoảng (ô xanh) đang xét.', 15)

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 10)
    D.code('UOCTANG.CPP: ghép hai dãy ước + lower_bound', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(√n) để tìm ước, O(d(n)) để ghép, O(Q log d(n)) cho các khách: khoảng 10^{6} + 1,3 · 10^{6} phép tính. '
        'Test xấu nhất mất ' + tm('opt.cpp', 3) + ', phần lớn là thời gian đọc ghi.')
    D.box('blue', 'MỞ RỘNG: KHÔNG CẦN HAI MẢNG', [
        'Có thể chỉ dùng một mảng: đẩy các ước nhỏ vào, rồi duyệt ngược mảng ấy (bỏ qua √n nếu là số chính phương) và đẩy thêm n / d. '
        'Vì d giảm thì n / d tăng, phần sau tự động tăng dần.'])
    D.h('6. Bẫy thường gặp')
    D.bullets([
        '**In √n hai lần** khi n là số chính phương: dãy của 36 sẽ có hai số 6, và số ước thành 10.',
        '**Quên trường hợp x > n:** `lower_bound` trả về `end()`; truy cập `*it` lúc đó là lỗi. In −1.',
        '**Dùng int** cho n, x, ước: tất cả tới 10^{12}.',
        '**Sắp xếp lại không cần thiết:** không sai, nhưng là dấu hiệu chưa thấy cấu trúc "tăng – giảm" của hai nửa.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
