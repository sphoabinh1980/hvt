def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Kim nhảy k vạch mỗi giây sẽ thăm các vạch 0, k, 2k, ... (mod n). Các vị trí này đúng là các bội của g = gcd(k, n) (Bézout: tập {t·k mod n} là tập các bội của g). '
        'Vậy kim thăm đủ n vạch khi và chỉ khi g = 1. Đáp số là **số k ∈ [1, n] nguyên tố cùng nhau với n**, tức **hàm φ(n)** của Euler (Tập 1, Bài 11).')
    D.fig(P.fig('clocks'), 'Mặt đồng hồ 12 vạch: bước 5 đi qua đủ 12 vạch, bước 4 chỉ quanh quẩn ở 0, 4, 8.', 15)
    D.p('Riêng n = 1: mặt đồng hồ chỉ có vạch 0, k = 1 thỏa mãn, φ(1) = 1.')

    D.h('2. Cách ngây thơ: Đếm trực tiếp')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách đếm trực tiếp', 12)
    D.code('Cách ngây thơ: đếm k với gcd(k, n) = 1', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n log n) mỗi câu hỏi: 10^{4} · 14 phép chia với n = 10^{4}, nhưng 10^{12} · 40 với n = 10^{12}.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1**: **' + str(P.pts('naive.cpp', 1)) + ' điểm**.', '**Subtask 2, 3**: **0 điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Đếm từng số là không cần thiết: các số **không** nguyên tố cùng nhau với n là các bội của ước nguyên tố của n, và tỉ lệ của chúng có công thức chính xác.'])

    D.h('4. Phá bế tắc: Công thức tích')
    D.eq('**φ(n) = n · Π_{p | n} (1 − 1/p),**')
    D.p('tích lấy qua các ước nguyên tố **khác nhau** của n. Trực giác: trong 1..n, đúng 1/p số chia hết cho p; bỏ chúng đi, rồi bỏ tiếp 1/q phần còn lại cho ước q khác...')
    D.fig(P.fig('sieve12'), 'φ(12): loại các số chia hết cho 2, rồi cho 3.', 15)
    D.p('Cài đặt bằng số nguyên: `res -= res / p` (luôn chia hết vì res vẫn còn chứa thừa số p). Thử chia tới √n để tìm ước nguyên tố; **sau vòng lặp**, nếu phần còn lại n > 1 '
        'thì đó là một ước nguyên tố lớn hơn √n ban đầu, phải nhân thêm (1 − 1/n).')
    D.p('Chương trình `bay.cpp` quên đúng dòng cuối ấy: với n = 7 nó trả về 7 (vòng thử chia không tìm thấy ước nào), sai ngay ở ví dụ 1: **' + S('bay.cpp') + ' điểm**.')
    D.box('purple', 'VÌ SAO CHỈ CÒN MỘT ƯỚC LỚN?', ['Sau khi chia hết mọi ước nguyên tố p ≤ √n, phần còn lại không có ước nguyên tố nào ≤ √n. Nếu nó có hai thừa số nguyên tố thì tích > n: vô lí. '
        'Vậy phần còn lại là 1 hoặc **đúng một** số nguyên tố.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối hàm φ(n)', 14)
    D.code('PHI.CPP: φ(n) bằng thử chia, O(√n)', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(√n): thử 2 rồi các số lẻ, khoảng 5 · 10^{5} phép chia với n ≈ 10^{12}; 100 số nguyên tố cỡ 10^{12} chạy trong '
        + P.scores['opt.cpp']['detail'][2].split()[1].replace('.', ',').replace('s', ' giây') + '.')
    D.box('blue', 'MỞ RỘNG: φ LÀ HÀM NHÂN TÍNH', ['φ(ab) = φ(a)φ(b) khi gcd(a, b) = 1, và φ(p^{k}) = p^{k} − p^{k−1}. Từ đó suy ra công thức tích. '
        'Một hệ quả đẹp: Σ_{d | n} φ(d) = n (phân loại các số 1..n theo gcd của chúng với n).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Quên ước nguyên tố lớn còn lại.**', '**Nhân bằng số thực** n · (1 − 1/p): sai số làm tròn.', '**Biến p kiểu int:** p * p tràn.', '**n = 1:** trả về 1 (vòng lặp không chạy, res = 1).'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'bay.cpp', 'opt.cpp'])
