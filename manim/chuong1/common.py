"""Thành phần dùng chung cho video Chương 1 — Nền tảng quy hoạch động.

Khung hình dọc TikTok 1080x1920 (9:16). Đơn vị Manim: rộng 9, cao 16,
gốc tọa độ ở giữa màn hình.

Vùng an toàn (tránh giao diện TikTok):
  * trên cùng  y > 6.6  : thanh "Đang theo dõi / Dành cho bạn"
  * bên phải   x > 3.4  : cột nút tim / bình luận / chia sẻ
  * dưới cùng  y < -4.0 : dải phụ đề + tên kênh, mô tả
Nội dung chính nằm trong khung x ∈ [-4.1, 3.4], y ∈ [-3.9, 6.5].

Mỗi câu thuyết minh được khai báo bằng ``with self.voice("..."):``.
Thời lượng câu được ước lượng theo số âm tiết (tốc độ đọc thong thả),
các hoạt cảnh bên trong khối ``with`` chạy trong thời gian đó, phần dư
được bù bằng ``wait``. Khi cảnh kết thúc, danh sách câu (thời điểm bắt
đầu/kết thúc) được ghi ra JSON để ``build.py`` ghép thành tệp .srt.
"""

from __future__ import annotations

import json
import os
import re
from contextlib import contextmanager
from pathlib import Path

from manim import *  # noqa: F401,F403

# ----------------------------------------------------------------------------
# Cấu hình khung hình
# ----------------------------------------------------------------------------
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.frame_rate = 30
if os.environ.get("PREVIEW"):
    # bản nháp nhanh để kiểm tra bố cục
    config.pixel_width = 540
    config.pixel_height = 960
    config.frame_rate = 10
config.background_color = "#0B1220"

FONT = "Inter"
MONO = "DejaVu Sans Mono"

# Bảng màu
BG = "#0B1220"
PANEL = "#141E33"
PANEL_2 = "#1C2944"
INK = "#E8EEF9"
MUTED = "#8FA3C4"
ACCENT = "#FFD166"   # vàng: ô đang tính / điểm nhấn
GOOD = "#4ADE80"     # xanh lá: ô nguồn, đúng
BLUEC = "#60A5FA"    # xanh dương
BAD = "#F87171"      # đỏ: đá trơn, sai, ô cấm
ORANGE = "#FB923C"
PURPLE = "#C084FC"
WATER = "#1D4E89"
STONE = "#9AA5B1"

SAFE_TOP = 6.5
SAFE_BOTTOM = -3.9
SAFE_LEFT = -4.1
SAFE_RIGHT = 3.4
CENTER_X = (SAFE_LEFT + SAFE_RIGHT) / 2  # ≈ -0.35

SUB_DIR = Path(os.environ.get("SUB_DIR", Path(__file__).parent / "build" / "subs"))

# Tốc độ đọc (âm tiết / giây) và khoảng nghỉ cuối câu.
SYLLABLES_PER_SECOND = 3.6
PAUSE = 0.45


def syllable_count(text: str) -> int:
    """Ước lượng số âm tiết khi đọc to một câu tiếng Việt."""
    count = 0
    for token in re.findall(r"[\wÀ-ỹ]+|[^\s\w]", text):
        if re.fullmatch(r"\d+", token):
            # số nhiều chữ số đọc dài hơn: "một nghìn không trăm..."
            count += max(1, min(len(token), 7))
        elif re.fullmatch(r"[\wÀ-ỹ]+", token):
            count += 1
    return count


def speech_duration(text: str) -> float:
    return syllable_count(text) / SYLLABLES_PER_SECOND + PAUSE


# ----------------------------------------------------------------------------
# Hàm dựng hình tiện ích
# ----------------------------------------------------------------------------
MAX_W = 7.5


def _fit(m, max_width):
    if max_width and m.width > max_width:
        m.scale_to_fit_width(max_width)
    return m


def T(text, size=34, color=INK, weight=NORMAL, font=FONT, max_width=MAX_W, **kw):
    """Text tiếng Việt, tự thu nhỏ nếu rộng quá vùng an toàn."""
    return _fit(Text(text, font=font, font_size=size, color=color, weight=weight, **kw), max_width)


def TB(text, size=34, color=INK, **kw):
    return T(text, size=size, color=color, weight=BOLD, **kw)


def M(text, size=34, color=INK, max_width=MAX_W, **kw):
    """Chữ đơn cách (công thức, code ngắn)."""
    return _fit(Text(text, font=MONO, font_size=size, color=color, **kw), max_width)


def rich(markup, size=34, color=INK, font=FONT, max_width=MAX_W, **kw):
    """MarkupText (Pango) để tô màu từng phần trong một dòng."""
    return _fit(MarkupText(markup, font=font, font_size=size, color=color, **kw), max_width)


def placeholder(w=6.0, h=1.0):
    """Ô giữ chỗ vô hình trong bố cục."""
    return Rectangle(width=w, height=h, stroke_opacity=0, fill_opacity=0)


def fit_stack(*mobs, buff=0.45, top=5.15, bottom=-3.8, max_w=7.5, max_scale=1.45, center_x=None):
    """Xếp các khối theo chiều dọc rồi phóng to/thu nhỏ để lấp đầy vùng nội dung.

    Trả về hệ số phóng (để tạo thêm đối tượng cùng cỡ về sau)."""
    g = VGroup(*mobs).arrange(DOWN, buff=buff)
    avail = top - bottom
    s = min(max_w / g.width, avail / g.height, max_scale)
    g.scale(s)
    # Nếu bị giới hạn bởi chiều rộng: giãn khoảng cách để nội dung trải đều theo chiều dọc
    if len(mobs) > 1 and g.height < avail * 0.85:
        extra = (avail * 0.85 - g.height) / (len(mobs) - 1)
        g.arrange(DOWN, buff=min(buff * s + extra, buff * s * 2.2))
    g.move_to([CENTER_X if center_x is None else center_x, (top + bottom) / 2, 0])
    return s


def wrap_lines(lines, size=32, color=INK, buff=0.18, align=LEFT, markup=False, font=FONT):
    mobs = []
    for l in lines:
        if l == "":
            # dòng trống: khoảng đệm vô hình
            mobs.append(Rectangle(width=0.01, height=size * 0.004, stroke_opacity=0, fill_opacity=0))
        elif markup:
            mobs.append(rich(l, size=size, color=color, font=font))
        else:
            mobs.append(T(l, size=size, color=color, font=font))
    return VGroup(*mobs).arrange(DOWN, aligned_edge=align, buff=buff)


def panel(mob, color=PANEL, stroke=MUTED, pad=0.35, radius=0.25, stroke_width=1.5, width=None):
    if width is not None and mob.width > width - 2 * pad:
        mob.scale_to_fit_width(width - 2 * pad)
    w = width if width is not None else mob.width + 2 * pad
    box = RoundedRectangle(
        width=w, height=mob.height + 2 * pad, corner_radius=radius,
        fill_color=color, fill_opacity=1, stroke_color=stroke, stroke_width=stroke_width,
    )
    box.move_to(mob)
    return VGroup(box, mob)


def tag_box(title, body_lines, accent=ACCENT, width=7.2, size=30, title_size=30, markup=False):
    """Hộp kiểu sách: dải tiêu đề màu + nội dung. width là chiều rộng TỐI ĐA; hộp ôm sát nội dung."""
    title_mob = TB(title, size=title_size, color=BG, max_width=width - 0.4)
    body = wrap_lines(body_lines, size=size, markup=markup)
    if body.width > width - 0.6:
        body.scale_to_fit_width(width - 0.6)
    width = min(width, max(body.width + 0.6, title_mob.width + 0.6))
    head = RoundedRectangle(width=width, height=title_mob.height + 0.35, corner_radius=0.18,
                            fill_color=accent, fill_opacity=1, stroke_width=0)
    title_mob.move_to(head)
    body_box = RoundedRectangle(width=width, height=body.height + 0.6, corner_radius=0.18,
                                fill_color=PANEL, fill_opacity=1, stroke_color=accent, stroke_width=2)
    body_box.next_to(head, DOWN, buff=-0.12)
    body.move_to(body_box).align_to(body_box, LEFT).shift(RIGHT * 0.3)
    return VGroup(body_box, head, title_mob, body)


def cell(value="", w=0.8, h=0.8, fill=PANEL_2, stroke=MUTED, size=34, color=INK, sw=2):
    sq = Rectangle(width=w, height=h, fill_color=fill, fill_opacity=1, stroke_color=stroke, stroke_width=sw)
    txt = TB(str(value), size=size, color=color) if value != "" else VGroup()
    if isinstance(txt, Text) and txt.width > w * 0.86:
        txt.scale_to_fit_width(w * 0.86)
    txt.move_to(sq)
    return VGroup(sq, txt)


def array_row(values, w=0.8, h=0.8, size=34, index_from=0, show_index=True, index_color=MUTED,
              index_size=22, label=None, label_size=30):
    cells = VGroup(*[cell(v, w=w, h=h, size=size) for v in values]).arrange(RIGHT, buff=0)
    group = VGroup(cells)
    idx = VGroup()
    if show_index:
        for k, c in enumerate(cells):
            t = T(str(index_from + k), size=index_size, color=index_color)
            t.next_to(c, UP, buff=0.1)
            idx.add(t)
        group.add(idx)
    lab = VGroup()
    if label:
        lab = TB(label, size=label_size, color=ACCENT)
        lab.next_to(cells, LEFT, buff=0.25)
        group.add(lab)
    group.cells = cells
    group.idx = idx
    group.lab = lab
    return group


def set_cell_value(c, value, color=INK, size=None):
    """Trả về Text mới đặt đúng chỗ của ô c (để Transform). Cỡ chữ theo chiều cao ô."""
    if size is None:
        size = c[0].height * 42
    t = TB(str(value), size=size, color=color)
    w = c[0].width
    if t.width > w * 0.86:
        t.scale_to_fit_width(w * 0.86)
    t.move_to(c[0])
    return t


def code_block(src, size=22, width=MAX_W, line_numbers=False):
    """Khối code C++ tô màu bằng pygments (không cần LaTeX)."""
    code = Code(
        code_string=src.strip("\n"),
        language="cpp",
        formatter_style="monokai",
        background="rectangle",
        add_line_numbers=line_numbers,
        background_config={"fill_color": "#0F172A", "stroke_color": "#334155", "stroke_width": 2},
        paragraph_config={"font": MONO, "font_size": size},
    )
    if width is not None and code.width > width:
        code.scale_to_fit_width(width)
    return code


def big_arrow(start, end, color=ACCENT, sw=6, tip=0.25):
    return Arrow(start, end, buff=0.08, color=color, stroke_width=sw, max_tip_length_to_length_ratio=0.35,
                 tip_length=tip)


def jump_arc(p1, p2, color=ACCENT, height=0.9, sw=6):
    return ArcBetweenPoints(p1, p2, angle=-PI * 0.65, color=color, stroke_width=sw)


# ----------------------------------------------------------------------------
# Vẽ dòng suối, hòn đá, chú ếch
# ----------------------------------------------------------------------------
def make_water(width=8.4, height=2.2):
    water = RoundedRectangle(width=width, height=height, corner_radius=0.3, fill_color=WATER,
                             fill_opacity=1, stroke_width=0)
    waves = VGroup()
    for row in range(3):
        y = -height / 2 + (row + 0.7) * height / 3.3
        for k in range(6):
            x = -width / 2 + 0.5 + k * width / 6 + (0.35 if row % 2 else 0)
            w = ArcBetweenPoints([x, y, 0], [x + 0.5, y, 0], angle=-PI / 3, color="#3B82C4",
                                 stroke_width=3)
            waves.add(w)
    return VGroup(water, waves)


def make_stone(label, slippery=False, r=0.42, bank=False):
    if bank:
        body = RoundedRectangle(width=0.95, height=0.95, corner_radius=0.2, fill_color="#6B8E4E",
                                fill_opacity=1, stroke_color="#A3C77A", stroke_width=3)
    else:
        body = Ellipse(width=2 * r * 1.15, height=2 * r * 0.95, fill_color=STONE, fill_opacity=1,
                       stroke_color="#CBD5E1", stroke_width=3)
    group = VGroup(body)
    if slippery:
        body.set_fill("#B91C1C")
        body.set_stroke(BAD, 4)
        moss = VGroup(*[Dot(radius=0.06, color="#4D7C0F").move_to(body.get_center() + [dx, dy, 0])
                        for dx, dy in [(-0.18, 0.12), (0.15, 0.16), (0.02, -0.15), (0.22, -0.05)]])
        group.add(moss)
    num = TB(str(label), size=30, color=BG if not slippery else INK)
    num.move_to(body)
    group.add(num)
    group.body = body
    group.num = num
    return group


def make_frog(scale=1.0):
    body = Ellipse(width=0.62, height=0.5, fill_color="#22C55E", fill_opacity=1, stroke_color="#14532D",
                   stroke_width=3)
    eyes = VGroup()
    for dx in (-0.16, 0.16):
        white = Circle(radius=0.1, fill_color=WHITE, fill_opacity=1, stroke_color="#14532D", stroke_width=2)
        white.move_to(body.get_top() + [dx, 0.0, 0])
        pupil = Dot(radius=0.045, color=BLACK).move_to(white.get_center() + [0, 0.01, 0])
        eyes.add(white, pupil)
    smile = ArcBetweenPoints([-0.12, -0.05, 0], [0.12, -0.05, 0], angle=PI / 2.5, color="#14532D",
                             stroke_width=3)
    smile.move_to(body.get_center() + [0, -0.06, 0])
    frog = VGroup(body, eyes, smile).scale(scale)
    return frog


def stream_with_stones(n=5, slippery=(3,), spacing=1.22, y=0.0, labels=None):
    water = make_water(width=spacing * (n + 0.4) + 0.4)
    stones = VGroup()
    for i in range(n + 1):
        lab = labels[i] if labels else i
        s = make_stone(lab, slippery=(i in slippery), bank=(i == 0 or i == n))
        s.move_to([(i - n / 2) * spacing, 0, 0])
        stones.add(s)
    water.move_to(stones)
    # khoảng trống vô hình phía trên để chừa chỗ cho các cung nhảy
    spacer = Rectangle(width=0.1, height=0.75, stroke_opacity=0, fill_opacity=0)
    spacer.next_to(water, UP, buff=0)
    g = VGroup(water, stones, spacer).move_to([CENTER_X, y, 0])
    g.water = water
    g.stones = stones
    return g


def hop(scene, mob, target, height=1.2, run_time=0.5):
    """Ếch nhảy theo đường cong parabol."""
    start = mob.get_center()
    end = target
    path = ArcBetweenPoints(start, end, angle=-PI / 1.6)
    scene.play(MoveAlongPath(mob, path), run_time=run_time, rate_func=smooth)


# ----------------------------------------------------------------------------
# Scene có thuyết minh
# ----------------------------------------------------------------------------
class NarratedScene(Scene):
    """Scene ghi lại mốc thời gian của từng câu thuyết minh."""

    lesson_tag = ""   # ví dụ "BÀI 1"
    lesson_title = ""

    def setup(self):
        self._subs: list[dict] = []
        self._header = None

    # -- thuyết minh -----------------------------------------------------------
    @contextmanager
    def voice(self, text: str, min_duration: float = 0.0):
        start = self.renderer.time
        target = max(speech_duration(text), min_duration)
        yield target
        elapsed = self.renderer.time - start
        if elapsed < target - 1e-3:
            self.wait(target - elapsed)
        self._subs.append({"start": start, "end": self.renderer.time, "text": text})

    def say(self, text: str, *animations, run_time: float | None = None, **play_kw):
        """Một câu thuyết minh + (tuỳ chọn) một nhóm hoạt cảnh chạy song song."""
        with self.voice(text) as dur:
            if animations:
                rt = run_time if run_time is not None else min(dur * 0.8, 2.0)
                self.play(*animations, run_time=rt, **play_kw)

    def tear_down(self):
        SUB_DIR.mkdir(parents=True, exist_ok=True)
        out = SUB_DIR / f"{type(self).__name__}.json"
        out.write_text(json.dumps({"duration": self.renderer.time, "subs": self._subs},
                                  ensure_ascii=False, indent=1), encoding="utf-8")
        super().tear_down()

    # -- khung trình bày --------------------------------------------------------
    def header(self, section: str = ""):
        """Thanh tiêu đề bài học ở đầu khung (dưới vùng giao diện TikTok)."""
        tag = TB(self.lesson_tag, size=26, color=BG)
        tag_bg = RoundedRectangle(width=tag.width + 0.4, height=0.55, corner_radius=0.27,
                                  fill_color=ACCENT, fill_opacity=1, stroke_width=0)
        tag.move_to(tag_bg)
        pill = VGroup(tag_bg, tag)
        title = TB(self.lesson_title, size=28, color=INK)
        row = VGroup(pill, title).arrange(RIGHT, buff=0.25)
        if row.width > SAFE_RIGHT - SAFE_LEFT:
            row.scale_to_fit_width(SAFE_RIGHT - SAFE_LEFT)
        row.move_to([CENTER_X, 6.2, 0])
        sec = T(section, size=26, color=MUTED, max_width=7.4) if section else VGroup()
        if section:
            sec.next_to(row, DOWN, buff=0.18)
        grp = VGroup(row, sec)
        return grp

    def show_header(self, section=""):
        new = self.header(section)
        if self._header is None:
            self.play(FadeIn(new, shift=DOWN * 0.3), run_time=0.6)
        else:
            self.play(ReplacementTransform(self._header, new), run_time=0.6)
        self._header = new
        return new

    def section_title(self, number: str, title: str, subtitle: str = ""):
        """Thẻ chuyển mục lớn ở giữa màn hình."""
        num = TB(number, size=90, color=ACCENT)
        ttl = TB(title, size=46, color=INK)
        if ttl.width > 7.3:
            ttl = Paragraph(*self._split(title, 18), font=FONT, font_size=46, color=INK,
                            alignment="center", weight=BOLD)
        grp = VGroup(num, ttl)
        if subtitle:
            sub = T(subtitle, size=30, color=MUTED)
            if sub.width > 7.3:
                sub.scale_to_fit_width(7.3)
            grp.add(sub)
        grp.arrange(DOWN, buff=0.35).move_to([CENTER_X, 1.3, 0])
        line = Line([CENTER_X - 2, 0, 0], [CENTER_X + 2, 0, 0], color=ACCENT, stroke_width=4)
        line.next_to(grp, DOWN, buff=0.4)
        return VGroup(grp, line)

    @staticmethod
    def _split(text, n):
        words, lines, cur = text.split(), [], ""
        for w in words:
            if len(cur) + len(w) + 1 > n and cur:
                lines.append(cur)
                cur = w
            else:
                cur = (cur + " " + w).strip()
        if cur:
            lines.append(cur)
        return lines

    def clear_body(self, keep=(), run_time=0.6):
        """Xoá mọi thứ trừ thanh tiêu đề và các đối tượng trong keep."""
        keep_set = set(keep)
        if self._header is not None:
            keep_set.add(self._header)
        olds = [m for m in self.mobjects if m not in keep_set]
        if olds:
            self.play(*[FadeOut(m) for m in olds], run_time=run_time)
