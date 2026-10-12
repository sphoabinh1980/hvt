def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Tổng đoạn [l, r] chia hết cho k ⇔ **S_{r} ≡ S_{l−1} (mod k)**. Với r cố định, đoạn dài nhất kết thúc tại r bắt đầu ngay sau **chỉ số nhỏ nhất** i < r có S_{i} cùng số dư với S_{r}. '
        'Vì vậy chỉ cần nhớ, với mỗi số dư d, vị trí đầu tiên first[d] mà nó xuất hiện (Tập 1, Bài 19, Mở rộng 2).')
    D.fig(P.fig('arcs'), 'Ví dụ 1 (k = 3): mũi tên nối vị trí đầu tiên của mỗi số dư với vị trí xa nhất cùng số dư.', 15.2)

    D.h('2. Cách ngây thơ: Duyệt mọi đoạn')
    D.code('Cách ngây thơ: O(n²)', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n^{2}): **' + str(P.pts('naive.cpp', 1)) + ' điểm** với n ≤ 3000.')

    D.h('3. Bế tắc')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Với mỗi r, cách ngây thơ thử mọi l. Nhưng mọi l − 1 có cùng số dư với S_{r} đều cho đoạn hợp lệ, và ta chỉ cần l − 1 **nhỏ nhất**: một giá trị duy nhất cho mỗi số dư, nhớ trong mảng first[0..k − 1].'])

    D.h('4. Phá bế tắc: Vị trí đầu tiên của mỗi số dư')
    D.p('Duyệt r = 1..n, giữ s = S_{r} mod k. Nếu first[s] = −1 (chưa gặp) thì ghi first[s] = r; ngược lại đoạn [first[s] + 1, r] dài r − first[s] là ứng viên. '
        'first[0] = 0 thay cho S_{0}.')
    D.table(['r', 'S_r', 'S_r mod 3', 'first[s] trước đó', 'đoạn ứng viên', 'đáp án tạm'], [
        ['1', '2', '2', '−1 → ghi 1', '', ''], ['2', '−5', '1', '−1 → ghi 2', '', ''], ['3', '0', '0', '0', '[1, 3], dài 3', '3 1'],
        ['4', '4', '1', '2', '[3, 4], dài 2', '3 1'], ['5', '1', '1', '2', '[3, 5], dài 3', '3 1 (không dài hơn hẳn)'], ['6', '2', '2', '1', '[2, 6], dài 5', '**5 2**']],
        widths=[0.5, 0.7, 1.1, 1.7, 1.7, 2.4], align=['center'] * 6, sz=19, hl=[5])
    D.sub('Luật chọn l nhỏ nhất')
    D.p('Chỉ cập nhật khi độ dài **lớn hơn hẳn**. Nếu hai đoạn cùng độ dài, đoạn kết thúc sớm hơn (r nhỏ hơn) được gặp trước và được giữ; cùng độ dài thì r nhỏ hơn cũng là l nhỏ hơn.')
    D.box('purple', 'BẪY: SỐ DƯ ÂM', ['$int s = S % k;',
                                      'Trong C++, phép % giữ dấu của số bị chia: −1 % 6 = −1. Dùng s làm chỉ số first[s] là truy cập ngoài mảng. '
                                      'Chương trình `trap.cpp` chỉ đúng khi mọi a_{i} ≥ 0 (subtask 2): **' + S('trap.cpp') + ' điểm**. '
                                      'Sửa: s = ((s + a) % k + k) % k, giữ s luôn trong [0, k).'])
    D.p('Ví dụ 3 (k = 6): S = 0, −1, 1, 8, −1, 4, 2; số dư đúng 0, 5, 1, 2, 5, 4, 2. S_{1} và S_{4} cùng dư 5 cho [2, 4]; S_{3} và S_{6} cùng dư 2 cho [4, 6], cùng dài 3 nhưng gặp sau: đáp số "3 2".')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối', 12.5)
    D.code('DOANDAI.CPP: vị trí đầu tiên của số dư', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(n + k) thời gian, O(k) bộ nhớ (không cần lưu cả dãy); chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Đoạn **ngắn nhất** (độ dài ≥ 1) có tổng chia hết cho k: thay first bằng last (vị trí gần nhất), cập nhật last[s] = r sau mỗi bước.',
                              'Đoạn dài nhất có tổng bằng 0 (không theo mô-đun): S có thể rất lớn, dùng sắp xếp (bài 19.1) hoặc map để lưu vị trí đầu tiên.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Số dư âm.**', '**Thiếu first[0] = 0**: bỏ sót các đoạn bắt đầu từ 1.', '**Cập nhật cả khi bằng**: chọn sai l.', '**Cộng dồn S bằng int** trước khi lấy dư: tràn.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'trap.cpp', 'opt.cpp'])
