def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('BCNN của cả dãy có thể có hàng trăm nghìn chữ số; ta chỉ cần nó theo mô-đun 10^{9} + 7, và cần biết khi xóa a_{i} thì BCNN có nhỏ đi không. '
        'Cả hai câu hỏi đều trả lời được bằng **bảng số mũ** (Tập 1, Bài 7, Mở rộng 2):')
    D.eq('**L = Π_{p} p^{M(p)},   M(p) = số mũ lớn nhất của p trong các a_{i}.**')
    D.fig(P.fig('table'), 'Bảng số mũ của ví dụ 1. Ô vàng: đạt số mũ lớn nhất của cột.', 15)

    D.h('2. Cách ngây thơ: BCNN chính xác')
    D.p('Với số nhỏ (subtask 1: a_{i} ≤ 50, n ≤ 20), BCNN thật không vượt lcm(1, ..., 50) ≈ 3,1 · 10^{21}, vừa `__int128`. '
        'Tính L, rồi với mỗi i tính lại BCNN khi bỏ a_{i} và so sánh.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách ngây thơ', 12)
    D.code('Cách ngây thơ: BCNN chính xác bằng __int128', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n²) lần gọi gcd; nhưng điều quan trọng hơn là BCNN thật tràn cả __int128 khi các số lớn.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1**: **' + str(P.pts('naive.cpp', 1)) + ' điểm**. Ở các subtask sau, BCNN thật vượt 1,7 · 10^{38}: kết quả sai.',
               'Có người nghĩ "thì lấy dư sau mỗi bước": `L = L / gcd(L, a) * a % MOD`. Sai: L đã lấy dư thì gcd(L, a) không còn liên quan gì tới gcd của số thật (hình dưới).'])
    D.fig(P.fig('residue'), 'Phép lấy dư không "đi xuyên qua" gcd.', 13)
    D.p('Làm việc với bảng số mũ (phân tích từng a_{i} bằng thử chia), rồi với mỗi i "xóa thử" và tính lại số mũ lớn nhất của từng thừa số của a_{i}: '
        'chương trình `mid.cpp` đúng, qua **subtask 2** (n ≤ 2000), nhưng O(n²) không kịp với n = 10^{5}: **' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Để biết "xóa a_{i} thì M(p) có giảm không", ta tính lại M(p) trên n − 1 phần tử. Nhưng câu trả lời chỉ phụ thuộc vào một con số: '
                                 '**có bao nhiêu phần tử đạt M(p)**.'])

    D.h('4. Phá bế tắc: Số mũ lớn nhất và số phần tử đạt')
    D.p('Xóa a_{i} chỉ ảnh hưởng tới các p chia hết a_{i}. Với mỗi p như vậy, M(p) giảm khi và chỉ khi a_{i} đạt M(p) **và là phần tử duy nhất** đạt. Vậy:')
    D.nums(['**Lượt 1:** phân tích mọi a_{i} (bằng sàng spf như bài 7.1), cập nhật M(p) và cnt(p) = số phần tử đạt M(p): gặp e > M(p) thì M(p) ← e, cnt(p) ← 1; gặp e = M(p) thì cnt(p) tăng 1.',
            '**L mod (10^{9} + 7)** = tích p^{M(p)}, nhân dần và lấy dư.',
            '**Lượt 2:** a_{i} cần thiết khi và chỉ khi có một thừa số p với e_{p}(a_{i}) = M(p) và cnt(p) = 1.'])
    D.box('purple', 'CÁC TRƯỜNG HỢP ĐẶC BIỆT', ['- Hai phần tử bằng nhau cùng đạt max (hai số 4 ở ví dụ 1): cnt = 2, không ai cần thiết vì cột ấy.',
                                               '- Số 1 không có thừa số nguyên tố: không bao giờ cần thiết.',
                                               '- n = 1, a_{1} > 1: a_{1} cần thiết (xóa đi, BCNN của dãy rỗng bằng 1).'])
    D.p('Bộ nhớ: mảng spf (int, 40 MB), M (char, 10 MB) và cnt (int, 40 MB) theo chỉ số p ≤ 10^{7}: tổng khoảng 90 MB < 256 MB. Chỉ cần sàng tới max(a).')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 14)
    D.code('BCNNDAY.CPP: sàng spf, M[p], cnt[p], hai lượt duyệt', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(A log log A) để sàng (A = max a_{i}), O(n log A) cho hai lượt phân tích, O(A + Σ M(p)) để tính L. Test lớn nhất mất ' + tm('opt.cpp', 3) + '.')
    D.box('blue', 'MỞ RỘNG: ƯCLN CỦA DÃY QUA BẢNG SỐ MŨ', ['ƯCLN lấy số mũ **nhỏ nhất** của mỗi p (và p phải chia hết mọi phần tử). '
        'Câu hỏi "xóa phần tử nào để ƯCLN lớn nhất" (bài BỎ MỘT SỐ, 3.2) cũng giải được bằng bảng số mũ, nhưng tiền tố – hậu tố gọn hơn nhiều.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Lấy dư trong công thức lcm:** gcd của số dư vô nghĩa.',
               '**So sánh e ≥ M[p] để đánh dấu "cần thiết":** quên điều kiện duy nhất (cnt = 1).',
               '**Mảng theo p cỡ 10^{7}** khai báo trong main: tràn ngăn xếp.',
               '**Nhân L không lấy dư:** tích của p^{M(p)} tràn ngay.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
