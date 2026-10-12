def build(D, P):
    D.objectives([
        'Áp dụng nguyên tắc "chữ số bên trái quan trọng nhất" để làm **tham lam** trên chữ số.',
        'Xóa k chữ số khỏi một số dài 10^{6} chữ số để được số nhỏ nhất, trong O(L) bằng **ngăn xếp**, và chứng minh vì sao tham lam đúng.',
        'Ghép nhiều số thành một số lớn nhất bằng phép so sánh "ghép thử" ab với ba.',
        'Nhận ra các bài cùng họ: giữ lại k chữ số lớn nhất, đổi chỗ một lần...'])
    D.kbox('KHỞI ĐỘNG', [
        'Trên bảng có số 1 432 219. Cô giáo cho phép xóa đúng 3 chữ số. Muốn số còn lại nhỏ nhất, em xóa những chữ số nào?',
        'Xóa ba chữ số lớn nhất (4, 3, 9) được 1221. Nhưng xóa 4, 3 và một chữ số 2 lại được 1219, nhỏ hơn! Trực giác "xóa chữ số lớn nhất" sai, vì vị trí quan trọng hơn giá trị. '
        'Bài học này tìm ra quy tắc đúng.'])

    D.h('1. Chữ số bên trái quyết định')
    D.p('Như đã chứng minh ở Bài 13: với hai số cùng số chữ số, số nào lớn hơn ở **vị trí khác nhau đầu tiên** thì lớn hơn. Sau khi xóa đúng k chữ số, mọi kết quả có cùng độ dài L − k '
        '(trước khi bỏ số 0 ở đầu), nên muốn kết quả nhỏ nhất ta phải làm chữ số đầu nhỏ nhất có thể, rồi đến chữ số thứ hai, ...')
    D.kbox('ĐỊNH LÍ (XÓA ĐỈNH ĐẦU TIÊN)', ['Nếu chỉ được xóa **một** chữ số, cách tốt nhất là xóa chữ số s[i] đầu tiên mà s[i] > s[i + 1] (một "đỉnh"); nếu dãy không giảm ở đâu cả, xóa chữ số cuối cùng.'])
    D.kbox('VÌ SAO ĐÚNG?', ['Gọi i là đỉnh đầu tiên: s[0] ≤ s[1] ≤ ... ≤ s[i] > s[i + 1]. Xóa một chữ số ở vị trí j < i thay s[j] bằng s[j + 1] ≥ s[j]: không tốt hơn. '
                            'Xóa s[i] thay s[i] bằng s[i + 1] < s[i]: kết quả nhỏ hơn mọi cách xóa ở vị trí > i (các cách đó giữ nguyên s[0..i]). Nếu dãy không giảm, xóa ở cuối giữ nguyên phần đầu nhỏ nhất.'])

    D.h('2. Bài toán XOACS')
    D.problem_box('XOACS', 'Cho một số n dưới dạng xâu chữ số và số nguyên k. Hãy xóa đúng k chữ số của n (các chữ số còn lại giữ nguyên thứ tự) để được số nhỏ nhất. Bỏ các chữ số 0 thừa ở đầu kết quả; nếu không còn chữ số nào thì in 0.',
                  'Một dòng chứa n (1 ≤ độ dài ≤ 10^{6}, không có chữ số 0 ở đầu) và k (0 ≤ k ≤ độ dài của n).', 'Số nhỏ nhất thu được.')
    D.examples('XOACS', [('1432219 3', '1219', 'Xóa 4, 3 và một chữ số 2.'), ('10200 1', '200', 'Xóa chữ số 1, được 0200 = 200.'), ('2026 1', '26', '026 = 26 nhỏ hơn 226, 206, 202.'),
                         ('10 2', '0', 'Xóa hết, in 0.')])

    D.h('3. Ý tưởng ngây thơ: Xóa từng chữ số một')
    D.p('Áp dụng định lí ở mục 1 k lần: mỗi lần tìm đỉnh đầu tiên và xóa nó. Đúng (mỗi lần xóa đều tối ưu và các lần xóa không làm hỏng nhau, xem mục 4), nhưng chậm.')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách xóa từng chữ số.', 12)
    D.code('XOACS.CPP (ngây thơ): k lần tìm và xóa đỉnh', P.src('naive.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi lần tìm đỉnh có thể phải quét gần hết xâu (khi xâu gần như không giảm), mỗi lần xóa dịch chuyển phần sau của xâu: O(k · L). '
                               'Đo thực tế với xâu chữ số không giảm và k = L/2: L = 10^{5} mất **2,5 giây**, L = 3 · 10^{5} mất **25 giây**; L = 10^{6} cần khoảng **5 phút**.'])
    D.kbox('BẾ TẮC', ['Sau khi xóa đỉnh ở vị trí i, đỉnh tiếp theo chỉ có thể ở vị trí i − 1 (nếu chữ số trước nó giờ lớn hơn chữ số mới kề nó) hoặc xa hơn về bên phải. '
                      'Vậy mà mỗi lần ta lại quét từ đầu xâu. Có cách nào "nhớ" phần đầu đã quét không?'])

    D.h('4. Phá bế tắc: Ngăn xếp các chữ số giữ lại')
    D.step(1, 'Phần đã quét luôn không giảm')
    D.p('Đọc các chữ số từ trái sang phải và giữ phần kết quả đã chốt trong một **ngăn xếp**. Khi đọc chữ số c: chừng nào còn lượt xóa và chữ số ở đỉnh ngăn xếp **lớn hơn** c, '
        'đỉnh ấy chính là "đỉnh đầu tiên" của xâu hiện tại: bỏ nó đi. Sau đó đẩy c vào. Nhờ vậy ngăn xếp luôn là một dãy không giảm.')
    D.step(2, 'Hết xâu mà còn lượt xóa')
    D.p('Ngăn xếp không giảm, đỉnh đầu tiên chính là phần tử cuối: bỏ k phần tử cuối. Cuối cùng bỏ các chữ số 0 ở đầu (rỗng thì in 0).')
    D.step(3, 'Chạy tay với 1432219, k = 3')
    D.fig(P.fig('stack'), 'Ngăn xếp sau mỗi chữ số được đọc.', 11)
    D.kbox('VÌ SAO ĐÚNG?', ['Mỗi lần bỏ đỉnh ngăn xếp, ta đúng là xóa "đỉnh đầu tiên" của xâu hiện tại (các chữ số trong ngăn xếp không giảm, chữ số tiếp theo nhỏ hơn đỉnh). '
                            'Vậy chương trình làm đúng k lần áp dụng định lí ở mục 1, theo cùng thứ tự với cách ngây thơ, chỉ là không quét lại phần đầu. '
                            'Thực hiện liên tiếp các lần xóa tối ưu cho kết quả tối ưu vì: kết quả tối ưu khi xóa k chữ số luôn chứa kết quả tối ưu khi xóa 1 chữ số làm bước đầu (đổi thứ tự các lần xóa không đổi tập bị xóa).'])
    D.step(4, 'Chương trình')
    D.fig(P.fig('opt'), 'Sơ đồ khối của cách dùng ngăn xếp.', 12.5)
    D.code('XOACS.CPP: tham lam với ngăn xếp', P.src('opt.cpp'))
    D.kbox('ĐẾM SỐ PHÉP TÍNH', ['Mỗi chữ số được đẩy vào và lấy ra ngăn xếp nhiều nhất một lần: O(L). Với L = 10^{6}, chương trình chạy khoảng **0,04 giây**. '
                               'Đã đối chiếu với cách thử mọi tập chữ số bị xóa trên các xâu tới 12 chữ số.'])

    D.h('5. Mở rộng')
    D.sub('Mở rộng 1: Giữ lại số lớn nhất')
    D.p('Đổi dấu so sánh: bỏ đỉnh ngăn xếp khi nó **nhỏ hơn** chữ số mới. Kết quả là số lớn nhất gồm L − k chữ số (bài "chọn k chữ số tạo số lớn nhất", rất hay gặp).')
    D.sub('Mở rộng 2: Ghép các số thành số lớn nhất')
    D.p('Cho các số 3, 30, 34, 9: ghép theo thứ tự nào được số lớn nhất? Sắp xếp theo độ lớn hay theo xâu đều sai (3 phải đứng trước 30 vì 330 > 303). Quy tắc đúng: **x đứng trước y khi xâu xy > xâu yx**. '
        'Kết quả: 9 34 3 30 → 9 534 330. Phép so sánh này có tính bắc cầu (có thể chứng minh bằng cách coi mỗi xâu x như phân số x / (10^{|x|} − 1)), nên sắp xếp theo nó là hợp lệ.')
    D.code('Ghép các số thành số lớn nhất', P.src('ex_ghep.cpp'))
    D.p('Chương trình đã được đối chiếu với cách thử mọi hoán vị trên 300 bộ dữ liệu nhỏ. Nhớ trường hợp toàn số 0: in "0" chứ không phải "000".')
    D.sub('Mở rộng 3: Đổi chỗ đúng một lần')
    D.p('Được đổi chỗ hai chữ số **một lần** để số lớn nhất: đi từ trái sang, tìm vị trí đầu tiên mà phía sau có chữ số lớn hơn; đổi nó với **lần xuất hiện cuối cùng** của chữ số lớn nhất phía sau '
        '(lấy lần cuối để chữ số nhỏ bị đẩy về càng xa càng tốt). Ví dụ 1993 → 9913, không phải 9193. O(L) với mảng "vị trí cuối của mỗi chữ số".')
    D.kbox('BẪY THƯỜNG GẶP', [
        '- **Xóa chữ số lớn nhất** thay vì đỉnh đầu tiên: 1432219 → 1221 thay vì 1219.',
        '- **Quên dùng hết lượt xóa:** khi xâu không giảm (12345), ngăn xếp không bỏ gì; phải bỏ ở cuối.',
        '- **Không bỏ chữ số 0 ở đầu** hoặc in xâu rỗng thay vì 0.',
        '- **So sánh ghép bằng số:** xy có thể dài hàng nghìn chữ số; so sánh **xâu**.'])
    D.kbox('GHI NHỚ', [
        '- Tham lam trên chữ số: làm chữ số bên trái tốt nhất có thể trước.',
        '- Xóa k chữ số để nhỏ nhất: ngăn xếp không giảm, bỏ đỉnh khi đỉnh > chữ số mới; còn lượt thì bỏ ở cuối. O(L).',
        '- Ghép số lớn nhất: sắp xếp với phép so sánh xy > yx.'])
    D.luyentap([('14.1', 'GIỮ K CHỮ SỐ', 'Chọn k chữ số (giữ thứ tự) của một xâu 10^{6} chữ số để được số lớn nhất: Mở rộng 1.'),
                ('14.2', 'GHÉP SỐ', 'Ghép n ≤ 10^{5} số (mỗi số tới 10^{9}) thành số lớn nhất và số nhỏ nhất (không có 0 ở đầu nếu có thể): Mở rộng 2.'),
                ('14.3', 'MỘT LẦN ĐỔI', 'Đổi chỗ hai chữ số đúng một lần để số lớn nhất, hoặc để số nhỏ nhất mà không có 0 ở đầu: Mở rộng 3.')])
    D.tukiemtra([('Xóa 2 chữ số khỏi 2026 để nhỏ nhất?', '2 (giữ 0 và 2 cuối: 02 = 2)'), ('Xóa 1 chữ số khỏi 12345?', '1234 (xóa chữ số cuối)'),
                 ('Ghép 3, 30, 34, 9 thành số lớn nhất?', '9534330'), ('Đổi chỗ một lần để 2026 lớn nhất?', '6022 (đổi 2 đầu với 6)')])
