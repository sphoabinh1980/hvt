def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Cạnh s của miếng vuông phải chia hết cả a lẫn b (để cắt vừa khít theo cả hai chiều). Cạnh lớn nhất như vậy chính là '
        '**ƯCLN g = gcd(a, b)**, và số miếng là (a / g) · (b / g).')
    D.fig(P.fig('tiles'), 'Tấm 252 × 105 cắt thành 12 · 5 = 60 miếng cạnh 21.', 15)
    D.p('Bài toán có hai cái khó tách biệt nhau: tính gcd của hai số tới 10^{18} cho 10^{5} tấm gạch, và **in ra một số miếng có thể tới gần 10^{36}**.')

    D.h('2. Cách ngây thơ: Thử cạnh giảm dần')
    D.p('Bắt đầu từ s = min(a, b) và giảm dần cho tới khi s chia hết cả a và b. Số đầu tiên gặp được là ƯCLN.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử cạnh giảm dần', 9.5)
    D.code('Cách ngây thơ: thử cạnh giảm dần', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** tới min(a, b) bước mỗi tấm (khi a, b nguyên tố cùng nhau, phải giảm tới tận s = 1). Với T = 10, a, b ≤ 10^{6}: 10^{7} bước, ổn. '
        'Với T = 10^{5}, a, b ≤ 10^{9}: tới 10^{14} bước.')

    D.h('3. Bế tắc')
    D.bullets([
        '**Subtask 1** (T ≤ 10, a, b ≤ 10^{6}): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
        '**Subtask 2, 3**: quá giới hạn thời gian: **0 điểm**.'])
    D.p('Thay vòng thử bằng thuật toán Euclid (Tập 1, Bài 3) là đủ nhanh: chương trình `mid.cpp` qua subtask 2 trong vài phần trăm giây. '
        'Nhưng nó in số miếng bằng `long long`: ở subtask 3, (a / g) · (b / g) có thể tới 10^{36}, phép nhân tràn số mà không báo lỗi. '
        'Kết quả **' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', [
        '(1) Tìm ƯCLN bằng cách thử từng số là quá chậm; Euclid chỉ cần khoảng 85 bước với số ≤ 10^{18}.',
        '(2) Đáp số vượt khỏi mọi kiểu số nguyên 64 bit; cần kiểu 128 bit và tự viết hàm in.'])

    D.h('4. Phá bế tắc: Euclid và số nguyên 128 bit')
    D.sub('Bước 1. Thuật toán Euclid')
    D.p('gcd(a, b) = gcd(b, a mod b), và gcd(a, 0) = a. Mỗi hai bước, số nhỏ hơn giảm ít nhất một nửa, nên số bước là O(log min(a, b)); '
        'trường hợp xấu nhất là hai số Fibonacci liên tiếp (bộ test có cặp F_{87}, F_{86} cỡ 10^{18}).')
    D.table(['Bước', 'a', 'b', 'a mod b'], [['1', '252', '105', '42'], ['2', '105', '42', '21'], ['3', '42', '21', '0'], ['4', '21', '0', '→ g = **21**']],
            widths=[1, 1.5, 1.5, 2])
    D.sub('Bước 2. Ước lượng độ lớn của mọi đại lượng')
    D.fig(P.fig('sizes'), 'Độ lớn (số mũ của 10) của các đại lượng trong bài so với sức chứa của các kiểu số.', 14)
    D.p('a, b, g, a / g, b / g đều ≤ 10^{18} và vừa `unsigned long long`. Chỉ có tích cuối cùng cần 128 bit: ép **một thừa số** sang '
        '`unsigned __int128` **trước khi nhân**: `(u128)(a / g) * (b / g)`.')
    D.box('purple', 'VÌ SAO PHẢI CHIA TRƯỚC?', [
        'Công thức a · b / g^{2} cũng đúng về mặt toán, nhưng a · b tới 10^{36} và g^{2} tới 10^{36}: tích a · b vẫn vừa __int128, '
        'còn g^{2} cũng vậy, nhưng chỉ cần thêm một phép nhân trung gian là vượt. Chia trước khiến cả hai thừa số ≤ 10^{18}, tích chắc chắn < 2^{128}.'])
    D.sub('Bước 3. In số 128 bit')
    D.p('`printf` và `cout` không biết in `__int128`. Ta tách chữ số bằng phép chia cho 10 (chữ số hàng đơn vị ra trước), cất vào mảng rồi in ngược lại. '
        'Vòng `do ... while` đảm bảo số 0 vẫn in ra "0".')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu cho một tấm gạch', 10)
    D.code('CATGACH.CPP: Euclid + unsigned __int128', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(log min(a, b)) mỗi tấm (≤ 90 phép chia), cộng khoảng 37 phép chia 128 bit để in. Cả bộ 10^{5} tấm chạy trong '
        + P.scores['opt.cpp']['detail'][2].split()[1].replace('.', ',').replace('s', ' giây') + '.')
    D.box('blue', 'MỞ RỘNG: std::gcd', [
        'Từ C++17 có sẵn `std::gcd` trong `<numeric>` (và `__gcd` của GCC). Tự viết Euclid vẫn đáng giá: em sẽ cần sửa nó thành Euclid mở rộng ở Bài 4.'])
    D.h('6. Bẫy thường gặp')
    D.bullets([
        '**Tràn số ở số miếng:** đáp số tới 10^{36}; long long chỉ tới 9,2 · 10^{18}.',
        '**Ép kiểu sai chỗ:** `(u128)((a / g) * (b / g))` nhân trong 64 bit rồi mới ép, vô ích. Phải ép trước khi nhân.',
        '**Đọc bằng %d:** a, b tới 10^{18} cần `%lld`/`%llu`.',
        '**Đệ quy Euclid sâu:** không sao (≤ 90 tầng), nhưng vòng lặp vẫn gọn hơn.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
