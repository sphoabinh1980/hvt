def build(D, P):
    D.objectives([
        'Hiểu **số tự đồng cấu** (automorphic): n^{2} kết thúc bằng chính n, như 76^{2} = 5776.',
        'Biến điều kiện về chữ số cuối thành phương trình đồng dư x^{2} ≡ x (mod 10^{k}), và hiểu vì sao nó có đúng 4 nghiệm.',
        'Nắm kĩ thuật **dựng nghiệm từng chữ số một** (nâng nghiệm): từ nghiệm k chữ số suy ra nghiệm k + 1 chữ số.',
        'Làm quen với số Kaprekar, số tam đồng cấu và số tự sinh.'])
    D.kbox('KHỞI ĐỘNG', [
        '25^{2} = 625, 76^{2} = 5776, 376^{2} = 141 376, 9376^{2} = 87 909 376. Bình phương các số này lại "đẻ" ra chính chúng ở cuối. Hãy để ý: 76 nằm trong 376, 376 nằm trong 9376...',
        'Có vẻ như các số tự đồng cấu được dựng lên **từ phải sang trái**, mỗi lần thêm một chữ số. Bài học này biến quan sát ấy thành thuật toán, và tìm hết các số tự đồng cấu dưới 10^{18} trong chưa tới một phần nghìn giây.'])
    D.fig(P.fig('squares'), 'Ba số tự đồng cấu và bình phương của chúng.', 13)

    D.h('1. Số tự đồng cấu và phương trình đồng dư')
    D.kbox('ĐỊNH NGHĨA', ['Số nguyên dương n có k chữ số là **số tự đồng cấu** nếu k chữ số cuối của n^{2} chính là n, tức **n^{2} ≡ n (mod 10^{k})**.'])
    D.p('Điều kiện viết lại là n(n − 1) ≡ 0 (mod 2^{k} · 5^{k}). Vì n và n − 1 là hai số liên tiếp, chúng nguyên tố cùng nhau: thừa số 2^{k} phải nằm trọn trong một số, thừa số 5^{k} cũng vậy.')
    D.kbox('ĐỊNH LÍ (BỐN NGHIỆM)', [
        'Phương trình x^{2} ≡ x (mod 10^{k}) có đúng 4 nghiệm trong [0, 10^{k}):',
        '- x ≡ 0 và x ≡ 1 (hai nghiệm tầm thường);',
        '- x ≡ 0 (mod 5^{k}), x ≡ 1 (mod 2^{k}): họ 5, 25, 625, 0625, 90625, ...;',
        '- x ≡ 1 (mod 5^{k}), x ≡ 0 (mod 2^{k}): họ 6, 76, 376, 9376, 09376, ...',
        'Hai nghiệm không tầm thường có tổng bằng 10^{k} + 1 (ví dụ 0625 + 9376 = 10 001).'])
    D.kbox('VÌ SAO ĐÚNG?', ['Mỗi cách đặt 2^{k} và 5^{k} vào n hoặc n − 1 cho một hệ hai phương trình đồng dư theo hai mô-đun nguyên tố cùng nhau 2^{k} và 5^{k}; theo định lí Trung Hoa, mỗi hệ có đúng một nghiệm theo mô-đun 10^{k}. '
                            'Bốn cách đặt cho bốn nghiệm. Nếu x là một nghiệm không tầm thường thì 10^{k} + 1 − x đổi vai 2^{k} và 5^{k}, nên là nghiệm còn lại.'])

    D.h('2. Bài toán TUDONGCAU')
    D.problem_box('TUDONGCAU', 'Cho K. Hãy in theo thứ tự tăng dần mọi số tự đồng cấu nhỏ hơn 10^{K}.', 'Một số nguyên K (1 ≤ K ≤ 18).', 'Mỗi dòng một số.')
    D.examples('TUDONGCAU', [('3', '1\n5\n6\n25\n76\n376\n625', 'Số 0625 có 3 chữ số thật sự (625) và 625 đã có mặt; số 1 thỏa 1^{2} = 1.')])

    D.h('3. Ý tưởng ngây thơ: Kiểm tra từng số')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách kiểm tra từng số.', 13)
    D.code('TUDONGCAU.CPP (ngây thơ): kiểm tra n² mod 10ᵏ', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['10^{K} số, mỗi số một phép nhân và một phép chia __int128. Đo thực tế: K = 8 mất **0,43 giây**, K = 9 mất **4,4 giây**; K = 18 cần khoảng **140 năm**.'])
    D.kbox('BẾ TẮC', ['Theo định lí ở mục 1, với mỗi k chỉ có 2 số tự đồng cấu không tầm thường (nếu chữ số đầu khác 0), vậy mà ta phải thử 9 · 10^{k−1} số. '
                      'Mặt khác, nếu x là nghiệm theo mô-đun 10^{k+1} thì x mod 10^{k} là nghiệm theo mô-đun 10^{k}: **nghiệm dài chứa nghiệm ngắn ở cuối**. Vậy hãy dựng nghiệm dài từ nghiệm ngắn.'])

    D.h('4. Phá bế tắc: Nâng nghiệm từng chữ số')
    D.step(1, 'Từ k chữ số lên k + 1 chữ số')
    D.p('Giả sử x là nghiệm theo mô-đun 10^{k}. Nghiệm theo mô-đun 10^{k+1} có dạng y = x + d · 10^{k} với chữ số d ∈ {0, ..., 9}. Thử cả 10 chữ số, giữ chữ số làm y^{2} ≡ y (mod 10^{k+1}). '
        'Theo định lí ở mục 1 (mỗi họ có đúng một nghiệm ở mỗi mô-đun), **luôn có đúng một** chữ số d thỏa mãn.')
    D.step(2, 'Hai họ, bắt đầu từ 5 và 6')
    D.p('Xuất phát từ hai nghiệm một chữ số không tầm thường 5 và 6, nâng dần lên K chữ số. Ở bước k, nghiệm x là một số tự đồng cấu k chữ số khi và chỉ khi chữ số đầu của nó khác 0 (x ≥ 10^{k−1}); '
        'nếu chữ số đầu bằng 0 (như 0625) thì bỏ qua nhưng **vẫn nâng tiếp**, vì 90625 được dựng từ 0625.')
    D.fig(P.fig('lift'), 'Nâng nghiệm trong hai họ: mỗi mũi tên thêm một chữ số bên trái.', 15.2)
    D.step(3, 'Chạy tay một bước: từ 76 lên 3 chữ số')
    D.table(['d', 'y = 76 + 100d', 'y² mod 1000', 'y² ≡ y ?'], [
        ['0', '76', '776', 'không'], ['1', '176', '976', 'không'], ['2', '276', '176', 'không'], ['3', '**376**', '**376**', '**có**'], ['4..9', '476, ..., 976', '576, 776, 976, 176, 376, 576', 'không']],
        widths=[0.8, 2.2, 3.2, 1.4], sz=20, hl=[3])
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của cách nâng nghiệm.', 12.5)
    D.code('TUDONGCAU.CPP: dựng nghiệm từng chữ số', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Hai họ, mỗi họ K bước, mỗi bước thử tối đa 10 chữ số: khoảng 360 phép nhân __int128 với K = 18. Chương trình chạy **tức thì** và in 33 số tự đồng cấu dưới 10^{18}, '
                               'số lớn nhất là 743 740 081 787 109 376. Kết quả trùng với cách kiểm tra từng số cho mọi K ≤ 7.'])
    D.kbox('LƯU Ý: TRÀN SỐ', ['Với K = 18, y < 10^{18} và y^{2} tới 10^{36}; mô-đun 10^{k+1} tới 10^{19} vượt cả long long. Mọi phép tính kiểm tra phải làm bằng __int128.'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Số Kaprekar')
    D.p('Số n có k chữ số là **số Kaprekar** nếu tách n^{2} thành phần phải gồm k chữ số cuối (khác 0) và phần trái còn lại, tổng hai phần bằng n: 45^{2} = 2025 và 20 + 25 = 45; 297^{2} = 88 209 và 88 + 209 = 297. '
        'Các số Kaprekar không vượt quá 10^{4} là 1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4950, 5050, 7272, 7777, 9999. Với n tới 10^{9}, n^{2} tới 10^{18} vẫn vừa long long; lớn hơn thì cần __int128.')
    D.sub('Mở rộng 2: Số tam đồng cấu')
    D.p('Số mà n^{3} kết thúc bằng n: 4, 9, 24, 49, 51, 75, 99, 125, 249, ... (và mọi số tự đồng cấu). Phương trình x^{3} ≡ x (mod 10^{k}) có nhiều nghiệm hơn, nhưng kĩ thuật nâng nghiệm từng chữ số vẫn dùng được: '
        'giữ **tất cả** các nghiệm ở mỗi mức (thay vì một nghiệm mỗi họ) và nâng tất cả lên.')
    D.sub('Mở rộng 3: Số tự sinh')
    D.p('Số n là **số tự sinh** (self number) nếu không có m nào với m + S(m) = n. Ví dụ 20: không số nào cộng tổng chữ số của nó ra 20. Các số tự sinh nhỏ nhất: 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97, 108, 110. '
        'Cách tìm: **sàng** — với mỗi m đánh dấu m + S(m); số không bị đánh dấu là số tự sinh. Dưới 10^{7} có 977 787 số tự sinh.')
    D.code('Sàng số tự sinh', P.src('ex_self.cpp'))
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Dừng nâng khi gặp chữ số 0 ở đầu:** sẽ mất 90625, 109376...',
        '- **Đếm 0625 là số 4 chữ số:** một số không bắt đầu bằng 0; 625 chỉ được in một lần.',
        '- **Quên số 1** (và số 0 nếu đề cho phép).',
        '- **Nhân hai số 10^{18} bằng long long:** tràn; dùng __int128 cho cả phép nhân và mô-đun.'])
    D.kbox('GHI NHỚ', [
        '- Số tự đồng cấu: n^{2} ≡ n (mod 10^{k}); mỗi k có đúng hai nghiệm không tầm thường, tổng bằng 10^{k} + 1.',
        '- Nghiệm theo mô-đun 10^{k+1} chứa nghiệm theo mô-đun 10^{k} ở cuối: **dựng từ phải sang trái**, mỗi lần một chữ số.',
        '- Kĩ thuật nâng nghiệm dùng cho mọi điều kiện "các chữ số cuối thỏa mãn ...".',
        '- Số tự sinh: sàng đánh dấu m + S(m).'])
    D.luyentap([('12.1', 'TỰ ĐỒNG CẤU', 'Số tự đồng cấu k chữ số với k ≤ 1000: nâng nghiệm trên mảng chữ số (số lớn), mỗi bước chỉ cần tính chữ số thứ k của y^{2}.'),
                ('12.2', 'KAPREKAR', 'Đếm số Kaprekar trong [L, R] (R ≤ 10^{9}): duyệt và tách bình phương, Mở rộng 1.'),
                ('12.3', 'SỐ TỰ SINH', 'Đếm số tự sinh không vượt quá N ≤ 10^{8} bằng mảng bit, và tìm số tự sinh thứ k: Mở rộng 3.')])
    D.tukiemtra([('Kiểm tra 9376 là số tự đồng cấu.', '9376^{2} = 87 909 376'), ('Số tự đồng cấu 5 chữ số kết thúc bằng 625 là số nào?', '90 625 (90 625^{2} = 8 212 890 625)'),
                 ('Tổng của hai nghiệm không tầm thường theo mô-đun 10^{6}?', '109 376 + 890 625 = 1 000 001'), ('20 có phải là số tự sinh không?', 'có: không m nào có m + S(m) = 20')])
