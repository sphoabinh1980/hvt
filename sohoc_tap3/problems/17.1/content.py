def build(D, P):
    S = lambda f: str(P.total(f))
    D.h('1. Hiểu bài toán')
    D.p('Hai số tới 10^{5} chữ số không vừa kiểu số nào: phải lưu thành **xâu chữ số** và tự làm phép tính như trên giấy (Tập 1, Bài 17). '
        'Tách dấu ra khỏi trị tuyệt đối, bài toán chia thành hai trường hợp:')
    D.bullets(['**Cùng dấu:** |a + b| = |a| + |b|, dấu giữ nguyên. Chỉ cần phép **cộng** hai số không âm.',
               '**Khác dấu:** |a + b| = (số có trị tuyệt đối lớn) − (số còn lại), dấu là dấu của số có trị tuyệt đối lớn hơn. Cần phép **so sánh** và phép **trừ**.'])
    D.fig(P.fig('ops'), 'Ví dụ 1 và một phiên bản thu nhỏ của ví dụ 2 (10⁵ − 1).', 14)

    D.h('2. Cách ngây thơ: long long')
    D.code('Cách ngây thơ: long long', P.src('naive.cpp'))
    D.p('Với |a|, |b| ≤ 10^{18}, tổng tới 2 · 10^{18} < 9,2 · 10^{18}: đúng subtask 1, **' + S('naive.cpp') + ' điểm**. Số dài hơn 19 chữ số đọc vào đã sai.')

    D.h('3. Bế tắc')
    D.p('Bước tiếp theo tự nhiên là cộng hai xâu chữ số từ hàng đơn vị (`mid.cpp`, chỉ cộng trị tuyệt đối và giữ dấu của a). '
        'Đúng khi hai số cùng dấu (subtask 2), nhưng sai ngay cả ở subtask 1 khi hai số khác dấu: **' + S('mid.cpp') + ' điểm**.')
    D.box('red', 'ĐIỂM BẾ TẮC', ['Phép cộng hai số khác dấu thực chất là **phép trừ** hai trị tuyệt đối, và phải biết trước số nào lớn hơn. '
                                  'Ba hàm cần viết: so sánh, cộng, trừ (số lớn trừ số nhỏ).'])

    D.h('4. Phá bế tắc: Ba hàm trên xâu chữ số')
    D.fig(P.fig('cases'), 'Phân chia trường hợp theo dấu.', 13)
    D.sub('So sánh trị tuyệt đối')
    D.p('Số nhiều chữ số hơn thì lớn hơn (vì không có chữ số 0 thừa ở đầu); chỉ khi **dài bằng nhau** mới so như hai xâu.')
    D.box('purple', 'BẪY: SO SÁNH NHƯ XÂU', ['$return x < y ? -1 : (x > y ? 1 : 0);',
                                             'So sánh từ điển cho "9" > "10". Với a = −9, b = 10, chương trình `trap.cpp` lấy 9 trừ 10 và ra kết quả vô nghĩa. '
                                             'Hai số cùng dấu không cần so sánh nên subtask 2 vẫn đúng: **' + S('trap.cpp') + ' điểm**.'])
    D.sub('Cộng và trừ')
    D.p('Đi từ cuối xâu về đầu, ghi chữ số kết quả theo thứ tự ngược rồi đảo lại. Khi cộng, số nhớ chỉ là 0 hoặc 1 (9 + 9 + 1 = 19); '
        'kết quả có thể dài hơn một chữ số (ví dụ 1). Khi trừ x − y với x ≥ y, chữ số âm thì cộng 10 và mượn 1 ở hàng trên; '
        'việc mượn có thể lan rất xa (ví dụ 2) và để lại các chữ số 0 ở đầu, phải xóa nhưng **giữ ít nhất một chữ số**.')
    D.box('blue', 'KHÔNG IN -0', ['Khi |a| = |b| và khác dấu, kết quả bằng 0: in "0" ngay (ví dụ 3). Đây là trường hợp duy nhất phép trừ cho 0, '
                                  'nên trong mọi trường hợp còn lại kết quả khác 0 và dấu trừ (nếu có) là đúng.'])

    D.h('5. Cách tối ưu')
    D.code('TONGLON.CPP: cộng, trừ, so sánh trên xâu', P.src('opt.cpp'))
    D.p('**Độ phức tạp:** O(L) với L = 10^{5} là số chữ số; chạy ' + P.scores['opt.cpp']['detail'][2].split()[1] + '.')
    D.box('blue', 'MỞ RỘNG', ['Lưu số theo khối 9 chữ số (cơ số 10^{9}) làm số phép tính giảm 9 lần; với phép cộng điều này không cần thiết, nhưng là chìa khóa của bài 17.2 và 17.3.',
                              'Phép trừ a − b chính là a + (−b): đổi dấu b rồi dùng lại chương trình này.'])
    D.h('6. Bẫy thường gặp')
    D.bullets(['**So sánh hai xâu khác độ dài** bằng toán tử <.', '**In -0** khi a = −b.', '**Không xóa chữ số 0 thừa** sau phép trừ, hoặc xóa hết khi kết quả là 0.',
               '**Quên số nhớ cuối cùng** sau khi cộng xong (98765 + 4789 có 6 chữ số).', '**Dùng cin không tắt đồng bộ** với dữ liệu lớn hơn nhiều: chậm.'])
    D.h('7. Bảng điểm theo thuật toán')
    P.score(['naive.cpp', 'mid.cpp', 'trap.cpp', 'opt.cpp'])
