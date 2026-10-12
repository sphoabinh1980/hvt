def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Tính S = 1 + a + a^{2} + ... + a^{n} mod m (n + 1 số hạng), với n tới 10^{18} và m **bất kì** tới 10^{18}. '
        'Công thức cấp số nhân (a^{n+1} − 1)/(a − 1) cần một phép chia, mà theo mô-đun hợp số thì phép chia thường không tồn tại.')

    D.h('2. Cách ngây thơ: Cộng dồn')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách cộng dồn', 11)
    D.code('Cách ngây thơ: cộng dồn n + 1 số hạng', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(n) mỗi bộ. Đúng với mọi m (chỉ có cộng và nhân), nhưng n = 10^{18} thì không chạy xong.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1** (n ≤ 10^{6}): **' + str(P.pts('naive.cpp', 1)) + ' điểm**.'])
    D.p('Với m nguyên tố và a ≢ 0, 1 (mod m) (subtask 2), công thức cấp số nhân dùng được: chia cho a − 1 là nhân với (a − 1)^{m−2}. '
        'Chương trình `formula.cpp` qua subtask 2, nhưng sai khi m hợp số hoặc a ≡ 1 (mod m), như bộ "5 3 4" của ví dụ 2: 5 ≡ 1 (mod 4) nên a − 1 ≡ 0, không có nghịch đảo. '
        'Tổng cộng **' + S('formula.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Cần một cách tính tổng cấp số nhân **chỉ dùng cộng và nhân** (đúng với mọi mô-đun) nhưng nhanh như lũy thừa nhanh.'])

    D.h('4. Phá bế tắc: Chia đôi trên số số hạng')
    D.p('Gọi S(k) = 1 + a + ... + a^{k−1} (k số hạng). Hai quan sát:')
    D.fig(P.fig('split'), 'Nửa sau của S(2h) là nửa đầu nhân với a^{h}.', 14)
    D.nums(['**k chẵn, k = 2h:** S(2h) = S(h) + a^{h} · S(h) = S(h) · (1 + a^{h}).', '**k lẻ:** S(k) = 1 + a · S(k − 1) (tách số hạng đầu, các số hạng còn lại có chung thừa số a).'])
    D.p('Hàm đệ quy trả về **đồng thời** S(k) và a^{k} (để dùng a^{h} ở bước chẵn). Cứ hai lần gọi thì k giảm ít nhất một nửa, nên có O(log n) lời gọi (≤ 120 với n ≤ 10^{18}). Đáp số là S(n + 1).')
    D.fig(P.fig('tree'), 'Chuỗi lời gọi khi tính S(10) với a = 2, m = 1000.', 15.5)
    D.box('purple', 'CHỐNG TRÀN SỐ', ['m tới 10^{18} nên mọi phép nhân hai số dư phải qua `__int128`. Cũng cẩn thận 1 + a^{h} có thể bằng m (khi a^{h} = m − 1): '
        'lấy (1 + q) % m trước khi nhân.'])

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối hàm đệ quy S(k)', 11)
    D.code('TONGLT.CPP: chia để trị trên số số hạng', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(log n) mỗi bộ, mỗi bước vài phép nhân 128 bit; 10^{4} bộ chạy tức thì.')
    D.box('blue', 'MỞ RỘNG: LŨY THỪA MA TRẬN', ['Vectơ (S(k), a^{k}) chuyển sang (S(k + 1), a^{k+1}) = (S(k) + a^{k}, a · a^{k}) bằng một ma trận 2 × 2. '
        'Lũy thừa ma trận (Bài 15) cũng cho lời giải O(log n) chỉ dùng cộng và nhân.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**Nhầm số số hạng:** từ a^{0} tới a^{n} là n + 1 số hạng.', '**Dùng công thức chia** với mô-đun hợp số.',
               '**Nhân 64 bit** khi m tới 10^{18}.', '**a = 0:** S = 1 (chỉ số hạng 0^{0} = 1); hàm đệ quy cho đúng nếu khởi tạo a^{0} = 1 mod m.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'formula.cpp', 'opt.cpp'])
