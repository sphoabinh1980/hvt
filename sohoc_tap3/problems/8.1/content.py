def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Đếm và cộng các số nguyên tố trong [L, R], với R tới 10^{12} nhưng đoạn chỉ dài tới 10^{6}. Hai cách quen thuộc đều vướng: sàng Eratosthenes cần mảng tới R, '
        'còn thử chia từng số cần √R cho mỗi số nguyên tố. Công cụ đúng là **sàng trên đoạn** (Tập 1, Bài 8).')

    D.h('2. Hai cách ngây thơ')
    D.sub('Cách 1: Sàng tới R')
    D.code('Cách ngây thơ 1: sàng Eratosthenes tới R', P.src('sieveR.cpp'))
    D.p('O(R log log R) thời gian và O(R) bộ nhớ: chạy tốt khi R ≤ 10^{7} (subtask 1), nhưng không cấp phát nổi mảng 10^{12} phần tử.')
    D.sub('Cách 2: Thử chia từng số')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử chia', 13)
    D.code('Cách ngây thơ 2: thử chia từng số trong đoạn', P.src('naive.cpp'))
    D.p('O((R − L) · √R / 3) trường hợp xấu: tốt khi đoạn ngắn (subtask 2: 100 số), nhưng một đoạn 10^{6} số gần 10^{12} chứa 36 400 số nguyên tố, '
        'mỗi số tốn 3,3 · 10^{5} phép chia: 1,2 · 10^{10} phép chia.')

    D.h('3. Bế tắc')
    D.bullets(['**Sàng tới R:** subtask 1, **' + S('sieveR.cpp') + ' điểm** (subtask 2, 3: không cấp phát được bộ nhớ).',
               '**Thử chia:** subtask 2, **' + S('naive.cpp') + ' điểm**. Thú vị là nó **không** qua subtask 1: đoạn 10^{6} số dưới 10^{7} có khoảng 6 · 10^{4} số nguyên tố, '
               'mỗi số tới 10^{3} phép chia, nhân 10 đoạn: chậm hơn giới hạn.',
               'Ghép hai cách theo subtask được 60 điểm, nhưng subtask 3 cần cả hai ưu điểm: **bộ nhớ theo độ dài đoạn** và **gạch thay vì thử chia**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Sàng tới R lãng phí vì phần lớn mảng nằm ngoài [L, R]. Thử chia lãng phí vì mỗi số đi tìm ước riêng. '
                                 'Mà để gạch một hợp số x ∈ [L, R], chỉ cần các số nguyên tố p ≤ √R ≤ 10^{6}.'])

    D.h('4. Phá bế tắc: Sàng trên đoạn')
    D.nums(['**Sàng nhỏ một lần:** các số nguyên tố ≤ 10^{6} (78 498 số), dùng chung cho mọi truy vấn.',
            '**Mảng đánh dấu cho đoạn:** chỉ R − L + 1 phần tử; số x nằm ở ô x − L.',
            '**Gạch:** với mỗi p, p² ≤ R, gạch các bội của p trong [L, R] bắt đầu từ max(p², ⌈L/p⌉ · p), bước p.',
            '**Số 1:** khi L = 1, gạch ô 0 riêng.'])
    D.fig(P.fig('window'), 'Cửa sổ [100, 130]: mỗi hàng là một lượt gạch của p ≤ √130; hàng cuối là các số còn lại.', 15.5)
    D.sub('Ô bắt đầu')
    D.p('⌈L/p⌉ · p = (L + p − 1) / p * p là bội nhỏ nhất của p không nhỏ hơn L. Lấy max với p² vì hai lẽ: các bội nhỏ hơn p² đã bị số nguyên tố nhỏ hơn gạch, '
        'và quan trọng hơn, **không được gạch chính p** khi p nằm trong đoạn.')
    D.fig(P.fig('start'), 'Tính ô bắt đầu với L = 100.', 14)
    D.box('purple', 'VÌ SAO ĐÚNG?', ['Hợp số x ≤ R có một ước nguyên tố p ≤ √x ≤ √R, và x ≥ p² (vì x = p · (x/p) với x/p ≥ p). Vậy x là một bội của p không nhỏ hơn '
                                     'max(p², L): nó bị gạch. Ngược lại, số nguyên tố x không là bội của p nào nhỏ hơn nó, và không bị gạch bởi chính nó vì ta bắt đầu từ p².'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 14)
    D.code('NTDOAN.CPP: sàng trên đoạn', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(√R log log √R) cho sàng nhỏ, O((R − L) log log R + π(√R)) cho mỗi đoạn: khoảng 3 · 10^{6} phép gạch. Test lớn nhất chạy trong ' + tm('opt.cpp', 3) + '.')
    D.box('blue', 'MỞ RỘNG: CHỈ LƯU SỐ LẺ', ['Bỏ qua các số chẵn (xử lí riêng số 2) thì mảng đánh dấu giảm một nửa và số phép gạch giảm đáng kể. '
                                           'Với p lẻ, bước gạch là 2p trên trục số (bước p trên mảng số lẻ).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Gạch chính p** khi L ≤ p ≤ R: quên max với p².', '**Quên L = 1.**',
               '**Tổng tràn int:** tổng tới 3,6 · 10^{16}; dùng long long.', '**(ll)p * p:** p tới 10^{6}, p * p tính bằng int bị tràn.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['sieveR.cpp', 'naive.cpp', 'opt.cpp'])
