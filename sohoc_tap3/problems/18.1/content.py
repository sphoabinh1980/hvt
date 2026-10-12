def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Mọi phép đổi cơ số đều đi qua **giá trị thật** của số (≤ 10^{18}, vừa long long), theo hai bước (Tập 1, Bài 18):')
    D.nums(['**Cơ số a → giá trị:** sơ đồ Horner, đọc chữ số từ trái sang phải, v ← v · a + d.',
            '**Giá trị → cơ số b:** chia liên tiếp cho b; số dư là chữ số cuối, thương là phần còn lại; đọc các số dư theo thứ tự ngược.'])
    D.fig(P.fig('conv'), 'Ví dụ 1, yêu cầu thứ nhất: (7EA)₁₆ → 2026 → (3752)₈.', 15.2)

    D.h('2. Cách ngây thơ: Chỉ đổi sang thập phân')
    D.code('Cách ngây thơ: Horner + printf', P.src('naive.cpp'))
    D.p('Bước 1 cộng với printf("%lld") giải xong mọi yêu cầu có b = 10: **' + S('naive.cpp') + ' điểm**.')

    D.h('3. Bế tắc')
    D.box('red', 'ĐIỂM BẾ TẮC', ['printf chỉ biết in cơ số 10 (và 8, 16 bằng %o, %X). Với cơ số b bất kì phải tự sinh các chữ số: '
                                  'chia liên tiếp, cẩn thận với số 0 và với thứ tự ngược.'])
    D.p('Một cài đặt rất tự nhiên dùng vòng `while (v > 0)` để sinh chữ số (`trap.cpp`): khi giá trị bằng 0 vòng lặp không chạy lần nào và chương trình in **dòng trống**. '
        'Mọi subtask đều có số 0 ("0000" ở ví dụ 2), nên chương trình được **' + S('trap.cpp') + ' điểm** dù mọi trường hợp khác đều đúng.')

    D.h('4. Phá bế tắc: Horner + chia liên tiếp')
    D.sub('Vì sao dùng Horner chứ không cộng dᵢ · aⁱ?')
    D.p('Trong sơ đồ Horner, giá trị trung gian là giá trị của một **tiền tố** của xâu, luôn không vượt quá giá trị cuối cùng ≤ 10^{18}: không bao giờ tràn, '
        'kể cả khi S có 90 chữ số 0 ở đầu. Ngược lại, cách cộng d_{i} · a^{i} phải tính a^{i} tới a^{99}: tràn số. '
        '(Trên thực tế, tích của chữ số 0 với lũy thừa đã tràn vẫn bằng 0 nên chương trình kiểu ấy thường vẫn ra đúng, nhưng tràn số nguyên có dấu là hành vi không xác định trong C++; đừng dựa vào may mắn.)')
    D.sub('Số 0 và thứ tự ngược')
    D.bullets(['Dùng **do ... while**: thân vòng lặp chạy ít nhất một lần, nên v = 0 sinh đúng một chữ số "0".',
               'Các chữ số sinh ra từ hàng thấp tới hàng cao; lưu vào mảng rồi in ngược.',
               'Chữ số 0 thừa ở đầu S tự biến mất: Horner bỏ qua chúng (0 · a + 0 = 0).'])
    D.sub('Kí tự ↔ giá trị')
    D.p('Giá trị của kí tự c: c − \'0\' nếu c là chữ số, c − \'A\' + 10 nếu c là chữ cái. Chiều ngược lại tra xâu DIG = "0123456789ABC...Z".')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của một yêu cầu', 12)
    D.code('DOICOSO.CPP', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(|S| + log_{b} v) mỗi yêu cầu: khoảng 160 phép tính, 10^{5} yêu cầu chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Nếu S có giá trị vượt long long (ví dụ 1000 chữ số), đổi cơ số bằng phép chia **số lớn cho số nhỏ** lặp lại: mỗi lần chia S (trong cơ số a) cho b được một chữ số.',
                              'Đổi giữa cơ số 2 và 16 (hay 8) không cần đi qua giá trị: mỗi chữ số hexa ứng đúng 4 bit.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**while (v > 0)** in xâu rỗng cho số 0.', '**Quên đọc ngược** các số dư.', '**Cộng dᵢ · aⁱ:** lũy thừa tràn với xâu dài.',
               '**In chữ thường** hoặc nhầm A = 11.', '**Mảng S chỉ 100 phần tử:** cần thêm chỗ cho kí tự kết thúc xâu.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'trap.cpp', 'opt.cpp'])
