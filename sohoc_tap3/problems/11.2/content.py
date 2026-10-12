def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Cố định mẫu b ≥ 2. Phân số a/b trong (0, 1) tối giản khi 1 ≤ a ≤ b − 1 và gcd(a, b) = 1: có đúng **φ(b)** tử như vậy. Riêng b = 1 không cho phân số nào '
        '(a/1 ≥ 1), dù φ(1) = 1. Vậy đáp số của câu hỏi [L, R] là')
    D.eq('**Σ_{b = max(L, 2)}^{R} φ(b) = S(R) − S(L − 1),   S(x) = φ(2) + ... + φ(x).**')
    D.fig(P.fig('grid'), 'Phân số a/b với 1 ≤ a < b ≤ 8: ô xanh là phân số tối giản.', 15)

    D.h('2. Cách ngây thơ: Đếm cặp')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách đếm cặp', 12)
    D.code('Cách ngây thơ: đếm mọi cặp (a, b)', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(R^{2} log R) mỗi câu hỏi.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (R ≤ 1000): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               'Dùng hàm φ của bài 11.1 cho từng b và tổng tiền tố: `mid.cpp` tốn O(R√R), qua **subtask 2** (R ≤ 10^{5}, ' + tm('mid.cpp', 2) + '): **' + S('mid.cpp') + ' điểm**. '
               'Với R = 10^{7}: 10^{7} · 3162 ≈ 3 · 10^{10} phép chia.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Cần φ của **mọi** số tới 10^{7}. Phân tích từng số riêng lẻ là lặp lại công việc; hãy **sàng** hàm φ như sàng Eratosthenes.'])

    D.h('4. Phá bế tắc: Sàng φ')
    D.p('Khởi tạo phi[i] = i. Duyệt p tăng dần: nếu phi[p] vẫn bằng p thì p là số nguyên tố (chưa số nguyên tố nhỏ hơn nào "đụng" tới nó). Khi đó, với mọi bội j của p: '
        'phi[j] ← phi[j] − phi[j] / p, tức nhân với (1 − 1/p). Sau khi duyệt hết, phi[j] = j · Π_{p|j} (1 − 1/p) = φ(j).')
    D.fig(P.fig('phisieve'), 'Sàng φ tới 12: mỗi hàng là trạng thái sau khi một số nguyên tố p sửa các bội của nó.', 15.5)
    D.box('purple', 'VÌ SAO phi[j] − phi[j]/p LUÔN CHIA HẾT?', ['Trước khi xử lí p, phi[j] = j · Π_{q < p, q|j} (1 − 1/q) = j · Π (q − 1)/q. Mọi mẫu q đều khác p, nên thừa số p của j còn nguyên: '
        'phi[j] vẫn chia hết cho p.'])
    D.p('Độ phức tạp sàng: Σ_{p ≤ N} N/p ≈ N ln ln N. Bộ nhớ: phi kiểu int (40 MB) và S kiểu long long (80 MB, vì S(10^{7}) ≈ 3 · 10^{13}). '
        'Chỉ cần sàng tới R lớn nhất: đọc hết câu hỏi trước.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 14)
    D.code('PHANSO.CPP: sàng φ + tổng tiền tố', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(N log log N + Q). Test lớn nhất mất ' + tm('opt.cpp', 3) + '.')
    D.box('blue', 'MỞ RỘNG: DÃY FAREY', ['Các phân số tối giản trong [0, 1] với mẫu ≤ N, xếp tăng dần, tạo thành dãy Farey F_{N}, có 1 + Σ_{b ≤ N} φ(b) phần tử. '
        'Tổng S(N) ≈ 3N^{2}/π^{2}: với N = 10^{7} khoảng 3,04 · 10^{13}, khớp ví dụ 2.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Tính cả b = 1:** φ(1) = 1 nhưng mẫu 1 không cho phân số nào trong (0, 1).', '**Tổng tiền tố kiểu int:** tràn (tới 3 · 10^{13}).',
               '**Sàng tới 10^{7} khi R nhỏ:** không sai, chỉ tốn thời gian; đọc trước để biết max R.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
