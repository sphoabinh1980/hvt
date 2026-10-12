"""Dữ liệu chung của cuốn sách: chương, bài học, bài tập."""

LESSONS = {
    1: 'Phép chia có dư và đồng dư', 2: 'Ước số: liệt kê, đếm và tính tổng',
    3: 'Ước chung lớn nhất và bội chung nhỏ nhất', 4: 'Euclid mở rộng và phương trình ax + by = c',
    5: 'Số nguyên tố và kiểm tra nguyên tố', 6: 'Sàng Eratosthenes', 7: 'Phân tích thừa số nguyên tố',
    8: 'Sàng trên đoạn', 9: 'Lũy thừa nhanh', 10: 'Nghịch đảo mô-đun', 11: 'Hàm phi Euler và định lí Euler',
    12: 'Định lí số dư Trung Hoa', 13: 'Tổ hợp và hệ số nhị thức', 14: 'Nguyên lí bù trừ',
    15: 'Dãy truy hồi và lũy thừa ma trận', 16: 'Kĩ thuật chia khối ⌊n / i⌋', 17: 'Số nguyên lớn',
    18: 'Hệ cơ số và biểu diễn nhị phân', 19: 'Tổng tiền tố và số dư', 20: 'Điểm nguyên và hình học số nguyên',
}

CHAPTERS = [
    (1, 'CHIA HẾT VÀ ƯỚC SỐ', [1, 2, 3, 4]),
    (2, 'SỐ NGUYÊN TỐ', [5, 6, 7, 8]),
    (3, 'SỐ HỌC ĐỒNG DƯ', [9, 10, 11, 12]),
    (4, 'TỔ HỢP VÀ ĐẾM', [13, 14, 15, 16]),
    (5, 'KĨ THUẬT SỐ HỌC TRONG LẬP TRÌNH', [17, 18, 19, 20]),
]

# pid: (tên, tệp, mức độ, TL, ML)
PROBLEMS = {
    '1.1': ('NGÀY TRONG TUẦN', 'NGAYTHU', 1, 1, 256),
    '1.2': ('CHỮ SỐ CUỐI', 'CHUSOCUOI', 2, 1, 256),
    '1.3': ('VIẾT LIỀN', 'VIETLIEN', 3, 1, 64),
    '2.1': ('XẾP HÀNG', 'XEPHANG', 1, 1, 256),
    '2.2': ('ƯỚC TĂNG DẦN', 'UOCTANG', 2, 1, 256),
    '2.3': ('SỐ BẠN BÈ', 'BANBE', 3, 2, 64),
    '3.1': ('CẮT GẠCH', 'CATGACH', 1, 1, 256),
    '3.2': ('BỎ MỘT SỐ', 'BOMOTSO', 2, 1, 256),
    '3.3': ('ĐÈN NHÁY', 'DENNHAY', 3, 1, 256),
    '4.1': ('ĐONG NƯỚC', 'DONGNUOC', 1, 1, 256),
    '4.2': ('MUA HÀNG', 'MUAHANG', 2, 1, 256),
    '4.3': ('ĐỒNG HỒ HỎNG', 'DONGHO', 3, 1, 256),
    '5.1': ('NGUYÊN TỐ GẦN NHẤT', 'NTGANNHAT', 1, 1, 256),
    '5.2': ('TỔNG HAI SỐ NGUYÊN TỐ', 'GOLDBACH', 2, 1, 256),
    '5.3': ('NGUYÊN TỐ 64 BIT', 'NT64', 3, 2, 256),
    '6.1': ('ĐẾM SỐ NGUYÊN TỐ', 'DEMNGUYENTO', 1, 1, 256),
    '6.2': ('SỐ NGUYÊN TỐ SINH ĐÔI', 'SINHDOI', 2, 2, 256),
    '6.3': ('SỐ CÓ ĐÚNG BA ƯỚC', 'BAUOC', 3, 1, 256),
    '7.1': ('SỐ ƯỚC', 'SOUOC', 1, 2, 256),
    '7.2': ('CHỮ SỐ 0 CỦA GIAI THỪA', 'CHUSO0', 2, 1, 256),
    '7.3': ('BCNN CỦA DÃY', 'BCNNDAY', 3, 1, 256),
    '8.1': ('NGUYÊN TỐ TRÊN ĐOẠN', 'NTDOAN', 1, 1, 256),
    '8.2': ('KHOẢNG CÁCH LỚN NHẤT', 'KHOANGCACH', 2, 1, 256),
    '8.3': ('SỐ ƯỚC TRÊN ĐOẠN', 'UOCDOAN', 3, 1, 256),
    '9.1': ('LŨY THỪA', 'LUYTHUAQ', 1, 1, 256),
    '9.2': ('SỐ MŨ KHỔNG LỒ', 'SOMULON', 2, 1, 256),
    '9.3': ('TỔNG LŨY THỪA', 'TONGLT', 3, 1, 256),
    '10.1': ('XÁC SUẤT', 'XACSUAT', 1, 1, 256),
    '10.2': ('NGHỊCH ĐẢO DÃY', 'NGHICHDAO', 2, 1, 256),
    '10.3': ('PHƯƠNG TRÌNH ĐỒNG DƯ', 'PTDONGDU', 3, 1, 256),
    '11.1': ('PHI', 'PHI', 1, 1, 256),
    '11.2': ('PHÂN SỐ TỐI GIẢN', 'PHANSO', 2, 1, 256),
    '11.3': ('THÁP LŨY THỪA', 'THAPLT', 3, 1, 256),
    '12.1': ('ĐIỂM BINH', 'DIEMBINH', 1, 1, 256),
    '12.2': ('HAI NGỌN ĐÈN', 'HAIDEN', 2, 1, 256),
    '12.3': ('LỊCH CAN CHI', 'CANCHI', 3, 1, 256),
    '13.1': ('CHIA KẸO', 'CHIAKEO', 1, 1, 256),
    '13.2': ('ĐƯỜNG ĐI TRÊN LƯỚI', 'DUONGLUOI', 2, 1, 256),
    '13.3': ('TỔ HỢP KHỔNG LỒ', 'TOHOPLON', 3, 1, 256),
    '14.1': ('BỘI SỐ', 'BOISO', 1, 1, 256),
    '14.2': ('NGUYÊN TỐ CÙNG NHAU', 'NTCN', 2, 1, 256),
    '14.3': ('TẶNG QUÀ', 'TANGQUA', 3, 1, 256),
    '15.1': ('LÁT GẠCH', 'LATGACH', 1, 1, 256),
    '15.2': ('TRIBONACCI', 'TRIBO', 2, 1, 256),
    '15.3': ('ĐƯỜNG ĐI ĐỘ DÀI K', 'DUONGK', 3, 1, 256),
    '16.1': ('TỔNG ƯỚC', 'TONGSIGMA', 1, 1, 256),
    '16.2': ('TỔNG DƯ', 'TONGDU', 2, 1, 256),
    '16.3': ('HAI THƯƠNG', 'HAITHUONG', 3, 1, 256),
    '17.1': ('TỔNG LỚN', 'TONGLON', 1, 1, 256),
    '17.2': ('LŨY THỪA ĐẦY ĐỦ', 'LUYTHUALON', 2, 1, 256),
    '17.3': ('TÍCH LỚN', 'TICHLON', 3, 1, 256),
    '18.1': ('ĐỔI CƠ SỐ', 'DOICOSO', 1, 1, 256),
    '18.2': ('BIT TRONG ĐOẠN', 'BITDOAN', 2, 1, 256),
    '18.3': ('SỐ CÓ K BIT 1', 'KBIT', 3, 1, 256),
    '19.1': ('TỔNG BẰNG KHÔNG', 'TONG0', 1, 1, 256),
    '19.2': ('ĐOẠN DÀI NHẤT', 'DOANDAI', 2, 1, 256),
    '19.3': ('HÌNH CHỮ NHẬT CHIA HẾT', 'HCNCHIAHET', 3, 1, 256),
    '20.1': ('TRỒNG CÂY', 'TRONGCAY', 1, 1, 256),
    '20.2': ('ĐA GIÁC LƯỚI', 'DAGIAC', 2, 1, 256),
    '20.3': ('TAM GIÁC NGUYÊN', 'TAMGIAC', 3, 1, 256),
}


def link(pid):
    l = int(pid.split('.')[0])
    return 'Tập 1, Bài %d (%s) · Tập 2, bài tập %s' % (l, LESSONS[l], pid)

SKILLS = {'1.1': 'Lấy số dư không âm; tránh vòng lặp đếm từng ngày.', '1.2': 'Tìm chu kì của dãy số dư; xử lí số cho dưới dạng xâu.', '1.3': 'Mở rộng sơ đồ Horner cho những "chữ số" có độ dài thay đổi; tiết kiệm bộ nhớ.', '2.1': 'Duyệt ước tới √n; xử lí trường hợp suy biến n = 1 và số nguyên tố.', '2.2': 'Ghép hai dãy ước nhỏ, ước lớn thành dãy tăng; trả lời nhanh nhiều truy vấn trên dãy đã sắp.', '2.3': 'Đổi chiều câu hỏi "k có những ước nào" thành "d là ước của những số nào"; tiết kiệm bộ nhớ.', '3.1': 'Dùng gcd cho số tới 10¹⁸; nhận ra đáp số vượt long long và in số __int128.', '3.2': 'Tính trước tiền tố, hậu tố để "bỏ một phần tử" trong O(1).', '3.3': 'Khai thác "chỉ có ít giá trị khác nhau" để trả lời truy vấn trên đoạn; BCNN không tràn số.', '4.1': 'Áp dụng Bézout cho nhiều số; trả lời truy vấn trong O(1).', '4.2': 'Tìm nghiệm có x nhỏ nhất không âm rồi đếm số nghiệm trong một đoạn; tránh tràn số.', '4.3': 'Đưa bài toán về phương trình đồng dư; xử lí trường hợp suy biến và tràn số với mô-đun tới 10¹⁸.', '5.1': 'Cài đặt đúng và nhanh phép kiểm tra nguyên tố; duyệt "loang" ra hai phía.', '5.2': 'Dùng tính chẵn lẻ để thu hẹp tìm kiếm; sắp xếp các phép kiểm tra rẻ trước, đắt sau.', '5.3': 'Cài đặt Miller–Rabin không tràn số cho mọi số không dấu 64 bit.', '6.1': 'Sàng một lần, trả lời hai loại truy vấn bằng hai mảng.', '6.2': 'Thiết kế mảng tiền tố cho một "cặp" thay vì một số; xử lí biên của đoạn.', '6.3': 'Nhận dạng số có đúng ba ước; chỉ cần thử chia tới căn bậc ba thay vì căn bậc hai.', '7.1': 'Dùng sàng spf cho rất nhiều truy vấn; tính đồng thời số ước và tổng ước.', '7.2': 'Đưa bài toán "chữ số 0 tận cùng" trong cơ số bất kì về số mũ của từng ước nguyên tố.', '7.3': 'Làm việc với BCNN khổng lồ qua bảng số mũ; đếm phần tử "không thể thay thế".', '8.1': 'Sàng nhỏ một lần, dùng lại cho nhiều cửa sổ; tính tổng không tràn số.', '8.2': 'Duyệt các số nguyên tố liên tiếp trong cửa sổ; xử lí hòa và trường hợp suy biến.', '8.3': 'Phân tích cùng lúc mọi số trong cửa sổ; nhận ra phần còn lại là số nguyên tố.', '9.1': 'Cài đặt lũy thừa nhanh chuẩn; lấy dư cơ số trước khi nhân.', '9.2': 'Áp dụng sơ đồ Horner cho số mũ; không lạm dụng định lí Fermat khi mô-đun là hợp số.', '9.3': 'Chia để trị trên số mũ khi không chia được theo mô-đun; chống tràn số 10¹⁸ · 10¹⁸.', '10.1': 'Biểu diễn phân số theo mô-đun 10⁹ + 7; trừ theo mô-đun không ra số âm.', '10.2': 'Công thức truy hồi cho nghịch đảo; tiết kiệm thời gian và bộ nhớ với n = 10⁷.', '10.3': 'Giải a · x ≡ c (mod m) tổng quát; đếm nghiệm trên đoạn với số âm và số cỡ 10¹⁸.', '11.1': 'Nhận ra hàm φ trong một câu chuyện; cài đặt O(√n) không sai ước lớn còn lại.', '11.2': 'Sàng một hàm số học tới 10⁷; trả lời truy vấn đoạn bằng tổng tiền tố.', '11.3': 'Rút gọn số mũ với mô-đun bất kì; biết khi nào được rút gọn bằng cách chặn trên giá trị thật của tháp.', '12.1': 'Cài đặt gộp từng cặp phương trình bằng Euclid mở rộng; tìm nghiệm nhỏ nhất không nhỏ hơn một ngưỡng.', '12.2': 'Gộp hai phương trình tổng quát; xử lí điều kiện "đã bắt đầu" ngoài đồng dư.', '12.3': 'Gộp nhiều phương trình khi lcm vượt xa 10¹⁸; tính lcm theo mô-đun qua phân tích thừa số.', '13.1': 'Đưa bài đếm về một số C(a, b); chuẩn bị bảng giai thừa đủ lớn.', '13.2': 'Tách đường đi qua một điểm thành hai đoạn; bù trừ khi có hai điểm cấm.', '13.3': 'Tính C(n, k) theo mô-đun không nguyên tố: tách theo từng ước nguyên tố rồi ghép lại.', '14.1': 'Đổi điều kiện "hoặc", "nhưng không" thành công thức bù trừ; chống tràn số.', '14.2': 'Phân tích nhiều số tới 10¹² đủ nhanh nhờ danh sách số nguyên tố sàng sẵn.', '14.3': 'Phối hợp quy tắc nhân, truy hồi D(n) và tổ hợp với n vượt mô-đun.', '15.1': 'Lập hệ thức truy hồi bằng cách nhìn vào phần cuối của hình.', '15.2': 'Ngắt dãy truy hồi tại các vị trí đặc biệt: lũy thừa ma trận theo từng đoạn.', '15.3': 'Tính sẵn các lũy thừa A¹, A², A⁴, ...; nhân vectơ với ma trận thay cho ma trận với ma trận.', '16.1': 'Cộng theo khối với trọng số là cấp số cộng; chống tràn bằng __int128.', '16.2': 'Chia khối trên đoạn [1, min(n, k)]; xử lí riêng phần i > n.', '16.3': 'Khai triển thành các tổng Σ 1, Σ i, Σ i² trên mỗi khối chung của hai thương.', '17.1': 'Cộng, trừ số lớn; xử lí dấu, số 0 thừa và kết quả bằng 0.', '17.2': 'Nhân số lớn với số nhỏ trong cơ số 10⁹; in đúng định dạng.', '17.3': 'Nhân hai số lớn O(L₁ · L₂); chọn cơ số vừa nhanh vừa không tràn.', '18.1': 'Đổi qua lại giữa hai cơ số bất kì; xử lí chữ cái, số 0 và chữ số 0 thừa.', '18.2': 'Trả lời truy vấn đoạn bằng hiệu hai "tiền tố"; xử lí đáp số vượt 2⁶⁴.', '18.3': 'Đếm số có tính chất về chữ số không vượt quá n; tìm số thứ m theo thứ tự.', '19.1': 'Đổi "đếm đoạn" thành "đếm cặp"; gom nhóm bằng sắp xếp.', '19.2': 'Tối ưu độ dài đoạn bằng vị trí xuất hiện đầu tiên; số dư không âm; chọn đáp án theo luật phụ.', '19.3': 'Hạ bài toán 2 chiều xuống 1 chiều; xóa mảng đếm thông minh.', '20.1': 'Áp dụng công thức gcd cho từng đoạn; không đếm trùng đỉnh chung.', '20.2': 'Kết hợp diện tích và số điểm trên biên để đếm điểm bên trong.', '20.3': 'Ước lượng mọi đại lượng trung gian; tính toán và in số __int128.'}
