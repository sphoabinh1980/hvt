"""Bìa, lời nói đầu, cấu trúc lời giải, mục lục, trang mở chương, phụ lục."""
import os, json
from render import inline, para, table, cellxml, rpr, t, NOB, W, spacer
import book

ROOT = os.path.dirname(os.path.abspath(__file__))


def cover(D):
    D.raw('<w:p><w:pPr><w:spacing w:after="360" w:line="276" w:lineRule="auto"/><w:jc w:val="right"/></w:pPr><w:r>%s%s</w:r></w:p>'
          % (rpr(b=True, i=True, color='595959', sz=22), t('Tổng hợp và biên soạn: Lê Thành Nam')))
    def cp(text, color, sz, after, b=True, i=False, font='A'):
        return '<w:p><w:pPr><w:spacing w:after="%d" w:line="276" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr><w:r>%s%s</w:r></w:p>' % (
            after, rpr(b=b, i=i, color=color, sz=sz, font=font), t(text))
    top = cp('TÀI LIỆU BỒI DƯỠNG HỌC SINH GIỎI TIN HỌC', 'FFD966', 22, 200) + cp('SỐ HỌC', 'FFFFFF', 64, 80) + \
        cp('Từ cơ bản đến nâng cao', 'FFFFFF', 30, 0, b=False, i=True, font=None)
    band = cp('TẬP 3  ·  HƯỚNG DẪN GIẢI', 'FFFFFF', 28, 0)
    D.raw(table([W], [('', [cellxml(W, top, fill='1F3864', borders=NOB, mar=(420, 300, 420, 300))]),
                      ('', [cellxml(W, band, fill='C0504D', borders=NOB, mar=(160, 300, 160, 300))])], center=False, borders=False))
    D.raw(spacer(240, 276))
    D.fig(os.path.join(ROOT, 'assets', 'cover.png'), None, 15.2)
    for num, title, _ in book.CHAPTERS:
        D.raw('<w:p><w:pPr><w:spacing w:after="70" w:line="276" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr><w:r>%s%s</w:r></w:p>'
              % (rpr(b=True, color='1F3864', sz=22, font='A'), t('Chương %d. %s' % (num, title))))
    D.raw('<w:p><w:pPr><w:spacing w:before="260" w:after="0" w:line="276" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr><w:r>%s%s</w:r></w:p>'
          % (rpr(i=True, color='595959', sz=20), t('60 lời giải · từ cách ngây thơ đến cách tối ưu · chương trình đã chấm thật trên bộ test')))
    D.section_break(D.short, title_pg=True)


def intro(D):
    D.big_title('LỜI NÓI ĐẦU')
    for x in [
        'Tập 3 trình bày lời giải cho cả **60 bài tập** của Tập 2. Mỗi lời giải không chỉ đưa ra một chương trình đạt 100 điểm, '
        'mà đi lại đúng con đường một học sinh giỏi suy nghĩ trong phòng thi: bắt đầu từ cách ngây thơ, **đếm số phép tính** để thấy bế tắc, '
        'rồi phá bế tắc bằng một quan sát số học hay một công cụ phù hợp của Tập 1.',
        'Số học trong lập trình có một đặc điểm riêng: ý tưởng thường gói gọn trong một công thức, nhưng khoảng cách giữa "đúng ý tưởng" và '
        '"đúng 100 điểm" lại nằm ở những chi tiết rất nhỏ: một phép nhân tràn số, một số dư âm, một trường hợp n = 1, một mô-đun không nguyên tố. '
        'Vì vậy, ngoài lời giải ngây thơ và lời giải tối ưu, nhiều bài còn có một lời giải **"trông như đúng"**: chương trình mà rất nhiều bạn sẽ nộp, '
        'qua được ví dụ nhưng mất điểm vì một cái bẫy. Em sẽ thấy rõ cái bẫy ấy làm mất bao nhiêu điểm.',
        'Mọi chương trình trong sách đều đã được kiểm tra hai lần: đối chiếu với lời giải vét cạn (hoặc phép tính số lớn chính xác của Python) '
        'trên hàng trăm bộ dữ liệu nhỏ ngẫu nhiên, và chấm trên bộ test theo đúng các subtask của Tập 2, với giới hạn thời gian và bộ nhớ của từng bài. '
        'Các con số trong **bảng điểm** cuối mỗi bài là điểm thực tế mà từng chương trình nhận được, không phải ước lượng.']:
        D.p(x)
    D.raw(para('<w:r>%s%s</w:r>' % (rpr(i=True), t('Lê Thành Nam')), after=100, jc='right'))
    D.pagebreak()
    D.big_title('CẤU TRÚC MỘT LỜI GIẢI')
    D.table(['Mục', 'Nội dung'], [
        ['**1. Hiểu bài toán**', 'Diễn đạt lại đề bằng ngôn ngữ số học, thường kèm một hình vẽ; nhận ra công cụ quen thuộc ẩn sau câu chuyện.'],
        ['**2. Cách ngây thơ**', 'Sơ đồ khối, chương trình và độ phức tạp của cách làm đầu tiên ai cũng nghĩ ra.'],
        ['**3. Bế tắc**', 'Cách hiện tại ăn được subtask nào, vì sao không đi xa hơn; đôi khi kèm một lời giải trung gian hoặc một lời giải sai "trông như đúng".'],
        ['**4. Phá bế tắc**', 'Quan sát then chốt, công thức, hình vẽ chạy tay trên ví dụ, lập luận vì sao đúng.'],
        ['**5. Cách tối ưu**', 'Sơ đồ khối, chương trình hoàn chỉnh và độ phức tạp.'],
        ['**6. Bẫy thường gặp**', 'Những lỗi làm mất điểm hay gặp nhất: tràn số, số dư âm, trường hợp biên...'],
        ['**7. Bảng điểm**', 'Điểm thực tế của từng cách làm trên bộ test. Dòng tô xanh là lời giải mẫu.'],
    ], widths=[1.6, 6.4], align=['left', 'left'], sz=21)
    D.p('Các khung màu trong sách:', after=60)
    D.table(['Khung', 'Ý nghĩa'], [
        ['{{ĐIỂM BẾ TẮC}}', 'Chỉ ra chính xác chỗ cách làm hiện tại "kẹt": phép tính nào lặp lại, đại lượng nào quá lớn.'],
        ['[[VÌ SAO ĐÚNG? / CHỨNG MINH]]', 'Lập luận ngắn gọn cho một công thức hay một nhận xét then chốt.'],
        ['[[MỞ RỘNG]]', 'Một cách làm khác, một bài toán tổng quát hơn, hoặc một mẹo cài đặt đáng nhớ.'],
    ], widths=[2.4, 5.6], align=['left', 'left'], sz=21)
    D.box('blue', 'LỜI KHUYÊN', [
        'Đừng đọc lời giải như đọc truyện. Sau mục 3, hãy gấp sách và tự tìm cách phá bế tắc trong ít nhất mười lăm phút. '
        'Sau mục 5, hãy tự viết lại chương trình mà không nhìn sách, rồi tự sinh test để đối chiếu với cách ngây thơ của chính em (Tập 2, Phụ lục B).',
        'Mỗi chương trình đọc từ tệp .INP nếu tệp tồn tại, ngược lại đọc từ bàn phím; vì vậy em có thể chạy thử trực tiếp hoặc đối chiếu bằng ống dẫn (<, >).'])
    D.pagebreak()
    D.big_title('MỤC LỤC', toc=False)
    D.raw('<!--TOC-->')


def chapter(D, num, title, lessons):
    intros = {
        1: 'Mười hai lời giải đầu tiên xoay quanh những kĩ năng nền móng: lấy số dư (kể cả số âm và số rất lớn), duyệt ước tới √n, '
           'thuật toán Euclid và Euclid mở rộng. Ý tưởng không khó; cái khó là đếm đúng số phép tính để biết cách ngây thơ dừng ở đâu, '
           'và giữ cho mọi đại lượng trung gian không tràn số.',
        2: 'Mười hai lời giải của chương này luyện bốn công cụ làm việc với số nguyên tố: thử chia tới √n, Miller–Rabin, sàng Eratosthenes '
           '(và sàng ước nguyên tố nhỏ nhất), sàng trên đoạn. Mỗi bài đều có một câu hỏi chung: có bao nhiêu số cần xét, mỗi số lớn tới đâu? '
           'Trả lời được câu hỏi ấy là chọn được công cụ.',
        3: 'Mười hai lời giải của chương này đều in kết quả "theo mô-đun". Lũy thừa với số mũ khổng lồ, chia theo mô-đun, rút gọn số mũ bằng φ, '
           'ghép số dư bằng định lí Trung Hoa. Điều phân biệt lời giải đúng với lời giải gần đúng là các chi tiết: mô-đun có nguyên tố không, '
           'có ước chung không, tích hai số dư có tràn không.',
        4: 'Mười hai lời giải của chương này biến câu hỏi "có bao nhiêu" thành một công thức tổ hợp, một phép bù trừ, một phép nhân ma trận '
           'hay một tổng chia khối. Cách ngây thơ luôn là liệt kê (hoặc quy hoạch động) rồi đếm; cách tối ưu là đếm mà không liệt kê.',
        5: 'Chương cuối là những "mẹo nghề" khi đem số học vào máy tính: số nguyên lớn, đổi cơ số và đếm bit theo cột, tổng tiền tố theo số dư, '
           'đếm điểm nguyên bằng ƯCLN và định lí Pick. Kẻ thù lớn nhất vẫn là tràn số: nhiều đáp số vượt 2^{64}, nhiều phép tính trung gian vượt long long.',
    }
    D.chapter_title(num, title, intros[num])
    rows = []
    for l in lessons:
        for k in (1, 2, 3):
            pid = '%d.%d' % (l, k)
            name, f, lv, _, _ = book.PROBLEMS[pid]
            rows.append(['**%s**' % pid, name, {1: '★ CƠ BẢN', 2: '★★ TRUNG BÌNH', 3: '★★★ NÂNG CAO'}[lv], book.SKILLS[pid]])
    D.table(['Bài', 'Tên bài', 'Mức độ', 'Trọng tâm của lời giải'], rows, widths=[0.7, 2.3, 1.6, 5.2], align=['center', 'left', 'center', 'left'], sz=19)


def appendix(D, hdr_prev):
    D.section_break(hdr_prev)
    D.big_title('PHỤ LỤC A. BẢNG TỔNG HỢP ĐIỂM')
    D.p('Bảng dưới đây tóm tắt điểm (trên thang 100) của cách ngây thơ đầu tiên và của lời giải mẫu ở cả 60 bài, đo trên cùng bộ test. '
        'Khoảng cách giữa hai cột chính là "giá trị" của quan sát then chốt trong từng bài.')
    rows = []
    for pid in book.PROBLEMS:
        sp = os.path.join(ROOT, 'problems', pid, 'scores.json')
        if not os.path.exists(sp):
            continue
        sc = json.load(open(sp))
        meta = {}
        exec(open(os.path.join(ROOT, 'problems', pid, 'meta.py')).read(), meta)
        first = meta['SOLS'][0][0]
        ref = meta['REF']
        rows.append([pid, book.PROBLEMS[pid][0], sc[first]['title'], str(sum(sc[first]['pts'])), str(sum(sc[ref]['pts']))])
    D.table(['Bài', 'Tên bài', 'Cách ngây thơ', 'Điểm', 'Lời giải mẫu'], rows, widths=[0.7, 2.6, 4.2, 0.8, 1.2], align=['center', 'left', 'left', 'center', 'center'], sz=18, bold_cols=(4,))
    D.pagebreak()
    import appendix_b
    appendix_b.build(D)
