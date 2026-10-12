def build(D, P):
    D.objectives([
        'Chứng minh được tính chất nền tảng: **một số và tổng các chữ số của nó có cùng số dư khi chia cho 9**.',
        'Tính **căn số** (cộng chữ số lặp lại tới khi còn một chữ số) bằng một công thức O(1): dr(n) = 1 + (n − 1) mod 9.',
        'Đếm các số có căn số cho trước trên một đoạn tới 10^{18}, và tính căn số của tích, của lũy thừa khổng lồ.',
        'Biết dùng "phép thử bỏ chín" để kiểm tra phép tính, và biết giới hạn của nó.'])
    D.kbox('KHỞI ĐỘNG', [
        'Lấy số 987 654 321, cộng các chữ số được 45; cộng tiếp được 9. Lấy 2026: 2 + 0 + 2 + 6 = 10, rồi 1 + 0 = 1. Con số một chữ số cuối cùng gọi là **căn số** (digital root).',
        'Người xưa dùng căn số để kiểm tra phép nhân trên giấy mà không cần máy tính. Có cách nào biết ngay căn số của 2^{2026} mà không cần viết ra 610 chữ số của nó không?'])
    D.fig(P.fig('chain'), 'Cộng chữ số lặp lại cho tới khi chỉ còn một chữ số.', 15)

    D.h('1. Tổng chữ số và số dư khi chia cho 9')
    D.kbox('ĐỊNH NGHĨA (TỔNG CHỮ SỐ, CĂN SỐ)', [
        'S(n) là tổng các chữ số của n. **Căn số** dr(n) của số n ≥ 1 là số một chữ số thu được khi thay n bởi S(n) lặp đi lặp lại cho tới khi n < 10. Quy ước dr(0) = 0.'])
    D.kbox('ĐỊNH LÍ', ['$eq **S(n) ≡ n (mod 9)**', 'Hệ quả: dr(n) ≡ n (mod 9). Vì dr(n) ∈ {1, ..., 9} với n ≥ 1, ta có công thức', '$eq **dr(n) = 1 + (n − 1) mod 9**   (n ≥ 1).'])
    D.kbox('VÌ SAO ĐÚNG?', [
        'Vì 10 ≡ 1 (mod 9) nên 10^{i} ≡ 1 (mod 9) với mọi i (Bài 5: trọng số của 9 đều bằng 1). Do đó n = Σ d_{i} · 10^{i} ≡ Σ d_{i} = S(n) (mod 9).',
        'Mỗi lần thay n bởi S(n), số dư khi chia cho 9 không đổi, nên căn số đồng dư với n. Trong 1..9 có đúng một số đồng dư với n theo mô-đun 9: số 9 thay cho số dư 0. '
        'Công thức 1 + (n − 1) mod 9 làm đúng việc ấy: n = 9, 18, 27... cho 9 chứ không phải 0.'])
    D.fig(P.fig('grid'), 'Căn số của 1..36: lặp lại với chu kì 9, đúng như số dư khi chia cho 9.', 15)
    D.kbox('LƯU Ý: TỐC ĐỘ CỦA VIỆC CỘNG CHỮ SỐ', [
        'S(n) nhỏ hơn n rất nhiều: n ≤ 10^{18} cho S(n) ≤ 162, rồi S ≤ 18, rồi một chữ số. Ngay cả một số dài 10^{6} chữ số cũng về một chữ số sau tối đa 4 lần cộng. '
        'Nhưng nếu cần căn số của **rất nhiều** số, thì công thức O(1) vẫn hơn hẳn.'])

    D.h('2. Bài toán CANSO')
    D.problem_box('CANSO', 'Cho Q câu hỏi, mỗi câu gồm ba số L, R, d. Hãy đếm các số nguyên x thuộc đoạn [L, R] có căn số bằng d.',
                  'Dòng đầu chứa Q (Q ≤ 10^{5}). Mỗi dòng tiếp theo chứa L, R, d (1 ≤ L ≤ R ≤ 10^{18}, 1 ≤ d ≤ 9).', 'Q dòng, mỗi dòng một số nguyên.')
    D.examples('CANSO', [('3\n1 100 1\n2026 2026 1\n1 1000000000000000000 9', '12\n1\n111111111111111111',
                          'Các số 1, 10, 19, ..., 100 (12 số). dr(2026) = 1. Các bội của 9 không vượt quá 10^{18}.')])

    D.h('3. Ý tưởng ngây thơ: Tính căn số từng số')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử từng số.', 12.5)
    D.code('CANSO.CPP (ngây thơ): thử từng x', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi số tốn khoảng 20 phép chia (hai vòng cộng chữ số): O((R − L) · log R). Đo thực tế: đoạn dài 10^{8} mất **1,3 giây**, dài 10^{9} mất **13,5 giây**. '
                               'Một đoạn dài 10^{18} cần khoảng 4 · 10^{11} năm, gấp 30 lần tuổi của vũ trụ.'])
    D.kbox('BẾ TẮC', ['Theo định lí ở mục 1, căn số chỉ phụ thuộc vào n mod 9. Tức là trên trục số, căn số lặp lại 1, 2, ..., 9, 1, 2, ..., 9 đều đặn. Đếm một dãy tuần hoàn thì đâu cần duyệt?'])

    D.h('4. Phá bế tắc: Căn số chính là số dư cho 9')
    D.step(1, 'Viết lại điều kiện')
    D.p('Với x ≥ 1: dr(x) = d ⇔ x ≡ d (mod 9) (với d = 9 hiểu là x ≡ 0). Các số như vậy là d, d + 9, d + 18, ...: một cấp số cộng công sai 9.')
    D.step(2, 'Đếm trên đoạn bằng hiệu hai tiền tố')
    D.p('Gọi dem(n) là số x ∈ [1, n] có căn số d. Nếu n < d thì dem(n) = 0; ngược lại các số d, d + 9, ..., d + 9t ≤ n với t = ⌊(n − d)/9⌋, nên **dem(n) = ⌊(n − d)/9⌋ + 1**. Đáp số là dem(R) − dem(L − 1).')
    D.step(3, 'Chạy tay câu hỏi (1, 100, 1)')
    D.p('dem(100) = ⌊99/9⌋ + 1 = 12, dem(0) = 0 (vì 0 < 1). Đáp số 12. Câu hỏi (1, 10^{18}, 9): dem(10^{18}) = ⌊(10^{18} − 9)/9⌋ + 1 = 111 111 111 111 111 110 + 1 = 111 111 111 111 111 111.')
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của cách đếm bằng công thức.', 11)
    D.code('CANSO.CPP: căn số = số dư cho 9', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi câu hỏi O(1): 10^{5} câu hỏi chạy trong thời gian đọc dữ liệu (khoảng **0,3 giây** khi dùng cin; dưới 0,1 giây với scanf).'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Căn số của tích và của lũy thừa')
    D.p('Vì căn số giữ nguyên số dư cho 9: dr(a · b) = dr(dr(a) · dr(b)) và dr(a + b) = dr(dr(a) + dr(b)). Với lũy thừa: tính r = a^{b} mod 9 bằng lũy thừa nhanh, rồi dr = r nếu r ≠ 0, dr = 9 nếu r = 0 (với a ≥ 1). '
        'Ví dụ: 2^{2026} mod 9 = 7 nên dr(2^{2026}) = 7, không cần viết ra 610 chữ số.')
    D.sub('Mở rộng 2: Phép thử bỏ chín')
    D.p('Để kiểm tra một phép nhân viết tay, so sánh căn số hai vế. Nếu khác nhau thì chắc chắn tính sai. Nếu giống nhau thì **chưa chắc** đã đúng: viết nhầm 8 754 346 thành 8 745 346 (đổi chỗ hai chữ số) không làm đổi căn số.')
    D.fig(P.fig('cast'), 'Kiểm tra 2026 × 4321 = 8 754 346 bằng căn số.', 14)
    D.sub('Mở rộng 3: Độ bền cộng và độ bền nhân')
    D.p('Số lần phải cộng chữ số trước khi về một chữ số gọi là **độ bền cộng**: 199 → 19 → 10 → 1 có độ bền 3; số nhỏ nhất có độ bền 4 là 1 theo sau bởi 22 chữ số 9. '
        'Thay tổng bằng **tích** các chữ số được **độ bền nhân**: 39 → 27 → 14 → 4 có độ bền 3; 277 777 788 888 899 có độ bền nhân 11, và người ta chưa tìm được số nào có độ bền nhân lớn hơn 11. '
        'Khác với căn số, tích chữ số không có công thức đồng dư đẹp: phải mô phỏng (may là dãy ngắn).')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Quên trường hợp chia hết cho 9:** dùng n % 9 cho 9, 18, 27 ra 0 thay vì 9.',
        '- **Căn số của 0** là 0, không phải 9: công thức 1 + (n − 1) % 9 chỉ dùng cho n ≥ 1.',
        '- **dem(L − 1) khi L = 1:** dem(0) phải bằng 0; công thức (n − d)/9 + 1 với n < d cho kết quả sai nếu không kiểm tra n < d.',
        '- **Tin phép thử bỏ chín tuyệt đối:** nó chỉ phát hiện được sai, không chứng minh được đúng.'])
    D.kbox('GHI NHỚ', [
        '- S(n) ≡ n (mod 9) vì 10 ≡ 1 (mod 9).',
        '- dr(n) = 1 + (n − 1) mod 9 với n ≥ 1; dr(0) = 0.',
        '- Các số có căn số d là d, d + 9, d + 18, ...: đếm bằng công thức, trên đoạn dùng hiệu hai tiền tố.',
        '- Căn số đi qua cộng, nhân, lũy thừa như số dư cho 9.'])
    D.luyentap([('6.1', 'CĂN SỐ LỚN', 'Căn số của một số dài 10^{6} chữ số, và của a^{b} với a, b cho dưới dạng xâu: Mở rộng 1.'),
                ('6.2', 'DÃY CĂN SỐ', 'Tổng căn số của mọi số trong [L, R] (L, R ≤ 10^{18}): mỗi chu kì 9 số góp 45.'),
                ('6.3', 'ĐỘ BỀN', 'Độ bền nhân của các số trong một đoạn nhỏ, và số nhỏ nhất có độ bền nhân cho trước (k ≤ 8): mô phỏng và sinh có hướng.')])
    D.tukiemtra([('Căn số của 123 456 789 là bao nhiêu?', '9 (tổng chữ số 45)'), ('Trong 1..1000 có bao nhiêu số có căn số 1?', '112 (1, 10, ..., 1000)'),
                 ('Căn số của 2^{2026}?', '2^{2026} mod 9 = 7, căn số 7'), ('Vì sao dr(9 · n) = 9 với mọi n ≥ 1?', '9n chia hết cho 9 và khác 0')])
