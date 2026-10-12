def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Dấu của tích tính riêng: âm khi đúng một thừa số âm, và không in dấu khi tích bằng 0. Phần còn lại là **nhân hai số lớn không âm**. '
        'Nếu x = Σ x[i] · B^{i} và y = Σ y[j] · B^{j} (B là cơ số, x[0] là ô thấp nhất) thì')
    D.eq('x · y = Σ_{k} c[k] · B^{k},   **c[k] = Σ_{i + j = k} x[i] · y[j]**')
    D.p('Cách làm "trên giấy" của Tập 1: cộng dồn mọi tích x[i] · y[j] vào cột c[i + j], sau đó mới **dồn nhớ một lượt** từ cột thấp lên cột cao.')
    D.fig(P.fig('grid'), 'Ví dụ 1 (123 × 45) trong cơ số 10: mỗi màu là một cột k = i + j.', 15.2)

    D.h('2. Cách ngây thơ: __int128')
    D.code('Cách ngây thơ: __int128', P.src('naive.cpp'))
    D.p('|a · b| ≤ 10^{36} < 1,7 · 10^{38}: đúng subtask 1. Phải tự in __int128 bằng cách tách từng chữ số. **' + S('naive.cpp') + ' điểm**.')

    D.h('3. Bế tắc')
    D.p('Nhân cộng dồn trong cơ số 10 (`mid.cpp`) đúng với mọi độ dài. Với 5000 chữ số là 2,5 · 10^{7} phép nhân (' + P.scores['mid.cpp']['detail'][1].split()[1] + '), '
        'nhưng 5 · 10^{4} chữ số là 2,5 · 10^{9}: quá thời gian, **' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Số phép nhân là (số ô của a) × (số ô của b). Gộp nhiều chữ số vào một ô làm số ô giảm, số phép nhân giảm theo **bình phương**. '
                                  'Nhưng ô càng lớn, mỗi tích càng lớn, và c[k] cộng dồn hàng nghìn tích có thể tràn.'])

    D.h('4. Phá bế tắc: Chọn cơ số 10⁴')
    D.fig(P.fig('bases'), 'So sánh ba cơ số với hai số 50 000 chữ số.', 14.5)
    D.p('Với cơ số 10^{4}: mỗi tích < 10^{8}, mỗi cột cộng tối đa 12 500 tích, nên c[k] < 12 500 · 9999^{2} ≈ 1,25 · 10^{12}, rất xa giới hạn 9,2 · 10^{18} của long long. '
        'Khi dồn nhớ, c[k + 1] tăng thêm tối đa c[k] / 10^{4} ≈ 1,25 · 10^{8}: vẫn an toàn.')
    D.box('purple', 'BẪY: CƠ SỐ 10⁹ NHƯ BÀI 17.2', ['$c[i + j] += x[i] * y[j];   // cơ số 10^9',
                                                    'Mỗi tích tới 10^{18}; cộng 10 tích đã tràn. Chương trình `trap.cpp` chỉ đúng khi mỗi số có 1–2 ô (subtask 1): **' + S('trap.cpp') + ' điểm**. '
                                                    'Bài 17.2 dùng được 10^{9} vì ở đó mỗi lần chỉ nhân với một số nhỏ, không cộng dồn.'])
    D.sub('Chạy tay ví dụ 2')
    D.p('99 999 999 = [9999, 9999] trong cơ số 10^{4}. c[0] = 9999^{2} = 99 980 001, c[1] = 2 · 9999^{2} = 199 960 002, c[2] = 99 980 001. Dồn nhớ:')
    D.table(['Cột', 'Trước khi dồn', 'Cộng nhớ', 'Giữ lại (mod 10⁴)', 'Nhớ lên'], [
        ['c[0]', '99 980 001', '0', '0001', '9 998'], ['c[1]', '199 960 002', '9 998', '0000', '19 997'],
        ['c[2]', '99 980 001', '19 997', '9998', '9 999'], ['c[3]', '0', '9 999', '9999', '0']],
        widths=[0.8, 1.8, 1.4, 2.0, 1.4], align=['center'] * 5, sz=20)
    D.p('Đọc từ ô cao: 9999 | 9998 | 0000 | 0001, in ô cao nhất bình thường và các ô sau đủ 4 chữ số: −9 999 999 800 000 001.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối', 12.5)
    D.code('TICHLON.CPP: nhân cộng dồn cơ số 10⁴', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(n · m) với n, m ≤ 12 500 ô: 1,56 · 10^{8} phép nhân-cộng trong một vòng lặp rất đơn giản, chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Thuật toán Karatsuba chia đôi mỗi số: 3 phép nhân nửa kích thước thay vì 4, độ phức tạp O(n^{1,585}). Với số hàng triệu chữ số, dùng biến đổi Fourier nhanh (FFT/NTT), O(n log n).',
                              'Có thể dùng cơ số 10^{6} nếu dồn nhớ định kì (sau mỗi khoảng 9 hàng i), nhưng 10^{4} đã đủ nhanh và an toàn.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Cơ số quá lớn:** c[k] tràn.', '**In thiếu số 0 đầu ô** (%04lld).', '**In -0** khi một thừa số bằng 0.',
               '**Cắt khối từ đầu xâu** thay vì từ cuối: khối ngắn phải là khối cao nhất.', '**Mảng c thiếu một ô** cho số nhớ cuối cùng.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'trap.cpp', 'opt.cpp'])
