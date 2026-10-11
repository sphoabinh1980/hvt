"""BÀI 3 — Quy hoạch động trên lưới và truy vết (THUHOACH)."""

from math import comb

from common import *  # noqa: F401,F403
from bai1 import list_cards, line_box

GRID = [[2, 3, -1, -1, 4],
        [8, 7, 5, 7, 4],
        [9, 1, 1, 8, 6],
        [2, 5, 2, 7, 6]]
ROWS, COLS = len(GRID), len(GRID[0])
NEG = None


def solve_best(g):
    m, n = len(g), len(g[0])
    best = [[NEG] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if g[i][j] < 0:
                continue
            if i == 0 and j == 0:
                best[i][j] = g[0][0]
                continue
            c = [x for x in [best[i - 1][j] if i > 0 else NEG, best[i][j - 1] if j > 0 else NEG] if x is not None]
            if c:
                best[i][j] = max(c) + g[i][j]
    return best


def solve_ways(g):
    m, n = len(g), len(g[0])
    ways = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if g[i][j] < 0:
                continue
            ways[i][j] = 1 if (i, j) == (0, 0) else (ways[i - 1][j] if i else 0) + (ways[i][j - 1] if j else 0)
    return ways


def trace(best, g):
    i, j = len(g) - 1, len(g[0]) - 1
    steps = []  # (from_cell, to_cell, letter, need)
    while (i, j) != (0, 0):
        need = best[i][j] - g[i][j]
        if i > 0 and best[i - 1][j] == need:
            steps.append(((i, j), (i - 1, j), "D", need))
            i -= 1
        else:
            steps.append(((i, j), (i, j - 1), "R", need))
            j -= 1
    return steps


def greedy(g):
    i = j = 0
    path, total = [(0, 0)], g[0][0]
    while (i, j) != (len(g) - 1, len(g[0]) - 1):
        opts = []
        if i + 1 < len(g) and g[i + 1][j] >= 0:
            opts.append((g[i + 1][j], 1, 0))
        if j + 1 < len(g[0]) and g[i][j + 1] >= 0:
            opts.append((g[i][j + 1], 0, 1))
        _, di, dj = max(opts)
        i, j = i + di, j + dj
        path.append((i, j))
        total += g[i][j]
    return path, total


BEST = solve_best(GRID)
WAYS = solve_ways(GRID)
STEPS = trace(BEST, GRID)
BEST_PATH = [(0, 0)]
for s in reversed(STEPS):
    BEST_PATH.append(s[0])
LETTERS = "".join(s[2] for s in reversed(STEPS))
GREEDY_PATH, GREEDY_TOTAL = greedy(GRID)
assert BEST[3][4] == 50 and LETTERS == "DRRRDDR" and WAYS[3][4] == 25 and GREEDY_TOTAL == 41


class B3Scene(NarratedScene):
    lesson_tag = "BÀI 3"
    lesson_title = "Quy hoạch động trên lưới và truy vết"


def make_apple(scale=1.0):
    body = Circle(radius=0.13, fill_color="#EF4444", fill_opacity=1, stroke_width=0)
    leaf = Ellipse(width=0.12, height=0.06, fill_color="#22C55E", fill_opacity=1, stroke_width=0)
    leaf.move_to(body.get_top() + [0.05, 0.02, 0]).rotate(PI / 6)
    return VGroup(body, leaf).scale(scale)


def make_rock(size=0.9):
    pts = [[-0.4, -0.25, 0], [-0.3, 0.15, 0], [-0.05, 0.3, 0], [0.25, 0.22, 0], [0.42, -0.05, 0], [0.3, -0.28, 0]]
    rock = Polygon(*pts, fill_color="#6B7280", fill_opacity=1, stroke_color="#D1D5DB", stroke_width=2)
    return rock.scale(size / 1.0)


def make_robot(scale=1.0):
    head = RoundedRectangle(width=0.55, height=0.45, corner_radius=0.1, fill_color="#93C5FD", fill_opacity=1,
                            stroke_color="#1E3A8A", stroke_width=3)
    eyes = VGroup(*[Dot(radius=0.05, color="#1E3A8A").move_to(head.get_center() + [dx, 0.04, 0]) for dx in (-0.12, 0.12)])
    mouth = Line([-0.1, -0.1, 0], [0.1, -0.1, 0], color="#1E3A8A", stroke_width=3).move_to(head.get_center() + [0, -0.1, 0])
    ant = Line(head.get_top(), head.get_top() + UP * 0.15, color="#1E3A8A", stroke_width=3)
    bulb = Dot(radius=0.05, color=ACCENT).move_to(ant.get_end())
    return VGroup(head, eyes, mouth, ant, bulb).scale(scale)


class Grid(VGroup):
    """Lưới m×n; mỗi ô có số táo (góc) và vùng giá trị giữa ô."""

    def __init__(self, g, w=1.2, show_apples=True, corner=False):
        super().__init__()
        self.g = g
        self.w = w
        self.cells = {}
        self.marks = {}
        m, n = len(g), len(g[0])
        for i in range(m):
            for j in range(n):
                v = g[i][j]
                sq = Square(w, fill_color="#3F3F46" if v < 0 else "#14301F", fill_opacity=1,
                            stroke_color=MUTED, stroke_width=2)
                sq.move_to([j * w, -i * w, 0])
                if v < 0:
                    mark = make_rock(w * 0.8).move_to(sq)
                elif corner:
                    mark = VGroup(make_apple(0.75), TB(str(v), size=20, color=ORANGE)).arrange(RIGHT, buff=0.04)
                    mark.move_to(sq.get_corner(UL) + [0.27 * w, -0.14 * w, 0])
                else:
                    mark = VGroup(make_apple(1.1), TB(str(v), size=32, color=INK)).arrange(RIGHT, buff=0.08)
                    mark.move_to(sq)
                self.cells[(i, j)] = sq
                self.marks[(i, j)] = mark
                self.add(sq, mark)
        rlab = VGroup(*[T(str(i + 1), size=22, color=MUTED).next_to(self.cells[(i, 0)], LEFT, buff=0.12)
                        for i in range(m)])
        clab = VGroup(*[T(str(j + 1), size=22, color=MUTED).next_to(self.cells[(0, j)], UP, buff=0.1)
                        for j in range(n)])
        self.labels = VGroup(rlab, clab)
        self.add(self.labels)

    def center_of(self, ij):
        return self.cells[ij].get_center()

    def path_line(self, path, color=GOOD, sw=8):
        return VMobject(stroke_color=color, stroke_width=sw).set_points_as_corners([self.center_of(p) for p in path])


# ----------------------------------------------------------------------------
class B3_00_Intro(B3Scene):
    def construct(self):
        tag = TB("BÀI 3", size=80, color=ACCENT)
        ttl = VGroup(TB("Quy hoạch động trên lưới", size=48), TB("và truy vết", size=48)).arrange(DOWN, buff=0.15)
        line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Bảng phương án HAI CHIỀU, thứ tự điền",
            "✓ Ô cấm, ô không tới được: giá trị −∞",
            "✓ TRUY VẾT: chỉ ra đường đi tốt nhất",
            "✓ Đếm đường đi & tam giác Pascal",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit_stack(VGroup(tag, ttl, line).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Chào mừng các em đến với Bài 3: Quy hoạch động trên lưới và truy vết."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), run_time=1.5)
            self.play(GrowFromCenter(line), run_time=0.5)
        with self.voice("Học xong bài này, em sẽ xây dựng được bảng phương án hai chiều, chọn đúng thứ tự điền bảng, "
                        "và xử lí ô cấm bằng giá trị âm vô cùng."):
            self.play(FadeIn(goals[0:2], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Quan trọng hơn, em sẽ học truy vết: không chỉ tính được giá trị tốt nhất mà còn chỉ ra được "
                        "đường đi đạt giá trị đó. Cuối cùng là đếm số đường đi và mối liên hệ với tam giác Pascal."):
            self.play(FadeIn(goals[2:], shift=RIGHT * 0.3), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B3_01_KhoiDong(B3Scene):
    def construct(self):
        self.show_header("Khởi động: Robot hái táo")
        grid = Grid(GRID)
        story = VGroup(T("Robot chỉ đi SANG PHẢI hoặc ĐI XUỐNG,", size=30),
                       T("hái hết táo ở mỗi ô đi qua. Ô đá: cấm vào.", size=30)).arrange(DOWN, buff=0.12)
        start = T("Xuất phát", size=22, color=BLUEC)
        goal = T("Kho", size=22, color=GOOD)
        res_slot = placeholder(7.2, 1.3)
        sc = fit_stack(story, grid, res_slot, buff=0.6, max_scale=1.2)
        start.scale(sc).next_to(grid.cells[(0, 0)], UP, buff=0.35).shift(LEFT * 0.2)
        goal.scale(sc).next_to(grid.cells[(ROWS - 1, COLS - 1)], DOWN, buff=0.1)
        robot = make_robot(sc * 0.9).move_to(grid.center_of((0, 0)))
        with self.voice("Một chú robot nông trại đứng ở góc trên bên trái của một vườn táo hình chữ nhật, "
                        "cần đi tới kho ở góc dưới bên phải."):
            self.play(LaggedStart(*[FadeIn(grid.cells[k]) for k in grid.cells], lag_ratio=0.03), run_time=1.2)
            self.play(LaggedStart(*[FadeIn(grid.marks[k], scale=0.5) for k in grid.marks], lag_ratio=0.03),
                      FadeIn(grid.labels), run_time=1.2)
            self.play(FadeIn(robot, shift=DOWN * 0.3), FadeIn(start), FadeIn(goal), run_time=0.6)
        with self.voice("Robot chỉ biết sang phải hoặc đi xuống. Ô nào nó đi qua thì nó hái hết táo ở ô đó. "
                        "Một vài ô có tảng đá, robot không đi vào được."):
            self.play(FadeIn(story), run_time=0.8)
            self.play(*[Indicate(grid.marks[k], color=BAD) for k in grid.marks if GRID[k[0]][k[1]] < 0], run_time=1.0)
        with self.voice("Nếu em là người lập trình cho robot, em có dám để nó mỗi bước chọn ô kế bên có nhiều táo hơn không? "
                        "Hãy thử xem."):
            q = TB("Mỗi bước chọn ô kế bên nhiều táo hơn?", size=30, color=ORANGE).scale(sc).move_to(res_slot)
            self.play(FadeIn(q), run_time=0.6)
        # Tham lam
        gline = grid.path_line(GREEDY_PATH, color=ORANGE, sw=10)
        gsegs = []
        with self.voice("Ở ô 1 1, ô dưới có 8 quả hấp dẫn hơn ô phải có 3 quả. Ở ô 2 1, ô dưới có 9 quả lại hấp dẫn hơn. "
                        "Robot bị dụ xuống cột 1, rồi phải đi qua hàng 4 nghèo táo."):
            for k in range(1, len(GREEDY_PATH)):
                seg = Line(grid.center_of(GREEDY_PATH[k - 1]), grid.center_of(GREEDY_PATH[k]), color=ORANGE,
                           stroke_width=10)
                gsegs.append(seg)
                self.play(Create(seg), robot.animate.move_to(grid.center_of(GREEDY_PATH[k])), run_time=0.45)
            gt = TB(f"Tham lam: {GREEDY_TOTAL} quả", size=36, color=ORANGE).scale(sc).move_to(res_slot)
            self.play(Transform(q, gt), run_time=0.5)
        with self.voice("Tham lam chỉ được 41 quả."):
            self.play(Indicate(q, color=ORANGE), run_time=0.8)
        with self.voice("Đường tốt nhất phải chịu thiệt ở ô 3 1 bằng cách không xuống tiếp, để đi qua dải táo 7, 5, 7, 8, 7. "
                        "Kết quả: 50 quả!"):
            self.play(*[s.animate.set_stroke(opacity=0.25) for s in gsegs], robot.animate.move_to(grid.center_of((0, 0))),
                      run_time=0.5)
            for k in range(1, len(BEST_PATH)):
                seg = Line(grid.center_of(BEST_PATH[k - 1]), grid.center_of(BEST_PATH[k]), color=GOOD, stroke_width=10)
                self.play(Create(seg), robot.animate.move_to(grid.center_of(BEST_PATH[k])), run_time=0.45)
            bt = VGroup(TB("Tốt nhất: 50 quả", size=36, color=GOOD),
                        M("DRRRDDR", size=32, color=GOOD)).arrange(DOWN, buff=0.12).scale(sc).move_to(res_slot)
            self.play(Transform(q, bt), run_time=0.5)

        self.clear_body()
        self.show_header("1. Bài toán THUHOACH")
        box = tag_box("BÀI TOÁN: THUHOACH", [
            "Vườn m hàng, n cột. Ô (i, j) có aᵢⱼ quả táo,",
            "hoặc aᵢⱼ = −1 nếu có đá.",
            "Robot đi từ (1, 1) tới (m, n), mỗi bước",
            "sang phải (R) hoặc đi xuống (D).",
            "Tìm số táo LỚN NHẤT và chỉ ra MỘT đường đi.",
            "Không có đường: in −1.  (m, n ≤ 1000)",
        ], width=7.4, size=29)
        out = VGroup(T("Kết quả ví dụ:", size=30, color=MUTED), TB("50", size=40, color=ACCENT),
                     M("DRRRDDR", size=34, color=ACCENT)).arrange(RIGHT, buff=0.35)
        fit_stack(box, out, buff=0.8, max_scale=1.2)
        with self.voice("Phát biểu tổng quát, ta có bài toán THUHOACH. Vườn có m hàng, n cột. Ô i j có a i j quả táo, "
                        "hoặc trừ 1 nếu có đá. Robot xuất phát từ ô 1 1, mỗi bước sang phải hoặc đi xuống, cần tới ô m n."):
            self.play(FadeIn(box, shift=UP * 0.3), run_time=1.0)
        with self.voice("Hãy tìm số táo lớn nhất robot hái được, và chỉ ra một đường đi bằng xâu gồm các kí tự R, "
                        "sang phải, và D, đi xuống. Với ví dụ: 50 quả, đường đi D R R R D D R."):
            self.play(FadeIn(out), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B3_02_NgayTho(B3Scene):
    def construct(self):
        self.show_header("2. Ý tưởng ngây thơ: Thử mọi đường đi")
        idea = VGroup(T("Quay lui: từ mỗi ô thử cả hai hướng", size=30),
                      T("Thử(i+1, j)  và  Thử(i, j+1)", size=30, color=ACCENT)).arrange(DOWN, buff=0.15)
        word = VGroup(*[panel(TB(c, size=36, color=BG), color=(BLUEC if c == "D" else GOOD),
                              stroke=(BLUEC if c == "D" else GOOD), pad=0.15) for c in LETTERS]).arrange(RIGHT, buff=0.12)
        expl = VGroup(T("Mỗi đường đi = (m−1) chữ D + (n−1) chữ R,", size=28),
                      T("xếp theo thứ tự bất kì", size=28)).arrange(DOWN, buff=0.1)
        formula = TB("Số đường = C(m + n − 2, m − 1)", size=36, color=ACCENT)
        heads = ["Lưới", "Số đường đi"]
        data = [("4 × 5", "C(7, 3) = 35"), ("10 × 10", "C(18, 9) = 48 620"), ("20 × 20", "≈ 3,5·10¹⁰"),
                ("1000 × 1000", "gần 600 chữ số!")]
        table = VGroup()
        for r, (a, b) in enumerate([heads] + data):
            fill = ACCENT if r == 0 else (PANEL if r % 2 else PANEL_2)
            ca = Rectangle(width=2.6, height=0.75, fill_color=fill, fill_opacity=1, stroke_color=BG, stroke_width=2)
            cb = Rectangle(width=4.2, height=0.75, fill_color=fill, fill_opacity=1, stroke_color=BG, stroke_width=2)
            cb.next_to(ca, RIGHT, buff=0)
            col = BG if r == 0 else (BAD if r == 4 else INK)
            ta = (TB if r == 0 else T)(a, size=26, color=col).move_to(ca)
            tb = (TB if r == 0 else T)(b, size=26, color=col).move_to(cb)
            table.add(VGroup(ca, cb, ta, tb))
        table.arrange(DOWN, buff=0)
        assert comb(7, 3) == 35 and comb(18, 9) == 48620
        fit_stack(idea, word, expl, formula, table, buff=0.5, max_scale=1.2)
        with self.voice("Từ mỗi ô, robot có hai lựa chọn, nên ta viết một hàm quay lui thử cả hai: đi xuống và sang phải. "
                        "Khi tới đích thì cập nhật đáp án."):
            self.play(FadeIn(idea), run_time=0.8)
        with self.voice("Đếm số phép tính: mỗi đường đi gồm đúng m trừ 1 bước D và n trừ 1 bước R, xếp theo thứ tự bất kì."):
            self.play(LaggedStart(*[FadeIn(w, shift=DOWN * 0.2) for w in word], lag_ratio=0.12), run_time=1.2)
            self.play(FadeIn(expl), run_time=0.6)
        with self.voice("Số đường đi, khi không có đá, là số cách chọn vị trí cho m trừ 1 chữ D trong m cộng n trừ 2 bước: "
                        "tổ hợp chập m trừ 1 của m cộng n trừ 2."):
            self.play(FadeIn(formula), run_time=0.8)
        with self.voice("Lưới 4 nhân 5 có 35 đường. Lưới 10 nhân 10 có bốn mươi tám nghìn sáu trăm hai mươi đường. "
                        "Lưới 20 nhân 20 có khoảng ba mươi lăm tỉ đường."):
            for r in table[:4]:
                self.play(FadeIn(r, shift=UP * 0.15), run_time=0.45)
        with self.voice("Còn lưới 1000 nhân 1000, con số có gần 600 chữ số. Quay lui chỉ chạy được khi m cộng n không quá "
                        "khoảng 25."):
            self.play(FadeIn(table[4], shift=UP * 0.15), run_time=0.6)

        self.clear_body()
        self.show_header("Bế tắc: các đường đi dùng chung rất nhiều đoạn")
        grid = Grid(GRID)
        note = VGroup(T("Mọi đường đi qua ô (3, 4) đều có chung", size=30),
                      T("“phần đường từ (3, 4) tới đích”.", size=30, color=ACCENT),
                      T("Quay lui tính lại phần chung ấy cho TỪNG đường!", size=28, color=BAD)).arrange(DOWN, buff=0.15)
        q = TB("Làm sao để mỗi ô chỉ xử lí MỘT lần?", size=34, color=GOOD)
        fit_stack(grid, note, q, buff=0.6, max_scale=1.2)
        paths_to = [[(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3)],
                    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3)],
                    [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3)],
                    [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3)]]
        tail = [(2, 3), (3, 3), (3, 4)]
        cols = [BLUEC, PURPLE, ORANGE, "#F472B6"]
        with self.voice("Có quá nhiều đường đi. Nhưng các đường đi dùng chung rất nhiều đoạn."):
            self.play(FadeIn(grid), run_time=0.8)
            lines = VGroup(*[grid.path_line(p, color=c, sw=7) for p, c in zip(paths_to, cols)])
            self.play(LaggedStart(*[Create(l) for l in lines], lag_ratio=0.3), run_time=1.6)
        with self.voice("Mọi đường đi qua ô 3 4 đều có chung phần đường từ ô 3 4 tới đích. Quay lui tính lại phần đường "
                        "chung ấy cho từng đường đi tới ô 3 4."):
            tl = grid.path_line(tail, color=ACCENT, sw=12)
            self.play(Create(tl), Indicate(grid.cells[(2, 3)], color=ACCENT), run_time=1.0)
            self.play(FadeIn(note), run_time=0.8)
            for _ in range(2):
                self.play(tl.animate.set_stroke(opacity=0.2), run_time=0.3)
                self.play(tl.animate.set_stroke(opacity=1), run_time=0.3)
        with self.voice("Làm sao để mỗi ô chỉ phải xử lí một lần?"):
            self.play(Write(q), run_time=1.0)
        self.clear_body()


# ----------------------------------------------------------------------------
def best_text(v):
    return "−∞" if v is None else str(v)


class B3_03_CongThuc(B3Scene):
    def construct(self):
        self.show_header("3. Phá bế tắc: Bước cuối cùng tới ô (i, j)")
        defi = panel(VGroup(TB("best(i, j) =", size=34, color=ACCENT),
                            T("số táo lớn nhất trên một đường đi", size=30),
                            T("từ (1, 1) tới (i, j)", size=30)).arrange(DOWN, buff=0.1), stroke=ACCENT)
        # sơ đồ 2 ô nguồn
        w = 1.4
        c_ij = Square(w, fill_color=ACCENT, fill_opacity=0.9, stroke_color=INK, stroke_width=2)
        c_up = Square(w, fill_color=PANEL_2, fill_opacity=1, stroke_color=BLUEC, stroke_width=3).next_to(c_ij, UP, buff=0)
        c_lf = Square(w, fill_color=PANEL_2, fill_opacity=1, stroke_color=GOOD, stroke_width=3).next_to(c_ij, LEFT, buff=0)
        t_ij = TB("(i, j)", size=26, color=BG).move_to(c_ij)
        t_up = T("(i−1, j)", size=24).move_to(c_up)
        t_lf = T("(i, j−1)", size=24).move_to(c_lf)
        a_up = Arrow(c_up.get_center(), c_ij.get_center(), buff=0.35, color=BLUEC, stroke_width=6)
        a_lf = Arrow(c_lf.get_center(), c_ij.get_center(), buff=0.35, color=GOOD, stroke_width=6)
        l_up = T("đi xuống", size=24, color=BLUEC).next_to(c_up, RIGHT, buff=0.2)
        l_lf = T("sang phải", size=24, color=GOOD).next_to(c_lf, DOWN, buff=0.15)
        diag = VGroup(c_ij, c_up, c_lf, t_ij, t_up, t_lf, a_up, a_lf, l_up, l_lf)
        formula = tag_box("CÔNG THỨC", [
            "best(i, j) = max( best(i−1, j), best(i, j−1) ) + aᵢⱼ",
            "• Cơ sở: best(1, 1) = a₁₁; ngoài lưới: −∞",
            "• Ô đá / không tới được: −∞",
            "• Đáp án: best(m, n); nếu −∞ thì in −1",
        ], width=7.5, size=28)
        formula[3][0].set_color(ACCENT)
        fit_stack(defi, diag, formula, buff=0.6, max_scale=1.3)
        with self.voice("Bước một: đặt trạng thái và hỏi bước cuối cùng là gì. "
                        "Đặt best của i j là số táo lớn nhất hái được trên một đường đi từ ô 1 1 tới ô i j."):
            self.play(FadeIn(defi), run_time=0.8)
        with self.voice("Robot chỉ có thể tới ô i j từ ô phía trên, bằng một bước đi xuống, hoặc từ ô bên trái, "
                        "bằng một bước sang phải."):
            self.play(FadeIn(c_ij), FadeIn(t_ij), run_time=0.5)
            self.play(FadeIn(c_up), FadeIn(t_up), GrowArrow(a_up), FadeIn(l_up), run_time=0.8)
            self.play(FadeIn(c_lf), FadeIn(t_lf), GrowArrow(a_lf), FadeIn(l_lf), run_time=0.8)
        with self.voice("Vậy best của i j bằng max của best ô trên và best ô trái, cộng số táo của ô i j."):
            self.play(FadeIn(formula[0:3]), FadeIn(formula[3][0]), run_time=1.0)
        with self.voice("Cơ sở: best của 1 1 bằng a 1 1. Ô ngoài lưới, ô đá và ô không tới được mang giá trị âm vô cùng. "
                        "Nếu cả hai ô nguồn đều âm vô cùng thì ô i j cũng âm vô cùng. Đáp án là best của m n."):
            self.play(FadeIn(formula[3][1:]), run_time=1.2)

        self.clear_body()
        self.show_header("Bước 2: Chọn thứ tự điền bảng")
        grid = Grid(GRID, corner=True)
        order = VGroup(T("Từng hàng TỪ TRÊN XUỐNG,", size=32, color=GOOD),
                       T("mỗi hàng TỪ TRÁI SANG PHẢI (như đọc sách)", size=30, color=GOOD)).arrange(DOWN, buff=0.1)
        eq_slot = placeholder(7.4, 1.2)
        sc = fit_stack(order, grid, eq_slot, buff=0.55, max_scale=1.25)
        with self.voice("Bước hai: chọn thứ tự điền bảng. Ô i j cần ô phía trên và ô bên trái. Nếu ta điền từng hàng từ "
                        "trên xuống, trong mỗi hàng từ trái sang phải, giống như đọc sách, thì khi tới ô i j, "
                        "cả hai ô cần dùng đều đã được điền."):
            self.play(FadeIn(grid), run_time=0.8)
            self.play(FadeIn(order), run_time=0.6)
            cursor = SurroundingRectangle(grid.cells[(0, 0)], color=ACCENT, buff=0, stroke_width=6)
            self.play(Create(cursor), run_time=0.3)
            for i in range(ROWS):
                for j in range(COLS):
                    if (i, j) != (0, 0):
                        self.play(cursor.animate.move_to(grid.cells[(i, j)]), run_time=0.12)
            self.play(FadeOut(cursor), run_time=0.3)
        warn = T("Điền từ dưới lên thì SAI: ô phía trên chưa có giá trị!", size=28, color=BAD).scale(sc).move_to(eq_slot)
        with self.voice("Điền từng cột từ trái sang phải cũng đúng. Nhưng điền từ dưới lên thì sai, vì ô phía trên chưa có giá trị."):
            self.play(FadeIn(warn), run_time=0.6)
        self.play(FadeOut(warn), run_time=0.4)

        # Bước 3: chạy tay
        self.show_header("Bước 3: Chạy tay — điền bảng best")
        vals = {}

        def put(i, j, col):
            v = BEST[i][j]
            t = TB(best_text(v), size=36, color=BAD if v is None else INK)
            t.scale(sc).move_to(grid.cells[(i, j)].get_center() + DOWN * 0.1 * sc)
            vals[(i, j)] = t
            anims = [FadeIn(t, scale=1.3)]
            if v is None and GRID[i][j] >= 0:
                anims.append(grid.cells[(i, j)].animate.set_fill("#7F1D1D", 1))
            elif v is not None:
                anims.append(grid.cells[(i, j)].animate.set_fill(col, 1))
            return anims

        eq = None

        def show_eq(text, color=INK):
            nonlocal eq
            new = M(text, size=28, color=color).scale(sc)
            if new.width > 7.4:
                new.scale_to_fit_width(7.4)
            new.move_to(eq_slot)
            if eq is None:
                eq = new
                return FadeIn(eq)
            return Transform(eq, new)

        key = {
            (0, 1): ("Hàng 1: best của 1 2 bằng 2 cộng 3, bằng 5.", "best(1,2) = 2 + 3 = 5"),
            (0, 4): ("Hai ô đá chặn đường, nên ô 1 5 không tới được dù không có đá: âm vô cùng. Đây là lí do ta phải "
                     "đánh dấu âm vô cùng chứ không thể coi ô ấy bằng 0.", "best(1,5) = −∞  (bị đá chặn!)"),
            (1, 1): ("best của 2 2 bằng max của 5 và 10, cộng 7, bằng 17.", "best(2,2) = max(5, 10) + 7 = 17"),
            (1, 2): ("best của 2 3: ô phía trên là đá, chỉ còn đường từ bên trái: 17 cộng 5 bằng 22.",
                     "best(2,3) = max(−∞, 17) + 5 = 22"),
        }
        with self.voice("Bắt đầu: best của 1 1 bằng 2."):
            self.play(show_eq("best(1,1) = 2"), *put(0, 0, "#166534"), run_time=0.6)
        order_cells = [(i, j) for i in range(ROWS) for j in range(COLS) if (i, j) != (0, 0)]
        batch = []
        for (i, j) in order_cells:
            if (i, j) in key:
                if batch:
                    with self.voice("Các ô còn lại trong đoạn này điền tương tự."):
                        for (bi, bj) in batch:
                            self.play(*put(bi, bj, "#166534"), run_time=0.3)
                    batch = []
                sp, f = key[(i, j)]
                with self.voice(sp):
                    self.play(show_eq(f, BAD if BEST[i][j] is None else ACCENT), run_time=0.5)
                    self.play(*put(i, j, "#166534"), run_time=0.5)
            else:
                batch.append((i, j))
        last = batch.pop()  # ô đích
        with self.voice("Cứ thế điền hết từng hàng, mỗi ô chỉ cần một phép max và một phép cộng."):
            for (bi, bj) in batch:
                self.play(*put(bi, bj, "#166534"), run_time=0.25)
        with self.voice("Ô đích: best của 4 5 bằng max của 43 và 44, cộng 6, bằng 50!"):
            self.play(show_eq("best(4,5) = max(43, 44) + 6 = 50", GOOD), run_time=0.5)
            self.play(*put(*last, ACCENT), run_time=0.6)
            self.play(Circumscribe(grid.cells[last], color=ACCENT), run_time=0.8)

        self.clear_body()
        self.show_header("Vì sao đúng? Độ phức tạp?")
        why = tag_box("VÌ SAO ĐÚNG?", [
            "Lấy một đường tốt nhất tới (i, j), bước cuối",
            "đi từ ô trên. Phần đường (1,1) → (i−1, j) phải",
            "là đường TỐT NHẤT tới (i−1, j) — nếu không,",
            "thay vào sẽ được đường tới (i, j) tốt hơn.",
            "Tương tự với ô trái ⇒ lấy max là đúng.",
            "Lại là CẤU TRÚC CON TỐI ƯU như Bài 1!",
        ], accent=GOOD, width=7.4, size=28)
        why[3][5].set_color(ACCENT)
        cx = VGroup(TB("O(m·n)", size=48, color=GOOD),
                    T("1000 × 1000: chỉ khoảng 10⁶ phép, chạy tức thì", size=28)).arrange(DOWN, buff=0.2)
        fit_stack(why, cx, buff=0.9, max_scale=1.2)
        with self.voice("Vì sao đúng? Lấy một đường tốt nhất tới ô i j, giả sử bước cuối đi từ ô phía trên. Phần đường từ "
                        "1 1 tới ô trên phải là đường tốt nhất tới ô đó, vì nếu có đường tốt hơn, thay vào sẽ được đường "
                        "tới i j tốt hơn. Tương tự với ô bên trái. Đây lại là cấu trúc con tối ưu như Bài 1."):
            self.play(FadeIn(why), run_time=1.0)
        with self.voice("Độ phức tạp: mỗi ô tính bằng một phép max và một phép cộng, có m nhân n ô, nên O của m nhân n. "
                        "Với lưới 1000 nhân 1000 chỉ khoảng một triệu phép, chạy tức thì."):
            self.play(FadeIn(cx), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
TRACE_CODE = """
string path;
int row = rowCount, column = columnCount;
while (row != 1 || column != 1) {
    long long need = best[row][column] - apple[row][column];
    if (row > 1 && best[row - 1][column] == need) {
        path += 'D'; row--;
    } else {
        path += 'R'; column--;
    }
}
reverse(path.begin(), path.end());
"""


class B3_04_TruyVet(B3Scene):
    def construct(self):
        self.show_header("4. Truy vết: Tìm lại đường đi")
        idea = VGroup(T("Đi NGƯỢC từ đích về xuất phát,", size=30),
                      T("ở mỗi ô hỏi: “mình đã tới đây từ đâu?”", size=30, color=ACCENT)).arrange(DOWN, buff=0.12)
        grid = Grid(GRID, corner=True)
        rec_slot = placeholder(7.4, 1.0)
        eq_slot = placeholder(7.4, 0.9)
        sc = fit_stack(idea, grid, eq_slot, rec_slot, buff=0.5, max_scale=1.25)
        texts = VGroup()
        for i in range(ROWS):
            for j in range(COLS):
                v = BEST[i][j]
                if v is None and GRID[i][j] >= 0:
                    grid.cells[(i, j)].set_fill("#7F1D1D", 1)
                elif v is not None:
                    grid.cells[(i, j)].set_fill("#166534", 1)
                t = TB(best_text(v), size=36, color=BAD if v is None else INK).scale(sc)
                if GRID[i][j] < 0:
                    continue
                t.move_to(grid.cells[(i, j)].get_center() + DOWN * 0.1 * sc)
                texts.add(t)
        with self.voice("Bảng best cho biết giá trị tốt nhất, nhưng đề còn hỏi đường đi. Kĩ thuật lấy lại lời giải từ bảng "
                        "phương án gọi là truy vết."):
            self.play(FadeIn(grid), FadeIn(texts), run_time=1.0)
        with self.voice("Ý tưởng: đi ngược từ đích về xuất phát, ở mỗi ô hỏi: mình đã tới đây từ đâu?"):
            self.play(FadeIn(idea), run_time=0.8)
        with self.voice("Tại ô i j, ta biết best của i j bằng best của ô trước cộng a i j. Vậy ô trước phải có giá trị đúng bằng "
                        "best của i j trừ a i j. Kiểm tra ô phía trên: nếu bằng thì robot đã đi xuống, ghi D; "
                        "ngược lại thì robot đã sang phải từ ô trái, ghi R."):
            self.play(Indicate(grid.cells[(ROWS - 1, COLS - 1)], color=ACCENT), run_time=1.0)

        letters = ""
        rec = None
        eq = None
        for k, ((i, j), (pi, pj), letter, need) in enumerate(STEPS):
            letters += letter
            up = BEST[i - 1][j] if i > 0 else None
            left = BEST[i][j - 1] if j > 0 else None
            f = f"({i + 1},{j + 1}): cần {BEST[i][j]} − {GRID[i][j]} = {need}"
            f2 = f"ô trên = {best_text(up)}, ô trái = {best_text(left)}  →  {letter}"
            new_eq = VGroup(T(f, size=28), T(f2, size=28, color=BLUEC if letter == "D" else GOOD)).arrange(DOWN, buff=0.08)
            new_eq.scale(sc).move_to(eq_slot)
            if new_eq.width > 7.4:
                new_eq.scale_to_fit_width(7.4)
            new_rec = VGroup(T("Ghi được:", size=30, color=MUTED), M(letters, size=36, color=ACCENT)).arrange(RIGHT, buff=0.3)
            new_rec.scale(sc).move_to(rec_slot)
            if k == 0:
                sp = (f"Tại ô 4 5, cần ô trước có giá trị 50 trừ 6 bằng 44. Ô trên là 43, ô trái là 44: "
                      f"robot đến từ bên trái, ghi R.")
            elif k == 1:
                sp = "Tại ô 4 4, cần 44 trừ 7 bằng 37. Ô trên là 37: ghi D."
            else:
                src = "ô trên" if letter == "D" else "ô trái"
                sp = f"Tại ô {i + 1} {j + 1}, cần {need}: khớp với {src}, ghi {letter}."
            with self.voice(sp):
                arr = Arrow(grid.center_of((i, j)), grid.center_of((pi, pj)), buff=0.25 * sc, color=BAD, stroke_width=8,
                            max_tip_length_to_length_ratio=0.3)
                anims = [GrowArrow(arr)]
                if eq is None:
                    eq, rec = new_eq, new_rec
                    anims += [FadeIn(eq), FadeIn(rec)]
                else:
                    anims += [Transform(eq, new_eq), Transform(rec, new_rec)]
                self.play(*anims, run_time=0.7 if k < 2 else 0.5)
        final = VGroup(T("Đảo ngược:", size=30, color=MUTED), M(letters, size=34, color=MUTED), T("→", size=30),
                       M(LETTERS, size=40, color=GOOD)).arrange(RIGHT, buff=0.25).scale(sc).move_to(rec_slot)
        with self.voice("Tới ô 1 1, ta ghi được R D D R R R D. Vì đi ngược nên xâu cũng ngược, cuối cùng cần đảo ngược "
                        "thành D R R R D D R."):
            self.play(Transform(rec, final), run_time=1.0)
            self.play(Indicate(rec[3], color=GOOD), run_time=0.8)

        self.clear_body()
        self.show_header("Hai cách truy vết")
        two = list_cards([
            ("Tính lại khi truy vết", "Không tốn thêm bộ nhớ, nhưng phải so sánh đúng giá trị"),
            ("Lưu mảng “từ đâu tới” from[i][j]", "Dễ viết, dễ kiểm tra; tốn thêm một bảng cùng cỡ"),
        ], accent=ACCENT)
        code = code_block(TRACE_CODE, size=20)
        fit_stack(two, code, buff=0.6)
        with self.voice("Có hai cách truy vết. Cách một, tính lại khi truy vết như vừa làm: không tốn thêm bộ nhớ, "
                        "nhưng phải cẩn thận so sánh đúng giá trị."):
            self.play(FadeIn(two[0], shift=RIGHT * 0.3), run_time=0.7)
        with self.voice("Cách hai, lưu mảng từ đâu tới ngay khi điền bảng: dễ viết, dễ kiểm tra, tốn thêm một bảng. "
                        "Khi công thức có nhiều lựa chọn, cách này an toàn hơn."):
            self.play(FadeIn(two[1], shift=RIGHT * 0.3), run_time=0.7)
        with self.voice("Đây là đoạn code truy vết. Điều kiện row lớn hơn 1 đảm bảo không đi ra ngoài lưới, "
                        "và cuối cùng nhớ đảo ngược xâu."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 4, BLUEC)
            self.play(FadeIn(hl), run_time=0.4)
            self.play(Transform(hl, line_box(code, 10, GOOD)), run_time=0.5)
        self.clear_body()


# ----------------------------------------------------------------------------
class B3_05_DemDuong(B3Scene):
    def construct(self):
        self.show_header("5. Đếm số đường đi")
        formula = tag_box("CÔNG THỨC ĐẾM", [
            "ways(i, j) = ways(i−1, j) + ways(i, j−1)",
            "ways(1, 1) = 1;  ô đá = 0;  ngoài lưới = 0",
        ], accent=BLUEC, width=7.4, size=29)
        grid = Grid(GRID, corner=True)
        res = TB("Có 25 đường đi tránh đá", size=36, color=GOOD)
        sc = fit_stack(formula, grid, res, buff=0.55, max_scale=1.25)
        with self.voice("Đổi câu hỏi: có bao nhiêu đường đi từ ô 1 1 tới ô m n tránh các ô đá? Lập luận bước cuối vẫn "
                        "y nguyên, chỉ đổi phép max thành phép cộng."):
            self.play(FadeIn(formula), run_time=0.8)
            self.play(FadeIn(grid), run_time=0.6)
        with self.voice("Điền bảng theo hàng: mỗi ô bằng ô trên cộng ô trái, ô đá bằng 0."):
            for i in range(ROWS):
                anims = []
                for j in range(COLS):
                    v = WAYS[i][j]
                    t = TB(str(v), size=36, color=INK if GRID[i][j] >= 0 else MUTED).scale(sc)
                    if GRID[i][j] < 0:
                        continue
                    t.move_to(grid.cells[(i, j)].get_center() + DOWN * 0.1 * sc)
                    anims += [FadeIn(t, scale=1.3), grid.cells[(i, j)].animate.set_fill(
                        "#1E3A8A" if v else "#7F1D1D", 1)]
                self.play(LaggedStart(*anims, lag_ratio=0.1), run_time=0.9)
        with self.voice("Ô đích có giá trị 25: có 25 đường đi tránh đá. Thường bài đếm sẽ yêu cầu lấy dư cho mười mũ chín cộng bảy."):
            self.play(FadeIn(res), Circumscribe(grid.cells[(ROWS - 1, COLS - 1)], color=GOOD), run_time=1.0)

        self.clear_body()
        self.show_header("Không có đá: tam giác Pascal!")
        pm, pn = 5, 6
        cells = VGroup()
        for i in range(pm):
            for j in range(pn):
                v = comb(i + j, i)
                c = cell(v, w=1.05, h=1.05, fill=PANEL_2, size=30)
                c.move_to([j * 1.05, -i * 1.05, 0])
                cells.add(c)
        note = VGroup(M("ways(i, j) = C(i + j − 2, i − 1)", size=30, color=ACCENT),
                      T("Một tảng đá thôi là công thức tổ hợp hết dùng được,", size=27),
                      T("còn quy hoạch động vẫn chạy đúng như cũ!", size=27, color=GOOD)).arrange(DOWN, buff=0.15)
        fit_stack(cells, note, buff=0.6, max_scale=1.2)
        with self.voice("Nếu không có đá, bảng ways chính là tam giác Pascal đặt nghiêng: mỗi số bằng số phía trên cộng số bên trái."):
            for d in range(pm + pn - 1):
                grp = [cells[i * pn + j] for i in range(pm) for j in range(pn) if i + j == d]
                self.play(*[FadeIn(g, scale=0.6) for g in grp], *[g[0].animate.set_fill(
                    interpolate_color(ManimColor("#1E3A8A"), ManimColor("#7C3AED"), d / (pm + pn - 2)), 1) for g in grp],
                    run_time=0.3)
            diag = VGroup(*[cells[i * pn + j] for i in range(pm) for j in range(pn) if i + j == 4])
            self.play(Indicate(diag, color=ACCENT), run_time=1.0)
        with self.voice("Công thức là tổ hợp chập i trừ 1 của i cộng j trừ 2. Nhưng chỉ cần một tảng đá, công thức tổ hợp "
                        "không còn dùng được, còn quy hoạch động vẫn chạy đúng như cũ. Đó là sức mạnh của cách nghĩ bước cuối cùng."):
            self.play(FadeIn(note), run_time=1.0)

        self.clear_body()
        self.show_header("6. Tiết kiệm bộ nhớ: Chỉ giữ một hàng")
        upper = array_row([10, 17, 22, 29, 33], w=1.1, h=0.9, size=32, label="hàng 2", index_from=1)
        line = array_row([""] * 5, w=1.1, h=0.95, size=34, label="line", show_index=False)
        for k, c in enumerate(line.cells):
            c.move_to(upper.cells[k].get_center() + DOWN * 1.5)
        line.lab.next_to(line.cells, LEFT, buff=0.2)
        expl = VGroup(T("Trước khi ghi đè: line[j] = giá trị HÀNG TRÊN,", size=27),
                      T("line[j − 1] vừa cập nhật = HÀNG HIỆN TẠI", size=27, color=GOOD)).arrange(DOWN, buff=0.1)
        mem = VGroup(T("Bộ nhớ:", size=32), TB("O(m·n)", size=40, color=BAD), T("→", size=32),
                     TB("O(n)", size=40, color=GOOD)).arrange(RIGHT, buff=0.2)
        cost = T("Cái giá: KHÔNG còn truy vết được (hàng cũ bị ghi đè)", size=28, color=BAD)
        sc = fit_stack(VGroup(upper, line), expl, mem, cost, buff=0.6, max_scale=1.2)
        with self.voice("Khi điền hàng i, ta chỉ cần hàng i trừ 1. Hơn nữa, có thể dùng một mảng một chiều tên line, "
                        "điền j từ trái sang phải."):
            for k, c in enumerate(line.cells):
                c[1].become(set_cell_value(c, [10, 17, 22, 29, 33][k], color=INK))
            self.play(FadeIn(upper), run_time=0.6)
            self.play(TransformFromCopy(VGroup(*upper.cells), VGroup(*line.cells)), FadeIn(line.lab), run_time=0.8)
        third = [19, 20, 23, 37, 43]
        with self.voice("Trước khi ghi đè, line j đang giữ giá trị của hàng trên, còn line j trừ 1 vừa được cập nhật là "
                        "giá trị của hàng hiện tại. Lấy max của hai ô này, cộng số táo, ta được hàng 3."):
            self.play(FadeIn(expl), FadeOut(upper), run_time=0.6)
            for k in range(5):
                hi = [line.cells[k][0].animate.set_stroke(BLUEC, 6)]
                if k > 0:
                    hi.append(line.cells[k - 1][0].animate.set_stroke(GOOD, 6))
                self.play(*hi, run_time=0.3)
                c = line.cells[k]
                self.play(Transform(c[1], set_cell_value(c, third[k], color=BG)), c[0].animate.set_fill(ACCENT, 1),
                          run_time=0.35)
                self.play(*[cc[0].animate.set_stroke(MUTED, 2) for cc in line.cells], run_time=0.15)
        with self.voice("Bộ nhớ cho bảng giảm từ O của m nhân n xuống O của n."):
            self.play(FadeIn(mem), run_time=0.6)
        with self.voice("Cái giá phải trả: không còn truy vết được, vì các hàng cũ đã bị ghi đè."):
            self.play(FadeIn(cost), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B3_06_TongKet(B3Scene):
    def construct(self):
        self.show_header("7. Mở rộng")
        ext = [
            ("Thêm hướng chéo xuống phải", "Thêm best(i−1, j−1) vào phép max",
             "Mở rộng một: nếu robot được đi thêm chéo xuống phải, chỉ cần thêm best của i trừ 1, j trừ 1 vào phép max. "
             "Nếu được đi sang trái nữa thì lưới có thể có chu trình, khi ấy bài toán trở thành tìm đường trên đồ thị."),
            ("Xuất phát ở bất kì ô nào cột đầu", "best(i, 1) = max(aᵢ₁, best(i−1, 1) + aᵢ₁)",
             "Mở rộng hai: nếu được xuất phát ở bất kì ô nào của cột đầu, cơ sở thay đổi. Mỗi lần đổi đề, hãy trả lời lại "
             "bốn câu hỏi thay vì sửa công thức theo cảm tính."),
            ("Hình vuông lớn nhất toàn số 1", "“Góc dưới phải tại (i, j)”: kết thúc tại i, hai chiều",
             "Mở rộng ba: bài hình vuông lớn nhất toàn số 1 dùng trạng thái hình vuông có góc dưới phải tại i j, "
             "tức là kiểu kết thúc tại của Bài 2 mang sang hai chiều."),
            ("Hai robot cùng đi", "Trạng thái: số bước + hàng của hai robot",
             "Mở rộng bốn: hai robot cùng đi, ô chung chỉ hái một lần. Cho hai robot đi đồng thời, "
             "trạng thái gồm số bước đã đi và hàng của hai robot."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Coi ô không tới được bằng 0", "Ô (1, 5) bị coi là tới được → đáp án sai",
             "Bẫy một: coi ô không tới được bằng 0. Ô 1 5 trong ví dụ sẽ bị coi là tới được."),
            ("Cộng vào −∞", "−10¹⁸ + 10⁶ ≠ −10¹⁸: kiểm tra TRƯỚC khi cộng",
             "Bẫy hai: cộng vào âm vô cùng. Âm mười mũ mười tám cộng một triệu vẫn rất âm nhưng khác âm mười mũ mười tám, "
             "phép so sánh bằng sẽ sai. Luôn kiểm tra trước khi cộng."),
            ("Quên đảo ngược xâu truy vết", "Đi ngược nên xâu ghi được cũng ngược",
             "Bẫy ba: quên đảo ngược xâu truy vết."),
            ("Đọc nhầm m và n", "m = số hàng, n = số cột: thử lưới 2 × 7",
             "Bẫy bốn: đọc nhầm m và n. m là số hàng, n là số cột. Hãy thử chương trình với lưới không vuông."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 3", [
            "• Lưới: trạng thái (i, j), điền theo hàng",
            "   từ trên xuống, trái sang phải.",
            "• Ô không tới được: −∞ (bài max) hoặc 0",
            "   (bài đếm), kiểm tra trước khi cộng.",
            "• TRUY VẾT = đi ngược từ đáp án, hỏi",
            "   “đã tới đây bằng lựa chọn nào?”, rồi đảo.",
            "• Giữ một hàng: tiết kiệm bộ nhớ nhưng",
            "   mất khả năng truy vết.",
        ], accent=GOOD, width=7.4, size=30)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: trên lưới, trạng thái là i j, thứ tự điền theo hàng từ trên xuống, trái sang phải. "
                        "Ô không tới được mang giá trị âm vô cùng với bài max, hoặc 0 với bài đếm, và phải kiểm tra trước khi cộng."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:4]), run_time=1.0)
        with self.voice("Truy vết là đi ngược từ đáp án, ở mỗi bước hỏi: mình đã tới đây bằng lựa chọn nào, rồi đảo ngược. "
                        "Giữ một hàng giúp tiết kiệm bộ nhớ nhưng làm mất khả năng truy vết."):
            self.play(FadeIn(mem[3][4:]), run_time=1.0)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Lưới 3 × 3 không có đá", "có bao nhiêu đường đi?"], size=38, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        cells = VGroup()
        for i in range(3):
            for j in range(3):
                c = cell("", w=1.1, h=1.1)
                c.move_to([j * 1.1, -i * 1.1, 0])
                cells.add(c)
        ans = TB("C(4, 2) = 6 đường", size=40, color=GOOD)
        fit_stack(q, timer_slot, cells, ans, buff=0.6, max_scale=1.2)
        with self.voice("Câu hỏi tự kiểm tra: lưới 3 nhân 3 không có đá có bao nhiêu đường đi? Dừng video và thử nhé!"):
            self.play(FadeIn(q), FadeIn(cells), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("Điền tam giác Pascal: 1, 1, 1; 1, 2, 3; 1, 3, 6. Đáp án là 6, bằng tổ hợp chập 2 của 4."):
            for d in range(5):
                grp = [(i, j) for i in range(3) for j in range(3) if i + j == d]
                self.play(*[Transform(cells[i * 3 + j][1], set_cell_value(cells[i * 3 + j], comb(i + j, i), color=BG))
                            for i, j in grp],
                          *[cells[i * 3 + j][0].animate.set_fill(GOOD if (i, j) == (2, 2) else ACCENT, 1) for i, j in grp],
                          run_time=0.4)
            self.play(FadeIn(ans), run_time=0.5)

        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
        self._header = None
        done = TB("HOÀN THÀNH CHƯƠNG 1", size=50, color=ACCENT)
        recap = VGroup(*[T(t, size=32) for t in [
            "Bài 1 · Đệ quy → có nhớ → điền bảng",
            "Bài 2 · “Kết thúc tại i” & “chọn hay bỏ”",
            "Bài 3 · Lưới hai chiều & truy vết",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        key = VGroup(T("Câu hỏi then chốt:", size=32, color=MUTED),
                     TB("“BƯỚC CUỐI CÙNG LÀ GÌ?”", size=44, color=GOOD)).arrange(DOWN, buff=0.2)
        nxt = T("Hẹn gặp lại ở Chương 2: Các mô hình kinh điển!", size=30, color=ACCENT)
        fit_stack(done, recap, key, nxt, buff=0.8, max_scale=1.2)
        with self.voice("Chúc mừng các em đã hoàn thành Chương 1: Nền tảng quy hoạch động!"):
            self.play(FadeIn(done, scale=1.3), run_time=1.0)
        with self.voice("Bài 1: con đường nâng cấp từ đệ quy, đệ quy có nhớ, đến điền bảng. Bài 2: hai kiểu trạng thái "
                        "kết thúc tại i và chọn hay bỏ. Bài 3: lưới hai chiều và truy vết."):
            for r in recap:
                self.play(FadeIn(r, shift=RIGHT * 0.3), run_time=0.7)
        with self.voice("Và hãy luôn nhớ câu hỏi then chốt: bước cuối cùng là gì?"):
            self.play(FadeIn(key), run_time=0.8)
            self.play(Indicate(key[1], color=GOOD), run_time=1.0)
        with self.voice("Hẹn gặp lại các em ở Chương 2: Các mô hình kinh điển!"):
            self.play(FadeIn(nxt), run_time=0.8)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)


SCENES = [B3_00_Intro, B3_01_KhoiDong, B3_02_NgayTho, B3_03_CongThuc, B3_04_TruyVet, B3_05_DemDuong, B3_06_TongKet]
