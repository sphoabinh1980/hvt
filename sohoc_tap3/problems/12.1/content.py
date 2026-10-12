def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Tìm x nhỏ nhất ≥ L thỏa hệ x ≡ a_{i} (mod m_{i}), các m_{i} đôi một nguyên tố cùng nhau. Theo định lí số dư Trung Hoa (Tập 1, Bài 12), tập nghiệm là '
        '**một lớp đồng dư** x ≡ r (mod M) với M = m_{1} ··· m_{k} ≤ 10^{18}. Việc còn lại: tìm r, rồi tìm phần tử nhỏ nhất ≥ L của lớp.')

    D.h('2. Cách ngây thơ: Thử từng x')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách thử từng x', 10)
    D.code('Cách ngây thơ: thử x = L, L + 1, ...', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** tới M bước (nghiệm nằm trong [L, L + M)): 10^{6} ở subtask 1, 10^{18} ở các subtask sau.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1**: **' + str(P.pts('naive.cpp', 1)) + ' điểm**.', '**Subtask 2, 3**: **0 điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Không thể thử từng số. Nhưng nghiệm của hệ có cấu trúc: gộp từng phương trình một, ta luôn biết tập nghiệm hiện tại là một lớp r + M·t.'])

    D.h('4. Phá bế tắc: Gộp từng cặp')
    D.p('Giữ cặp (r, M): mọi x thỏa các phương trình đã gộp có dạng x = r + M·t. Thay vào phương trình mới x ≡ a (mod m):')
    D.eq('**M · t ≡ a − r (mod m)  ⇒  t ≡ (a − r) · M^{−1} (mod m),   r ← r + M·t,   M ← M·m.**')
    D.p('Nghịch đảo M^{−1} mod m tồn tại vì gcd(M, m) = 1, và phải tính bằng **Euclid mở rộng** (m không nhất thiết nguyên tố, không dùng được Fermat). Bắt đầu từ (r, M) = (0, 1).')
    D.fig(P.fig('merge'), 'Gộp lần lượt ba phương trình của Hàn Tín (ví dụ 2).', 14.5)
    D.sub('Nghiệm nhỏ nhất ≥ L')
    D.p('Có r ∈ [0, M). Các nghiệm là r, r + M, r + 2M, ...; số nhỏ nhất ≥ L là **L + ((r − L) mod M)** (với phép lấy dư không âm), không cần vòng lặp.')
    D.fig(P.fig('jump'), 'Ví dụ 2: từ r = 23, bước M = 105, số đầu tiên ≥ 100 là 128.', 15)
    D.p('Chương trình `onestep.cpp` chỉ "nhảy thêm một bước": in r nếu r ≥ L, ngược lại r + M. Đúng với cả ba ví dụ, nhưng sai khi L ≥ r + M (L tới 10^{18}, còn M có thể nhỏ): '
        '**' + S('onestep.cpp') + ' điểm**. Ba ví dụ đẹp vẫn chưa phải là một bộ test.')
    D.box('purple', 'ƯỚC LƯỢNG ĐỂ KHÔNG TRÀN', ['- r + M·t < M + M·(m − 1) = M·m ≤ 10^{18}.', '- (a − r) mod m < 10^{9} và u < 10^{9}: tích < 10^{18} (lời giải dùng __int128 cho chắc).',
        '- Đáp số < L + M ≤ 2 · 10^{18}: vừa long long.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 13)
    D.code('DIEMBINH.CPP: gộp Trung Hoa', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(k log m).')
    D.box('blue', 'MỞ RỘNG', ['Khi các m_{i} có ước chung, phép gộp vẫn làm được nhưng có thể vô nghiệm, và M mới là lcm thay cho tích: đó là bài HAI NGỌN ĐÈN (12.2) và LỊCH CAN CHI (12.3).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Dùng Fermat** để tìm M^{−1} mod m khi m hợp số.', '**a − r âm:** lấy dư không âm.', '**Chỉ nhảy một bước M** từ r.', '**m = 1:** phương trình luôn đúng; extgcd(0, 1) cho u = 0, t = 0, vẫn đúng.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'onestep.cpp', 'opt.cpp'])
