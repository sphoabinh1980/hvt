def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Một cách trả quà là một **hoán vị** của n người; người may mắn là **điểm cố định**. Đặt k = n − m (số người không may mắn). '
        'Đếm theo hai bước:')
    D.nums(['**Chọn** k người không may mắn: C(n, k) cách (những người còn lại nhận đúng quà của mình).',
            '**Trả quà** cho k người ấy sao cho không ai nhận lại quà của mình: đó là số **hoán vị không điểm cố định** D(k).'])
    D.eq('**đáp số = C(n, k) · D(k) mod (10^{9} + 7)**,   k = n − m ≤ 10^{7}.')
    D.fig(P.fig('perms'), 'Ví dụ 1 (n = 4, m = 1): 8 cách trả quà; cột "ng. j" ghi chủ của món quà người j nhận.', 15)

    D.h('2. Cách ngây thơ: Duyệt mọi hoán vị')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách duyệt hoán vị', 11.5)
    D.code('Cách ngây thơ: duyệt n! hoán vị', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n! · n). Với n ≤ 8 là 8! · 8 ≈ 3 · 10^{5} phép tính: **' + str(P.pts('naive.cpp', 1)) + ' điểm** subtask 1; '
        'n = 10 đã là 3,6 · 10^{7}, n = 13 vượt 10^{10}.')

    D.h('3. Bế tắc')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Liệt kê là vô vọng; phải **đếm bằng công thức**. Có hai trở ngại: tính D(k) cho k tới 10^{7}, '
                                  'và tính C(n, k) khi n tới 10^{18}, không thể lập bảng giai thừa tới n.'])

    D.h('4. Phá bế tắc')
    D.sub('Bước 1: Hệ thức truy hồi của D(k)')
    D.fig(P.fig('rec'), 'Lập hệ thức cho D(k) bằng cách nhìn người thứ k.', 15.2)
    D.p('D(k) chỉ phụ thuộc vào hai giá trị trước nên tính trong O(k), không cần mảng (chỉ giữ hai biến). Cẩn thận: (k − 1) · (D(k−1) + D(k−2)) phải lấy dư tổng trước khi nhân.')
    D.fig(P.fig('dtab'), 'Mười một giá trị đầu của D(k): D(3) = 2 dùng ở ví dụ 1, D(10) = 1 334 961 ở ví dụ 3.', 15)
    D.sub('Bước 2: C(n, k) với n khổng lồ, k nhỏ')
    D.p('Vì C(n, m) = C(n, k) và k ≤ 10^{7}:')
    D.eq('C(n, k) = n · (n − 1) · ... · (n − k + 1) / k!')
    D.p('Tử số có k thừa số, mẫu số k! khả nghịch theo mô-đun p = 10^{9} + 7 vì k < p (mọi thừa số 1..k đều không chia hết cho p). '
        'Vậy C(n, k) ≡ num · (k!)^{p − 2} (mod p) theo định lí Fermat nhỏ.')
    D.box('blue', 'VÌ SAO ĐÚNG KHI MỘT THỪA SỐ CHIA HẾT CHO p?', ['Đẳng thức C(n, k) · k! = n(n − 1)...(n − k + 1) là đẳng thức số nguyên. '
                                                               'Lấy dư hai vế: nếu một thừa số n − i chia hết cho p thì vế phải ≡ 0, mà k! khả nghịch nên C(n, k) ≡ 0. '
                                                               'Công thức không cần xử lí riêng trường hợp này.'])
    D.box('purple', 'BẪY: NHÂN (n − i) KHI CHƯA LẤY DƯ', ['$num = num * (n - i) % MOD;',
                                                          'num < 10^{9} + 7 nhưng n − i có thể tới 10^{18}: tích tới 10^{27}, tràn long long. '
                                                          'Khi n ≤ 10^{6} tích chỉ tới 10^{15} nên chương trình `trap.cpp` vẫn đúng ở subtask 1, 2 và sai ở subtask 3: **' + S('trap.cpp') + ' điểm**. '
                                                          'Sửa: `num * ((n - i) % MOD) % MOD`.'])
    D.sub('Chạy tay ví dụ 3')
    D.p('n = 10^{18}, k = 10: num = 10^{18} · (10^{18} − 1) · ... · (10^{18} − 9) mod p; chia cho 10! cho C(10^{18}, 10) ≡ 217 822 480. '
        'Nhân với D(10) = 1 334 961: 217 822 480 · 1 334 961 mod p = 513 687 792.')
    D.p('Ví dụ 2 (n = 5, m = 4): k = 1, D(1) = 0 nên đáp số 0: món quà cuối cùng buộc phải về tay chủ.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 12.5)
    D.code('TANGQUA.CPP: C(n, k) nhân dần, D(k) truy hồi', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(k + log p) thời gian, O(1) bộ nhớ. Với k = 10^{7}, chương trình chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Công thức bù trừ D(k) = k! · Σ_{i=0..k} (−1)^{i} / i! cũng tính được trong O(k), nhưng cần nghịch đảo của mọi i!.',
                              'D(k) = k · D(k − 1) + (−1)^{k}: hệ thức bậc một, cũng rất tiện.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Lập bảng giai thừa tới n:** không thể với n = 10^{18}.',
               '**Nhân (n − i) khi chưa lấy dư:** tràn số.',
               '**D(1) = 0, D(0) = 1:** m = n − 1 cho đáp số 0, m = n cho 1.',
               '**Lấy C(n, m) thay vì C(n, k):** m có thể tới 10^{18}, phải dùng k = n − m.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'trap.cpp', 'opt.cpp'])
