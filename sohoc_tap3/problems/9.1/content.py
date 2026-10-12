def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Tính a^{b} mod (10^{9} + 7) cho 10^{5} câu hỏi với a, b tới 10^{18}. Đây là bài "chuẩn" của lũy thừa nhanh (Tập 1, Bài 9); '
        'cái cần luyện là cài đặt **đúng mọi chi tiết**: lấy dư cơ số trước, khởi tạo đúng, quy ước 0^{0} = 1.')

    D.h('2. Cách ngây thơ: Nhân b lần')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách nhân b lần', 6.5)
    D.code('Cách ngây thơ: nhân b lần', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(b) mỗi câu hỏi; với b = 10^{18} không thể chạy xong.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (Q ≤ 10, b ≤ 10^{6}): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.', '**Subtask 2, 3**: **0 điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['a^{b} được tính bằng b phép nhân giống hệt nhau. Nhưng a^{2k} = (a^{k})^{2}: một phép bình phương thay cho k phép nhân.'])

    D.h('4. Phá bế tắc: Bình phương liên tiếp')
    D.p('Viết b trong hệ nhị phân: b = Σ 2^{i} (theo các bit 1). Khi đó a^{b} = Π a^{2^{i}}: tích các lũy thừa a, a^{2}, a^{4}, a^{8}, ... ứng với các bit 1. '
        'Duyệt bit từ phải sang trái: bit 1 thì nhân a hiện tại vào r, luôn bình phương a.')
    D.fig(P.fig('bits'), 'Tính 2^{10} bằng bình phương liên tiếp: chỉ nhân vào r ở các bit 1 (ô vàng).', 14.5)
    D.sub('Ba chi tiết làm mất điểm')
    D.nums(['**Lấy dư cơ số trước:** a tới 10^{18}, phép bình phương đầu tiên a · a đã tràn long long. Sau khi lấy dư, mọi số < 10^{9} + 7 và tích hai số < 1,01 · 10^{18} vừa long long.',
            '**Khởi tạo r = 1:** với mô-đun 10^{9} + 7 thì 1 mod M = 1; nhưng nếu mô-đun có thể bằng 1 thì phải khởi tạo 1 % M (bài 9.2).',
            '**Số mũ 0:** vòng lặp không chạy, trả về 1: đúng cả với 0^{0} và với a chia hết cho M.'])
    D.p('Chương trình `bay.cpp` viết lũy thừa nhanh đúng nhưng quên dòng `a %= MOD`. Nó đúng khi a < 10^{9} + 7 (subtask 2), sai khi a lớn: ví dụ 2 với a = 10^{18} '
        'đã cho kết quả sai, và cả subtask 1 (có a tới 10^{18}) lẫn subtask 3 đều mất: **' + S('bay.cpp') + ' điểm**.')
    D.box('purple', 'VÌ SAO ĐƯỢC LẤY DƯ CƠ SỐ?', ['a ≡ a mod M (mod M), và đồng dư giữ nguyên qua phép nhân, nên a^{b} ≡ (a mod M)^{b}. '
        'Chú ý: được lấy dư **cơ số** theo M, nhưng **không** được lấy dư số mũ theo M (số mũ chỉ rút gọn được theo M − 1 khi M nguyên tố và M ∤ a, bài 9.2).'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối hàm lũy thừa nhanh', 10)
    D.code('LUYTHUAQ.CPP: lũy thừa nhanh theo mô-đun', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(log b) ≤ 60 lượt mỗi câu hỏi, 10^{5} câu hỏi chỉ 1,2 · 10^{7} phép nhân.')
    D.box('blue', 'MỞ RỘNG: DÙNG LẠI HÀM power', ['Hàm power(a, b) là "viên gạch" của gần như cả chương: nghịch đảo theo Fermat (b = M − 2, bài 10.1), Miller–Rabin (bài 5.3), '
        'tháp lũy thừa (bài 11.3). Hãy viết một lần, kiểm tra kĩ với 0^{0}, a = M, a > M, rồi lưu vào thư viện.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Quên a %= MOD.**', '**Dùng pow của C++:** hàm số thực, sai hoàn toàn với số mũ lớn.',
               '**Đệ quy power(a, b/2) gọi hai lần:** `power(a, b/2) * power(a, b/2)` biến O(log b) thành O(b). Gọi một lần, lưu vào biến.',
               '**Đọc ghi chậm** với 10^{5} dòng: dùng scanf/printf.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'bay.cpp', 'opt.cpp'])
