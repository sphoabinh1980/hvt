#!/usr/bin/env python3
"""Lượt 2 của mục lục: đọc PDF đã dựng, tìm trang của từng mục, ghi out/pagemap.json."""
import json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools')); sys.path.insert(0, ROOT)
pdf = os.path.join(ROOT, 'out', 'SoDacBiet_Tap1_LyThuyet.pdf')
n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
pages = []
for k in range(1, n + 1):
    t = subprocess.run(['pdftotext', '-f', str(k), '-l', str(k), '-layout', pdf, '-'], capture_output=True, text=True).stdout
    pages.append(t)
norm = lambda s: re.sub(r'\s+', ' ', s)
# trang mục lục: có dòng "Bài x.y. ..." kèm dấu chấm dẫn, hoặc tiêu đề MỤC LỤC
toc_pages = {i for i, t in enumerate(pages) if re.search(r'Bài \d+\.\d+\. .*\.{5}', t) or 'MỤC LỤC' in t}
# danh sách mục theo thứ tự xuất hiện: lấy từ document.xml (bookmark + văn bản)
import zipfile
doc = zipfile.ZipFile(os.path.join(ROOT, 'out', 'SoDacBiet_Tap1_LyThuyet.docx')).read('word/document.xml').decode('utf-8')
entries = re.findall(r'<w:hyperlink w:anchor="(_Toc\d+)"[^>]*>(.*?)</w:hyperlink>', doc)
items = []
for name, xml in entries:
    text = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', xml.split('<w:tab/>')[0]))
    items.append((name, text))
def key(text):
    m = re.match(r'Bài (\d+\.\d+)\. ', text)
    if m: return 'BÀI ' + m.group(1) + ' '
    return text.split(' (')[0]
pm = {}; cur = 0
for name, text in items:
    k = key(text)
    found = None
    for i in range(cur, n):
        if i in toc_pages: continue
        body = norm(pages[i])
        # bỏ dòng đầu trang (header) khi tìm tiêu đề chương
        lines = pages[i].split('\n')
        body_nohdr = norm('\n'.join(lines[2:])) if k.startswith('CHƯƠNG') else body
        if k in body_nohdr:
            found = i; break
    if found is None:
        print('NOT FOUND', name, text); continue
    pm[name] = found + 1; cur = found
json.dump(pm, open(os.path.join(ROOT, 'out', 'pagemap.json'), 'w'), indent=0)
print(len(pm), 'of', len(items), 'entries; pages', n, '; toc pages', sorted(p + 1 for p in toc_pages))
