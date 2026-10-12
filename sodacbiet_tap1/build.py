#!/usr/bin/env python3
"""Dựng Số đặc biệt và cấu trúc chữ số · Tập 1. Dùng: python3 build.py [figs] [số bài ...]"""
import sys, os, json, importlib.util
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, ROOT)
from lt import LDoc
import book

OUT = os.path.join(ROOT, 'out', 'SoDacBiet_Tap1_LyThuyet.docx')


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class Ctx:
    def __init__(self, D, n):
        self.D = D
        self.dir = os.path.join(ROOT, 'problems', str(n))
        sp = os.path.join(self.dir, 'scores.json')
        self.scores = json.load(open(sp)) if os.path.exists(sp) else {}

    def fig(self, name):
        return os.path.join(self.dir, 'fig', name + '.png')

    def src(self, name):
        return open(os.path.join(self.dir, name), encoding='utf-8').read()


def make_figs(n):
    d = os.path.join(ROOT, 'problems', str(n))
    if not os.path.exists(os.path.join(d, 'figs.py')):
        return
    sys.path.insert(0, d)
    m = load(os.path.join(d, 'figs.py'), 'figs_%d' % n)
    os.makedirs(os.path.join(d, 'fig'), exist_ok=True)
    m.make(lambda name: os.path.join(d, 'fig', name + '.png'))
    sys.path.remove(d)


def lesson(D, n):
    title, _ = book.LESSONS[n]
    D.lesson(n, title)
    m = load(os.path.join(ROOT, 'problems', str(n), 'content.py'), 'content_%d' % n)
    m.build(D, Ctx(D, n))


def main():
    args = sys.argv[1:]
    figs = 'figs' in args
    only = [int(a) for a in args if a.isdigit()]
    have = [n for n in book.LESSONS if os.path.exists(os.path.join(ROOT, 'problems', str(n), 'content.py'))]
    ls = [n for n in have if not only or n in only]
    if figs:
        if not only and os.path.exists(os.path.join(ROOT, 'assets', 'cover.py')):
            load(os.path.join(ROOT, 'assets', 'cover.py'), 'cover').make(os.path.join(ROOT, 'assets', 'cover.png'))
        for n in ls:
            make_figs(n)
    D = LDoc(os.path.join(ROOT, 'template'), book.SHORT)
    import front
    pm = os.path.join(ROOT, 'out', 'pagemap.json')
    if os.path.exists(pm):
        D.pagemap = json.load(open(pm))
    front.cover(D)
    front.intro(D)
    prev = None
    for num, title, lessons in book.CHAPTERS:
        chl = [n for n in lessons if n in ls]
        if not chl:
            continue
        D.section_break(D.short if prev is None else D.short + ' · CHƯƠNG %d. %s' % prev)
        prev = (num, title)
        front.chapter(D, num, title, lessons)
        for n in chl:
            D.pagebreak()
            lesson(D, n)
    front.appendix(D, D.short + ' · CHƯƠNG %d. %s' % prev if prev else D.short)
    os.makedirs(os.path.join(ROOT, 'out'), exist_ok=True)
    D.save(OUT, D.short + ' · PHỤ LỤC')
    print('saved', OUT, len(D.images), 'images')


if __name__ == '__main__':
    main()
