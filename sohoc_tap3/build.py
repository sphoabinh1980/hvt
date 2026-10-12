#!/usr/bin/env python3
"""Dựng toàn bộ cuốn Tập 3. Dùng: python3 build.py [figs] [pid ...]"""
import sys, os, json, importlib.util
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, ROOT)
from render import Doc
import book


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class Ctx:
    def __init__(self, D, pid):
        self.D = D
        self.pid = pid
        self.dir = os.path.join(ROOT, 'problems', pid)
        self.meta = load(os.path.join(self.dir, 'meta.py'), 'meta_' + pid.replace('.', '_'))
        sp = os.path.join(self.dir, 'scores.json')
        self.scores = json.load(open(sp)) if os.path.exists(sp) else {}

    def fig(self, name):
        return os.path.join(self.dir, 'fig', name + '.png')

    def src(self, name):
        return open(os.path.join(self.dir, name), encoding='utf-8').read()

    def pts(self, f, st):
        return self.scores[f]['pts'][st - 1]

    def total(self, f):
        return sum(self.scores[f]['pts'])

    def score(self, order):
        self.D.score(self.pid, self.scores, self.meta.SUBTASKS, order=order, ref=self.meta.REF)


def make_figs(pid):
    d = os.path.join(ROOT, 'problems', pid)
    if not os.path.exists(os.path.join(d, 'figs.py')):
        return
    sys.path.insert(0, d)
    m = load(os.path.join(d, 'figs.py'), 'figs_' + pid.replace('.', '_'))
    os.makedirs(os.path.join(d, 'fig'), exist_ok=True)
    m.make(lambda n: os.path.join(d, 'fig', n + '.png'))
    sys.path.remove(d)


def problem(D, pid):
    name, fname, level, tl, ml = book.PROBLEMS[pid]
    D.problem(pid, name, fname, tl, ml, level, book.link(pid))
    P = Ctx(D, pid)
    m = load(os.path.join(P.dir, 'content.py'), 'content_' + pid.replace('.', '_'))
    m.build(D, P)


def main():
    args = sys.argv[1:]
    figs = 'figs' in args
    only = [a for a in args if a[0].isdigit()]
    pids = only or [p for p in book.PROBLEMS if os.path.exists(os.path.join(ROOT, 'problems', p, 'content.py'))]
    if figs:
        for p in pids:
            make_figs(p)
    D = Doc(os.path.join(ROOT, 'template'), 'Số học · Tập 3: Hướng dẫn giải')
    import front
    front.cover(D)
    pm = os.path.join(ROOT, 'out', 'pagemap.json')
    if os.path.exists(pm):
        D.pagemap = json.load(open(pm))
    front.intro(D)
    first = True
    for num, title, lessons in book.CHAPTERS:
        chp = [p for p in pids if int(p.split('.')[0]) in lessons]
        if not chp:
            continue
        hdr_prev = D.short if first else D.short + ' · CHƯƠNG %d. %s' % (prev[0], prev[1])
        D.section_break(hdr_prev)
        first = False
        prev = (num, title)
        front.chapter(D, num, title, lessons)
        for i, p in enumerate(chp):
            D.pagebreak()
            problem(D, p)
    if not first:
        front.appendix(D, D.short + ' · CHƯƠNG %d. %s' % (prev[0], prev[1]))
    os.makedirs(os.path.join(ROOT, 'out'), exist_ok=True)
    out = os.path.join(ROOT, 'out', 'SoHoc_Tap3_HuongDanGiai.docx')
    D.save(out, D.short + ' · PHỤ LỤC')
    print('saved', out, len(D.images), 'images')


if __name__ == '__main__':
    main()
