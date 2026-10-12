"""Thư viện vẽ hình dùng chung cho Tập 3 (cùng bảng màu với Tập 1, Tập 2)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle, FancyArrowPatch, Circle
import os

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['mathtext.fontset'] = 'dejavusans'

NAVY = '#1F3864'
RED = '#C0504D'
DRED = '#C00000'
GREEN = '#548235'
PURPLE = '#6A4C93'
ORANGE = '#C55A11'
GRAY = '#7F7F7F'
BLUE = '#2E75B6'

KIND = {
    'ans':    ('#FFE699', DRED, 1.8),
    'done':   ('#DEEBF7', BLUE, 1.0),
    'in':     ('#FBE5D6', ORANGE, 1.0),
    'gray':   ('#EDEDED', '#A6A6A6', 1.0),
    'plain':  ('#FFFFFF', '#7F7F7F', 1.0),
    'green':  ('#E2F0D9', GREEN, 1.0),
    'purple': ('#EDE5F5', PURPLE, 1.0),
    'yellow': ('#FFF2CC', '#BF9000', 1.0),
    'pink':   ('#F8DEDD', RED, 1.0),
    'navy':   ('#1F3864', '#1F3864', 1.0),
    'dblue':  ('#9DC3E6', BLUE, 1.0),
}

FIGDIR = None


def new(w, h):
    fig = plt.figure(figsize=(w, h), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.set_aspect('equal')
    ax.axis('off')
    return fig, ax


def save(fig, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fig.savefig(path, dpi=200, facecolor='white')
    plt.close(fig)


def cell(ax, x, y, w, h, text='', kind='plain', fs=10, bold=False, color=None, ha='center', lw=None, ls='-', z=2):
    fc, ec, l = KIND[kind]
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, lw=lw or l, ls=ls, zorder=z))
    if text != '' and text is not None:
        tc = color or ('white' if kind == 'navy' else '#1A1A1A')
        tx = x + w / 2 if ha == 'center' else x + 0.06
        ax.text(tx, y + h / 2, str(text), ha=ha, va='center', fontsize=fs,
                fontweight='bold' if bold else 'normal', color=tc, zorder=z + 1)


def rbox(ax, x, y, w, h, text='', kind='done', fs=10, bold=False, color=None, r=0.08, lw=None):
    fc, ec, l = KIND[kind]
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=%g' % r,
                                facecolor=fc, edgecolor=ec, lw=lw or l, zorder=2))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha='center', va='center', fontsize=fs,
                fontweight='bold' if bold else 'normal', color=color or '#1A1A1A', zorder=3)


def txt(ax, x, y, s, fs=10, color='#1A1A1A', ha='center', va='center', bold=False, italic=False, **kw):
    ax.text(x, y, s, fontsize=fs, color=color, ha=ha, va=va,
            fontweight='bold' if bold else 'normal', style='italic' if italic else 'normal', zorder=5, **kw)


def arrow(ax, p, q, color=NAVY, lw=1.2, style='-|>', rad=0.0, ms=10, ls='-', z=4):
    a = FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                        connectionstyle='arc3,rad=%g' % rad, linestyle=ls, zorder=z, shrinkA=0, shrinkB=0)
    ax.add_patch(a)


def line(ax, pts, color=NAVY, lw=1.2, ls='-', z=3):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=z, solid_capstyle='round')


def polyarrow(ax, pts, color=NAVY, lw=1.2):
    if len(pts) > 2:
        line(ax, pts[:-1], color=color, lw=lw)
    arrow(ax, pts[-2], pts[-1], color=color, lw=lw)


# ---------------------------------------------------------------- sơ đồ khối
FC_STYLE = {
    'start': ('#DEEBF7', NAVY, 'round'),
    'end':   ('#DEEBF7', NAVY, 'round'),
    'proc':  ('#F8DEDD', RED, 'rect'),
    'dec':   ('#FFF2CC', '#BF9000', 'diamond'),
    'io':    ('#E2F0D9', GREEN, 'para'),
    'note':  ('#FFFFFF', NAVY, 'rect'),
    'sub':   ('#EDE5F5', PURPLE, 'rect'),
}


class Flow:
    """Sơ đồ khối: đặt nút theo tọa độ tâm (đơn vị inch), nối bằng mũi tên."""

    def __init__(self, fs=9.5):
        self.nodes = {}
        self.edges = []
        self.labels = []
        self.fs = fs

    def node(self, nid, kind, text, x, y, w=None, h=None):
        n = max(len(l) for l in text.split('\n'))
        lines = text.count('\n') + 1
        if w is None:
            w = 0.075 * n * self.fs / 9.5 + (0.75 if kind == 'dec' else 0.38)
        if h is None:
            h = (0.36 + 0.17 * (lines - 1)) * (1.45 if kind == 'dec' else 1.0)
        self.nodes[nid] = dict(kind=kind, text=text, x=x, y=y, w=w, h=h)
        return self

    def anchor(self, nid, side):
        n = self.nodes[nid]
        x, y, w, h = n['x'], n['y'], n['w'], n['h']
        return {'t': (x, y + h / 2), 'b': (x, y - h / 2), 'l': (x - w / 2, y), 'r': (x + w / 2, y)}[side]

    def edge(self, a, b, sa='b', sb='t', via=(), label=None, lpos=None, lcolor=None):
        self.edges.append((a, b, sa, sb, list(via), label, lpos, lcolor))
        return self

    def draw(self, path, pad=0.12):
        xs = []; ys = []
        for n in self.nodes.values():
            xs += [n['x'] - n['w'] / 2, n['x'] + n['w'] / 2]
            ys += [n['y'] - n['h'] / 2, n['y'] + n['h'] / 2]
        for e in self.edges:
            for p in e[4]:
                xs.append(p[0]); ys.append(p[1])
        x0, x1, y0, y1 = min(xs) - pad - 0.15, max(xs) + pad + 0.15, min(ys) - pad, max(ys) + pad
        W, H = x1 - x0, y1 - y0
        fig = plt.figure(figsize=(W, H), dpi=200)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(x0, x1); ax.set_ylim(y0, y1); ax.set_aspect('equal'); ax.axis('off')
        for n in self.nodes.values():
            fc, ec, shape = FC_STYLE[n['kind']]
            x, y, w, h = n['x'], n['y'], n['w'], n['h']
            if shape == 'round':
                ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle='round,pad=0,rounding_size=%g' % (h / 2.2),
                                            facecolor=fc, edgecolor=ec, lw=1.3, zorder=2))
            elif shape == 'rect':
                ax.add_patch(Rectangle((x - w / 2, y - h / 2), w, h, facecolor=fc, edgecolor=ec, lw=1.2, zorder=2))
            elif shape == 'diamond':
                ax.add_patch(Polygon([(x - w / 2, y), (x, y + h / 2), (x + w / 2, y), (x, y - h / 2)], closed=True,
                                     facecolor=fc, edgecolor=ec, lw=1.2, zorder=2))
            elif shape == 'para':
                s = 0.12
                ax.add_patch(Polygon([(x - w / 2 + s, y + h / 2), (x + w / 2 + s, y + h / 2), (x + w / 2 - s, y - h / 2),
                                      (x - w / 2 - s, y - h / 2)], closed=True, facecolor=fc, edgecolor=ec, lw=1.2, zorder=2))
            bold = n['kind'] in ('start', 'end')
            ax.text(x, y, n['text'], ha='center', va='center', fontsize=self.fs, color='#1A1A1A',
                    fontweight='bold' if bold else 'normal', zorder=3, linespacing=1.25)
        for a, b, sa, sb, via, label, lpos, lcolor in self.edges:
            p = self.anchor(a, sa); q = self.anchor(b, sb)
            pts = [p] + via + [q]
            polyarrow(ax, pts)
            if label:
                if lpos is None:
                    (px, py), (qx, qy) = pts[0], pts[1]
                    if abs(py - qy) < 1e-6:
                        lpos = ((px + qx) / 2, py + 0.09)
                    else:
                        lpos = (px + 0.2, py - 0.13)
                col = lcolor or (GREEN if label.startswith('Đ') else RED if label.startswith('S') else NAVY)
                ax.text(lpos[0], lpos[1], label, fontsize=self.fs - 1.5, color=col, fontweight='bold', ha='center', va='center', zorder=6)
        save(fig, path)


def chain(fl, items, x=0, y0=0, dy=0.62):
    """Thêm một dãy nút thẳng đứng; items = [(id, kind, text)]. Trả về y cuối."""
    y = y0
    prev = None
    for nid, kind, text in items:
        fl.node(nid, kind, text, x, y)
        if prev:
            fl.edge(prev, nid)
        prev = nid
        y -= dy
    return y + dy
