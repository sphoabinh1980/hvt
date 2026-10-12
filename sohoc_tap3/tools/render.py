"""Dựng tệp .docx theo đúng phong cách của mẫu Tập 3 (Quy hoạch động)."""
import os, re, shutil, struct, zipfile, html, json

W = 8618            # bề rộng vùng chữ (dxa)
NAVY = '1F3864'
FONT_A = '<w:rFonts w:ascii="Arial" w:eastAsia="Arial" w:hAnsi="Arial" w:cs="Arial"/>'
FONT_C = '<w:rFonts w:ascii="Courier New" w:eastAsia="Courier New" w:hAnsi="Courier New" w:cs="Courier New"/>'
NOB = '<w:top w:val="none" w:sz="0" w:space="0" w:color="FFFFFF"/><w:left w:val="none" w:sz="0" w:space="0" w:color="FFFFFF"/><w:bottom w:val="none" w:sz="0" w:space="0" w:color="FFFFFF"/><w:right w:val="none" w:sz="0" w:space="0" w:color="FFFFFF"/>'
TBL_NOB = '<w:tblBorders>' + NOB + '<w:insideH w:val="none" w:sz="0" w:space="0" w:color="FFFFFF"/><w:insideV w:val="none" w:sz="0" w:space="0" w:color="FFFFFF"/></w:tblBorders>'
TBL_TAIL = '<w:tblLayout w:type="fixed"/><w:tblCellMar><w:left w:w="10" w:type="dxa"/><w:right w:w="10" w:type="dxa"/></w:tblCellMar><w:tblLook w:val="0000" w:firstRow="0" w:lastRow="0" w:firstColumn="0" w:lastColumn="0" w:noHBand="0" w:noVBand="0"/>'
TRPREX = '<w:tblPrEx><w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/></w:tblCellMar></w:tblPrEx>'


def esc(s):
    return html.escape(s, quote=False)


def t(s):
    return '<w:t xml:space="preserve">%s</w:t>' % esc(s)


def rpr(b=False, i=False, color=None, sz=None, font=None, va=None, hl=None):
    s = ''
    if font == 'A':
        s += FONT_A
    elif font == 'C':
        s += FONT_C
    if b:
        s += '<w:b/><w:bCs/>'
    if i:
        s += '<w:i/><w:iCs/>'
    if color:
        s += '<w:color w:val="%s"/>' % color
    if sz:
        s += '<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (sz, sz)
    if hl:
        s += '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % hl
    if va:
        s += '<w:vertAlign w:val="%s"/>' % va
    return '<w:rPr>%s</w:rPr>' % s if s else ''


# ------------------------------------------------------------ inline markup
# **đậm**  __nghiêng__  `mã`  ^{trên}  _{dưới}  {{đỏ đậm}}  [[xanh đậm]]
def inline(text, base=None):
    base = dict(base or {})
    out = []
    st = dict(b=base.get('b', False), i=base.get('i', False), va=None, color=base.get('color'), code=False)
    stack = []
    buf = []

    def flush():
        if buf:
            s = ''.join(buf)
            buf.clear()
            if st['code']:
                out.append('<w:r>%s%s</w:r>' % (rpr(color='C0392B' if not st['color'] else st['color'], sz=base.get('csz', 20), font='C', va=st['va'], b=st['b']), t(s)))
            else:
                out.append('<w:r>%s%s</w:r>' % (rpr(b=st['b'], i=st['i'], color=st['color'], sz=base.get('sz'), font=base.get('font'), va=st['va']), t(s)))
    k = 0
    n = len(text)
    while k < n:
        c = text[k]
        two = text[k:k + 2]
        if st['code']:
            if c == '`':
                flush(); st['code'] = False; k += 1; continue
            buf.append(c); k += 1; continue
        if c == '\\' and k + 1 < n:
            buf.append(text[k + 1]); k += 2; continue
        if c == '`':
            flush(); st['code'] = True; k += 1; continue
        if two == '**':
            flush(); st['b'] = not st['b']; k += 2; continue
        if two == '__':
            flush(); st['i'] = not st['i']; k += 2; continue
        if two == '^{' or two == '_{':
            flush(); stack.append(('va', st['va'])); st['va'] = 'superscript' if c == '^' else 'subscript'; k += 2; continue
        if two == '{{':
            flush(); stack.append(('red', (st['color'], st['b']))); st['color'] = 'C00000'; st['b'] = True; k += 2; continue
        if two == '}}' and stack and stack[-1][0] == 'red':
            flush(); _, (st['color'], st['b']) = stack.pop(); k += 2; continue
        if two == '[[':
            flush(); stack.append(('nv', (st['color'], st['b']))); st['color'] = NAVY; st['b'] = True; k += 2; continue
        if two == ']]' and stack and stack[-1][0] == 'nv':
            flush(); _, (st['color'], st['b']) = stack.pop(); k += 2; continue
        if c == '}' and stack and stack[-1][0] == 'va':
            flush(); st['va'] = stack.pop()[1]; k += 1; continue
        buf.append(c); k += 1
    flush()
    return ''.join(out)


def para(content, after=110, before=None, jc='both', line=276, keep=False, ind=None, extra=''):
    sp = '<w:spacing%s w:after="%d" w:line="%d" w:lineRule="auto"/>' % (' w:before="%d"' % before if before is not None else '', after, line)
    p = '<w:pPr>%s%s%s%s<w:jc w:val="%s"/></w:pPr>' % ('<w:keepNext/>' if keep else '', extra, sp, ind or '', jc)
    return '<w:p>%s%s</w:p>' % (p, content)


def cellxml(width, content, fill=None, borders=None, mar=(50, 90, 50, 90), valign='center', span=1):
    b = borders if borders is not None else ''.join(
        '<w:%s w:val="single" w:sz="4" w:space="0" w:color="A6B4CC"/>' % s for s in ('top', 'left', 'bottom', 'right'))
    sh = '<w:shd w:val="clear" w:color="auto" w:fill="%s"/>' % fill if fill else ''
    m = '<w:tcMar><w:top w:w="%d" w:type="dxa"/><w:left w:w="%d" w:type="dxa"/><w:bottom w:w="%d" w:type="dxa"/><w:right w:w="%d" w:type="dxa"/></w:tcMar>' % mar
    gs = '<w:gridSpan w:val="%d"/>' % span if span > 1 else ''
    return '<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/>%s<w:tcBorders>%s</w:tcBorders>%s%s<w:vAlign w:val="%s"/></w:tcPr>%s</w:tc>' % (
        width, gs, b, sh, m, valign, content)


def table(widths, rows, center=True, borders=True):
    """rows: list of (trPr_extra, [cellxml...])"""
    tb = ('<w:tblBorders>' + ''.join('<w:%s w:val="single" w:sz="4" w:space="0" w:color="auto"/>' % s for s in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV')) + '</w:tblBorders>') if borders else TBL_NOB
    g = ''.join('<w:gridCol w:w="%d"/>' % x for x in widths)
    body = ''.join('<w:tr>%s%s%s</w:tr>' % (TRPREX, tr, ''.join(cs)) for tr, cs in rows)
    return '<w:tbl><w:tblPr><w:tblW w:w="%d" w:type="dxa"/>%s%s%s</w:tblPr><w:tblGrid>%s</w:tblGrid>%s</w:tbl>' % (
        sum(widths), '<w:jc w:val="center"/>' if center else '', tb, TBL_TAIL, g, body)


def spacer(after=80, line=200):
    return '<w:p><w:pPr><w:spacing w:after="%d" w:line="%d" w:lineRule="auto"/><w:jc w:val="both"/></w:pPr></w:p>' % (after, line)


# ------------------------------------------------------------ tô màu mã C++
KW = set('''auto bool break case char const continue default do double else enum false float for if inline int long namespace
return short signed sizeof static struct switch true typedef unsigned using void while nullptr __int128 vector string
template typename class public private operator const_cast static_cast pair array map unordered_map set size_t
ios_base cin cout int64_t uint64_t uint32_t'''.split())
TOK = re.compile(r'(//.*$)|("(?:\\.|[^"\\])*")|(\'(?:\\.|[^\'\\])*\')|(\b\d[\w.]*\b)|([A-Za-z_]\w*)|(\s+)|(.)')


def code_line(no, line, width_no):
    runs = ['<w:r>%s%s</w:r>' % (rpr(color='A0A0A0', sz=17, font='C'), t(str(no).rjust(width_no) + '  '))]
    if line.lstrip().startswith('#'):
        runs.append('<w:r>%s%s</w:r>' % (rpr(color='6A4C93', sz=17, font='C'), t(line)))
    else:
        for m in TOK.finditer(line):
            s = m.group(0)
            if m.group(1):
                r = rpr(color='7F7F7F', sz=17, font='C', i=True)
            elif m.group(2) or m.group(3):
                r = rpr(color='548235', sz=17, font='C')
            elif m.group(4):
                r = rpr(color='C55A11', sz=17, font='C')
            elif m.group(5) and s in KW:
                r = rpr(color=NAVY, sz=17, font='C', b=True)
            else:
                r = rpr(color='1A1A1A', sz=17, font='C')
            runs.append('<w:r>%s%s</w:r>' % (r, t(s)))
    return '<w:p><w:pPr><w:keepLines/><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>%s</w:p>' % ''.join(runs)


def png_size(path):
    with open(path, 'rb') as f:
        d = f.read(24)
    return struct.unpack('>II', d[16:24])


class Doc:
    def __init__(self, tpl_dir, short_title):
        self.tpl = tpl_dir
        self.body = []
        self.images = []        # (rid, path)
        self.headers = []       # (hname, text)
        self.sections = []
        self.toc = []           # (level, text, bookmark)
        self.bm = 0
        self.short = short_title
        self.figno = {}
        self.pagemap = {}
        self.warn = []

    # ---------------------------------------------------- khối cơ bản
    def raw(self, x):
        self.body.append(x)

    def p(self, text, after=110, jc='both', keep=False, i=False, color=None, sz=None, before=None):
        self.raw(para(inline(text, dict(i=i, color=color, sz=sz)), after=after, jc=jc, keep=keep, before=before))

    def h(self, text):
        self.raw('<w:p><w:pPr><w:pStyle w:val="Heading3"/><w:keepNext/><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="2" w:color="B4C6E7"/></w:pBdr><w:spacing w:before="260" w:after="120"/></w:pPr>%s</w:p>' % inline(text))

    def sub(self, text):
        self.raw('<w:p><w:pPr><w:keepNext/><w:spacing w:before="160" w:after="80" w:line="276" w:lineRule="auto"/></w:pPr>%s</w:p>' % inline(text, dict(font='A', b=True, color='C0504D', sz=22)))

    def bullets(self, items, after=60):
        for it in items:
            c = '<w:r>%s<w:t>•</w:t></w:r><w:r>%s<w:tab/></w:r>' % (rpr(b=True, color=NAVY), rpr(b=True, color=NAVY)) + inline(it)
            self.raw(para(c, after=after, ind='<w:ind w:left="480" w:hanging="280"/>', extra='<w:tabs><w:tab w:val="left" w:pos="480"/></w:tabs>'))
        self.raw(spacer(40, 120))

    def nums(self, items, start=1, after=70):
        for k, it in enumerate(items, start):
            c = '<w:r>%s%s</w:r>' % (rpr(b=True, color=NAVY), t('%d. ' % k)) + inline(it)
            self.raw(para(c, after=after, ind='<w:ind w:left="420" w:hanging="300"/>'))

    def eq(self, text, after=110):
        """Công thức đặt giữa dòng."""
        self.raw(para(inline(text, dict(b=False)), after=after, jc='center', before=40))

    def fig(self, path, caption, width_cm=14.0, num=None):
        if not os.path.exists(path):
            self.warn.append('missing fig ' + path)
            return
        pw, ph = png_size(path)
        maxw = W / 1440 * 2.54
        width_cm = min(width_cm, maxw)
        cx = int(width_cm / 2.54 * 914400)
        cy = int(cx * ph / pw)
        rid = 'rIdImg%d' % (len(self.images) + 1)
        self.images.append((rid, path))
        iid = len(self.images)
        drawing = ('<w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="%d" cy="%d"/>'
                   '<wp:docPr id="%d" name="Hinh %d"/><wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
                   '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
                   '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="%d" name="img%d.png"/><pic:cNvPicPr/></pic:nvPicPr>'
                   '<pic:blipFill><a:blip r:embed="%s"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
                   '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="%d"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>'
                   '</a:graphicData></a:graphic></wp:inline></w:drawing>') % (cx, cy, iid, iid, iid, iid, rid, cx, cy)
        self.raw('<w:p><w:pPr><w:keepNext/><w:spacing w:before="60" w:after="40"/><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:noProof/></w:rPr>%s</w:r></w:p>' % drawing)
        if caption:
            if num is None:
                key = self.cur_pid
                self.figno[key] = self.figno.get(key, 0) + 1
                num = '%s.%d' % (key, self.figno[key])
            c = '<w:r>%s%s</w:r>' % (rpr(b=True, i=True, color='404040', sz=19), t('Hình %s. ' % num)) + inline(caption, dict(i=True, color='404040', sz=19))
            self.raw(para(c, after=160, jc='center'))

    def code(self, title, src):
        lines = src.rstrip('\n').split('\n')
        wn = len(str(len(lines)))
        for ln in lines:
            if len(ln) > 76:
                self.warn.append('long code line (%d): %s' % (len(ln), ln))
        ps = ['<w:p><w:pPr><w:keepNext/><w:spacing w:after="60" w:line="276" w:lineRule="auto"/></w:pPr><w:r>%s%s</w:r></w:p>' % (rpr(b=True, color='595959', sz=17, font='A'), t(title))]
        ps += [code_line(k + 1, ln.replace('\t', '    '), wn) for k, ln in enumerate(lines)]
        brd = ('<w:top w:val="single" w:sz="4" w:space="0" w:color="D0D0D0"/><w:left w:val="single" w:sz="18" w:space="0" w:color="9AA9C4"/>'
               '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D0D0"/><w:right w:val="single" w:sz="4" w:space="0" w:color="D0D0D0"/>')
        self.raw(table([W], [('', [cellxml(W, ''.join(ps), fill='F7F7F7', borders=brd, mar=(90, 160, 90, 120))])], center=False, borders=False))
        self.raw(spacer(80, 200))

    BOX = {'red': ('C0504D', 'FBEAEA'), 'purple': ('6A4C93', 'F1ECF8'), 'blue': (NAVY, 'F3F6FA'),
           'green': ('548235', 'EAF5E6'), 'orange': ('C55A11', 'FDF0E6'), 'teal': ('2E7D7A', 'E8F4F3')}

    def box(self, kind, title, paras):
        col, fill = self.BOX[kind]
        if isinstance(paras, str):
            paras = [paras]
        ps = ['<w:p><w:pPr><w:keepNext/><w:spacing w:after="60" w:line="276" w:lineRule="auto"/><w:jc w:val="both"/></w:pPr><w:r>%s%s</w:r></w:p>' % (rpr(b=True, color=col, sz=19, font='A'), t(title))]
        for k, x in enumerate(paras):
            last = k == len(paras) - 1
            if x.startswith('- '):
                c = '<w:r>%s<w:t>•</w:t></w:r><w:r>%s<w:tab/></w:r>' % (rpr(b=True, color=col), rpr(b=True, color=col)) + inline(x[2:])
                ps.append(para(c, after=40 if not last else 40, ind='<w:ind w:left="360" w:hanging="260"/>', extra='<w:tabs><w:tab w:val="left" w:pos="360"/></w:tabs>'))
            elif x.startswith('$code '):
                for ln in x[6:].split('\n'):
                    ps.append('<w:p><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:left="200"/></w:pPr><w:r>%s%s</w:r></w:p>' % (rpr(sz=18, font='C', color='1A1A1A'), t(ln)))
            else:
                ps.append(para(inline(x), after=70 if not last else 40))
        brd = NOB.replace('<w:left w:val="none" w:sz="0" w:space="0" w:color="FFFFFF"/>', '<w:left w:val="single" w:sz="24" w:space="0" w:color="%s"/>' % col)
        self.raw(table([W], [('', [cellxml(W, ''.join(ps), fill=fill, borders=brd, mar=(100, 180, 80, 160))])], center=False, borders=False))
        self.raw(spacer(100, 200))

    def table(self, headers, rows, widths=None, align=None, hl=(), sz=20, bold_cols=(), mono_cols=(), hdr_sz=20, fills=None):
        n = len(headers) if headers else len(rows[0])
        widths = widths or [1] * n
        tot = sum(widths)
        ws = [int(W * x / tot) for x in widths]
        ws[-1] = W - sum(ws[:-1])
        align = align or ['center'] * n
        trs = []
        if headers:
            cs = [cellxml(ws[j], '<w:p><w:pPr><w:keepNext/><w:spacing w:after="0" w:line="252" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr>%s</w:p>' % inline(h, dict(font='A', b=True, color=NAVY, sz=hdr_sz)), fill='E8EEF7') for j, h in enumerate(headers)]
            trs.append(('<w:trPr><w:cantSplit/><w:tblHeader/><w:jc w:val="center"/></w:trPr>', cs))
        for i, r in enumerate(rows):
            cs = []
            for j, v in enumerate(r):
                lines = str(v).split('\n')
                base = dict(sz=sz, b=(j in bold_cols) or (i in hl and j == n - 1))
                if j in mono_cols:
                    base['font'] = 'C'; base['sz'] = sz - 2
                kn = '<w:keepNext/>' if (len(rows) <= 14 and i < len(rows) - 1) else ''
                ps = ''.join('<w:p><w:pPr>%s<w:spacing w:after="0" w:line="252" w:lineRule="auto"/><w:jc w:val="%s"/></w:pPr>%s</w:p>' % (
                    kn, {'center': 'center', 'left': 'left', 'right': 'right', 'both': 'both'}[align[j]], inline(l, base)) for l in lines)
                fill = 'EAF5E6' if i in hl else (fills[i][j] if fills and fills[i] and fills[i][j] else None)
                cs.append(cellxml(ws[j], ps, fill=fill))
            trs.append(('<w:trPr><w:cantSplit/><w:jc w:val="center"/></w:trPr>', cs))
        self.raw(table(ws, trs))
        self.raw(spacer(100, 200))

    def iotable(self, fname, inp, out, expl=None, widths=None):
        """Bảng ví dụ dạng INP | OUT | Giải thích (mono)."""
        hdr = ['%s.INP' % fname, '%s.OUT' % fname] + (['Giải thích'] if expl else [])
        row = [inp.rstrip('\n'), out.rstrip('\n')] + ([expl] if expl else [])
        self.table(hdr, [row], widths=widths or ([2.2, 2.2, 5] if expl else [1, 1]), align=['left', 'left', 'both'][:len(hdr)], mono_cols=(0, 1))

    def pagebreak(self):
        self.raw('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

    def bookmark(self, text, level):
        self.bm += 1
        name = '_Toc%06d' % self.bm
        self.toc.append((level, text, name))
        return name

    # ---------------------------------------------------- khối lớn
    def section_break(self, header_text, title_pg=False):
        """Kết thúc section hiện tại; header_text là đầu trang của section vừa kết thúc."""
        hid = len(self.headers) + 1
        self.headers.append(header_text)
        hdr = '' if header_text is None else '<w:headerReference w:type="default" r:id="rIdHdr%d"/><w:footerReference w:type="default" r:id="rIdFtr1"/>' % hid
        sect = ('<w:sectPr>%s<w:pgSz w:w="10772" w:h="15024"/><w:pgMar w:top="1134" w:right="1077" w:bottom="1134" w:left="1077" w:header="560" w:footer="520" w:gutter="0"/><w:cols w:space="720"/>%s<w:docGrid w:linePitch="360"/></w:sectPr>'
                % (hdr, '<w:titlePg/>' if title_pg else ''))
        self.raw('<w:p><w:pPr>%s</w:pPr></w:p>' % sect)

    def big_title(self, text, toc=True):
        name = self.bookmark(text, 0) if toc else None
        bms = '<w:bookmarkStart w:id="%d" w:name="%s"/>' % (self.bm, name) if name else ''
        bme = '<w:bookmarkEnd w:id="%d"/>' % self.bm if name else ''
        self.raw('<w:p><w:pPr><w:pStyle w:val="Heading1"/><w:spacing w:before="200" w:after="200"/><w:jc w:val="center"/></w:pPr>%s<w:r><w:rPr><w:sz w:val="34"/><w:szCs w:val="34"/></w:rPr>%s</w:r>%s</w:p>' % (bms, t(text), bme))

    def chapter_title(self, num, title, intro):
        name = self.bookmark('CHƯƠNG %d. %s' % (num, title), 0)
        self.raw('<w:p><w:pPr><w:spacing w:after="600" w:line="276" w:lineRule="auto"/><w:jc w:val="both"/></w:pPr></w:p>')
        self.raw('<w:p><w:pPr><w:pStyle w:val="Heading1"/><w:pBdr><w:bottom w:val="single" w:sz="14" w:space="6" w:color="C0504D"/></w:pBdr><w:spacing w:after="160"/></w:pPr>'
                 '<w:bookmarkStart w:id="%d" w:name="%s"/><w:r><w:rPr><w:color w:val="C0504D"/></w:rPr>%s</w:r><w:r>%s</w:r><w:bookmarkEnd w:id="%d"/></w:p>' % (self.bm, name, t('CHƯƠNG %d. ' % num), t(title), self.bm))
        for x in (intro if isinstance(intro, list) else [intro]):
            self.raw(para(inline(x, dict(i=True, color='404040')), before=60, after=200))

    def problem(self, pid, name, fname, tl, ml, level, link):
        self.cur_pid = pid
        self.figno[pid] = 0
        bmname = self.bookmark('Bài %s. %s' % (pid, name), 1)
        lab = '<w:r>%s%s</w:r><w:r>%s%s</w:r>' % (rpr(color='FFD966', sz=30), t('BÀI %s  ' % pid), rpr(color='FFFFFF'), t(name))
        pp = '<w:p><w:pPr><w:pStyle w:val="Heading2"/><w:keepNext/></w:pPr><w:bookmarkStart w:id="%d" w:name="%s"/>%s<w:bookmarkEnd w:id="%d"/></w:p>' % (self.bm, bmname, lab, self.bm)
        self.raw(table([W], [('', [cellxml(W, pp, fill='1F3864', borders=NOB, mar=(120, 200, 120, 200))])], center=False, borders=False))
        self.raw(spacer(80, 200))
        stars = {1: '★', 2: '★★', 3: '★★★'}[level]
        lvl = {1: 'CƠ BẢN', 2: 'TRUNG BÌNH', 3: 'NÂNG CAO'}[level]
        ws = [2154, 2154, 1120, 1120, 2070]
        hdr = ['Dữ liệu vào', 'Kết quả', 'Thời gian', 'Bộ nhớ', 'Mức độ']
        hc = [cellxml(ws[j], '<w:p><w:pPr><w:keepNext/><w:spacing w:after="0" w:line="252" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr><w:r>%s%s</w:r></w:p>' % (rpr(font='A', b=True, color=NAVY, sz=20), t(h)), fill='E8EEF7') for j, h in enumerate(hdr)]
        vals = ['%s.INP' % fname, '%s.OUT' % fname, '%g giây' % tl, '%d MB' % ml]
        vc = [cellxml(ws[j], '<w:p><w:pPr><w:keepNext/><w:spacing w:after="0" w:line="252" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr><w:r>%s%s</w:r></w:p>' % (rpr(sz=20), t(v))) for j, v in enumerate(vals)]
        vc.append(cellxml(ws[4], '<w:p><w:pPr><w:keepNext/><w:spacing w:after="0" w:line="252" w:lineRule="auto"/><w:jc w:val="center"/></w:pPr><w:r>%s%s</w:r><w:r>%s%s</w:r></w:p>' % (
            rpr(color='BF9000', sz=20, b=True), t(stars + ' '), rpr(b=True, color=NAVY, sz=20), t(lvl))))
        self.raw(table(ws, [('<w:trPr><w:cantSplit/><w:tblHeader/><w:jc w:val="center"/></w:trPr>', hc), ('<w:trPr><w:cantSplit/><w:jc w:val="center"/></w:trPr>', vc)]))
        self.raw(spacer(60, 200))
        self.raw(para('<w:r>%s%s</w:r>' % (rpr(i=True, color='595959', sz=21), t('Liên hệ: ' + link)), after=120))

    def score(self, pid, scores, subtasks, order=None, ref=None):
        hdr = ['Thuật toán'] + ['Subtask %d (%d)' % (k + 1, p) for k, p in enumerate(subtasks)] + ['Tổng']
        rows = []
        hl = set()
        keys = order or list(scores.keys())
        for k, f in enumerate(keys):
            s = scores[f]
            rows.append([s['title']] + [str(x) for x in s['pts']] + [str(sum(s['pts']))])
            if f == ref:
                hl.add(k)
        n = len(subtasks)
        widths = [3.4] + [1.75 if n <= 3 else 1.35] * n + [1.2]
        self.table(hdr, rows, widths=widths, hl=hl, hdr_sz=19)

    # ---------------------------------------------------- mục lục
    def toc_xml(self):
        out = []
        for level, text, name in self.toc:
            pg = self.pagemap.get(name, '')
            if level == 0:
                lead = '<w:r>%s%s</w:r>' % (rpr(font='A', b=True, color=NAVY, sz=21), t(text))
                sp = '<w:spacing w:before="160" w:after="60"/>'
                ind = ''
            else:
                lead = '<w:r>%s%s</w:r>' % (rpr(sz=21), t(text))
                sp = '<w:spacing w:after="20"/>'
                ind = '<w:ind w:left="280"/>'
            fld = ('<w:r>%s<w:tab/></w:r><w:r>%s<w:fldChar w:fldCharType="begin"/></w:r><w:r>%s<w:instrText xml:space="preserve"> PAGEREF %s \\h </w:instrText></w:r>'
                   '<w:r>%s<w:fldChar w:fldCharType="separate"/></w:r><w:r>%s%s</w:r><w:r>%s<w:fldChar w:fldCharType="end"/></w:r>') % (
                rpr(sz=22), rpr(b=level == 0, sz=22), rpr(b=level == 0, sz=22), name, rpr(b=level == 0, sz=22), rpr(b=level == 0, sz=22), t(str(pg)), rpr(b=level == 0, sz=22))
            out.append('<w:p><w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="8618"/></w:tabs>%s%s</w:pPr><w:hyperlink w:anchor="%s" w:history="1">%s%s</w:hyperlink></w:p>' % (sp, ind, name, lead, fld))
        return ''.join(out)

    # ---------------------------------------------------- xuất tệp
    def save(self, path, last_header):
        self.section_break(last_header)  # section cuối dùng sectPr ở body
        body = ''.join(self.body)
        body = body.replace('<!--TOC-->', self.toc_xml())
        # sectPr cuối cùng phải nằm trực tiếp trong body
        i = body.rfind('<w:p><w:pPr><w:sectPr>')
        last = body[i:]
        sect = last[len('<w:p><w:pPr>'):-len('</w:pPr></w:p>')]
        body = body[:i] + sect
        tpl = open(os.path.join(self.tpl, 'word', 'document.xml'), encoding='utf-8').read()
        head = tpl[:tpl.find('<w:body>') + len('<w:body>')]
        doc = head + body + '</w:body></w:document>'
        tmp = path + '.dir'
        if os.path.exists(tmp):
            shutil.rmtree(tmp)
        os.makedirs(tmp)
        for root, dirs, files in os.walk(self.tpl):
            rel = os.path.relpath(root, self.tpl)
            if rel.startswith(os.path.join('word', 'media')):
                continue
            for f in files:
                if rel == 'word' and (f.startswith('header') or f.startswith('footer') or f == 'document.xml'):
                    continue
                if rel == os.path.join('word', '_rels'):
                    continue
                os.makedirs(os.path.join(tmp, rel), exist_ok=True)
                shutil.copy(os.path.join(root, f), os.path.join(tmp, rel, f))
        os.makedirs(os.path.join(tmp, 'word', 'media'), exist_ok=True)
        os.makedirs(os.path.join(tmp, 'word', '_rels'), exist_ok=True)
        open(os.path.join(tmp, 'word', 'document.xml'), 'w', encoding='utf-8').write(doc)
        hdr_tpl = open(os.path.join(self.tpl, 'word', 'header2.xml'), encoding='utf-8').read()
        ftr_tpl = open(os.path.join(self.tpl, 'word', 'footer2.xml'), encoding='utf-8').read()
        old = re.search(r'<w:t>([^<]*)</w:t>', hdr_tpl).group(1)
        rels = []
        ct_over = []
        for k, h in enumerate(self.headers, 1):
            if h is None:
                continue
            open(os.path.join(tmp, 'word', 'header%d.xml' % k), 'w', encoding='utf-8').write(hdr_tpl.replace('<w:t>%s</w:t>' % old, '<w:t>%s</w:t>' % esc(h)))
            rels.append('<Relationship Id="rIdHdr%d" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header%d.xml"/>' % (k, k))
            ct_over.append('<Override PartName="/word/header%d.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>' % k)
        open(os.path.join(tmp, 'word', 'footer1.xml'), 'w', encoding='utf-8').write(re.sub(r'(<w:noProof/>.*?<w:t>)\d+(</w:t>)', r'\g<1>1\2', ftr_tpl))
        rels.append('<Relationship Id="rIdFtr1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>')
        ct_over.append('<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>')
        for k, (rid, p) in enumerate(self.images, 1):
            shutil.copy(p, os.path.join(tmp, 'word', 'media', 'image%d.png' % k))
            rels.append('<Relationship Id="%s" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image%d.png"/>' % (rid, k))
        base_rels = open(os.path.join(self.tpl, 'word', '_rels', 'document.xml.rels'), encoding='utf-8').read()
        keep = re.findall(r'<Relationship [^>]*Target="(?:styles|settings|webSettings|fontTable|numbering|footnotes|endnotes|theme/theme1)\.xml"/>', base_rels)
        open(os.path.join(tmp, 'word', '_rels', 'document.xml.rels'), 'w', encoding='utf-8').write(
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">%s</Relationships>' % ''.join(keep + rels))
        ct = open(os.path.join(self.tpl, '[Content_Types].xml'), encoding='utf-8').read()
        ct = re.sub(r'<Override PartName="/word/(header|footer)\d+\.xml"[^>]*/>', '', ct)
        ct = ct.replace('</Types>', ''.join(ct_over) + '</Types>')
        open(os.path.join(tmp, '[Content_Types].xml'), 'w', encoding='utf-8').write(ct)
        if os.path.exists(path):
            os.remove(path)
        with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
            z.write(os.path.join(tmp, '[Content_Types].xml'), '[Content_Types].xml')
            for root, dirs, files in os.walk(tmp):
                for f in files:
                    full = os.path.join(root, f)
                    rel = os.path.relpath(full, tmp)
                    if rel == '[Content_Types].xml':
                        continue
                    z.write(full, rel)
        shutil.rmtree(tmp)
        for w in self.warn:
            print('WARN', w)
