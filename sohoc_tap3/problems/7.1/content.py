def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Tính d(n) và σ(n) cho 10^{6} số n ≤ 10^{7}. Nếu biết phân tích n = p_{1}^{e_{1}} ··· p_{k}^{e_{k}}, cả hai đại lượng có công thức tích (Tập 1, Bài 7):')
    D.eq('**d(n) = (e_{1} + 1) ··· (e_{k} + 1),     σ(n) = Π (1 + p_{i} + p_{i}^{2} + ... + p_{i}^{e_{i}}).**')
    D.fig(P.fig('grid72'), 'Các ước của 72 = 2³ · 3² xếp thành bảng 4 × 3; tổng mỗi hàng là 2^{i} · 13.', 14.5)
    D.p('Vậy bài toán là: **phân tích thật nhanh** 10^{6} số, mỗi số ≤ 10^{7}.')

    D.h('2. Cách ngây thơ: Thử mọi ước')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử mọi ước', 12)
    D.code('Cách ngây thơ: thử mọi k từ 1 tới n', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n) mỗi số: 10^{7} phép chia với n = 10^{7}.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (Q ≤ 1000, n ≤ 10^{4}): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               'Duyệt cặp ước tới √n (bài 2.1): `mid.cpp` còn 3163 bước mỗi số, qua **subtask 2** (Q ≤ 1000). Với Q = 10^{6} là 3 · 10^{9} phép chia: **' + S('mid.cpp') + ' điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Mỗi số được phân tích riêng rẽ "từ con số không". Nhưng mọi số đều ≤ 10^{7}: ta có thể **chuẩn bị trước** một lần, '
                                 'cho mỗi số biết một ước nguyên tố của nó, rồi phân tích bất kì số nào trong O(log n).'])

    D.h('4. Phá bế tắc: Sàng ước nguyên tố nhỏ nhất')
    D.p('Sửa sàng Eratosthenes: khi số nguyên tố p gạch số j **lần đầu tiên**, ghi spf[j] = p. Vì p được xét tăng dần, p là ước nguyên tố nhỏ nhất của j. '
        'Sau đó phân tích n bằng cách chia liên tiếp: p = spf[n], n ← n / p, ... Mỗi bước n giảm ít nhất một nửa nên chỉ O(log n) bước (≤ 23 bước với n ≤ 10^{7}).')
    D.fig(P.fig('spf'), 'Trên: mảng spf tới 24 (ô vàng: số nguyên tố). Dưới: phân tích 360 bằng các bước chia cho spf.', 15.5)
    D.p('Trong lúc gom các lần chia cho cùng một p, duy trì luôn lũy thừa p^{j} và tổng 1 + p + ... + p^{j}: không cần hàm `pow`, không cần chia (p^{e+1} − 1)/(p − 1).')
    D.box('purple', 'n = 1', ['Vòng phân tích không chạy lần nào, d = σ = 1: đúng với quy ước "tích rỗng bằng 1". Không cần xử lí riêng.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 14)
    D.code('SOUOC.CPP: sàng spf + công thức tích', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(N log log N) để sàng, O(log n) mỗi số. Test lớn nhất mất ' + tm('opt.cpp', 3) + ', phần lớn là sàng và đọc ghi 10^{6} dòng. '
        'Bộ nhớ: mảng spf kiểu int 40 MB.')
    D.box('blue', 'MỞ RỘNG: SÀNG TUYẾN TÍNH', ['Sàng tuyến tính (sàng Euler) gán spf cho mỗi hợp số đúng một lần, O(N), đồng thời cho danh sách số nguyên tố. '
                                             'Nó cũng tính được mọi hàm nhân tính (d, σ, φ, μ) cho cả dãy 1..N mà không cần phân tích từng số.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Mảng spf trong main:** 40 MB trên ngăn xếp sẽ làm chương trình dừng ngay; khai báo toàn cục.',
               '**p · p tràn int** khi p > 46 340 trong vòng sàng: dùng long long cho p, j.',
               '**Tích trung gian:** σ(n) ≤ 45 732 192 vừa int, nhưng p^{e} và các tích trung gian nên để long long.',
               '**Đọc ghi chậm:** 10^{6} truy vấn cần scanf/printf.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
