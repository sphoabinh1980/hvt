def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Cần d(x) cho **mọi** x trong một đoạn tới 10^{6} số, mỗi số tới 10^{12}. Theo công thức số ước, d(x) tính được từ phân tích thừa số của x; '
        'vậy bài toán là **phân tích đồng loạt** 10^{6} số lớn. Đây là bài kết hợp Bài 7 (công thức số ước) với Bài 8 (sàng trên đoạn).')

    D.h('2. Hai cách ngây thơ')
    D.sub('Cách 1: Sàng điều hòa tới R')
    D.code('Cách ngây thơ 1: sàng điều hòa đếm ước tới R', P.src('harm.cpp'))
    D.p('Với mỗi k, cộng 1 vào mọi bội của k: O(R log R). Tốt với R ≤ 10^{6}; không cấp phát nổi mảng tới 10^{12}.')
    D.sub('Cách 2: Đếm ước từng số')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách đếm ước từng số', 14)
    D.code('Cách ngây thơ 2: cặp ước cho từng số', P.src('naive.cpp'))
    D.p('O((R − L) · √R): 100 số cỡ 10^{12} chỉ 10^{8} phép chia (' + tm('naive.cpp', 2) + '), nhưng 10^{6} số thì gấp 10 000 lần.')

    D.h('3. Bế tắc')
    D.bullets(['**Sàng điều hòa:** subtask 1, **' + S('harm.cpp') + ' điểm**.', '**Đếm từng số:** subtask 2, **' + S('naive.cpp') + ' điểm** (subtask 1 có 10^{6} số, cũng quá chậm).',
               '**Subtask 3** cần một cách chạy tốt với cả đoạn dài lẫn số lớn.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Thử chia từng số tới √x là mỗi số tự đi tìm ước. Hãy **đảo vòng lặp** như khi sàng: mỗi số nguyên tố p ≤ √R tự "ghé thăm" các bội của nó trong đoạn.'])

    D.h('4. Phá bế tắc: Phân tích đồng loạt')
    D.nums(['Mảng rest[i] = L + i (phần chưa phân tích), d[i] = 1.',
            'Với mỗi số nguyên tố p ≤ √R, duyệt **mọi** bội j của p trong [L, R] (bắt đầu từ ⌈L/p⌉ · p, **không** lấy max với p² như khi sàng: ở đây p là thừa số của chính nó cũng phải đếm). '
            'Chia rest[j − L] cho p tới hết, được số mũ e, nhân d[j − L] với (e + 1).',
            'Cuối cùng, nếu rest[i] > 1 thì nó không có ước nguyên tố nào ≤ √R, nên **là một số nguyên tố** (lớn hơn 10^{6}): nhân d[i] với 2.'])
    D.fig(P.fig('table'), 'Phân tích đồng loạt [999 999 999 990, 999 999 999 995].', 15.5)
    D.box('purple', 'VÌ SAO PHẦN CÒN LẠI LÀ SỐ NGUYÊN TỐ?', ['Sau bước 2, rest[i] không có ước nguyên tố nào ≤ √R. Nếu rest[i] là hợp số thì nó có ít nhất hai thừa số > √R, '
        'khi đó rest[i] > R ≥ x: vô lí. Vậy rest[i] = 1 hoặc là một số nguyên tố, với số mũ 1.'])
    D.p('Tổng số lần "ghé" xấp xỉ (R − L) · Σ_{p ≤ 10^{6}} 1/p ≈ (R − L) · ln ln 10^{6} ≈ 2,6 · 10^{6}, cộng thêm số lần chia lặp cho các lũy thừa.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 14)
    D.code('UOCDOAN.CPP: phân tích đồng loạt trên đoạn', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(√R log log √R + (R − L) log log R + (R − L) log R). Đoạn 10^{6} số chạy trong ' + tm('opt.cpp', 3) + '. '
        'Bộ nhớ: hai mảng long long 10^{6} phần tử (16 MB).')
    D.box('blue', 'MỞ RỘNG', ['Cùng khung này tính được σ(x), φ(x), số ước nguyên tố phân biệt... cho mọi x trong đoạn: chỉ thay công thức "nhân dần" ở bước 2 và bước 3.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Bắt đầu từ max(p², ...):** bỏ sót thừa số p của chính các số x = p · (nhỏ hơn p) trong đoạn; với L nhỏ (như [1, 10]) kết quả sai.',
               '**Quên phần còn lại > 1:** thiếu thừa số 2 cho mọi số có ước nguyên tố lớn (999 999 999 991 = 757 · 1321 · 1 000 003).',
               '**Luật hòa:** chỉ cập nhật khi d lớn hơn hẳn để giữ x nhỏ nhất.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['harm.cpp', 'naive.cpp', 'opt.cpp'])
