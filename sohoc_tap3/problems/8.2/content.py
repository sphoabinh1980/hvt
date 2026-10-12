def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Cần mọi số nguyên tố trong [L, R] theo thứ tự tăng dần; mỗi hai số nguyên tố kề nhau trong danh sách ấy là một cặp liên tiếp. '
        'Vì p, q đều thuộc [L, R], không có số nguyên tố nào "nằm giữa" bị bỏ sót bên ngoài đoạn: các cặp liên tiếp trong đoạn đúng là các cặp kề nhau sau khi sàng đoạn.')
    D.fig(P.fig('arcs'), 'Ví dụ 1 trên trục số: mỗi cung nối hai số nguyên tố liên tiếp, kèm khoảng cách.', 15)
    D.p('Hai luật phụ: khi hòa chọn cặp có p nhỏ nhất; nếu đoạn có ít hơn hai số nguyên tố thì in −1.')

    D.h('2. Cách ngây thơ: Thử chia từng số')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ', 14)
    D.code('Cách ngây thơ: thử chia từng số', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O((R − L) · √R) trường hợp xấu. Với R − L = 10^{4} gần 10^{12}: khoảng 360 số nguyên tố × 3,3 · 10^{5} phép chia ≈ 1,2 · 10^{8}, '
        'kịp (' + tm('naive.cpp', 2) + '). Với R − L = 10^{7}: gấp 1000 lần.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1, 2**: **' + S('naive.cpp') + ' điểm**.', '**Subtask 3** (đoạn dài 10^{7} số cỡ 10^{12}): không kịp.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Kiểm tra từng số là làm lại một công việc chung cho cả đoạn. Sàng trên đoạn (bài 8.1) cho mọi số nguyên tố trong đoạn bằng khoảng (R − L) · ln ln R phép gạch.'])

    D.h('4. Phá bế tắc: Sàng đoạn rồi duyệt một lượt')
    D.p('Sàng [L, R] như bài 8.1, rồi duyệt x tăng dần, nhớ số nguyên tố vừa gặp `prev`. Mỗi khi gặp số nguyên tố mới x, (prev, x) là một cặp liên tiếp với khoảng cách x − prev.')
    D.box('purple', 'LUẬT HÒA BẰNG SO SÁNH CHẶT', ['Các cặp được duyệt theo p tăng dần. Chỉ cập nhật kỉ lục khi khoảng cách **lớn hơn hẳn** (hoặc **nhỏ hơn hẳn**) '
        'thì kỉ lục luôn là cặp đầu tiên đạt giá trị ấy, tức cặp có p nhỏ nhất. Dùng ≥ hay ≤ sẽ giữ cặp cuối cùng.'])
    D.p('Bộ nhớ: mảng đánh dấu 10^{7} ô kiểu char (10 MB). Đừng dùng `vector<int>` hay `long long` cho nó.')
    D.sub('Trường hợp đặc biệt')
    D.bullets(['Đoạn [1, 3]: cặp (2, 3) khoảng cách 1, cặp duy nhất có khoảng cách lẻ; vừa là lớn nhất vừa là nhỏ nhất.',
               'Đoạn có đúng một số nguyên tố (như [23, 28]) hoặc không có số nào: in −1.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 13)
    D.code('KHOANGCACH.CPP: sàng trên đoạn + một lượt duyệt', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(√R log log √R + (R − L) log log R). Đoạn 10^{7} số mất ' + tm('opt.cpp', 3) + '.')
    D.box('blue', 'MỞ RỘNG: KHOẢNG TRỐNG KỈ LỤC', ['Khoảng cách trung bình giữa hai số nguyên tố quanh N là ln N (≈ 27,6 khi N = 10^{12}), nhưng có những "khoảng trống" dài bất thường: '
        'khoảng trống dài nhất dưới 10^{12} dài 540 (sau số 738 832 927 927). Ví dụ 3 của đề là một khoảng trống dài 306.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Tính khoảng cách từ L hoặc tới R:** không phải cặp số nguyên tố.', '**Dùng ≥ khi cập nhật:** sai luật hòa.',
               '**Mảng đánh dấu kiểu int:** 40 MB, vẫn vừa nhưng chậm hơn; kiểu long long thì 80 MB.', '**Quên trường hợp ít hơn hai số nguyên tố.**'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'opt.cpp'])
