def build(D, P):
    D.objectives([
        'Biết các họ số nguyên tố "đặc biệt theo chữ số": đối xứng, xoay vòng, cắt phải, cắt trái, emirp.',
        'Chứng minh mọi số đối xứng có số chữ số chẵn (trừ 11) đều là hợp số, nhờ dấu hiệu chia hết cho 11.',
        'Đếm số nguyên tố đối xứng tới 10^{12} bằng cách **sinh** số đối xứng (Bài 9) rồi kiểm tra bằng **Miller–Rabin**, thay vì duyệt mọi số.',
        'Dùng các ràng buộc chữ số (chữ số cuối 1, 3, 7, 9) để cắt tỉa không gian tìm kiếm.'])
    D.kbox('KHỞI ĐỘNG', [
        'Số 2026 không phải số nguyên tố (2026 = 2 · 1013). Nhưng hãy nhìn số **73 939 133**: nó là số nguyên tố, và nếu lần lượt xóa chữ số cuối, ta được 7 393 913, 739 391, 73 939, 7 393, 739, 73, 7: '
        '**tất cả đều nguyên tố**! Và không có số nào lớn hơn có tính chất này.',
        'Làm sao máy tính biết điều đó mà không cần thử mọi số tới vô cùng? Bài học này trả lời câu hỏi ấy và nhiều câu hỏi tương tự.'])

    D.h('1. Các họ số nguyên tố đặc biệt')
    D.table(['Tên gọi', 'Định nghĩa', 'Ví dụ', 'Số lượng'], [
        ['**Đối xứng**', 'Số nguyên tố và là số đối xứng', '2, 11, 101, 131, 10 301', '20 số < 1000; 47 995 số < 10^{12}'],
        ['**Xoay vòng**', 'Mọi phép xoay vòng chữ số đều là số nguyên tố', '197 → 971 → 719', '55 số < 10^{7}'],
        ['**Cắt phải**', 'Xóa dần chữ số cuối, luôn được số nguyên tố', '2399, 73 939 133', 'Đúng 83 số'],
        ['**Cắt trái**', 'Xóa dần chữ số đầu (không có chữ số 0), luôn nguyên tố', '9137, 357 686 ... 137 (24 chữ số)', 'Đúng 4 260 số'],
        ['**Emirp**', 'Nguyên tố, đảo ngược được số nguyên tố **khác**', '13 ↔ 31, 107 ↔ 701', '36 số < 1000'],
    ], widths=[1.6, 3.2, 2.4, 2.4], align=['left', 'left', 'left', 'left'], sz=19)
    D.p('Tất cả các con số trong bảng đều được tính lại bằng chương trình trong bài này hoặc bằng thư viện số học của Python.')
    D.kbox('ĐỊNH LÍ (SỐ ĐỐI XỨNG ĐỘ DÀI CHẴN)', ['Mọi số đối xứng có số chữ số chẵn đều chia hết cho 11. Do đó số nguyên tố đối xứng có độ dài chẵn duy nhất là **11**.'])
    D.kbox('VÌ SAO ĐÚNG?', ['Theo dấu hiệu chia hết cho 11 (Bài 5): x chia hết cho 11 khi tổng đan dấu các chữ số (+, −, +, −, ... tính từ hàng đơn vị) chia hết cho 11. '
                            'Với độ dài chẵn 2m, chữ số ở vị trí i và vị trí 2m − 1 − i bằng nhau, và hai vị trí này khác tính chẵn lẻ, nên mang dấu ngược nhau: từng cặp triệt tiêu, tổng đan dấu bằng 0.'])
    D.fig(P.fig('eleven'), 'Tổng đan dấu của số đối xứng độ dài chẵn bằng 0.', 15)

    D.h('2. Bài toán NTDX')
    D.problem_box('NTDX', 'Cho hai số nguyên L ≤ R. Hãy đếm số các số nguyên tố đối xứng trong đoạn [L, R].', 'Một dòng chứa L, R (1 ≤ L ≤ R ≤ 10^{12}).', 'Số các số nguyên tố đối xứng trong [L, R].')
    D.examples('NTDX', [('1 100', '5', '2, 3, 5, 7, 11.'), ('100 1000', '15', 'Xem Hình 17.2.'), ('1 1000000000000', '47995', '')])
    D.p('Subtask 1 (30 điểm): R ≤ 10^{7}. Subtask 2 (70 điểm): R ≤ 10^{12}.')

    D.h('3. Ý tưởng ngây thơ: Duyệt và kiểm tra')
    D.p('Duyệt x từ L đến R. Kiểm tra đối xứng trước (rẻ: khoảng 12 phép chia), chỉ khi đối xứng mới thử chia tới √x.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách duyệt.', 14)
    D.code('NTDX.CPP (ngây thơ): duyệt và kiểm tra', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Phần tốn kém là kiểm tra đối xứng cho **mọi** số: R · 12 phép chia. Đo thực tế: R = 10^{8} mất **0,9 giây**, R = 10^{9} mất **10,7 giây**; R = 10^{12} cần khoảng 3 giờ. '
                               'Phép thử chia tới √x chạy rất ít lần (chỉ khoảng 2 · 10^{6} số ≤ 10^{12} là số đối xứng), nhưng mỗi lần tới 10^{6} phép chia.'])
    D.kbox('BẾ TẮC', ['Trong 10^{12} số, chỉ khoảng 2 · 10^{6} số là đối xứng. Ta tốn gần như toàn bộ thời gian để **loại** những số không đối xứng. Đã biết (Bài 9) cách **sinh trực tiếp** các số đối xứng, vậy tại sao còn duyệt?'])

    D.h('4. Phá bế tắc: Sinh số đối xứng, kiểm tra nhanh')
    D.step(1, 'Chỉ sinh số đối xứng độ dài lẻ')
    D.p('Số đối xứng độ dài 2h − 1 được xác định bởi h chữ số đầu a: ghép a với a đã bỏ chữ số cuối và đảo ngược (abc → abcba). Độ dài chẵn bỏ qua hoàn toàn, chỉ cộng riêng số 11. '
        'Với R ≤ 10^{12}, độ dài lớn nhất là 11, nên h ≤ 6 (chương trình duyệt tới h = 7 và dừng khi vượt R).')
    D.step(2, 'Cắt tỉa theo chữ số đầu')
    D.p('Chữ số đầu của số đối xứng cũng là chữ số cuối. Số nguyên tố có từ hai chữ số trở lên phải tận cùng bằng 1, 3, 7 hoặc 9. Vậy chỉ giữ các nửa đầu bắt đầu bằng 1, 3, 7, 9: **bỏ đi 5/9** số phải kiểm tra.')
    D.fig(P.fig('grid'), 'Các số đối xứng 3 chữ số: chỉ 40 trong 90 số cần kiểm tra, 15 số nguyên tố.', 15.5)
    D.step(3, 'Kiểm tra nguyên tố bằng Miller–Rabin')
    D.p('Số cần kiểm tra lớn tới 10^{12}, thử chia tới 10^{6} thì quá chậm khi có hàng trăm nghìn số. Dùng **Miller–Rabin tất định** với 12 cơ số nguyên tố đầu tiên (đúng cho mọi số 64 bit): '
        'mỗi lần kiểm tra chỉ khoảng 12 · 40 phép nhân theo mô-đun (dùng __int128 để không tràn).')
    D.kbox('VÌ SAO ĐÚNG?', ['Nếu n nguyên tố và n − 1 = 2^{s} · d (d lẻ), thì với mọi a, dãy a^{d}, a^{2d}, ..., a^{2^{s}d} (mod n) hoặc bắt đầu bằng 1, hoặc chứa n − 1 (định lí Fermat nhỏ và x^{2} ≡ 1 chỉ có nghiệm ±1). '
                            'Một hợp số "lọt" qua phép thử với cả 12 cơ số 2, 3, ..., 37 chỉ xuất hiện khi n > 3,1 · 10^{23}: đã được kiểm chứng bằng máy tính.'])
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của cách sinh và kiểm tra.', 13.5)
    D.code('NTDX.CPP: sinh số đối xứng độ dài lẻ và Miller–Rabin', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Với R = 10^{12}: khoảng 4 · (1 + 10 + ... + 10^{5}) ≈ 4,4 · 10^{5} lần Miller–Rabin, mỗi lần vài trăm phép nhân. Đo thực tế: **0,27 giây**. '
                               'Đã đối chiếu với cách duyệt trên 200 bộ dữ liệu. Số lượng 47 995 số nguyên tố đối xứng < 10^{12} khớp với các bảng số đã công bố.'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Số nguyên tố cắt phải')
    D.p('Tiền tố của một số nguyên tố cắt phải cũng là số nguyên tố cắt phải. Vậy dựng chúng **từ trái sang** như một cây: gốc là 2, 3, 5, 7; mỗi nút thử thêm chữ số 1, 3, 7, 9 vào cuối, '
        'giữ lại nếu được số nguyên tố. Cây tự dừng vì đến một lúc không còn con nào: cả cây chỉ có **83** nút, lớn nhất là 73 939 133.')
    D.code('Liệt kê mọi số nguyên tố cắt phải', P.src('ex_catphai.cpp'))
    D.p('Số nguyên tố cắt trái làm tương tự (thêm chữ số 1..9 vào **đầu**), nhưng cây lớn hơn nhiều: 4 260 số, số lớn nhất có 24 chữ số (357 686 312 646 216 567 629 137), vượt long long, '
        'phải dùng số lớn. Đây là một ví dụ đẹp về việc "tìm kiếm trên cây" biến một câu hỏi vô hạn thành hữu hạn.')
    D.sub('Mở rộng 2: Số nguyên tố xoay vòng')
    D.p('Mọi phép xoay của x phải nguyên tố, nên (nếu x có từ hai chữ số) mọi chữ số của x đều phải là 1, 3, 7, 9: bất kì chữ số nào khác, khi xoay về cuối, cho số chẵn hoặc chia hết cho 5. '
        'Với N ≤ 10^{7}, chỉ cần sàng Eratosthenes tới lũy thừa 10 kế tiếp và thử mọi phép xoay.')
    D.code('Đếm số nguyên tố xoay vòng nhỏ hơn N', P.src('ex_xoay.cpp'))
    D.p('Kết quả: 13 số < 100, 25 số < 1000, 43 số < 10^{5}, 55 số < 10^{6} và vẫn 55 số < 10^{7}. Đã đối chiếu với cách kiểm tra trực tiếp tới 10^{5}.')
    D.sub('Mở rộng 3: Emirp và "giả nguyên tố"')
    D.p('Emirp (prime viết ngược) là số nguyên tố mà số đảo ngược là một số nguyên tố **khác**: 13, 17, 31, 37, 71, 73, 79, 97, 107, ... Kiểm tra bằng sàng hoặc Miller–Rabin như trên. '
        'Lưu ý chỉ thử Fermat (a^{n−1} ≡ 1) là **không đủ**: số Carmichael 561 = 3 · 11 · 17 vượt qua phép thử Fermat với mọi cơ số nguyên tố cùng nhau với nó. Miller–Rabin không bị lừa như vậy.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Quên số 11** khi bỏ qua mọi độ dài chẵn, hoặc quên 2, 3, 5, 7 khi lọc chữ số đầu (lọc chỉ áp dụng cho số có từ 2 chữ số).',
        '- **Nhân tràn** trong Miller–Rabin: a · b với a, b gần 10^{12} vượt long long khi n lớn; dùng __int128.',
        '- **Dừng sớm sai:** "x > R thì break" chỉ đúng khi các số sinh ra **tăng dần** theo a (đúng với cùng độ dài).',
        '- **Xoay vòng có chữ số 0:** 101 xoay thành 011 = 11. Định nghĩa thường loại các số có chữ số 0; chương trình trên tự loại vì 110 chẵn.'])
    D.kbox('GHI NHỚ', [
        '- Số đối xứng độ dài chẵn chia hết cho 11; nguyên tố đối xứng chẵn duy nhất là 11.',
        '- Sinh trực tiếp các ứng viên (đối xứng, cây cắt phải) rồi kiểm tra bằng Miller–Rabin, thay vì duyệt mọi số.',
        '- Số nguyên tố ≥ 10 tận cùng bằng 1, 3, 7, 9: dùng để cắt tỉa.'])
    D.luyentap([('17.1', 'NGUYÊN TỐ ĐỐI XỨNG', 'Đếm và liệt kê số nguyên tố đối xứng trong [L, R], R ≤ 10^{12}: bài NTDX.'),
                ('17.2', 'CẮT PHẢI, CẮT TRÁI', 'Liệt kê số nguyên tố cắt phải không vượt quá N; đếm số nguyên tố vừa cắt trái vừa cắt phải: Mở rộng 1.'),
                ('17.3', 'XOAY VÒNG', 'Đếm số nguyên tố xoay vòng và số emirp nhỏ hơn N ≤ 10^{7}: Mở rộng 2, 3.')])
    D.tukiemtra([('Vì sao 1001 không phải số nguyên tố mà không cần thử chia?', 'Đối xứng độ dài chẵn nên chia hết cho 11 (1001 = 7 · 11 · 13)'),
                 ('2399 có phải số nguyên tố cắt phải không?', 'Có: 2399, 239, 23, 2 đều nguyên tố'),
                 ('Số nguyên tố xoay vòng 3 chữ số có thể chứa chữ số 5 không?', 'Không: xoay 5 về cuối thì chia hết cho 5'),
                 ('13 và 31 có phải emirp không? 11 thì sao?', '13, 31 là emirp; 11 không (đảo ngược ra chính nó)')])
