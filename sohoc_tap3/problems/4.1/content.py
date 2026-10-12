def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Thứ tự các thao tác không quan trọng: cuối cùng, lượng nước trong bể là a_{1}x_{1} + a_{2}x_{2} + ... + a_{n}x_{n}, với x_{i} là '
        '(số lần đổ vào) − (số lần múc ra) bằng can loại i, một số nguyên tùy ý (âm được). Bể đủ lớn nên ta luôn đổ trước, múc sau, không bao giờ bị "thiếu nước".')
    D.p('Vậy câu hỏi là: **những số c ≥ 0 nào viết được dưới dạng tổ hợp nguyên của a_{1}, ..., a_{n}?** Đó chính là định lí Bézout.')
    D.fig(P.fig('jumps'), 'Với can 6 lít và 4 lít, mỗi thao tác là một bước nhảy ±6 hoặc ±4 trên trục số.', 15)

    D.h('2. Cách ngây thơ: Loang trên các lượng nước')
    D.p('Coi mỗi lượng nước v là một đỉnh, thao tác đổ/múc can x nối v với v ± x. Loang (BFS) từ 0, chỉ xét các lượng 0..4000; '
        'với can nhỏ (≤ 1000) và câu hỏi nhỏ (≤ 1000) giới hạn này đủ để thăm mọi lượng đong được trong miền quan tâm.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách loang', 12)
    D.code('Cách ngây thơ: loang trên các lượng nước 0..4000', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(B · n) với B = 4000 là cận trên của lượng nước. Cách này chỉ dùng được khi các số nhỏ: với a_{i} tới 10^{18}, '
        'một bước nhảy đã vượt mọi mảng.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (n = 2, số ≤ 1000): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               '**Subtask 2, 3**: các lượng nước tới 10^{18}: không thể loang: **0 điểm**.'])
    D.p('Nhiều bạn nhớ ra định lí Bézout cho hai số và viết `g = gcd(a[0], a[1])`: đúng trọn subtask 2. Nhưng nếu quên các can thứ ba trở đi, '
        'chương trình `mid.cpp` sai ở subtask 3 (ví dụ 2: gcd(6, 10) = 2 nhưng đong được cả 1 lít): **' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Không thể liệt kê các lượng đong được. Phải mô tả **cả tập** ấy bằng một công thức: tập các bội của một số g nào đó.'])

    D.h('4. Phá bế tắc: Bézout cho nhiều số')
    D.sub('Hai loại can')
    D.p('Theo định lí Bézout (Tập 1, Bài 4): tập các số a_{1}x + a_{2}y (x, y nguyên) **đúng bằng** tập các bội của g = gcd(a_{1}, a_{2}). '
        'Một chiều là hiển nhiên: g chia hết a_{1} và a_{2} nên chia hết mọi tổ hợp. Chiều ngược lại do Euclid mở rộng: g = a_{1}x_{0} + a_{2}y_{0}, '
        'nhân lên được mọi bội của g.')
    D.sub('Gộp dần')
    D.p('Với ba loại can: a_{1}x + a_{2}y "đi được" đúng các bội của g_{2} = gcd(a_{1}, a_{2}), nên a_{1}x + a_{2}y + a_{3}z chính là g_{2}x\' + a_{3}z, '
        'tức các bội của gcd(g_{2}, a_{3}). Cứ thế gộp dần:')
    D.eq('**Lượng đong được = các bội của G = gcd(a_{1}, a_{2}, ..., a_{n}).**')
    D.fig(P.fig('chain'), 'Ví dụ 2: gcd(6, 10) = 2, gộp tiếp với 15 được 1. Dòng xám là cách đong thật sự: 16 can 6 lít vào, 8 can 10 lít ra, 1 can 15 lít ra.', 14)
    D.p('Vậy lượng dương nhỏ nhất đong được là G, và c đong được khi và chỉ khi G chia hết c (c = 0 luôn đúng: không làm gì cả).')
    D.box('purple', 'VÌ SAO KHÔNG BỊ "THIẾU NƯỚC"?', [
        'Một cách đong có thể cần múc ra trước khi đổ vào (chẳng hạn x_{2} < 0). Nhưng ta có quyền sắp xếp lại thứ tự: thực hiện mọi lần đổ vào trước, '
        'rồi mới múc ra. Khi đó lượng nước chỉ tăng rồi giảm dần về c ≥ 0, không bao giờ âm.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 11)
    D.code('DONGNUOC.CPP: gcd của cả dãy, mỗi câu hỏi O(1)', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(n log 10^{18}) để tính G, O(1) mỗi câu hỏi. Khởi tạo g = 0 nhờ gcd(0, x) = x.')
    D.box('blue', 'MỞ RỘNG: KHI KHÔNG ĐƯỢC MÚC RA', [
        'Nếu chỉ được đổ vào (x_{i} ≥ 0), bài toán khó hơn hẳn: đó là "bài toán đồng xu" (Frobenius). Với hai can nguyên tố cùng nhau a, b, '
        'số lớn nhất **không** đong được là ab − a − b (bài MUA HÀNG 4.2 sẽ gặp lại hiện tượng này).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Chỉ dùng hai can đầu:** bài cho n loại can; gcd phải lấy trên cả dãy.',
               '**c = 0:** luôn là CO (0 mod g = 0), đừng xử lí riêng thành KHONG.',
               '**Dùng int:** a_{i}, c_{j} tới 10^{18}.',
               '**Nghĩ "lượng nhỏ nhất là can nhỏ nhất":** ví dụ 2 cho thấy 1 lít đong được dù can nhỏ nhất là 6 lít.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
