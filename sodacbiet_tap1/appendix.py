"""Phụ lục A (tổng hợp thuật toán, công thức) và Phụ lục B (những con số đáng nhớ)."""
import os, json
import book

ROOT = os.path.dirname(os.path.abspath(__file__))

CPLX = {1: ('O(n · L)', 'O(L)'), 2: ('O(b²)', 'O(log b)'), 3: ('O(n)', 'O(log n)'), 4: ('O(k)', 'O(log k)'),
        5: ('O(q · n)', 'O(n + q)'), 6: ('O((R − L) · L)', 'O(1) mỗi câu hỏi'), 7: ('O(2^{L})', 'O(n)'), 8: ('O(n)', 'O(√n)'),
        9: ('O(N)', 'O(L)'), 10: ('O(10^{K})', 'O(C(K + 9, 9) · K)'), 11: ('O(K)', 'O(μ + λ)'), 12: ('O(10^{K})', 'O(10 · K)'),
        13: ('O(đáp số − n)', 'O(L)'), 14: ('O(k · L)', 'O(L)'), 15: ('O(R − L)', 'O(L · S · 10)'), 16: ('O(N)', 'O(L · Σ s² · 10)'),
        17: ('O(R)', 'O(√R · log R)'), 18: ('O(N√N)', 'O(N log N)'), 19: ('O(Q√n)', 'O(N + Q log n)'), 20: ('O(đáp số)', 'O(n)')}


def build(D):
    D.big_title('PHỤ LỤC A. TỔNG HỢP THUẬT TOÁN VÀ CÔNG THỨC')
    D.p('Bảng dưới đây tóm tắt 20 bài toán mẫu của sách: cách ngây thơ, cách tối ưu, độ phức tạp, và **điểm thực tế** mà mỗi cách nhận được trên bộ test của bài (thang 100). '
        'Khoảng cách giữa hai cột điểm chính là "giá trị" của quan sát then chốt trong từng bài.')
    rows = []
    for n in book.LESSONS:
        d = os.path.join(ROOT, 'problems', str(n))
        m = {}
        exec(open(os.path.join(d, 'meta.py')).read(), m)
        sc = json.load(open(os.path.join(d, 'scores.json')))
        a, b = m['SOLS'][0], m['SOLS'][-1]
        ca, cb = CPLX[n]
        rows.append(['**%d**' % n, m['CODE'], '%s\n%s' % (a[1], ca), str(sum(sc[a[0]]['pts'])), '%s\n%s' % (b[1], cb), str(sum(sc[b[0]]['pts']))])
    D.table(['Bài', 'Bài toán', 'Cách ngây thơ · độ phức tạp', 'Điểm', 'Cách tối ưu · độ phức tạp', 'Điểm'], rows,
            widths=[0.6, 1.6, 3.0, 0.75, 3.3, 0.75], align=['center', 'left', 'left', 'center', 'left', 'center'], sz=17, hdr_sz=18, bold_cols=(5,))
    D.p('L là số chữ số; với các bài có N, R tới 10^{18}, L ≤ 19.', after=120)

    D.h('A.1. Công thức về chữ số')
    D.table(['Đại lượng', 'Công thức', 'Bài'], [
        ['Số chữ số của n ≥ 1', '⌊log₁₀ n⌋ + 1', '2'],
        ['Chữ số đầu của aᵇ', '⌊10^{f}⌋ với f là phần lẻ của b · log₁₀ a', '2'],
        ['Chữ số hàng 10ᵏ của n', '⌊n / 10ᵏ⌋ mod 10', '1'],
        ['Số lần chữ số d ở hàng 10ᵏ trong [0, n]', 'tách n = cao · 10^{k+1} + d_k · 10ᵏ + thấp, đếm theo cột', '1'],
        ['Số chữ số 0 tận cùng của n!', 'Σ ⌊n / 5ⁱ⌋ (Legendre)', '3'],
        ['Chữ số khác 0 cuối cùng của n!', 'D(n) = 2^{⌊n/5⌋} · D(⌊n/5⌋) · D(n mod 5) (mod 10, xử lí riêng lũy thừa 2)', '3'],
        ['Tổng số chữ số dùng để viết 1..n', 'Σ theo nhóm độ dài: 9 · 10^{k−1} số có k chữ số', '4'],
        ['Căn số (digital root)', 'dr(n) = 1 + (n − 1) mod 9 với n ≥ 1', '6'],
        ['Số dư của đoạn chữ số [l, r]', '(P_{r} − P_{l−1} · 10^{r−l+1}) mod m với P là tiền tố số dư', '5'],
        ['Chu kì của 1/n', 'cấp của 10 modulo n′ (n′ = n bỏ hết thừa số 2, 5); độ dài phần không tuần hoàn = max(mũ của 2, mũ của 5)', '8'],
    ], widths=[2.6, 5.6, 0.6], align=['left', 'left', 'center'], sz=18)

    D.h('A.2. Dấu hiệu chia hết')
    D.table(['Chia hết cho', 'Dấu hiệu', 'Lí do'], [
        ['2, 5, 10', 'chữ số cuối', '10 ≡ 0'],
        ['4, 25 / 8, 125', 'hai / ba chữ số cuối', '100 ≡ 0 (mod 4, 25), 1000 ≡ 0 (mod 8, 125)'],
        ['3, 9', 'tổng các chữ số', '10 ≡ 1 (mod 9)'],
        ['11', 'tổng đan dấu các chữ số', '10 ≡ −1 (mod 11)'],
        ['7, 11, 13', 'tổng đan dấu các nhóm 3 chữ số', '1000 ≡ −1 (mod 1001 = 7 · 11 · 13)'],
        ['37', 'tổng các nhóm 3 chữ số', '1000 ≡ 1 (mod 999 = 27 · 37)'],
        ['m bất kì', 'Horner: r ← (10r + d) mod m', 'tính chất số dư của tổng và tích'],
    ], widths=[1.6, 3.2, 4.0], align=['left', 'left', 'left'], sz=18)

    D.h('A.3. Kĩ thuật và khi nào dùng')
    D.table(['Kĩ thuật', 'Dấu hiệu nhận biết', 'Bài'], [
        ['Đếm theo cột (theo hàng chữ số)', 'Tổng/đếm chữ số trên mọi số trong một đoạn', '1, 4'],
        ['Logarit, lũy thừa theo mô-đun', 'Chữ số đầu/cuối của số khổng lồ', '2, 3'],
        ['Tiền tố số dư', 'Nhiều truy vấn số dư của đoạn con chữ số', '5'],
        ['BFS trên số dư', 'Số nhỏ nhất có chữ số hạn chế chia hết cho n', '7'],
        ['Sinh theo nửa đầu', 'Số đối xứng: chỉ nửa đầu là tự do', '9, 17'],
        ['Duyệt tập chữ số thay vì số', 'Điều kiện chỉ phụ thuộc tập (đa tập) chữ số', '10'],
        ['Phát hiện chu trình ρ', 'Lặp một hàm trên tập hữu hạn', '11'],
        ['Dựng nghiệm từng chữ số', 'Điều kiện trên k chữ số cuối chỉ phụ thuộc k chữ số cuối', '12'],
        ['Tham lam từ trái sang, ngăn xếp', 'Số lớn/nhỏ nhất sau khi xóa, ghép, hoán vị', '13, 14'],
        ['Quy hoạch động chữ số', 'Đếm số trong [L, R] thỏa điều kiện trên chữ số; số thứ k', '15, 16'],
        ['Miller–Rabin', 'Kiểm tra nguyên tố số tới 10^{18}', '17'],
        ['Sàng tổng ước, sàng spf', 'Tính hàm số học cho mọi n ≤ 10^{7}', '18, 19'],
        ['Nhiều con trỏ', 'Sinh theo thứ tự tăng các số có dạng tích', '20'],
    ], widths=[2.8, 5.2, 0.8], align=['left', 'left', 'center'], sz=18)

    D.pagebreak()
    D.big_title('PHỤ LỤC B. NHỮNG CON SỐ ĐÁNG NHỚ')
    D.p('Các danh sách dưới đây đều được tính lại bằng chương trình (C++ trong sách hoặc Python với số nguyên lớn). Dùng chúng để kiểm tra nhanh chương trình của em.')
    D.table(['Họ số', 'Các số đầu tiên', 'Ghi chú'], [
        ['Số tự luân (Armstrong)', '1..9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834', 'Hữu hạn: 88 số, lớn nhất 39 chữ số (Bài 10)'],
        ['Tổng giai thừa chữ số', '1, 2, 145, 40585', 'Chỉ có 4 số (Bài 10)'],
        ['Số tự đồng cấu', '1, 5, 6, 25, 76, 376, 625, 9376, 90625, 109376, 890625', 'n² tận cùng bằng n (Bài 12)'],
        ['Số Kaprekar (bình phương)', '1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728', '45² = 2025 = 20 | 25, 20 + 25 = 45'],
        ['Hằng số Kaprekar', '495 (3 chữ số), 6174 (4 chữ số)', 'Sắp giảm − sắp tăng (Bài 11)'],
        ['Số vui vẻ ≤ 50', '1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49', '143 số ≤ 1000 (Bài 11, 15)'],
        ['Số tự sinh (self number)', '1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97', 'Không có dạng m + S(m) (Bài 12)'],
        ['Số Harshad ≤ 30', '1..10, 12, 18, 20, 21, 24, 27, 30', '33 số ≤ 100 (Bài 16)'],
        ['Số Lychrel ứng viên', '196 → 887 → 1675 → 7436 → ...', 'Chưa ai biết có về số đối xứng không'],
        ['Repunit nguyên tố', 'R₂, R₁₉, R₂₃, R₃₁₇, R₁₀₃₁', 'R_{n} = 11...1 (n chữ số) (Bài 8)'],
        ['Số tuần hoàn', '142857 = chu kì của 1/7', '142857 · k (k = 1..6) là hoán vị vòng của nó; 142857 · 7 = 999999'],
        ['Nguyên tố đối xứng', '2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, ...', '47 995 số < 10^{12} (Bài 17)'],
        ['Nguyên tố xoay vòng < 100', '2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97', '55 số < 10^{7} (Bài 17)'],
        ['Nguyên tố cắt phải', '2, 3, 5, 7, 23, 29, 31, 37, 53, 59, 71, 73, 79, ...', '83 số, lớn nhất 73 939 133 (Bài 17)'],
        ['Số hoàn hảo', '6, 28, 496, 8128, 33550336, 8589869056', 'Dạng 2^{p−1}(2^{p} − 1) (Bài 18)'],
        ['Cặp số thân thiết', '(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368)', '100 cặp với b ≤ 10^{7} (Bài 18)'],
        ['Số tam giác', '1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...', '2016 = T₆₃ (Bài 20)'],
        ['Số Hamming', '1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, ...', 'Số thứ 2026 là 9 · 10^{9} (Bài 20)'],
        ['Fibonacci', '1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...', 'F₉₃ vượt long long (Bài 20)'],
        ['Catalan', '1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, ...', 'Số dãy ngoặc đúng (Bài 20)'],
    ], widths=[2.1, 4.0, 2.7], align=['left', 'left', 'left'], sz=17, hdr_sz=18)
    D.h('B.1. Năm 2026 qua lăng kính của cuốn sách')
    D.table(['Câu hỏi', 'Trả lời', 'Bài'], [
        ['Tổng chữ số, căn số', '10; căn số 1', '1, 6'],
        ['Phân tích', '2026 = 2 · 1013 (1013 nguyên tố)', '18'],
        ['Tổng hai bình phương', '2026 = 1² + 45², đúng một cách', '19'],
        ['Tổng ba số tam giác', '2026 = T₄₃ + T₃₉ + T₂₄ = 946 + 780 + 300', '20'],
        ['Zeckendorf', '2026 = 1597 + 377 + 34 + 13 + 5', '20'],
        ['Hoán vị kế tiếp', '2062', '13'],
        ['Xóa một chữ số để nhỏ nhất', '26 (từ 026)', '14'],
        ['Có phải số Harshad?', 'Không (2026 không chia hết cho 10); nhưng 2024 và 2025 thì có', '16'],
        ['Số năm từ 1 đến 2026 có tổng chữ số 10', '121', '15'],
    ], widths=[3.2, 4.8, 0.8], align=['left', 'left', 'center'], sz=18)
    D.kbox('LỜI KHUYÊN', ['Khi tự viết lại một chương trình trong sách, hãy luôn viết kèm **một cách ngây thơ** và đối chiếu trên dữ liệu nhỏ ngẫu nhiên, như cuốn sách đã làm với mọi chương trình. '
                          'Những con số trong phụ lục này là "đáp số mẫu" để em kiểm tra nhanh; còn đối chiếu ngẫu nhiên mới là cách tìm ra lỗi thật sự.'])
