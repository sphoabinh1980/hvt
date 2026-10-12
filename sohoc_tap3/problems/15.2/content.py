def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Gọi f[x] là số cách lên đúng bậc x. Bước cuối cùng tới bậc x xuất phát từ bậc x − 1, x − 2 hoặc x − 3, nên')
    D.eq('**f[x] = f[x − 1] + f[x − 2] + f[x − 3]** (bậc x tốt),   **f[x] = 0** (bậc x hỏng),   f[0] = 1.')
    D.p('Bậc hỏng không chặn đường: các bậc phía trên vẫn cộng f[x − 1], f[x − 2], f[x − 3] như thường, chỉ có số hạng của chính bậc hỏng bằng 0.')
    D.fig(P.fig('stairs'), 'Ví dụ 2 (n = 6, bậc 2 và 4 hỏng): các mũi tên là những bước của bốn cách đi.', 15.2)
    D.p('Ví dụ 3: ba bậc hỏng liên tiếp 5, 6, 7 cho f[5] = f[6] = f[7] = 0, nên f[8] = 0 và mọi bậc phía trên cũng bằng 0.')

    D.h('2. Cách ngây thơ: Quy hoạch động trên mọi bậc')
    D.fig(P.fig('naive'), 'Sơ đồ khối của quy hoạch động', 11)
    D.code('Cách ngây thơ: f[0..n]', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n) thời gian và bộ nhớ. Với n ≤ 10^{6}: **' + str(P.pts('naive.cpp', 1)) + ' điểm** subtask 1.')

    D.h('3. Bế tắc')
    D.p('Khi không có bậc hỏng (subtask 2), f là dãy Tribonacci và có thể nhảy thẳng tới bậc n bằng lũy thừa ma trận 3 × 3, giống bài 15.1. '
        'Chương trình `mid.cpp` ghép hai cách: QHĐ khi n ≤ 10^{6}, lũy thừa ma trận khi n lớn (bỏ qua bậc hỏng): **' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['n = 10^{18} và có bậc hỏng: không lặp từng bậc được, mà dãy f lại không còn là một dãy truy hồi "đều" trên toàn bộ [0, n]. '
                                  'Nhưng chỉ có tối đa 10^{4} chỗ "gãy"; giữa hai chỗ gãy, dãy vẫn là Tribonacci.'])

    D.h('4. Phá bế tắc: Lũy thừa ma trận theo từng đoạn')
    D.sub('Ma trận đồng hành')
    D.fig(P.fig('matrix'), 'Một bước đi lên của vectơ trạng thái v = (f[x], f[x − 1], f[x − 2]).', 14)
    D.sub('Tại bậc hỏng chỉ sửa một thành phần')
    D.p('Đi từ bậc cur tới bậc hỏng x tiếp theo: v ← T^{x − cur} · v, khi đó v = (f[x], f[x − 1], f[x − 2]) tính **như thể** x tốt. '
        'Gán v[0] ← 0 là xong: f[x − 1], f[x − 2] không đổi, và từ đây hệ thức Tribonacci lại đúng cho x + 1, x + 2, ...')
    D.fig(P.fig('seg'), 'Chia [0, n] thành K + 1 đoạn: mỗi đoạn một lần lũy thừa, mỗi bậc hỏng một phép gán.', 15)
    D.box('blue', 'VÌ SAO ĐÚNG?', ['f[x + 1] = f[x] + f[x − 1] + f[x − 2] chỉ đọc ba giá trị liền trước. Sau khi gán f[x] = 0, vectơ trạng thái đúng là (0, f[x − 1], f[x − 2]): '
                                   'phép nhân T tiếp theo cho đúng f[x + 1]. Nếu x = n, ta gán f[n] = 0 rồi đi thêm 0 bước: đáp số 0.'])
    D.sub('Chạy tay ví dụ 2')
    D.table(['Bước', 'v = (f[x], f[x−1], f[x−2])', 'Ghi chú'], [
        ['khởi đầu, x = 0', '(1, 0, 0)', 'f[0] = 1'],
        ['T² · v, x = 2', '(2, 1, 1)', 'như thể bậc 2 tốt'],
        ['gán v[0] = 0', '(0, 1, 1)', 'bậc 2 hỏng'],
        ['T² · v, x = 4', '(3, 2, 0)', 'f[3] = 2, f[4] tạm = 3'],
        ['gán v[0] = 0', '(0, 2, 0)', 'bậc 4 hỏng'],
        ['T² · v, x = 6', '(**4**, 2, 0)', 'f[5] = 2, f[6] = 4'],
    ], widths=[2.4, 3.0, 2.8], align=['left', 'center', 'left'], sz=20, hl=[5])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12.5)
    D.code('TRIBO.CPP: lũy thừa ma trận theo từng đoạn', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(K log K + (K + 1) · 27 · 2 log n) ≈ 3 · 10^{7} phép nhân với K = 10^{4}, chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Tính sẵn T^{1}, T^{2}, T^{4}, ..., T^{2^{59}} một lần, rồi mỗi đoạn chỉ nhân **vectơ** với các ma trận này: 9 thay vì 27 phép nhân mỗi lần, '
                              'và không phải bình phương lại (kĩ thuật của bài 15.3).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Quên sắp xếp** các bậc hỏng: x − cur âm.',
               '**Coi bậc hỏng là "tường"** (đặt lại cả vectơ về 0): sai, vẫn bước qua được bậc hỏng.',
               '**Bậc n hỏng:** đáp số 0, lời giải trên tự xử lí đúng.',
               '**Khởi đầu f[0] = 0**, hoặc quên f[−1] = f[−2] = 0.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
