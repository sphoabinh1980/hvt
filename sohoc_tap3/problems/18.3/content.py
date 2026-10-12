def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Đặt **g(n) = số x ∈ [0, n] có đúng k bit 1** (g(−1) = 0). Câu hỏi loại 1 là g(R) − g(L − 1). '
        'Câu hỏi loại 2 là bài toán ngược: tìm x nhỏ nhất sao cho có đúng m số dương ≤ x có k bit 1. Cả hai đều giải bằng cách **duyệt bit từ cao xuống** kết hợp tổ hợp C(i, j): '
        'số các xâu i bit có đúng j bit 1.')

    D.h('2. Cách ngây thơ: Bảng tính sẵn')
    D.code('Cách ngây thơ: bảng đếm trên [0, 10⁵]', P.src('naive.cpp'))
    D.p('Q tới 10^{5} nên dù R ≤ 10^{5} cũng không thể duyệt lại đoạn ở mỗi câu hỏi (10^{10} phép tính). Tính sẵn popcount của mọi số ≤ 10^{5}, '
        'bảng đếm tiền tố cnt[k][x] cho loại 1 và danh sách các số có k bit 1 cho loại 2: mỗi câu hỏi O(1). **' + S('naive.cpp') + ' điểm**.')

    D.h('3. Bế tắc')
    D.box('red', 'ĐIỂM BẾ TẮC', ['R tới 10^{18}: không thể lập bảng. Phải **đếm mà không liệt kê** các số có k bit 1.'])

    D.h('4. Phá bế tắc')
    D.sub('Loại 1: tính g(n)')
    D.p('Mọi x < n đều "giống n ở các bit cao, rồi tới một bit i mà n có bit 1 còn x có bit 0, các bit thấp hơn tùy ý". Nhóm theo vị trí i đó: '
        'nếu phía trên i, n có t bit 1, thì x cần thêm k − t bit 1 trong i bit thấp, có **C(i, k − t)** số. Cộng thêm chính n nếu n có đúng k bit 1.')
    D.fig(P.fig('count'), 'Ví dụ 1, câu hỏi 1: g(12) = 3 + 2 + 1 = 6, và g(0) = 0.', 15)
    D.p('Chương trình `mid.cpp` dùng g(n) cho loại 1, còn loại 2 vẫn tra bảng tới 10^{5}: **' + S('mid.cpp') + ' điểm**.')
    D.sub('Loại 2: dựng số thứ m')
    D.p('Dựng x từ bit cao xuống, giữ k\' là số bit 1 còn cần. Ở bit i, nếu đặt bit i = 0 thì có C(i, k\') cách cho các bit thấp hơn, '
        'và các số ấy đều **nhỏ hơn** mọi số có bit i = 1. Vậy nếu m ≤ C(i, k\') thì bit i = 0; ngược lại bit i = 1, bỏ qua C(i, k\') số nhỏ hơn: m −= C(i, k\'), k\' −= 1.')
    D.fig(P.fig('kth'), 'Ví dụ 1, câu hỏi 2: số thứ 4 có 2 bit 1 là 9.', 15)
    D.box('blue', 'VÌ SAO ĐÚNG?', ['Tại mỗi bước ta giữ bất biến: "x là số thứ m trong các số có tiền tố bit đã chọn và đúng k\' bit 1 ở các bit còn lại". '
                                   'Các số có bit i = 0 đứng trước các số có bit i = 1, nên so sánh m với C(i, k\') cho biết số cần tìm thuộc nhóm nào. Số 0 không được đếm vì k ≥ 1.'])
    D.box('blue', 'BẢNG TỔ HỢP', ['C(60, 30) ≈ 1,18 · 10^{17} vừa long long. Dựng bằng tam giác Pascal (chỉ có phép cộng). Công thức n!/(k!(n−k)!) sẽ tràn vì 21! > 9,2 · 10^{18}.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối', 14)
    D.code('KBIT.CPP', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(61^{2}) chuẩn bị, O(61) mỗi câu hỏi; 10^{5} câu hỏi chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Đây là dạng đơn giản nhất của **quy hoạch động chữ số** (digit DP): đếm các số ≤ n có một tính chất về chữ số. Với tính chất phức tạp hơn (tổng chữ số chia hết cho 7...), '
                              'thay C(i, j) bằng một bảng QHĐ trên số chữ số còn lại và trạng thái.',
                              'Loại 2 cũng giải được bằng tìm kiếm nhị phân trên x với hàm g: O(60^{2}) mỗi câu hỏi, chậm hơn nhưng không cần nghĩ cách dựng.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Quên đếm chính n** trong g(n).', '**k = 0:** chỉ có số 0; g(n) = 1 với mọi n ≥ 0.', '**C(i, j) với j > i hoặc j < 0** phải bằng 0, không truy cập ngoài bảng.',
               '**1 << i** thay vì 1LL << i.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
