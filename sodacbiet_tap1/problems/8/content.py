def build(D, P):
    D.objectives([
        'Hiểu vì sao mọi phân số 1/n viết ra số thập phân đều **hữu hạn hoặc tuần hoàn**, nhờ việc theo dõi số dư của phép chia.',
        'Tính độ dài phần không tuần hoàn (= max số mũ của 2 và 5 trong n) và độ dài chu kì (= **cấp của 10** theo mô-đun phần còn lại).',
        'Tính cấp của 10 với n tới 10^{12} bằng định lí Euler và việc "bóc dần" các ước nguyên tố của φ.',
        'Làm quen với **repunit** 11...1 và **số vòng** 142857.'])
    D.kbox('KHỞI ĐỘNG', [
        'Bấm máy tính 1 ÷ 7 = 0,142857142857... Sáu chữ số 142857 lặp lại mãi. Nhân 142857 với 2, 3, 4, 5, 6: các tích 285714, 428571, 571428, 714285, 857142 đều là **cùng sáu chữ số ấy, chỉ quay vòng**. '
        'Còn 142857 × 7 = 999 999.',
        'Không có phép màu nào ở đây: tất cả đều là hệ quả của việc chỉ có 6 số dư khác 0 khi chia cho 7. Bài học này giải thích điều đó và đo độ dài chu kì của 1/n với n tới 10^{12}.'])

    D.h('1. Phép chia tay và dãy số dư')
    D.p('Khi chia 1 cho n "kiểu chia tay", ở mỗi bước ta nhân số dư hiện tại r với 10, lấy thương ⌊10r/n⌋ làm chữ số tiếp theo, và số dư mới là 10r mod n. '
        'Vậy các chữ số sau dấu phẩy hoàn toàn do **dãy số dư** r_{0} = 1, r_{i+1} = 10 · r_{i} mod n quyết định.')
    D.fig(P.fig('cycle7'), 'Dãy số dư của phép chia 1 cho 7 đi một vòng sáu bước.', 15.2)
    D.kbox('ĐỊNH LÍ (HỮU HẠN HOẶC TUẦN HOÀN)', [
        'Dãy số dư chỉ nhận các giá trị 0, 1, ..., n − 1. Nếu gặp số dư 0, phép chia dừng: số thập phân **hữu hạn**. Nếu không, trong n bước phải có một số dư lặp lại, '
        'và từ đó mọi thứ lặp lại: số thập phân **tuần hoàn**, chu kì không quá n − 1.'])
    D.p('Dãy số dư có hình chữ ρ (rô): một "đuôi" không lặp rồi một vòng lặp. Với 1/12: số dư 1 → 10 → 4 → 4 → ...: đuôi dài 2 (chữ số 0, 8), vòng dài 1 (chữ số 3).')
    D.fig(P.fig('rho'), 'Dãy số dư của 1/12: đuôi dài 2, chu kì dài 1.', 14.5)

    D.h('2. Đuôi và vòng tính bằng số học')
    D.kbox('ĐỊNH LÍ (ĐỘ DÀI ĐUÔI VÀ CHU KÌ)', [
        'Viết n = 2^{a} · 5^{b} · m với gcd(m, 10) = 1. Khi đó số thập phân của 1/n có:',
        '- phần không tuần hoàn dài **max(a, b)** chữ số;',
        '- chu kì dài **ord_{m}(10)**: số k ≥ 1 nhỏ nhất sao cho 10^{k} ≡ 1 (mod m) (gọi là **cấp** của 10 theo mô-đun m). Nếu m = 1 thì 1/n hữu hạn (chu kì 0).'])
    D.kbox('VÌ SAO ĐÚNG?', [
        'Đặt t = max(a, b). Nhân 1/n với 10^{t} khử hết thừa số 2 và 5 ở mẫu: 10^{t}/n = c/m với c nguyên. Dịch dấu phẩy t chữ số không đổi phần tuần hoàn, nên ta chỉ cần xét c/m với gcd(m, 10) = 1.',
        'Phân số A/m có chu kì k khi và chỉ khi 10^{k} · (A/m) − A/m là số nguyên, tức m | A · (10^{k} − 1); với gcd(A, m) = 1 điều này nghĩa là 10^{k} ≡ 1 (mod m). '
        'Vì gcd(10, m) = 1 nên số dư không bao giờ bằng 0 và dãy số dư tuần hoàn **ngay từ đầu**, do đó đuôi chỉ đến từ thừa số 2 và 5, dài đúng t.'])
    D.kbox('ĐỊNH LÍ (EULER)', ['Nếu gcd(10, m) = 1 thì 10^{φ(m)} ≡ 1 (mod m), với φ(m) là số các số trong 1..m nguyên tố cùng nhau với m. Hệ quả: **ord_{m}(10) là một ước của φ(m)**. '
                               'Với m = p nguyên tố, φ(p) = p − 1, nên chu kì của 1/p chia hết p − 1.'])

    D.h('3. Bài toán CHUKY')
    D.problem_box('CHUKY', 'Cho Q số n. Với mỗi n, hãy cho biết số thập phân của 1/n có phần không tuần hoàn dài bao nhiêu chữ số và chu kì dài bao nhiêu chữ số (chu kì 0 nếu số thập phân hữu hạn).',
                  'Dòng đầu chứa Q (Q ≤ 1000); mỗi dòng tiếp theo chứa một số n (1 ≤ n ≤ 10^{12}).', 'Q dòng, mỗi dòng hai số.')
    D.examples('CHUKY', [('4\n7\n12\n8\n2026', '0 6\n2 1\n3 0\n1 253', '1/7 = 0,(142857). 1/12 = 0,08(3). 1/8 = 0,125. 2026 = 2 · 1013, cấp của 10 theo mô-đun 1013 là 253 (một ước của 1012).')])

    D.h('4. Ý tưởng ngây thơ: Mô phỏng phép chia')
    D.p('Làm đúng như chia tay: lần lượt tính các số dư, ghi lại bước đầu tiên gặp mỗi số dư. Khi số dư bằng 0 thì hữu hạn; khi gặp lại một số dư đã có thì đuôi dài bằng bước đầu tiên gặp nó, chu kì bằng khoảng cách hai lần gặp.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách mô phỏng.', 13)
    D.code('CHUKY.CPP (ngây thơ): mô phỏng và nhớ số dư', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Số bước bằng đuôi + chu kì, có thể tới n − 1 (với n = 999 983 chu kì là 999 982). Đo thực tế: n ≈ 10^{6} mất **0,24 giây**, n ≈ 10^{7} mất **5,4 giây** '
                               '(bảng băm rất tốn bộ nhớ). Với n ≈ 10^{12}, bảng băm cần hàng chục terabyte.'])
    D.kbox('BẾ TẮC', ['Mô phỏng đi qua từng số dư một. Nhưng theo mục 2, chu kì là cấp của 10, và cấp ấy là một **ước của φ(m)**. Thay vì đi từng bước, có thể kiểm tra trực tiếp "10^{k} ≡ 1?" bằng lũy thừa nhanh, '
                      'chỉ cho những k là ước của φ(m). Câu hỏi còn lại: ước nào là nhỏ nhất?'])

    D.h('5. Phá bế tắc: Bóc dần các ước nguyên tố của φ')
    D.step(1, 'Tách thừa số 2 và 5')
    D.p('Chia n cho 2 và 5 tới khi hết, đếm được a, b và phần còn lại m. Độ dài đuôi là max(a, b); nếu m = 1 thì chu kì 0.')
    D.step(2, 'Tính φ(m)')
    D.p('Phân tích m bằng cách thử chia các số nguyên tố ≤ 10^{6} (sàng sẵn), rồi φ(m) = m · Π (1 − 1/p).')
    D.step(3, 'Tìm cấp bằng cách bóc từng thừa số')
    D.kbox('THUẬT TOÁN (CẤP CỦA 10)', [
        'Bắt đầu với ord = φ(m). Với mỗi ước nguyên tố p của φ(m): **chừng nào** p chia hết ord và 10^{ord/p} ≡ 1 (mod m) thì chia ord cho p. Kết thúc, ord chính là cấp.',
        'Lí do: tập các k có 10^{k} ≡ 1 chính là các bội của cấp. Cấp là ước của φ; ta lần lượt bỏ đi các thừa số nguyên tố "thừa" chừng nào việc bỏ vẫn giữ được tính chất 10^{ord} ≡ 1.'])
    D.step(4, 'Chạy tay với n = 2026')
    D.table(['Bước', 'Kết quả'], [
        ['Tách 2, 5', '2026 = 2^{1} · 5^{0} · 1013, đuôi max(1, 0) = 1'], ['φ(1013)', '1013 là số nguyên tố: φ = 1012 = 2^{2} · 11 · 23'],
        ['p = 2', '10^{506} ≡ 1 (mod 1013) → ord = 506;  10^{253} ≡ 1 → ord = 253;  253 lẻ, dừng'],
        ['p = 11', '10^{23} ≢ 1 → giữ nguyên 253'], ['p = 23', '10^{11} ≢ 1 → giữ nguyên 253'], ['Kết luận', '**1/2026 có đuôi 1 chữ số và chu kì 253 chữ số**']],
        widths=[1.6, 6.4], align=['center', 'left'], sz=20, hl=[5])
    D.step(5, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của cách tính bằng cấp.', 13.5)
    D.code('CHUKY.CPP: cấp của 10 theo mô-đun m', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Sàng 10^{6} một lần; mỗi truy vấn phân tích m và φ(m) bằng tối đa 78 498 số nguyên tố, cộng vài chục lần lũy thừa nhanh (mỗi lần khoảng 80 phép nhân __int128). '
                               '1000 truy vấn với n tới 10^{12} chạy khoảng **0,13 giây**. Chương trình đã được đối chiếu với cách mô phỏng cho mọi n trong hàng nghìn bộ test nhỏ.'])
    D.kbox('LƯU Ý: TRÀN SỐ', ['m tới 10^{12}, tích hai số dư tới 10^{24}: phải nhân bằng __int128 (hàm mulmod). φ(m) cũng tới 10^{12} nên phân tích φ cũng cần các số nguyên tố tới 10^{6}.'])

    D.h('6. Mở rộng')
    D.sub('Mở rộng 1: Repunit')
    D.p('Repunit R_{k} = 11...1 (k chữ số 1) = (10^{k} − 1)/9. Với gcd(n, 10) = 1, R_{k} chia hết cho n khi và chỉ khi 10^{k} ≡ 1 (mod 9n), nên repunit nhỏ nhất chia hết cho n là R_{k} với k = ord_{9n}(10). '
        'Ví dụ: R_{6} = 111 111 = 7 · 15 873; R_{7} = 1 111 111 = 239 · 4649 (cả 1/239 lẫn 1/4649 đều có chu kì 7); 1/81 = 0,(012345679) có chu kì 9.')
    D.sub('Mở rộng 2: Số vòng')
    D.fig(P.fig('cyclic'), 'Các bội của 142857: sáu vòng quay của cùng một dãy chữ số.', 14.5)
    D.p('Nếu p là số nguyên tố và chu kì của 1/p bằng đúng p − 1 (10 là **căn nguyên thủy** theo mô-đun p), thì C = (10^{p−1} − 1)/p là một **số vòng**: nhân C với 1, 2, ..., p − 1 chỉ làm quay vòng các chữ số của C '
        '(cho phép số 0 ở đầu). Các số nguyên tố như vậy dưới 100 là 7, 17, 19, 23, 29, 47, 59, 61, 97. Lí do: 1/p, 2/p, ..., (p − 1)/p có dãy số dư là **cùng một vòng** p − 1 số dư, chỉ bắt đầu ở chỗ khác nhau.')
    D.sub('Mở rộng 3: Chữ số thứ k sau dấu phẩy')
    D.p('Chữ số thứ k sau dấu phẩy của a/b (0 ≤ a < b) là ⌊10 · r / b⌋ với r = a · 10^{k−1} mod b: một lần lũy thừa nhanh, không cần mô phỏng k bước, kể cả khi k = 10^{18}.')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Quên thừa số 2, 5:** cấp của 10 theo mô-đun n chỉ có nghĩa khi gcd(n, 10) = 1.',
        '- **Lấy φ(m) làm chu kì:** chu kì chỉ là một **ước** của φ(m) (1/13 có chu kì 6 chứ không phải 12).',
        '- **Bóc mỗi thừa số một lần:** phải dùng `while`, vì p có thể xuất hiện nhiều lần trong ord (ví dụ 2026: bóc hai lần thừa số 2).',
        '- **Tràn số khi m > 3 · 10^{9}:** nhân bằng __int128.',
        '- **n = 1:** 1/1 = 1, hữu hạn: đuôi 0, chu kì 0.'])
    D.kbox('GHI NHỚ', [
        '- Chữ số của 1/n do dãy số dư r ← 10r mod n quyết định: hữu hạn hoặc tuần hoàn (hình ρ).',
        '- n = 2^{a} 5^{b} m: đuôi dài max(a, b), chu kì dài ord_{m}(10), là một ước của φ(m).',
        '- Tìm cấp: bắt đầu từ φ(m), bóc dần các ước nguyên tố khi 10^{ord/p} ≡ 1.',
        '- Repunit R_{k} = (10^{k} − 1)/9; số vòng 142857 = (10^{6} − 1)/7.'])
    D.luyentap([('8.1', 'REPUNIT', 'Repunit nhỏ nhất chia hết cho n (n ≤ 10^{12}, gcd(n, 10) = 1): cấp của 10 theo mô-đun 9n.'),
                ('8.2', 'CHỮ SỐ THỨ K', 'Chữ số thứ k sau dấu phẩy của a/b với k ≤ 10^{18}: Mở rộng 3.'),
                ('8.3', 'SỐ VÒNG', 'Liệt kê các số nguyên tố p ≤ 10^{6} mà 1/p có chu kì p − 1, và in số vòng tương ứng với p nhỏ.')])
    D.tukiemtra([('1/13 có chu kì bao nhiêu? (gợi ý: 10^{6} = 1 000 000 = 13 · 76 923 + 1)', '6'), ('1/40 có đuôi dài bao nhiêu, chu kì bao nhiêu?', '40 = 2^{3} · 5: đuôi 3, chu kì 0 (1/40 = 0,025)'),
                 ('1/37 có chu kì bao nhiêu?', '3, vì 999 = 27 · 37'), ('142857 × 8 bằng bao nhiêu? Có còn là vòng quay không?', '1 142 856: không, vì 8 > 6')])
