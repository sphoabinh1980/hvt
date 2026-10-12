def build(D, P):
    S = lambda f: str(P.total(f))
    tm = lambda f, k: P.scores[f]['detail'][k - 1].split()[1].replace('.', ',').replace('s', ' giây')
    D.h('1. Hiểu bài toán')
    D.p('Với mỗi i, gọi G_{i} là ƯCLN của dãy sau khi bỏ a_{i}. Cần tìm max G_{i} và chỉ số i nhỏ nhất đạt max. '
        'Có n cách bỏ, mỗi cách là một câu hỏi "ƯCLN của n − 1 số". Thử ví dụ 1: bỏ số 7 được gcd(12, 18, 24, 30) = 6; bỏ số nào khác thì số 7 còn lại '
        'và ƯCLN chỉ là 1 (7 nguyên tố, không chia hết các số kia).')

    D.h('2. Cách ngây thơ: Bỏ thử từng phần tử')
    D.p('Với mỗi i, tính lại gcd của mọi a_{j} (j ≠ i), giữ giá trị lớn nhất. Cập nhật khi g **lớn hơn hẳn** để giữ chỉ số nhỏ nhất khi hòa.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách bỏ thử từng phần tử', 12)
    D.code('Cách ngây thơ: O(n²) lần gọi gcd', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** n · (n − 1) lần gọi gcd: 9 · 10^{6} với n = 3000 (mất ' + tm('naive.cpp', 1) + '), nhưng 2,5 · 10^{11} với n = 5 · 10^{5}.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (n ≤ 3000): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.',
               '**Subtask 2** (n ≤ 5 · 10^{5}): quá giới hạn: **0 điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', [
        'Khi bỏ a_{i} và khi bỏ a_{i+1}, hai dãy còn lại giống nhau gần như hoàn toàn, nhưng ta tính lại ƯCLN từ đầu. '
        'Phần chung lớn nhất là: **khúc đầu a_{1..i−1}** và **khúc cuối a_{i+1..n}**.'])

    D.h('4. Phá bế tắc: ƯCLN tiền tố và hậu tố')
    D.p('Dãy còn lại sau khi bỏ a_{i} gồm hai khúc: a_{1}, ..., a_{i−1} (một **tiền tố**) và a_{i+1}, ..., a_{n} (một **hậu tố**). '
        'ƯCLN có tính "gộp dần" (gcd(x, y, z) = gcd(gcd(x, y), z)), nên:')
    D.eq('**G_{i} = gcd(L[i − 1], R[i + 1]),   L[i] = gcd(a_{1..i}),   R[i] = gcd(a_{i..n}).**')
    D.p('Hai mảng L, R tính được trong một lượt từ trái sang phải và một lượt từ phải sang trái: L[i] = gcd(L[i − 1], a_{i}), R[i] = gcd(R[i + 1], a_{i}).')
    D.fig(P.fig('prefix'), 'Ví dụ 1: mảng L (trái sang phải), R (phải sang trái) và kết quả bỏ từng phần tử.', 15)
    D.box('purple', 'MẸO: PHẦN TỬ TRUNG HÒA 0', [
        'gcd(0, x) = x với mọi x, nên 0 đóng vai "ƯCLN của dãy rỗng". Đặt L[0] = R[n + 1] = 0 thì bỏ a_{1} cho G_{1} = gcd(0, R[2]) = R[2] và bỏ a_{n} '
        'cho G_{n} = L[n − 1], không cần if riêng. Với n = 2 (ví dụ 2): G_{1} = a_{2} = 6, G_{2} = a_{1} = 4: in "6 1".'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 13)
    D.code('BOMOTSO.CPP: gcd tiền tố + hậu tố', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** 3n lần gọi gcd, mỗi lần O(log 10^{18}): thực tế rất nhanh vì giá trị gcd giảm rất sớm; bộ nhớ O(n) cho ba mảng long long (12 MB). '
        'Test lớn nhất mất ' + tm('opt.cpp', 2) + ', chủ yếu là đọc 5 · 10^{5} số.')
    D.box('blue', 'MỞ RỘNG: KĨ THUẬT TIỀN TỐ – HẬU TỐ', [
        'Mẫu "bỏ một phần tử" dùng được cho mọi phép toán có tính kết hợp: tích (khi không được chia), max, min, xor, BCNN... '
        'Chẳng hạn "tích các phần tử trừ a_{i}" theo mô-đun hợp số không thể làm bằng cách chia cho a_{i}, nhưng làm được bằng tiền tố × hậu tố.'])
    D.h('6. Bẫy thường gặp')
    D.bullets([
        '**Chọn sai chỉ số khi hòa:** dùng `>=` sẽ giữ chỉ số lớn nhất. Ví dụ 3 (5 5 5) phải in "5 1".',
        '**Truy cập L[−1] hoặc R[n + 2]:** cấp phát n + 2 phần tử và dùng phần tử trung hòa 0.',
        '**Dùng int:** a_{i} tới 10^{18}.',
        '**Dùng "gcd cả dãy" để suy ra:** không có công thức "bỏ a_{i} khỏi gcd" (khác với tổng, có thể trừ ra). Đây chính là lí do cần tiền tố và hậu tố.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'opt.cpp'])
