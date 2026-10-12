def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Đặt L = min(n, m), a = ⌊n/i⌋, b = ⌊m/i⌋. Viết số dư qua thương như bài 16.2:')
    D.eq('(n mod i) · (m mod i) = (n − a · i)(m − b · i) = **nm − (nb + ma) · i + ab · i^{2}**')
    D.p('Nếu trên một đoạn [i, j] cả a lẫn b đều không đổi, biểu thức trên là **đa thức bậc hai** theo i với hệ số cố định, và tổng của nó trên đoạn là')
    D.eq('nm · (j − i + 1) − (nb + ma) · Σ_{t=i..j} t + ab · Σ_{t=i..j} t^{2}')
    D.p('với Σ t = S_{1}(j) − S_{1}(i − 1), Σ t^{2} = S_{2}(j) − S_{2}(i − 1), S_{1}(r) = r(r + 1)/2 và S_{2}(r) = r(r + 1)(2r + 1)/6.')

    D.h('2. Cách ngây thơ: Cộng trực tiếp')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ', 12)
    D.code('Cách ngây thơ: O(min(n, m))', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(min(n, m)): 10^{7} bước chạy ' + P.scores['naive.cpp']['detail'][0].split()[1] + ' (**' + str(P.pts('naive.cpp', 1)) + ' điểm**).')

    D.h('3. Bế tắc')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Cần chia [1, L] thành ít đoạn mà trên mỗi đoạn **cả hai** thương không đổi. Chia theo một thương như bài 16.2 là chưa đủ.'])
    D.p('Chương trình `trap.cpp` chỉ chia khối theo ⌊n/i⌋ và coi b = ⌊m/i⌋ (tính tại đầu khối) là hằng số trên cả khối. '
        'Khi n = m hai cách chia trùng nhau nên đúng (subtask 2); ở mọi trường hợp khác sai, kể cả ví dụ 1: **' + S('trap.cpp') + ' điểm**.')

    D.h('4. Phá bế tắc: Khối chung của hai thương')
    D.fig(P.fig('common'), 'Ví dụ 1 (n = 10, m = 7): khối chung là giao của hai cách chia.', 15.2)
    D.p('Khối của n chứa i kết thúc tại ⌊n/a⌋, khối của m kết thúc tại ⌊m/b⌋. Cả hai thương cùng không đổi trên [i, j] với')
    D.eq('**j = min(⌊n/a⌋, ⌊m/b⌋)**')
    D.p('Mỗi lần nhảy i ← j + 1, ít nhất một trong hai thương đổi giá trị, nên số khối chung không vượt quá (số khối của n) + (số khối của m) ≤ 2√n + 2√m ≤ 4 · 10^{6}. '
        'Với n = m = 10^{12} có đúng 1 999 999 khối; với n = 10^{12}, m = 10^{12} − 1 có 2 000 082 khối.')
    D.sub('Chạy tay ví dụ 1')
    D.table(['Khối', 'a', 'b', 'Các tích (n mod i)(m mod i)', 'Tổng khối'], [
        ['1', '10', '7', '0 · 0', '0'], ['2', '5', '3', '0 · 1', '0'], ['3', '3', '2', '1 · 1', '1'],
        ['[4, 5]', '2', '1', '2 · 3,  0 · 2', '6'], ['[6, 7]', '1', '1', '4 · 1,  3 · 0', '4'], ['', '', '', '**S**', '**11**']],
        widths=[1.2, 0.7, 0.7, 3.4, 1.4], align=['center'] * 5, sz=20, hl=[5])
    D.p('Kiểm tra bằng công thức khối [4, 5]: nm · 2 − (10 · 1 + 7 · 2)(4 + 5) + 2 · 1 · (16 + 25) = 140 − 216 + 82 = 6.')
    D.box('blue', 'TRÁNH TRÀN SỐ', ['Với r = 10^{12}, tích r(r + 1)(2r + 1) cỡ 2 · 10^{36}: tính bằng __int128, chia 6 trên số nguyên đúng rồi mới lấy dư (tích r(r+1)(2r+1) luôn chia hết cho 6).',
                                    'n, m, a, b đều tới 10^{12}: lấy dư từng đại lượng trước khi nhân. Có một phép trừ: cộng MOD trước khi lấy dư.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 13)
    D.code('HAITHUONG.CPP: khối chung, ba tổng Σ1, Σi, Σi²', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(√n + √m), khoảng 2 · 10^{6} khối, chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Cùng cách: Σ ⌊n/i⌋ · ⌊m/i⌋ (đếm cặp, xuất hiện trong bài toán đếm cặp nguyên tố cùng nhau bằng hàm Möbius) dùng khối chung y hệt.',
                              'Thay S_{2} bằng tổng lũy thừa bậc cao hơn nếu biểu thức có bậc cao hơn theo i.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Chia khối theo một thương.**', '**Chạy i tới max(n, m):** thương của số nhỏ bằng 0, chia cho 0.',
               '**Chia 6 sau khi lấy dư:** sai; hoặc chia trước trên __int128, hoặc nhân nghịch đảo 166 666 668.',
               '**Không lấy dư a, b, n, m trước khi nhân:** tích tới 10^{24}.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'trap.cpp', 'opt.cpp'])
