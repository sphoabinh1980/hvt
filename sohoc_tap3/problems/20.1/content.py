def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Theo Tập 1, Bài 20: đoạn thẳng nối hai điểm nguyên với hiệu tọa độ (dx, dy) có **gcd(|dx|, |dy|) + 1** điểm nguyên, cách đều nhau với bước (dx/g, dy/g). '
        'Đường gấp khúc không tự cắt, không tự chạm nên hai đoạn chỉ chung nhau đúng các đỉnh P_{2}, ..., P_{n−1}, mỗi đỉnh thuộc hai đoạn.')
    D.fig(P.fig('path'), 'Ví dụ 1: 12 điểm nguyên trên đường gấp khúc.', 15.2)
    D.p('Cách đếm gọn nhất: mỗi đoạn góp **gcd(|dx|, |dy|)** điểm (không tính điểm đầu đoạn, vì nó là điểm cuối của đoạn trước), rồi cộng 1 cho P_{1}.')
    D.eq('**số cây = 1 + Σ_{i=2..n} gcd(|x_{i} − x_{i−1}|, |y_{i} − y_{i−1}|)**')

    D.h('2. Cách ngây thơ: Đánh dấu trên lưới')
    D.code('Cách ngây thơ: thử mọi điểm trong hình chữ nhật bao', P.src('naive.cpp'))
    D.p('Với tọa độ ≤ 100, thử mọi điểm trong hình chữ nhật bao của từng đoạn, kiểm tra thẳng hàng bằng tích chéo; mảng đánh dấu tự loại các điểm trùng. **' + S('naive.cpp') + ' điểm**.')

    D.h('3. Bế tắc')
    D.p('Khi mọi đoạn song song trục, đoạn có |dx| + |dy| bước đơn vị và cũng có |dx| + |dy| + 1 điểm nguyên (`mid.cpp`): **' + S('mid.cpp') + ' điểm**. Với đoạn xiên, |dx| + |dy| đếm thừa rất nhiều.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Không thể duyệt điểm khi tọa độ tới 10^{9}. Cần một công thức cho số điểm nguyên trên một đoạn xiên, và một cách không đếm trùng đỉnh chung.'])

    D.h('4. Phá bế tắc: gcd cho từng đoạn')
    D.box('blue', 'VÌ SAO LÀ gcd(|dx|, |dy|) + 1?', ['Điểm (x_{1} + t · dx, y_{1} + t · dy) với 0 ≤ t ≤ 1 là nguyên khi và chỉ khi t · dx và t · dy đều nguyên. '
                                                    'Với g = gcd(|dx|, |dy|), các giá trị t thỏa mãn chính là t = 0, 1/g, 2/g, ..., 1: có g + 1 giá trị. '
                                                    'Đoạn đứng (dx = 0): gcd(0, |dy|) = |dy|, công thức vẫn đúng.'])
    D.box('purple', 'BẪY: CỘNG gcd + 1 CHO TỪNG ĐOẠN', ['Mỗi đỉnh giữa P_{2}, ..., P_{n−1} bị đếm hai lần. Ví dụ 1 ra 13 thay vì 12. '
                                                         'Chương trình `trap.cpp` sai ở mọi subtask: **' + S('trap.cpp') + ' điểm**. Sửa: cộng gcd cho mỗi đoạn và cộng 1 một lần duy nhất.'])
    D.p('Ví dụ 3: đoạn (0,0)–(2,0) và (2,0)–(5,0) cùng nằm trên trục hoành nhưng (theo đề) chỉ chung điểm (2, 0): 1 + 2 + 3 + 3 = 9.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối', 11.5)
    D.code('TRONGCAY.CPP', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(n log C) với C = 2 · 10^{9}; chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Đường khép kín (đa giác): mọi đỉnh đều thuộc hai cạnh, số điểm trên biên là B = Σ gcd theo mọi cạnh kể cả cạnh P_{n}P_{1}, không cộng thêm 1 (bài 20.2).',
                              'Nếu đường gấp khúc được phép tự chồng (hai đoạn chồng lên nhau một khúc), phải loại điểm trùng bằng cách gom các đoạn cùng đường thẳng: bài toán khó hơn nhiều.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Đếm đỉnh chung hai lần.**', '**Hiệu tọa độ kiểu int:** 10^{9} − (−10^{9}) = 2 · 10^{9} tràn (ví dụ 2).', '**gcd của số âm:** lấy trị tuyệt đối trước.',
               '**Đáp số kiểu int:** tới 2 · 10^{14}.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'trap.cpp', 'opt.cpp'])
