"""Phụ lục B: thư viện hàm số học dùng lại được (mọi đoạn mã trong lib/ đã biên dịch và kiểm tra cùng nhau)."""
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
L = lambda f: open(os.path.join(ROOT, 'lib', f), encoding='utf-8').read()


def build(D):
    D.big_title('PHỤ LỤC B. THƯ VIỆN HÀM SỐ HỌC')
    D.p('Phụ lục này gom lại những hàm xuất hiện nhiều lần trong 60 lời giải, viết theo cùng một quy ước để em có thể chép nguyên vào bài thi. '
        'Tám đoạn mã dưới đây được ghép thành một tệp và biên dịch cùng nhau (g++ -std=gnu++17), mỗi hàm đều đã chạy thử trên các ví dụ ghi trong chú thích.')
    D.table(['Hàm', 'Công dụng', 'Độ phức tạp', 'Dùng ở bài'], [
        ['md, mulmod, power', 'Số dư không âm; nhân và lũy thừa theo mô-đun tới 10^{18}', 'O(1), O(log b)', '1.2, 9.1–9.3, 10.x, 11.x'],
        ['gcd, lcmCap', 'ƯCLN; BCNN có chặn trên, không tràn', 'O(log)', '3.x, 7.3, 14.1, 20.x'],
        ['extgcd, inverse', 'Nghiệm a x + b y = g; nghịch đảo mô-đun bất kì', 'O(log)', '4.x, 10.x, 12.x'],
        ['crt', 'Ghép hai phương trình đồng dư (mô-đun không cần nguyên tố cùng nhau)', 'O(log)', '12.x, 13.3'],
        ['sieve, factorSmall, factorBig', 'Sàng tuyến tính + ước nguyên tố nhỏ nhất; phân tích thừa số', 'O(n); O(log x); O(π(√x))', '6.x, 7.x, 8.x, 14.2'],
        ['isPrime', 'Miller–Rabin tất định cho long long', 'O(12 log n)', '5.3, 8.x'],
        ['initComb, C', 'Tổ hợp theo mô-đun nguyên tố bằng bảng giai thừa', 'O(N); O(1)', '13.x, 14.3'],
        ['mul, matPow', 'Lũy thừa ma trận theo mô-đun', 'O(k^{3} log e)', '15.x'],
        ['print128', 'In số __int128', 'O(39)', '18.2, 20.3'],
    ], widths=[2.3, 3.9, 1.7, 1.9], align=['left', 'left', 'center', 'center'], sz=18, mono_cols=(0,))

    D.h('B.1. Số dư và lũy thừa theo mô-đun')
    D.p('Mọi hàm nhận số dư âm hay dương đều trả về số dư trong [0, m). mulmod dùng __int128 nên an toàn với mô-đun tới 9,2 · 10^{18} (với mô-đun < 3 · 10^{9} có thể nhân trực tiếp bằng long long).')
    D.code('Số dư, nhân và lũy thừa theo mô-đun', L('s1_mod.cpp'))
    D.p('Chạy thử: md(−7, 3) = 2; power(2, 10^{9} + 6, 10^{9} + 7) = 1 (định lí Fermat nhỏ); mulmod(p − 14, p − 14, p) = 196 với p = 10^{18} + 3.')

    D.h('B.2. ƯCLN, BCNN có chặn, Euclid mở rộng')
    D.code('gcd, lcmCap, extgcd, inverse', L('s2_gcd.cpp'))
    D.p('Chạy thử: extgcd(240, 46) cho g = 2, x = −9, y = 47 (240 · (−9) + 46 · 47 = 2); inverse(3, 7) = 5; inverse(4, 8) = −1 (không tồn tại); '
        'lcmCap(10^{18}, 3) = INF.')

    D.h('B.3. Định lí Trung Hoa cho hai phương trình')
    D.p('Ghép lần lượt từng phương trình để giải hệ nhiều phương trình. Hàm xử lí cả trường hợp m_{1}, m_{2} không nguyên tố cùng nhau (khi đó có nghiệm khi và chỉ khi g | r_{2} − r_{1}).')
    D.code('crt', L('s3_crt.cpp'))
    D.p('Chạy thử: x ≡ 2 (mod 3), x ≡ 3 (mod 5) cho x ≡ 8 (mod 15); x ≡ 1 (mod 4), x ≡ 3 (mod 6) cho x ≡ 9 (mod 12); x ≡ 1 (mod 4), x ≡ 2 (mod 6) vô nghiệm.')

    D.h('B.4. Sàng và phân tích thừa số nguyên tố')
    D.p('Sàng tuyến tính đánh dấu mỗi hợp số đúng một lần (bởi ước nguyên tố nhỏ nhất của nó). factorSmall dùng cho số ≤ n đã sàng; factorBig cho số tới (max pr)^{2}, '
        'ví dụ sàng tới 10^{6} thì phân tích được mọi số ≤ 10^{12} (bài 14.2).')
    D.code('sieve, factorSmall, factorBig', L('s4_sieve.cpp'))
    D.p('Chạy thử: sieve(10^{6}) cho 78 498 số nguyên tố; factorSmall(360) = 2^{3} · 3^{2} · 5; factorBig(200 560 490 130) có 11 ước nguyên tố; factorBig(999 999 999 989) = chính nó.')

    D.h('B.5. Kiểm tra nguyên tố Miller–Rabin')
    D.p('Với 12 cơ số nguyên tố đầu tiên, kết quả đúng cho mọi n < 3,3 · 10^{24}, tức mọi số long long. Phải dùng mulmod (128 bit) vì n tới 10^{18}.')
    D.code('isPrime', L('s5_mr.cpp'))
    D.p('Chạy thử: isPrime(10^{18} + 3) = true; isPrime((10^{9} + 7) · 998 244 353) = false.')

    D.h('B.6. Tổ hợp theo mô-đun nguyên tố')
    D.code('initComb, C', L('s6_comb.cpp'))
    D.p('Chạy thử: C(12, 2) = 66; C(2 · 10^{6}, 10^{6}) mod (10^{9} + 7) = 192 151 600. Khi n rất lớn mà k nhỏ, nhân dần n(n − 1)...(n − k + 1) rồi nhân nghịch đảo của k! (bài 14.3).')

    D.h('B.7. Lũy thừa ma trận')
    D.p('Thứ tự vòng lặp i – t – j truy cập bộ nhớ liên tục và nhanh hơn i – j – t. Với ma trận lớn và nhiều truy vấn, tính sẵn A^{2^{i}} rồi nhân vectơ (bài 15.3).')
    D.code('mul, matPow', L('s7_mat.cpp'))
    D.p('Chạy thử: [[1, 1], [1, 0]]^{10} có phần tử góc trái trên 89 = F(11).')

    D.h('B.8. In số 128 bit')
    D.code('print128', L('s8_print.cpp'))
    D.p('Chạy thử: print128(−10^{18} · 10^{18}) in ra −1 và 36 chữ số 0.')
    D.box('blue', 'CÁCH DÙNG THƯ VIỆN', ['Chép theo thứ tự B.1 → B.8 vì các hàm sau dùng các hàm trước (crt dùng extgcd, mulmod; isPrime dùng power).',
                                         'Chỉ chép những gì cần: mỗi hàm thừa là một chỗ có thể gõ sai. Và luôn tự hỏi lại: các đại lượng của bài này lớn tới đâu, hàm có còn an toàn không?'])
