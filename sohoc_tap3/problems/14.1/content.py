def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Gọi A, B, C là tập các bội của a, b, c. Cần đếm các x ∈ [L, R] thuộc (A ∪ B) nhưng không thuộc C. Hai mẹo quen thuộc (Tập 1, Bài 14):')
    D.bullets(['**Đếm trên đoạn bằng hiệu hai tiền tố:** số lượng trên [L, R] là f(R) − f(L − 1), với f(N) đếm trên [1, N]. Số bội của a trong [1, N] là ⌊N/a⌋.',
               '**Bội chung của a và b là bội của lcm(a, b)**, không phải của a · b.'])
    D.fig(P.fig('grid'), 'Ví dụ 1, câu hỏi thứ nhất (đoạn [1, 30], a = 2, b = 3, c = 5).', 15)

    D.h('2. Cách ngây thơ: Duyệt mọi x')
    D.fig(P.fig('naive'), 'Sơ đồ khối của cách duyệt', 12)
    D.code('Cách ngây thơ: duyệt [L, R]', P.src('naive.cpp'))
    D.p('**Độ phức tạp:** O(R − L): tốt khi đoạn ngắn (subtask 1), vô vọng với đoạn dài 10^{18}.')

    D.h('3. Bế tắc')
    D.bullets(['**Subtask 1**: **' + str(P.pts('naive.cpp', 1)) + ' điểm**.'])
    D.box('red', 'ĐIỂM BẾ TẮC', ['Đếm từng số là thừa: số bội của một số trong [1, N] là một phép chia. Cần biểu diễn tập cần đếm qua các tập "bội của ..." bằng nguyên lí bù trừ.'])

    D.h('4. Phá bế tắc: Bù trừ')
    D.fig(P.fig('venn'), 'Tập cần đếm và công thức bù trừ.', 15)
    D.p('(A ∪ B) ∩ C = (A ∩ C) ∪ (B ∩ C) lại là hợp của hai tập; giao của hai tập này là A ∩ B ∩ C, tức bội của lcm(a, b, c). Vậy')
    D.eq('**f(N) = ⌊N/a⌋ + ⌊N/b⌋ − ⌊N/lcm(a,b)⌋ − ⌊N/lcm(a,c)⌋ − ⌊N/lcm(b,c)⌋ + ⌊N/lcm(a,b,c)⌋.**')
    D.sub('Chặn tràn số')
    D.p('Với a, b, c tới 10^{18}, lcm có thể tới 10^{54}. Nhưng nếu lcm > N thì ⌊N/lcm⌋ = 0: chỉ cần biết lcm có vượt 10^{18} hay không. '
        'Hàm lcm có chặn (như bài 3.3): x = a/gcd(a, b); nếu x > ⌊10^{18}/b⌋ thì trả về INF = 2 · 10^{18} (mọi phép chia cho INF đều cho 0).')
    D.p('Chương trình `mid.cpp` tính lcm thẳng `a / gcd * b`: đúng khi a, b, c ≤ 10^{6} (lcm ≤ 10^{18}), sai khi tích tràn ở subtask 3: **' + S('mid.cpp') + ' điểm**.')
    D.box('purple', 'BẪY: "KHÔNG CHIA HẾT CHO c" KHÔNG PHẢI TRỪ ⌊N/c⌋', ['Chỉ trừ những số vừa thuộc A ∪ B, vừa chia hết cho c. Trừ cả ⌊N/c⌋ là trừ cả những bội của c không chia hết cho a, b (như 5, 25 ở ví dụ 1).'])
    D.sub('Chạy tay ví dụ 1, câu hỏi 1')
    D.p('N = 30: ⌊30/2⌋ + ⌊30/3⌋ − ⌊30/6⌋ = 15 + 10 − 5 = 20; ⌊30/10⌋ + ⌊30/15⌋ − ⌊30/30⌋ = 3 + 2 − 1 = 4. Đáp số 20 − 4 = 16.')

    D.h('5. Cách tối ưu')
    D.fig(P.fig('opt'), 'Sơ đồ khối của lời giải tối ưu', 13)
    D.code('BOISO.CPP: bù trừ với lcm có chặn', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(log 10^{18}) mỗi câu hỏi (bốn lần gcd).')
    D.box('blue', 'MỞ RỘNG', ['Với k số a_{1}, ..., a_{k} (k ≤ 20), số x ≤ N chia hết cho ít nhất một số là Σ_{S ≠ ∅} (−1)^{|S|+1} ⌊N / lcm(S)⌋, duyệt 2^{k} tập con bằng mặt nạ bit (bài 14.2).'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**⌊(R − L + 1)/a⌋:** sai; đoạn [2, 4] có hai bội của 2.', '**a · b thay cho lcm.**', '**Tràn khi tính lcm.**', '**Trừ ⌊N/c⌋** thay vì chỉ trừ phần giao.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'opt.cpp'])
