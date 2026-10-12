def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Với tổng tiền tố S_{0} = 0, S_{i} = a_{1} + ... + a_{i}, tổng đoạn [l, r] là S_{r} − S_{l−1}. Vậy')
    D.eq('**a_{l} + ... + a_{r} = 0  ⇔  S_{r} = S_{l−1}**')
    D.p('Bài toán "đếm đoạn" trở thành "**đếm cặp chỉ số i < j trong 0..n có S_{i} = S_{j}**" (Tập 1, Bài 19).')
    D.fig(P.fig('plot'), 'Ví dụ 1: mỗi cặp điểm cùng độ cao trên đồ thị tổng tiền tố là một chuỗi hòa vốn.', 15.2)

    D.h('2. Cách ngây thơ: Duyệt mọi đoạn')
    D.code('Cách ngây thơ: O(n²)', P.src('naive.cpp'))
    D.p('Cố định l, cộng dồn khi tăng r: O(n^{2}). n = 3000 cho 4,5 · 10^{6} đoạn: **' + str(P.pts('naive.cpp', 1)) + ' điểm**. n = 10^{6} cho 5 · 10^{11} đoạn.')

    D.h('3. Bế tắc')
    D.p('Đếm cặp bằng nhau thường dùng mảng đếm: duyệt j tăng dần, cộng cnt[S_{j}] (số tiền tố trước bằng S_{j}) rồi tăng cnt[S_{j}]. '
        'Khi |a_{i}| ≤ 10 thì |S| ≤ 10^{7}, dời gốc thêm 10^{7} để làm chỉ số (`mid.cpp`): subtask 2 chạy ' + P.scores['mid.cpp']['detail'][1].split()[1] + ', nhưng các subtask khác truy cập ngoài mảng: **' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Với |a_{i}| ≤ 10^{9}, tổng tiền tố trải trên [−10^{15}, 10^{15}]: không thể làm chỉ số mảng. '
                                  'Nhưng chỉ có n + 1 giá trị thực sự xuất hiện; ta chỉ cần biết giá trị nào bằng nhau.'])

    D.h('4. Phá bế tắc: Sắp xếp rồi đếm nhóm')
    D.p('Sắp xếp n + 1 tổng tiền tố: các giá trị bằng nhau đứng liền nhau thành nhóm. Nhóm có c phần tử cho C(c, 2) = c(c − 1)/2 cặp, và cặp ở hai nhóm khác nhau không bao giờ bằng nhau.')
    D.fig(P.fig('groups'), 'Ví dụ 3: hai nhóm, mỗi nhóm 3 phần tử.', 14)
    D.box('blue', 'ĐỪNG QUÊN S₀ = 0', ['S_{0} đại diện cho các đoạn bắt đầu từ ngày 1. Thiếu nó, ví dụ 1 chỉ đếm được đoạn [2, 6] (S_{1} = S_{6}), bỏ sót [1, 3] (S_{0} = S_{3}).'])
    D.box('blue', 'KIỂU DỮ LIỆU', ['Đáp số tới n(n + 1)/2 ≈ 5 · 10^{11} (mọi a_{i} = 0): long long, kể cả biến c trong c(c − 1)/2. Tổng tiền tố tới 10^{15}: long long.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối', 13)
    D.code('TONG0.CPP: sắp xếp tổng tiền tố', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(n log n) cho sắp xếp, phần đếm O(n); n = 10^{6} chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Dùng unordered_map hoặc map thay cho sắp xếp cũng được (map: O(n log n), chậm hơn sort vài lần với 10^{6} phần tử).',
                              'Đếm đoạn có tổng bằng T bất kì: S_{r} − S_{l−1} = T ⇔ S_{l−1} = S_{r} − T; sắp xếp rồi tìm kiếm nhị phân, hoặc hai con trỏ.',
                              'Đếm đoạn có tổng chia hết cho k: thay S bằng S mod k (bài 19.2, 19.3).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Thiếu S_{0} = 0.**', '**int cho đáp số hoặc tổng tiền tố.**', '**Mảng đếm dời gốc** khi giá trị lớn: truy cập ngoài mảng.', '**Đọc 10^{6} số bằng cin chưa tắt đồng bộ.**'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
