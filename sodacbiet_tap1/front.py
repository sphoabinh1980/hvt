"""Bìa, lời nói đầu, cách học, mục lục, trang mở chương, phụ lục."""
import os
from render import inline, para, table, cellxml, rpr, t, NOB, W, spacer
from lt import KB
import book

ROOT = os.path.dirname(os.path.abspath(__file__))


def cover(D):
    D.raw('<w:p><w:pPr><w:spacing w:after="360" w:line="276" w:lineRule="auto"/><w:jc w:val="right"/></w:pPr><w:r>%s%s</w:r></w:p>'
          % (rpr(b=True, i=True, color='595959', sz=22), t('Tổng hợp và biên soạn: Lê Thành Nam')))

    def cp(text, color, sz, after, b=True, i=False, font='A'):
        return '<w:p><w:pPr><w:spacing w:after="%d" w:line="276" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr><w:r>%s%s</w:r></w:p>' % (
            after, rpr(b=b, i=i, color=color, sz=sz, font=font), t(text))
    top = (cp('TÀI LIỆU BỒI DƯỠNG HỌC SINH GIỎI TIN HỌC', 'FFD966', 22, 200) + cp('SỐ ĐẶC BIỆT', 'FFFFFF', 60, 40) +
           cp('VÀ CẤU TRÚC CHỮ SỐ', 'FFFFFF', 36, 100) + cp('Từ cơ bản đến nâng cao', 'FFFFFF', 30, 0, b=False, i=True, font=None))
    band = cp('TẬP 1  ·  LÝ THUYẾT', 'FFFFFF', 28, 0)
    D.raw(table([W], [('', [cellxml(W, top, fill='1F3864', borders=NOB, mar=(380, 300, 380, 300))]),
                      ('', [cellxml(W, band, fill='C0504D', borders=NOB, mar=(160, 300, 160, 300))])], center=False, borders=False))
    D.raw(spacer(200, 276))
    D.fig(os.path.join(ROOT, 'assets', 'cover.png'), None, 15.2)
    for num, title, _ in book.CHAPTERS:
        D.raw('<w:p><w:pPr><w:spacing w:after="60" w:line="276" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr><w:r>%s%s</w:r></w:p>'
              % (rpr(b=True, color='1F3864', sz=22, font='A'), t('Chương %d. %s' % (num, title))))
    D.section_break(D.short, title_pg=True)


def legend_table(D, rows):
    """Bảng khung màu: ô nhãn có viền trái đậm và nền như khung thật."""
    trs = []
    for lab, mean in rows:
        col, fill = KB[lab]
        brd = NOB.replace('<w:left w:val="none" w:sz="0" w:space="0" w:color="FFFFFF"/>', '<w:left w:val="single" w:sz="24" w:space="0" w:color="%s"/>' % col)
        c1 = cellxml(2200, '<w:p><w:pPr><w:spacing w:after="0"/></w:pPr><w:r>%s%s</w:r></w:p>' % (rpr(b=True, color=col, sz=18, font='A'), t(lab)), fill=fill or 'FFFFFF', borders=brd)
        c2 = cellxml(6418, para(inline(mean), after=0, line=252))
        trs.append(('<w:trPr><w:cantSplit/><w:jc w:val="center"/></w:trPr>', [c1, c2]))
    D.raw(table([2200, 6418], trs, borders=False))
    D.raw(spacer(100, 200))


def intro(D):
    D.big_title('LỜI NÓI ĐẦU')
    for x in [
        'Năm 1949, nhà toán học Ấn Độ D. R. Kaprekar phát hiện một điều kì lạ: lấy một số có bốn chữ số không giống hệt nhau, sắp các chữ số giảm dần rồi tăng dần, lấy hiệu hai số vừa sắp; '
        'lặp lại vài lần, em **luôn** về đúng một con số: 6174. Hơn bảy mươi năm sau, những "con số có tính cách" như thế (6174, 153, 142857, 28...) vẫn xuất hiện đều đặn trong các đề thi học sinh giỏi Tin học.',
        'Đề thi thích những con số đặc biệt vì chúng buộc người giải phải hiểu thật sự **cấu trúc chữ số** của một số: một số được ghép từ các chữ số theo giá trị vị trí, chữ số tuân theo những chu kì, '
        'và rất nhiều câu hỏi "có bao nhiêu số ..." hay "số thứ k là số nào?" có thể trả lời mà không cần duyệt qua từng số. Khoảng cách giữa "duyệt từng số" và "suy nghĩ theo chữ số" thường là khoảng cách giữa 30 điểm và 100 điểm.',
        'Cuốn sách này được viết theo đúng con đường của bộ **Số học: Từ cơ bản đến nâng cao**. Mỗi bài học đặt em trước một bài toán cụ thể, viết chương trình ngây thơ (có sơ đồ khối và code đầy đủ), '
        '**đếm số phép tính** để thấy bế tắc, rồi dẫn từng bước tới ý tưởng tốt, kèm chạy tay bằng bảng, hình vẽ và chứng minh vì sao nó đúng.',
        'Bộ tài liệu gồm ba tập đi cùng nhau:']:
        D.p(x)
    D.bullets(['**Tập 1: Lý thuyết** (cuốn sách này) gồm 20 bài học trong 5 chương: Cấu trúc chữ số; Chữ số và chia hết; Số đặc biệt theo chữ số; Biến đổi và đếm theo chữ số; Số đặc biệt theo ước số và hình dạng.',
               '**Tập 2: Bài tập** gồm các bài tập theo từng bài học, ở ba mức độ, có ràng buộc theo subtask như đề thi thật. Tên các bài tập được giới thiệu ở mục __Luyện tập__ cuối mỗi bài học.',
               '**Tập 3: Hướng dẫn giải** phân tích từng bài tập từ cách ngây thơ đến cách tối ưu, kèm chương trình hoàn chỉnh và bảng điểm theo thuật toán.'])
    D.p('Chương trình được viết bằng C++ theo chuẩn C++14, đọc và ghi tệp theo kiểu "có tệp thì đọc tệp" để dùng được cả với phần mềm chấm Themis lẫn các trang chấm trực tuyến. '
        'Mọi chương trình trong sách đều đã được biên dịch, chạy thử và đối chiếu với chương trình vét cạn trên hàng trăm bộ dữ liệu ngẫu nhiên; '
        'mọi con số trong các bảng chạy tay đều do chính chương trình sinh ra; thời gian chạy được đo thật trên máy tính.')
    D.p('Chúc các em học tập say mê và đạt kết quả cao!')
    D.raw(para('<w:r>%s%s</w:r>' % (rpr(i=True), t('Lê Thành Nam')), after=100, jc='right'))
    D.pagebreak()
    D.big_title('CÁCH HỌC VỚI TÀI LIỆU NÀY')
    D.p('Mỗi bài học đi theo cùng một con đường, giống như cách một người giỏi suy nghĩ khi gặp bài mới:')
    D.table(['Phần', 'Nội dung'], [
        ['**Khởi động**', 'Một câu chuyện, một câu đố gần gũi để em bắt đầu nghĩ.'],
        ['**Kiến thức nền**', 'Định nghĩa, định lí, hình vẽ trực quan và ví dụ tính tay.'],
        ['**Bài toán**', 'Đề bài cụ thể, có ví dụ được sinh bằng chính chương trình trong sách.'],
        ['**Ý tưởng ngây thơ**', 'Cách làm đầu tiên ai cũng nghĩ ra, kèm sơ đồ khối, chương trình đầy đủ và phần đếm số phép tính.'],
        ['**Bế tắc**', 'Chỉ ra chính xác vì sao cách ngây thơ chậm (hoặc sai, hoặc tràn số), và đặt câu hỏi dẫn tới ý tưởng mới.'],
        ['**Phá bế tắc**', 'Từng bước: ý tưởng, chạy tay bằng hình và bảng, chứng minh, chương trình.'],
        ['**Mở rộng**', 'Các biến thể và ứng dụng thường gặp trong đề thi.'],
        ['**Bẫy thường gặp**', 'Những lỗi đã làm mất điểm của nhiều thế hệ học sinh.'],
        ['**Ghi nhớ**', 'Tóm tắt những điều cốt lõi nhất.'],
        ['**Luyện tập**', 'Giới thiệu các bài tập tương ứng ở Tập 2 và vài câu tự kiểm tra có đáp số.']],
        widths=[1.8, 6.2], align=['left', 'left'], sz=20)
    D.p('Các khung màu trong sách có ý nghĩa cố định:', after=60)
    legend_table(D, [('KHỞI ĐỘNG', 'Câu hỏi mở đầu bài học.'), ('BÀI TOÁN', 'Đề bài chính thức.'), ('ĐỊNH NGHĨA', 'Khái niệm mới cần nắm chính xác.'),
                     ('ĐỊNH LÍ', 'Kết quả quan trọng, thường kèm chứng minh.'), ('THUẬT TOÁN', 'Các bước của thuật toán, viết bằng lời.'),
                     ('ĐẾM SỐ PHÉP TÍNH', 'Phân tích độ phức tạp và thời gian chạy đo thật.'), ('BẾ TẮC', 'Chỗ cách làm hiện tại không vượt qua được.'),
                     ('VÌ SAO ĐÚNG?', 'Lập luận chứng minh tính đúng đắn.'), ('HÃY HÌNH DUNG', 'Hình ảnh trực quan giúp nhớ lâu.'),
                     ('VÍ DỤ', 'Một ví dụ tính tay ngắn.'), ('LƯU Ý', 'Chi tiết nhỏ nhưng dễ sai.'), ('BẪY THƯỜNG GẶP', 'Các lỗi hay gặp.'), ('GHI NHỚ', 'Tóm tắt cuối bài.')])
    D.mini('Quy ước màu trong hình vẽ')
    D.table(['Màu', 'Ý nghĩa'], [
        ['Ô vàng viền đỏ', 'Giá trị đang xét ở bước đó, hoặc kết quả cuối cùng.'], ['Ô xanh dương', 'Giá trị đã tính xong.'],
        ['Ô cam nhạt', 'Dữ liệu vào (chữ số, số hạng...).'], ['Ô xám', 'Giá trị khởi tạo, hoặc số đã bị loại.'], ['Chữ đỏ', 'Kết luận, đáp số, hoặc chỗ cần chú ý.']],
        widths=[2.2, 5.8], align=['left', 'left'], sz=20, fills=[['FFE699', None], ['DEEBF7', None], ['FBE5D6', None], ['EDEDED', None], [None, None]])
    D.mini('Kí hiệu dùng trong sách')
    D.table(['Kí hiệu', 'Ý nghĩa'], [
        ['(d_{k−1} ... d_{1} d_{0})_{b}', 'Số viết trong cơ số b bằng các chữ số d_{k−1}, ..., d_{0}; không ghi b nghĩa là cơ số 10.'],
        ['S(n)', 'Tổng các chữ số của n.'], ['rev(n)', 'Số đảo ngược của n (đọc các chữ số từ phải sang trái).'],
        ['len(n)', 'Số chữ số của n.'], ['a mod m', 'Số dư (không âm) của a khi chia cho m.'], ['⌊x⌋, ⌈x⌉', 'Phần nguyên dưới, phần nguyên trên.'],
        ['b | a', 'b chia hết a (a chia hết cho b).'], ['a ≡ b (mod m)', 'a và b đồng dư theo mô-đun m.'],
        ['d(n), σ(n)', 'Số ước và tổng các ước của n.'], ['C(n, k)', 'Số cách chọn k phần tử từ n phần tử.'],
        ['O(...)', 'Độ phức tạp thời gian. Máy tính làm khoảng 10^{8} phép tính đơn giản mỗi giây.']],
        widths=[2.4, 5.6], align=['left', 'left'], sz=20)
    D.kbox('LỜI KHUYÊN KHI HỌC', ['Hãy đọc với giấy và bút bên cạnh. Mỗi khi gặp một bảng chạy tay, hãy che bảng lại và tự tính trước. Mỗi khi gặp một "con số đặc biệt", hãy tự kiểm tra nó bằng tay '
                                    '(153 = 1³ + 5³ + 3³ thật không?). Và mỗi khi viết chương trình, hãy tự hỏi ba câu: **số lớn nhất có thể là bao nhiêu? có số 0, số âm không? cần duyệt bao nhiêu số?**'])
    D.pagebreak()
    D.big_title('MỤC LỤC', toc=False)
    D.raw('<!--TOC-->')


INTROS = {
    1: ['Một số tự nhiên không chỉ là một "giá trị", nó còn là một **dãy chữ số** xếp theo vị trí. Chương này dạy em đọc cấu trúc ấy: tách chữ số, đếm chữ số, tìm chữ số đầu và chữ số cuối, '
        'và trả lời những câu hỏi về chữ số của những số khổng lồ như 2^{10^{18}} hay 10^{6}! mà không bao giờ phải viết chúng ra.',
        'Hai ý tưởng xuyên suốt chương: **đếm theo cột** (mỗi vị trí chữ số lặp theo một chu kì) và **nhóm theo độ dài** (có 9 số một chữ số, 90 số hai chữ số, 900 số ba chữ số...).'],
    2: ['Từ tiểu học em đã biết một số chia hết cho 3 khi tổng các chữ số của nó chia hết cho 3. Chương này giải thích **vì sao**, và biến những dấu hiệu ấy thành công cụ lập trình: '
        'số dư của một đoạn chữ số bất kì trong O(1), căn số, bội số nhỏ nhất chỉ gồm chữ số 0 và 1, và chu kì của phân số thập phân 1/n.',
        'Chìa khóa của cả chương là một nhận xét đơn giản: **10^{k} mod m chỉ nhận hữu hạn giá trị**, nên mọi thứ liên quan đến chữ số theo mô-đun m đều tuần hoàn.'],
    3: ['153 = 1³ + 5³ + 3³. 6174 là điểm dừng của mọi số bốn chữ số. 76² = 5776 kết thúc bằng chính 76. Chương này giới thiệu các họ số được định nghĩa qua **chữ số của chính chúng**: '
        'số đối xứng, số tự luân, số hạnh phúc, số Kaprekar, số tự đồng cấu...',
        'Với mỗi họ số, câu hỏi lập trình là: **làm sao tìm hết chúng mà không duyệt mọi số?** Ba câu trả lời sẽ xuất hiện nhiều lần: sinh số từ nửa đầu, duyệt theo tập chữ số, và dựng nghiệm từng chữ số một.'],
    4: ['Chương này chuyển từ "số có tính chất gì" sang "biến đổi chữ số thế nào": sắp xếp lại chữ số, xóa bớt chữ số, ghép nhiều số thành một, và đếm các số ≤ n có một tính chất về chữ số.',
        'Hai kĩ thuật trung tâm là **tham lam trên chữ số** (chữ số bên trái quan trọng hơn mọi chữ số bên phải cộng lại) và **quy hoạch động chữ số**, công cụ mạnh nhất để trả lời "có bao nhiêu số x ≤ 10^{18} thỏa mãn ...".'],
    5: ['Chương cuối giới thiệu các số đặc biệt định nghĩa qua **ước số** và **hình dạng**: số nguyên tố đối xứng, số hoàn hảo, số thân thiết, số chính phương, tổng hai bình phương, số tam giác, số Fibonacci...',
        'Đây là chỗ cấu trúc chữ số gặp số học: sàng, phân tích thừa số, căn bậc hai nguyên. Và lại một lần nữa, ý tưởng mạnh nhất thường là **sinh trực tiếp** các số cần tìm thay vì kiểm tra từng số.'],
}


def chapter(D, num, title, lessons):
    D.chapter_page(num, title, INTROS[num], [(n, '%s: %s' % book.LESSONS[n]) for n in lessons])


def appendix(D, hdr_prev):
    D.section_break(hdr_prev)
    import appendix as A
    A.build(D)
