"""Các khối riêng của sách lý thuyết (theo đúng mẫu Số học · Tập 1)."""
from render import Doc, inline, para, cellxml, table, rpr, t, NOB, W, spacer, NAVY

# nhãn khung -> (màu viền trái, màu nền)
KB = {
    'KHỞI ĐỘNG': ('C55A11', 'FDF0E6'), 'BÀI TOÁN': (NAVY, None), 'ĐỊNH NGHĨA': (NAVY, 'EEF3FA'),
    'ĐỊNH LÍ': ('6A4C93', 'F1ECF8'), 'THUẬT TOÁN': (NAVY, 'F3F6FA'), 'ĐẾM SỐ PHÉP TÍNH': ('1B7F79', 'E6F4F3'),
    'BẾ TẮC': ('C0504D', 'FBEAEA'), 'VÌ SAO ĐÚNG?': ('6A4C93', 'F1ECF8'), 'HÃY HÌNH DUNG': ('B26A00', 'FFF6DB'),
    'VÍ DỤ': ('1B7F79', 'E6F4F3'), 'LƯU Ý': ('C55A11', 'FDF0E6'), 'BẪY THƯỜNG GẶP': ('C0504D', 'FBEAEA'),
    'GHI NHỚ': ('2E7D32', 'EAF5E6'), 'TRONG CHƯƠNG NÀY': (NAVY, 'F3F6FA'), 'LỜI KHUYÊN': ('2E7D32', 'EAF5E6'),
}


def kind_of(title):
    for k in KB:
        if title.startswith(k):
            return k
    if title.startswith('CHỨNG MINH') or title.startswith('VÌ SAO'):
        return 'VÌ SAO ĐÚNG?'
    if title.startswith('MỞ RỘNG'):
        return 'THUẬT TOÁN'
    if title.startswith('CẨN THẬN') or title.startswith('BẪY'):
        return 'BẪY THƯỜNG GẶP'
    raise KeyError(title)


class LDoc(Doc):
    def kbox(self, title, paras, kind=None):
        """Khung màu: kind suy ra từ đầu nhãn (KHỞI ĐỘNG, ĐỊNH LÍ ...)."""
        col, fill = KB[kind or kind_of(title)]
        if isinstance(paras, str):
            paras = [paras]
        ps = ['<w:p><w:pPr><w:keepNext/><w:spacing w:after="60" w:line="276" w:lineRule="auto"/></w:pPr><w:r>%s%s</w:r></w:p>'
              % (rpr(b=True, color=col, sz=19, font='A'), t(title))]
        for k, x in enumerate(paras):
            last = k == len(paras) - 1
            if x.startswith('- '):
                c = '<w:r>%s<w:t>•</w:t></w:r><w:r>%s<w:tab/></w:r>' % (rpr(b=True, color=col), rpr(b=True, color=col)) + inline(x[2:])
                ps.append(para(c, after=50, ind='<w:ind w:left="360" w:hanging="260"/>', extra='<w:tabs><w:tab w:val="left" w:pos="360"/></w:tabs>'))
            elif x.startswith('$eq '):
                ps.append(para(inline(x[4:], dict(sz=23)), after=110, before=60, jc='center'))
            elif x.startswith('$code '):
                for ln in x[6:].split('\n'):
                    ps.append('<w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="200"/></w:pPr><w:r>%s%s</w:r></w:p>' % (rpr(sz=18, font='C', color='1A1A1A'), t(ln)))
            elif x.startswith('$n '):          # mục đánh số: "$n 1|nội dung"
                num, body = x[3:].split('|', 1)
                c = '<w:r>%s%s</w:r>' % (rpr(b=True, color=col), t(num + '. ')) + inline(body)
                ps.append(para(c, after=50, ind='<w:ind w:left="360" w:hanging="300"/>'))
            else:
                ps.append(para(inline(x), after=110 if not last else 60))
        if fill is None:   # BÀI TOÁN: khung viền đủ bốn cạnh
            brd = ('<w:top w:val="single" w:sz="6" w:space="0" w:color="%s"/><w:left w:val="single" w:sz="24" w:space="0" w:color="%s"/>'
                   '<w:bottom w:val="single" w:sz="6" w:space="0" w:color="%s"/><w:right w:val="single" w:sz="6" w:space="0" w:color="%s"/>') % ((col,) * 4)
        else:
            brd = NOB.replace('<w:left w:val="none" w:sz="0" w:space="0" w:color="FFFFFF"/>', '<w:left w:val="single" w:sz="24" w:space="0" w:color="%s"/>' % col)
        self.raw(table([W], [('<w:trPr><w:jc w:val="center"/></w:trPr>', [cellxml(W, ''.join(ps), fill=fill, borders=brd, mar=(100, 180, 80, 160))])], center=True, borders=False))
        self.raw('<w:p><w:pPr><w:spacing w:after="120" w:line="120" w:lineRule="exact"/></w:pPr></w:p>')

    def lesson(self, num, title, header=None):
        self.cur_pid = str(num)
        self.figno[str(num)] = 0
        name = self.bookmark('Bài %d. %s' % (num, title), 1)
        pp = ('<w:p><w:pPr><w:pStyle w:val="Heading2"/><w:keepNext/></w:pPr><w:bookmarkStart w:id="%d" w:name="%s"/>'
              '<w:r>%s%s</w:r><w:r>%s%s</w:r><w:bookmarkEnd w:id="%d"/></w:p>') % (
            self.bm, name, rpr(color='FFD966'), t('BÀI %d' % num), rpr(color='FFFFFF'), t('   ' + title), self.bm)
        brd = ''.join('<w:%s w:val="single" w:sz="4" w:space="0" w:color="1F3864"/>' % s for s in ('top', 'left', 'bottom', 'right'))
        self.raw(table([W], [('<w:trPr><w:cantSplit/><w:jc w:val="center"/></w:trPr>', [cellxml(W, pp, fill=NAVY, borders=brd, mar=(120, 200, 120, 160))])], center=True, borders=False))
        self.raw('<w:p><w:pPr><w:spacing w:after="160" w:line="120" w:lineRule="exact"/></w:pPr></w:p>')

    def objectives(self, items):
        self.raw(para('<w:r>%s%s</w:r>' % (rpr(b=True, i=True, color=NAVY), t('Học xong bài này, em sẽ:')), after=60, before=60, keep=True, jc='left'))
        for it in items:
            c = '<w:r>%s%s</w:r>' % (rpr(b=True, color='2E7D32', sz=24), t('✓  ')) + inline(it)
            self.raw(para(c, after=40, ind='<w:ind w:left="360" w:hanging="360"/>'))
        self.raw(spacer(80, 160))

    def step(self, n, title):
        c = ('<w:r>%s%s</w:r><w:r>%s</w:r>' % (rpr(b=True, color='FFFFFF', sz=19, font='A', hl='C0504D'), t(' Bước %d ' % n), t('  '))
             + inline(title, dict(font='A', b=True, color='C0504D', sz=21)))
        self.raw('<w:p><w:pPr><w:keepNext/><w:spacing w:before="180" w:after="80" w:line="276" w:lineRule="auto"/></w:pPr>%s</w:p>' % c)

    def mini(self, text):
        """Tiêu đề nhỏ màu xanh (Tự kiểm tra nhanh, Luyện tập...)."""
        self.raw('<w:p><w:pPr><w:keepNext/><w:spacing w:before="160" w:after="80" w:line="276" w:lineRule="auto"/></w:pPr><w:r>%s%s</w:r></w:p>'
                 % (rpr(font='A', b=True, color=NAVY, sz=21), t(text)))

    def problem_box(self, code, desc, inp, out):
        paras = (desc if isinstance(desc, list) else [desc]) + ['**Dữ liệu vào:** ' + inp, '**Kết quả:** ' + out]
        self.kbox('BÀI TOÁN: ' + code, paras)

    def examples(self, code, rows, widths=(2.3, 2.0, 5.2)):
        """rows: [(inp, out, giải thích)]; inp/out có thể nhiều dòng."""
        self.table(['%s.INP' % code, '%s.OUT' % code, 'Giải thích'], [list(r) for r in rows], widths=list(widths),
                   align=['left', 'left', 'both'], mono_cols=(0, 1), sz=20)

    def luyentap(self, rows):
        self.mini('Luyện tập')
        self.table(['Bài', 'Tên', 'Gợi ý liên hệ'], [['**%s**' % a, b, c] for a, b, c in rows], widths=[0.7, 2.4, 6.0],
                   align=['center', 'left', 'both'], sz=19)

    def tukiemtra(self, items):
        self.mini('Tự kiểm tra nhanh')
        for k, (q, a) in enumerate(items, 1):
            c = '<w:r>%s%s</w:r>' % (rpr(b=True, color=NAVY), t('%d) ' % k)) + inline(q) + '<w:r>%s%s</w:r>' % (rpr(i=True), t(' ')) + inline('(Đáp số: ' + a + ')', dict(i=True))
            self.raw(para(c, after=60, ind='<w:ind w:firstLine="567"/>'))

    def chapter_page(self, num, title, intro, lessons):
        self.chapter_title(num, title, [])
        for x in intro:
            self.p(x)
        self.kbox('TRONG CHƯƠNG NÀY', ['**Bài %d.** %s' % (n, s) for n, s in lessons])
