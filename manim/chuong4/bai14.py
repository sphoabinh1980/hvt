"""BÀI 14 — Quy hoạch động với cây Fenwick (DEMDAYTANG) và lũy thừa ma trận (MATMADEN)."""

from itertools import combinations

from shared import *  # noqa: F401,F403

A = [3, 1, 4, 1, 5]
VALS = sorted(set(A))
RANK = [VALS.index(x) + 1 for x in A]
assert VALS == [1, 3, 4, 5] and RANK == [2, 1, 3, 1, 4]


def count_inc(a):
    f = []
    for i in range(len(a)):
        f.append(1 + sum(f[j] for j in range(i) if a[j] < a[i]))
    return f


F = count_inc(A)
assert F == [1, 1, 3, 1, 7] and sum(F) == 13
_subs = [c for r in range(1, 6) for c in combinations(range(5), r)
         if all(A[c[k]] < A[c[k + 1]] for k in range(len(c) - 1))]
assert len(_subs) == 13 and sum(1 for c in _subs if len(c) == 2) == 6 and sum(1 for c in _subs if len(c) == 3) == 2
assert sum(count_inc([1, 2, 3])) == 7


def lowbit(i):
    return i & -i


def query_path(p):
    out = []
    while p > 0:
        out.append(p)
        p -= lowbit(p)
    return out


def add_path(p, m):
    out = []
    while p <= m:
        out.append(p)
        p += lowbit(p)
    return out


assert query_path(7) == [7, 6, 4] and add_path(3, 8) == [3, 4, 8]

# Chạy tay Fenwick trên trục giá trị (hạng 1..4)
AXIS = [0] * 5
TRACE = []
for _i, (_r, _f) in enumerate(zip(RANK, F)):
    _pre = sum(AXIS[1:_r])
    assert 1 + _pre == _f
    TRACE.append((_i + 1, A[_i], _r, _pre, _f))
    AXIS[_r] += _f
assert AXIS[1:] == [2, 1, 3, 7] and TRACE[4][3] == 6

# MATMADEN
M3 = [[0, 1, 1], [1, 1, 1], [1, 1, 0]]


def mat_mul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def mat_pow(m, e):
    r = [[int(i == j) for j in range(len(m))] for i in range(len(m))]
    while e:
        if e & 1:
            r = mat_mul(r, m)
        m = mat_mul(m, m)
        e >>= 1
    return r


ROWS = [(1, 1, 1)]
for _ in range(3):
    d, v, x = ROWS[-1]
    ROWS.append((v + x, d + v + x, d + v))
assert [sum(r) for r in ROWS] == [3, 7, 17, 41]
assert all(sum(map(sum, mat_pow(M3, n - 1))) == sum(ROWS[n - 1]) for n in range(1, 5))
assert format(13, "b") == "1101"
P13 = mat_mul(mat_mul(mat_pow(M3, 8), mat_pow(M3, 4)), M3)
assert P13 == mat_pow(M3, 13)

FEN_CODE = """
void add(int p, long long x) {
  for (; p <= m; p += p & (-p))
    t[p] = (t[p] + x) % MOD;
}
long long prefixSum(int p) {
  long long s = 0;
  for (; p > 0; p -= p & (-p))
    s = (s + t[p]) % MOD;
  return s;
}
// main: for each i (rank = compressed a[i])
long long f = (1 + prefixSum(rank - 1)) % MOD;
add(rank, f);
answer = (answer + f) % MOD;
"""

MAT_CODE = """
Matrix step = {{0,1,1},{1,1,1},{1,1,0}};
Matrix power = {{1,0,0},{0,1,0},{0,0,1}};
long long e = n - 1;
while (e > 0) {
  if (e & 1) power = multiply(power, step);
  step = multiply(step, step);
  e >>= 1;
}
// answer = sum of all entries of power
"""


class B14Scene(NarratedScene):
    lesson_tag = "BÀI 14"
    lesson_title = "Cây Fenwick và lũy thừa ma trận"


def ghost_row(n, **kw):
    r = array_row(["0"] * n, **kw)
    for c in r.cells:
        c[1].set_opacity(0)
    return r


def setv(c, v, col=INK):
    return Transform(c[1], set_cell_value(c, v, color=col))


def matrix_mob(m, size=34, cell_w=0.75, color=INK, highlight=None):
    cells = VGroup()
    for i, row in enumerate(m):
        for j, v in enumerate(row):
            col = color
            if highlight is not None and v:
                col = highlight
            cells.add(TB(str(v), size=size, color=col).move_to([j * cell_w, -i * cell_w * 0.85, 0]))
    h = cells.height + 0.3
    lb = VGroup(Line(UP * h / 2, DOWN * h / 2), Line(UP * h / 2, UP * h / 2 + RIGHT * 0.15),
                Line(DOWN * h / 2, DOWN * h / 2 + RIGHT * 0.15)).set_color(MUTED).set_stroke(width=3)
    rb = lb.copy().flip(UP)
    lb.next_to(cells, LEFT, buff=0.12)
    rb.next_to(cells, RIGHT, buff=0.12)
    g = VGroup(lb, cells, rb)
    g.cells = cells
    return g


COLORS = {"Đ": BAD, "V": ACCENT, "X": GOOD}


def bulb(c, r=0.32):
    return VGroup(Circle(radius=r, fill_color=COLORS[c], fill_opacity=1, stroke_color=INK, stroke_width=2),
                  TB(c, size=r * 70, color=BG))


# ----------------------------------------------------------------------------
class B14_00_Intro(B14Scene):
    def construct(self):
        tag = TB("BÀI 14", size=80, color=ACCENT)
        ttl = VGroup(TB("Quy hoạch động với", size=46), TB("cây Fenwick", size=52, color=ORANGE),
                     TB("và lũy thừa ma trận", size=52, color=PURPLE)).arrange(DOWN, buff=0.15)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Cây Fenwick + nén giá trị: tổng/max",
            "    của các trạng thái có GIÁ TRỊ nhỏ hơn",
            "✓ Truy hồi tuyến tính = NHÂN MA TRẬN;",
            "    lũy thừa nhanh khi n tới 10¹⁸",
            "✓ Công thức = “cái gì cần tính”;",
            "    cấu trúc dữ liệu = “tính nhanh thế nào”",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        for k in (1, 3, 5):
            goals[k].set_color(MUTED)
        fit_stack(VGroup(tag, ttl).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Chào mừng các em đến với Bài 14, bài cuối cùng: Quy hoạch động với cây Fenwick và lũy thừa ma trận."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), run_time=1.5)
        with self.voice("Học xong bài này, em sẽ dùng cây Fenwick, hay cây chỉ số nhị phân, để tính nhanh tổng hoặc max của các "
                        "trạng thái có giá trị nhỏ hơn một ngưỡng, kết hợp với nén giá trị."):
            self.play(FadeIn(goals[0:2]), run_time=0.6)
        with self.voice("Em sẽ viết công thức truy hồi tuyến tính dưới dạng nhân ma trận, rồi dùng lũy thừa nhanh khi n lên tới 10 "
                        "mũ 18."):
            self.play(FadeIn(goals[2:4]), run_time=0.6)
        with self.voice("Và hoàn thiện bức tranh: công thức quy hoạch động là cái gì cần tính, còn cấu trúc dữ liệu là tính nó "
                        "nhanh thế nào."):
            self.play(FadeIn(goals[4:]), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B14_01_KhoiDong(B14Scene):
    def construct(self):
        self.show_header("Khởi động: Hai câu hỏi mới")
        c1 = list_cards([("Câu 1 (Bài 6 nâng cấp)", "CÓ BAO NHIÊU dãy con tăng ngặt?")], accent=ORANGE,
                        title_size=32, body_size=30)
        need = VGroup(T("Cần TỔNG f(j) trên mọi j trước có a_j < a_i,", size=27),
                      T("không chỉ một số lớn nhất ⇒ mảng d bó tay", size=27, color=BAD)).arrange(DOWN, buff=0.08)
        c2 = list_cards([("Câu 2", "Đếm số dãy đèn dài n = 10¹⁸")], accent=PURPLE, title_size=32, body_size=30)
        jump = TB("Liệu có cách “nhảy cóc” qua bảng?", size=32, color=ACCENT)
        fit_stack(c1, need, c2, jump, buff=0.6, max_scale=1.25)
        with self.voice("Ở Bài 6, mảng d giúp ta tìm độ dài dãy con tăng dài nhất trong O của n log n. Nhưng nếu câu hỏi là có bao "
                        "nhiêu dãy con tăng ngặt?"):
            self.play(FadeIn(c1), run_time=0.7)
        with self.voice("Mảng d không còn giúp được: ta cần tổng của f j trên mọi j đứng trước có a j nhỏ hơn a i, chứ không chỉ "
                        "một con số lớn nhất."):
            self.play(FadeIn(need), run_time=0.7)
        with self.voice("Và một câu hỏi khác: đếm số dãy đèn dài n bằng 10 mũ 18. Không thể điền 10 mũ 18 ô bảng. Liệu có cách "
                        "nhảy cóc qua bảng?"):
            self.play(FadeIn(c2), run_time=0.7)
            self.play(FadeIn(jump), run_time=0.5)

        self.clear_body()
        self.show_header("1. Bài toán DEMDAYTANG")
        task = tag_box("BÀI TOÁN: DEMDAYTANG", [
            "Cho dãy n số (n ≤ 2·10⁵, |a_i| ≤ 10⁹). Đếm số dãy",
            "con khác rỗng TĂNG NGẶT, lấy dư 10⁹ + 7. Hai dãy",
            "con khác nhau nếu chọn các VỊ TRÍ khác nhau.",
        ], width=7.5, size=27)
        arr = array_row(A, w=1.0, h=0.95, size=40, index_from=1)
        groups = VGroup(
            VGroup(TB("5", size=36, color=BLUEC), T("dãy một phần tử", size=30)).arrange(RIGHT, buff=0.25),
            VGroup(TB("6", size=36, color=GOOD), T("dãy hai phần tử:", size=30)).arrange(RIGHT, buff=0.25),
            M("34  35  14  15  45  1′5", size=28, color=MUTED),
            VGroup(TB("2", size=36, color=ORANGE), T("dãy ba phần tử:", size=30)).arrange(RIGHT, buff=0.25),
            M("345  145", size=28, color=MUTED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        groups[2].shift(RIGHT * 0.5)
        groups[4].shift(RIGHT * 0.5)
        total = TB("5 + 6 + 2 = 13", size=40, color=ACCENT)
        fit_stack(task, arr, groups, total, buff=0.55, max_scale=1.2)
        with self.voice("Bài toán DEMDAYTANG: cho dãy n số nguyên. Đếm số dãy con khác rỗng tăng ngặt, lấy dư cho 10 mũ 9 cộng 7. "
                        "Hai dãy con khác nhau nếu chúng chọn các vị trí khác nhau."):
            self.play(FadeIn(task), run_time=0.8)
        with self.voice("Ví dụ: dãy 3, 1, 4, 1, 5."):
            self.play(FadeIn(arr), run_time=0.6)
        with self.voice("Có 5 dãy một phần tử. Có 6 dãy hai phần tử: 3 4, 3 5, 1 4, 1 5, 4 5, và 1 5 với số 1 thứ hai."):
            self.play(FadeIn(groups[0]), run_time=0.4)
            self.play(FadeIn(groups[1:3]), run_time=0.5)
        with self.voice("Và 2 dãy ba phần tử: 3 4 5, và 1 4 5 với số 1 ở vị trí 2. Tổng cộng 13."):
            self.play(FadeIn(groups[3:]), run_time=0.5)
            self.play(FadeIn(total), run_time=0.5)

        self.clear_body()
        self.show_header("Ngây thơ: Quy hoạch động O(n²)")
        f = panel(VGroup(M("f(i) = 1 + Σ f(j),  j < i, a_j < a_i", size=27, color=ACCENT),
                         T("Đáp án = Σ f(i).  Như Bài 6, nhưng ĐẾM thay vì max", size=24, color=MUTED)).arrange(DOWN, buff=0.12),
                  stroke=ACCENT)
        ar = array_row(A, w=1.0, h=0.9, size=36, index_from=1, label="a")
        fr = ghost_row(5, w=1.0, h=0.9, size=36, show_index=False, label="f")
        rows = VGroup(ar, fr).arrange(DOWN, buff=0.2, aligned_edge=RIGHT)
        calc_slot = placeholder(7.2, 0.7)
        cnt = tag_box("ĐẾM SỐ PHÉP TÍNH", [
            "Hai vòng lặp lồng nhau: ≈ n²/2 phép.",
            "n = 2·10⁵ ⇒ 2·10¹⁰ phép: QUÁ CHẬM",
        ], accent=BLUEC, width=7.5, size=27)
        cnt[3][1].set_color(BAD)
        sc = fit_stack(f, rows, calc_slot, cnt, buff=0.55, max_scale=1.2)
        with self.voice("Cách quy hoạch động tự nhiên: trạng thái kết thúc tại i như Bài 6, nhưng đếm thay vì lấy max. f của i "
                        "bằng 1, là dãy chỉ gồm a i, cộng tổng f của j với mọi j đứng trước có a j nhỏ hơn a i."):
            self.play(FadeIn(f), FadeIn(rows), run_time=1.0)
        texts = ["f của 1 bằng 1.", "f của 2 bằng 1: không có số nào nhỏ hơn 1 đứng trước.",
                 "f của 3: số 4 nối sau 3 và sau 1, nên bằng 1 cộng 1 cộng 1 bằng 3.",
                 "f của 4 bằng 1.", "f của 5: số 5 nối sau tất cả, bằng 1 cộng 1 cộng 1 cộng 3 cộng 1, bằng 7."]
        cur = None
        for i in range(5):
            js = [j for j in range(i) if A[j] < A[i]]
            line = M(f"f({i + 1}) = 1" + "".join(f" + f({j + 1})" for j in js) + f" = {F[i]}", size=26,
                     color=ACCENT).scale(sc)
            if line.width > calc_slot.width:
                line.scale_to_fit_width(calc_slot.width)
            line.move_to(calc_slot)
            with self.voice(texts[i]):
                hl = [ar.cells[j][0].animate.set_fill(GOOD, 0.6) for j in js]
                self.play(FadeIn(line) if cur is None else Transform(cur, line), *hl, run_time=0.5)
                if cur is None:
                    cur = line
                self.play(setv(fr.cells[i], F[i], GOOD if i == 4 else INK),
                          *[ar.cells[j][0].animate.set_fill(PANEL_2, 1) for j in js], run_time=0.4)
        with self.voice("Tổng 1 cộng 1 cộng 3 cộng 1 cộng 7 bằng 13. Nhưng hai vòng lặp lồng nhau tốn khoảng n bình phương chia 2 "
                        "phép: với n bằng hai trăm nghìn, hai mươi tỉ phép, quá chậm."):
            self.play(FadeIn(cnt), run_time=0.8)

        self.clear_body()
        self.show_header("Bế tắc: Tổng tiền tố trên TRỤC GIÁ TRỊ")
        ax = NumberLine(x_range=[0, 6, 1], length=6.5, include_numbers=False, color=MUTED, stroke_width=3)
        nums = VGroup(*[T(str(v), size=24, color=MUTED).next_to(ax.n2p(v), DOWN, buff=0.15) for v in range(0, 7)])
        stacks = VGroup()
        for i in range(4):
            d = Dot(ax.n2p(A[i]) + UP * (0.35 + 0.5 * sum(1 for j in range(i) if A[j] == A[i])), radius=0.2,
                    color=BLUEC)
            lab = T(f"f={F[i]}", size=20, color=BLUEC).next_to(d, RIGHT, buff=0.08)
            stacks.add(VGroup(d, lab))
        q = Arrow(ax.n2p(5) + UP * 1.8, ax.n2p(5) + UP * 0.3, color=ACCENT, buff=0, stroke_width=5)
        ql = T("a₅ = 5", size=24, color=ACCENT).next_to(q, UP, buff=0.08)
        br = BraceBetweenPoints(ax.n2p(0) + DOWN * 0.55, ax.n2p(4.6) + DOWN * 0.55, direction=DOWN, color=GOOD)
        bl = T("tổng các f ở vị trí < 5", size=24, color=GOOD).next_to(br, DOWN, buff=0.1)
        axis_g = VGroup(ax, nums, stacks, q, ql, br, bl)
        dead = VGroup(T("Coi a_j là VỊ TRÍ trên trục số: câu hỏi là", size=28),
                      TB("TỔNG TIỀN TỐ trên trục giá trị", size=32, color=GOOD),
                      T("Nhưng các giá trị được THÊM DẦN trong lúc hỏi", size=28, color=BAD),
                      T("(khác mảng cộng dồn tĩnh ở Bài 13)", size=26, color=MUTED)).arrange(DOWN, buff=0.12)
        need = TB("Cần: THÊM nhanh + HỎI tổng tiền tố nhanh", size=32, color=ACCENT)
        fit_stack(axis_g, dead, need, buff=0.7, max_scale=1.2)
        with self.voice("Bế tắc: với mỗi i, ta cần tổng của f j trên các j đã xử lí có a j nhỏ hơn a i. Coi giá trị a j là vị trí "
                        "trên một trục số."):
            self.play(Create(ax), FadeIn(nums), run_time=0.6)
            self.play(LaggedStart(*[FadeIn(s, shift=DOWN * 0.2) for s in stacks], lag_ratio=0.3), run_time=1.2)
        with self.voice("Khi tới a 5 bằng 5, câu hỏi là: tổng các f đã đặt tại những vị trí nhỏ hơn 5. Đó là một tổng tiền tố "
                        "trên trục giá trị."):
            self.play(GrowArrow(q), FadeIn(ql), run_time=0.5)
            self.play(GrowFromCenter(br), FadeIn(bl), FadeIn(dead[0:2]), run_time=0.8)
        with self.voice("Nhưng khác với mảng cộng dồn ở Bài 13, ở đây các giá trị được thêm dần trong lúc ta hỏi. Cần một cấu trúc "
                        "vừa thêm nhanh, vừa hỏi tổng tiền tố nhanh."):
            self.play(FadeIn(dead[2:]), run_time=0.6)
            self.play(FadeIn(need), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B14_02_Fenwick(B14Scene):
    def construct(self):
        self.show_header("Bước 1: Nén giá trị")
        why = VGroup(T("a_i tới 10⁹, nhưng chỉ có ≤ n giá trị khác nhau,", size=27),
                     T("và ta chỉ cần THỨ TỰ giữa chúng.", size=27, color=ACCENT)).arrange(DOWN, buff=0.08)
        ar = array_row(A, w=1.0, h=0.95, size=40, index_from=1, label="a")
        sorted_row = VGroup(T("giá trị khác nhau, sắp xếp:", size=26, color=MUTED),
                            array_row(VALS, w=0.95, h=0.9, size=36, index_from=1, label="hạng")).arrange(DOWN, buff=0.15)
        rr = ghost_row(5, w=1.0, h=0.95, size=40, show_index=False, label="hạng")
        res = M("3 1 4 1 5  →  2 1 3 1 4", size=30, color=GOOD)
        fit_stack(why, ar, sorted_row, rr, res, buff=0.5, max_scale=1.2)
        with self.voice("Bước một: nén giá trị. Giá trị a i có thể tới 10 mũ 9, nhưng chỉ có tối đa n giá trị khác nhau, và ta chỉ "
                        "quan tâm đến thứ tự giữa chúng."):
            self.play(FadeIn(why), FadeIn(ar), run_time=0.8)
        with self.voice("Sắp xếp các giá trị khác nhau: 1, 3, 4, 5. Thay mỗi a i bằng hạng của nó."):
            self.play(FadeIn(sorted_row), run_time=0.6)
            self.play(FadeIn(rr), run_time=0.4)
            self.play(LaggedStart(*[setv(rr.cells[i], RANK[i], ORANGE) for i in range(5)], lag_ratio=0.3), run_time=1.5)
        with self.voice("Dãy 3, 1, 4, 1, 5 trở thành 2, 1, 3, 1, 4. Trục giá trị giờ chỉ dài 4 ô thay vì 10 mũ 9."):
            self.play(FadeIn(res), run_time=0.6)

        self.clear_body()
        self.show_header("Bước 2: Cây Fenwick")
        m = 8
        cw = 0.85
        idx = VGroup(*[cell(str(i), w=cw, h=0.6, size=26, fill=BG, color=MUTED) for i in range(1, m + 1)]).arrange(RIGHT, buff=0)
        bars = {}
        for i in range(1, m + 1):
            lb = lowbit(i)
            lvl = {1: 0, 2: 1, 4: 2, 8: 3}[lb]
            x0 = idx[i - lb][0].get_left()[0]
            x1 = idx[i - 1][0].get_right()[0]
            r = RoundedRectangle(width=x1 - x0 - 0.08, height=0.5, corner_radius=0.1, fill_color=PANEL_2, fill_opacity=1,
                                 stroke_color=[BLUEC, GOOD, ORANGE, PURPLE][lvl], stroke_width=3)
            r.move_to([(x0 + x1) / 2, idx.get_top()[1] + 0.45 + lvl * 0.65, 0])
            t = TB(f"t[{i}]", size=22).move_to(r).align_to(r, RIGHT).shift(LEFT * 0.08)
            bars[i] = VGroup(r, t)
        tree = VGroup(idx, *bars.values())
        rule = VGroup(T("t[i] = tổng của đoạn dài (i & −i)", size=30),
                      T("KẾT THÚC tại i", size=30),
                      T("(i & −i = bit 1 thấp nhất của i)", size=26, color=MUTED)).arrange(DOWN, buff=0.08)
        qline = VGroup(VGroup(TB("Hỏi tổng 1..p:", size=30, color=GOOD), M("p -= p & -p", size=28, color=GOOD)
                              ).arrange(RIGHT, buff=0.3),
                       T("p = 7: t[7] + t[6] + t[4]", size=28)).arrange(DOWN, buff=0.08)
        aline = VGroup(VGroup(TB("Thêm vào p:", size=30, color=ORANGE), M("p += p & -p", size=28, color=ORANGE)
                              ).arrange(RIGHT, buff=0.3),
                       T("p = 3: t[3], t[4], t[8]", size=28)).arrange(DOWN, buff=0.08)
        cost = T("Mỗi thao tác ≤ log₂ m + 1 ô: O(log n)", size=30, color=ACCENT)
        fit_stack(rule, tree, qline, aline, cost, buff=0.5, max_scale=1.15)
        with self.voice("Bước hai: cây Fenwick. Nó là một mảng t từ 1 đến m, trong đó t của i lưu tổng của một đoạn dài i AND trừ "
                        "i, kết thúc tại i. i AND trừ i chính là giá trị của bit 1 thấp nhất của i."):
            self.play(FadeIn(rule), FadeIn(idx), run_time=0.8)
            self.play(LaggedStart(*[FadeIn(b, shift=DOWN * 0.1) for b in bars.values()], lag_ratio=0.15), run_time=1.6)
        with self.voice("Số lẻ có bit thấp nhất là 1, nên chỉ giữ chính nó. t của 2 và t của 6 giữ đoạn dài 2; t của 4 giữ đoạn "
                        "dài 4; t của 8 giữ cả 8 ô."):
            self.play(Indicate(VGroup(*[bars[i] for i in (2, 6)]), color=GOOD), run_time=0.8)
            self.play(Indicate(bars[4], color=ORANGE), Indicate(bars[8], color=PURPLE), run_time=0.8)

        def flash(path, col):
            return [bars[p][0].animate.set_fill(col, 0.75) for p in path]

        def reset():
            return [bars[p][0].animate.set_fill(PANEL_2, 1) for p in bars]

        with self.voice("Hỏi tổng tiền tố từ 1 đến p: cộng t của p, rồi bỏ bit thấp nhất của p, lặp tới khi p bằng 0. Ví dụ p "
                        "bằng 7: t 7, rồi t 6, rồi t 4. Ba ô ghép lại vừa khít đoạn 1 đến 7."):
            self.play(FadeIn(qline), run_time=0.5)
            for p in query_path(7):
                self.play(*flash([p], GOOD), run_time=0.4)
        self.play(*reset(), run_time=0.3)
        with self.voice("Thêm x vào vị trí p: cộng x vào t của p, rồi cộng bit thấp nhất vào p, lặp tới khi vượt m. Ví dụ p bằng "
                        "3: t 3, t 4, t 8, đúng các đoạn chứa ô 3."):
            self.play(FadeIn(aline), run_time=0.5)
            for p in add_path(3, m):
                self.play(*flash([p], ORANGE), run_time=0.4)
        with self.voice("Mỗi bước làm bit 1 thấp nhất dịch lên ít nhất một vị trí, nên mỗi thao tác đi qua tối đa log 2 của m "
                        "cộng 1 ô: O của log n."):
            self.play(*reset(), FadeIn(cost), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B14_03_ChayTay(B14Scene):
    def construct(self):
        self.show_header("Bước 3: Ghép vào QHĐ — chạy tay")
        rule = VGroup(M("f(i) = 1 + prefixSum(r − 1)", size=30, color=ACCENT),
                      VGroup(T("rồi", size=28), M("add(r, f(i))", size=30, color=ORANGE),
                             T("(r = hạng của a_i)", size=24, color=MUTED)).arrange(RIGHT, buff=0.2)).arrange(DOWN, buff=0.1)
        ar = array_row(A, w=1.0, h=0.85, size=34, index_from=1, label="a")
        rr = array_row(RANK, w=1.0, h=0.85, size=34, show_index=False, label="hạng")
        fr = ghost_row(5, w=1.0, h=0.85, size=34, show_index=False, label="f")
        top = VGroup(ar, rr, fr).arrange(DOWN, buff=0.12, aligned_edge=RIGHT)
        for c in rr.cells:
            c[1].set_color(ORANGE)
        axis_t = T("Trục giá trị (cây Fenwick lưu tổng các ô này):", size=25, color=MUTED)
        axis = ghost_row(4, w=1.3, h=0.95, size=36, index_from=1, label="hạng")
        for c in axis.cells:
            c[1].set_opacity(1).set_color(MUTED)
        calc_slot = placeholder(7.2, 0.8)
        res = TB("Đáp án = 1 + 1 + 3 + 1 + 7 = 13  ✓", size=34, color=GOOD)
        sc = fit_stack(rule, top, VGroup(axis_t, axis).arrange(DOWN, buff=0.2), calc_slot, res, buff=0.5, max_scale=1.15)
        with self.voice("Bước ba: ghép vào quy hoạch động. Duyệt i từ trái sang phải. Tại i, hỏi tổng tiền tố đến hạng của a i trừ "
                        "1, tức các giá trị nhỏ hơn hẳn a i đã xuất hiện, cộng 1 để được f của i; rồi thêm f của i vào vị trí "
                        "hạng."):
            self.play(FadeIn(rule), FadeIn(top), run_time=0.8)
            self.play(FadeIn(axis_t), FadeIn(axis), run_time=0.6)
        axis_val = [0] * 5
        speech = [
            "i bằng 1, a bằng 3, hạng 2: tổng tiền tố đến hạng 1 bằng 0, nên f bằng 1. Thêm 1 vào hạng 2.",
            "i bằng 2, a bằng 1, hạng 1: tổng đến hạng 0 bằng 0, f bằng 1. Thêm vào hạng 1.",
            "i bằng 3, a bằng 4, hạng 3: tổng đến hạng 2 bằng 1 cộng 1 bằng 2, f bằng 3. Thêm 3 vào hạng 3.",
            "i bằng 4, a bằng 1, hạng 1: tổng đến hạng 0 bằng 0, f bằng 1. Hạng 1 giờ là 2.",
            "i bằng 5, a bằng 5, hạng 4: tổng đến hạng 3 bằng 2 cộng 1 cộng 3 bằng 6, f bằng 7.",
        ]
        cur = None
        for (i, a, r, pre, fv), sp in zip(TRACE, speech):
            line = M(f"i={i}: hạng {r}, prefixSum({r - 1}) = {pre} ⇒ f = {fv}", size=26, color=ACCENT).scale(sc)
            if line.width > calc_slot.width:
                line.scale_to_fit_width(calc_slot.width)
            line.move_to(calc_slot)
            with self.voice(sp):
                hl = [axis.cells[k][0].animate.set_fill(GOOD, 0.6) for k in range(r - 1)]
                self.play(ar.cells[i - 1][0].animate.set_stroke(ACCENT, 5),
                          FadeIn(line) if cur is None else Transform(cur, line), *hl, run_time=0.5)
                if cur is None:
                    cur = line
                self.play(setv(fr.cells[i - 1], fv, GOOD if i == 5 else INK), run_time=0.4)
                axis_val[r] += fv
                self.play(axis.cells[r - 1][0].animate.set_fill(ORANGE, 0.6),
                          setv(axis.cells[r - 1], axis_val[r], INK), run_time=0.4)
                self.play(ar.cells[i - 1][0].animate.set_stroke(MUTED, 2),
                          *[axis.cells[k][0].animate.set_fill(PANEL_2, 1) for k in range(4)], run_time=0.3)
        with self.voice("Đáp án là tổng mọi f: 13, khớp với ví dụ."):
            self.play(FadeIn(res), run_time=0.6)

        self.clear_body()
        self.show_header("DEMDAYTANG.CPP: O(n log n)")
        code = code_block(FEN_CODE, size=21)
        cx = tag_box("ĐỘ PHỨC TẠP", [
            "Nén giá trị (sắp xếp): O(n log n)",
            "Mỗi phần tử: tìm hạng + hỏi + thêm, mỗi lần O(log n)",
            "Tổng O(n log n): n = 2·10⁵ ⇒ ≈ 10⁷ phép",
        ], accent=GOOD, width=7.5, size=27)
        fit_stack(code, cx, buff=0.7, max_scale=1.2)
        with self.voice("Code: hàm add đi lên bằng p cộng p AND trừ p; hàm prefixSum đi xuống bằng p trừ p AND trừ p. Trong main, "
                        "với mỗi phần tử: f bằng 1 cộng tổng tiền tố đến hạng trừ 1, rồi add vào hạng, và cộng vào đáp án."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 1, ORANGE)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 6, GOOD)), run_time=0.4)
            self.play(Transform(hl, line_box(code, 11, ACCENT)), run_time=0.4)
        with self.voice("Độ phức tạp: nén giá trị tốn O của n log n để sắp xếp; mỗi phần tử một lần tìm hạng, một lần hỏi, một lần "
                        "thêm, mỗi lần O của log n. Tổng O của n log n: khoảng 10 triệu phép."):
            self.play(FadeOut(hl), FadeIn(cx), run_time=0.8)

        self.clear_body()
        self.show_header("Biến thể: Cây Fenwick cho MAX")
        cards = list_cards([
            ("Dãy tăng có tổng trọng số lớn nhất", "f(i) = w_i + max f(j), a_j < a_i"),
            ("Fenwick cho max tiền tố", "điều kiện: giá trị mỗi vị trí CHỈ TĂNG"),
            ("Số dãy tăng DÀI NHẤT", "Fenwick lưu cặp (độ dài, số cách)"),
        ], accent=ORANGE)
        fit_stack(cards, max_scale=1.3)
        sp = ["Biến thể: muốn dãy con tăng có tổng trọng số lớn nhất, ta cần max thay vì tổng: f của i bằng w i cộng max f của j "
              "với a j nhỏ hơn a i.",
              "Cây Fenwick vẫn dùng được cho max tiền tố, với điều kiện giá trị tại mỗi vị trí chỉ tăng lên, đúng với bài này.",
              "Ghép cả hai, lưu cặp độ dài lớn nhất và số cách, ta đếm được số dãy con tăng dài nhất."]
        for c, s in zip(cards, sp):
            with self.voice(s):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B14_04_MaTran(B14Scene):
    def construct(self):
        self.show_header("3. Bài toán MATMADEN: n khổng lồ")
        task = tag_box("BÀI TOÁN: MATMADEN", [
            "Dãy n bóng đèn, mỗi bóng Đỏ, Vàng hoặc Xanh.",
            "KHÔNG có hai bóng ĐỎ cạnh nhau, KHÔNG có hai",
            "bóng XANH cạnh nhau. Đếm số cách, lấy dư 10⁹ + 7.",
            "1 ≤ n ≤ 10¹⁸",
        ], width=7.5, size=27)
        task[3][3].set_color(BAD)
        pairs = VGroup()
        for a in "ĐVX":
            for b in "ĐVX":
                g = VGroup(bulb(a, 0.26), bulb(b, 0.26)).arrange(RIGHT, buff=0.06)
                for bb in g:
                    bb[1].move_to(bb[0])
                if a == b and a != "V":
                    cross = Cross(g, stroke_color=BAD, stroke_width=5)
                    g.add(cross)
                pairs.add(g)
        pairs.arrange_in_grid(rows=3, cols=3, buff=(0.5, 0.25))
        ex = VGroup(T("n = 2:  9 − 2 =", size=30), TB("7", size=36, color=GOOD), T("n = 3:", size=30),
                    TB("17", size=36, color=GOOD)).arrange(RIGHT, buff=0.25)
        fit_stack(task, pairs, ex, buff=0.6, max_scale=1.2)
        with self.voice("Bài toán MATMADEN: một dãy đèn trang trí gồm n bóng xếp hàng, mỗi bóng có một trong ba màu đỏ, vàng, xanh. "
                        "Để đẹp mắt, không được có hai bóng đỏ cạnh nhau, và không được có hai bóng xanh cạnh nhau. n tới 10 mũ "
                        "18!"):
            self.play(FadeIn(task), run_time=0.8)
        with self.voice("Với n bằng 2: có 9 cách ghép hai màu, trừ đi đỏ đỏ và xanh xanh, còn 7. Với n bằng 3, có 17 cách."):
            self.play(LaggedStart(*[FadeIn(p) for p in pairs], lag_ratio=0.1), run_time=1.2)
            self.play(FadeIn(ex), run_time=0.5)

        self.clear_body()
        self.show_header("Quy hoạch động thông thường")
        pos = {"Đ": LEFT * 2.2 + DOWN * 0.3, "V": UP * 1.2, "X": RIGHT * 2.2 + DOWN * 0.3}
        nodes = {c: bulb(c, 0.42).move_to(p) for c, p in pos.items()}
        for nd in nodes.values():
            nd[1].move_to(nd[0])
        edges = VGroup()
        for a, b in [("Đ", "V"), ("Đ", "X"), ("V", "Đ"), ("V", "X"), ("X", "Đ"), ("X", "V")]:
            pa, pb = nodes[a][0].get_center(), nodes[b][0].get_center()
            d = (pb - pa) / np.linalg.norm(pb - pa)
            perp = np.array([-d[1], d[0], 0]) * 0.12
            edges.add(Arrow(pa + d * 0.45 + perp, pb - d * 0.45 + perp, buff=0, color=MUTED, stroke_width=3, tip_length=0.18))
        loop = CurvedArrow(nodes["V"][0].get_top() + LEFT * 0.25, nodes["V"][0].get_top() + RIGHT * 0.25, angle=-PI * 1.4,
                           color=MUTED, stroke_width=3, tip_length=0.15)
        graph = VGroup(edges, loop, *nodes.values())
        rec = VGroup(M("d[i] = v[i−1] + x[i−1]", size=30, color=BAD),
                     M("v[i] = d[i−1] + v[i−1] + x[i−1]", size=30, color=ACCENT),
                     M("x[i] = d[i−1] + v[i−1]", size=30, color=GOOD)).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        tbl = VGroup()
        head = VGroup(*[TB(h, size=34, color=c) for h, c in [("i", MUTED), ("d", BAD), ("v", ACCENT), ("x", GOOD),
                                                               ("tổng", INK)]]).arrange(RIGHT, buff=0.9)
        tbl.add(head)
        for i, r in enumerate(ROWS, 1):
            row = VGroup(*[M(str(v), size=34) for v in (i, *r, sum(r))])
            for k, mob in enumerate(row):
                mob.move_to([head[k].get_x(), 0, 0])
            tbl.add(row)
        for k in range(1, len(tbl)):
            tbl[k].next_to(tbl[k - 1], DOWN, buff=0.15)
            for j, mob in enumerate(tbl[k]):
                mob.set_x(head[j].get_x())
        slow = VGroup(T("n hàng, mỗi hàng O(1): O(n)", size=28),
                      T("n = 10¹⁸ ⇒ hơn 30 năm!", size=30, color=BAD)).arrange(DOWN, buff=0.08)
        fit_stack(graph, rec, tbl, slow, buff=0.45, max_scale=1.15)
        with self.voice("Màu tiếp theo chỉ phụ thuộc màu của bóng cuối, nên trạng thái là số bóng và màu bóng cuối. Đồ thị chuyển "
                        "màu: từ đỏ sang vàng hoặc xanh; từ vàng sang cả ba; từ xanh sang đỏ hoặc vàng."):
            self.play(*[FadeIn(n) for n in nodes.values()], run_time=0.5)
            self.play(LaggedStart(*[GrowArrow(e) for e in edges], lag_ratio=0.1), Create(loop), run_time=1.2)
        with self.voice("Gọi d i, v i, x i là số dãy dài i kết thúc bằng đỏ, vàng, xanh. d i bằng v cộng x của hàng trước; v i bằng "
                        "tổng cả ba; x i bằng d cộng v."):
            self.play(FadeIn(rec), run_time=0.8)
        with self.voice("Bảng: hàng 1 là 1, 1, 1; hàng 2 là 2, 3, 2, tổng 7; hàng 3 tổng 17; hàng 4 là 12, 17, 12, tổng 41."):
            self.play(FadeIn(tbl[0]), run_time=0.3)
            for r in tbl[1:]:
                self.play(FadeIn(r, shift=DOWN * 0.1), run_time=0.4)
        with self.voice("Bảng có n hàng, mỗi hàng O của 1. Với n bằng 10 mũ 18, cần hơn 30 năm. Mỗi hàng được tính từ hàng trước "
                        "bằng cùng một quy tắc tuyến tính, lặp lại 10 mũ 18 lần. Có cách nào gộp nhiều lần lặp thành một bước?"):
            self.play(FadeIn(slow), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B14_05_LuyThua(B14Scene):
    def construct(self):
        self.show_header("Phá bế tắc: Viết dưới dạng nhân ma trận")
        vec = VGroup(T("[d, v, x] ở bóng i  =", size=30, color=ACCENT),
                     T("[d, v, x] ở bóng i − 1  ·  M", size=30, color=ACCENT)).arrange(DOWN, buff=0.1)
        lab_r = VGroup(*[TB(c, size=26, color=COLORS[c]) for c in "ĐVX"])
        lab_c = VGroup(*[TB(c, size=26, color=COLORS[c]) for c in "ĐVX"])
        mm = matrix_mob(M3, size=40, cell_w=0.85, highlight=GOOD)
        for k, l in enumerate(lab_r):
            l.next_to(mm.cells[3 * k], LEFT, buff=0.55)
        for k, l in enumerate(lab_c):
            l.next_to(mm.cells[k], UP, buff=0.35)
        mlab = TB("M =", size=40).next_to(VGroup(mm, lab_r), LEFT, buff=0.3)
        mat = VGroup(mlab, mm, lab_r, lab_c)
        note = VGroup(T("hàng = màu trước, cột = màu sau,", size=26, color=MUTED),
                      T("ô = 1 nếu được chuyển", size=26, color=MUTED)).arrange(DOWN, buff=0.06)
        ans = VGroup(T("[d, v, x] ở bóng n = [1, 1, 1] · Mⁿ⁻¹", size=28, color=GOOD),
                     T("⇒ đáp án = TỔNG mọi phần tử của Mⁿ⁻¹", size=28)).arrange(DOWN, buff=0.12)
        fit_stack(vec, mat, note, ans, buff=0.6, max_scale=1.2)
        with self.voice("Phá bế tắc: xếp ba giá trị thành một vectơ hàng d, v, x. Quy tắc chuyển chính là phép nhân vectơ với một "
                        "ma trận M."):
            self.play(FadeIn(vec), run_time=0.6)
        with self.voice("Hàng của M là màu trước, cột là màu sau; ô bằng 1 nếu được chuyển. Hàng đỏ: không sang đỏ, sang vàng và "
                        "xanh được. Hàng vàng: sang cả ba. Hàng xanh: sang đỏ và vàng."):
            self.play(FadeIn(mat), FadeIn(note), run_time=1.0)
            for k in range(3):
                self.play(Indicate(VGroup(*mm.cells[3 * k:3 * k + 3]), color=COLORS["ĐVX"[k]]), run_time=0.5)
        with self.voice("Vì vậy vectơ ở bước n bằng vectơ toàn 1 nhân M mũ n trừ 1, và đáp án là tổng mọi phần tử của M mũ n trừ "
                        "1."):
            self.play(FadeIn(ans), run_time=0.8)

        self.clear_body()
        self.show_header("Lũy thừa nhanh: M¹³ = M⁸ · M⁴ · M¹")
        prop = VGroup(T("Nhân ma trận có tính KẾT HỢP ⇒ lũy thừa nhanh:", size=30),
                      T("M²ᵏ = (Mᵏ)²", size=34, color=ACCENT),
                      T("M²ᵏ⁺¹ = M²ᵏ · M", size=34, color=ACCENT)).arrange(DOWN, buff=0.12)
        bits = VGroup(T("13 =", size=36), *[cell(b, w=0.8, h=0.85, size=36, fill=GOOD if b == "1" else PANEL_2,
                                                 color=BG if b == "1" else MUTED) for b in "1101"],
                      T("₂", size=36)).arrange(RIGHT, buff=0.08)
        bitlab = VGroup(*[T(s, size=24, color=MUTED).next_to(bits[1 + k], DOWN, buff=0.1) for k, s in
                          enumerate(["M⁸", "M⁴", "M²", "M¹"])])
        chain = VGroup(*[panel(T(s, size=36), pad=0.18, stroke=c) for s, c in
                         [("M¹", GOOD), ("M²", MUTED), ("M⁴", GOOD), ("M⁸", GOOD)]]).arrange(RIGHT, buff=0.5)
        sq = VGroup(*[Arrow(chain[k].get_right(), chain[k + 1].get_left(), buff=0.05, color=MUTED, stroke_width=3,
                            tip_length=0.15) for k in range(3)])
        sql = T("bình phương liên tiếp", size=24, color=MUTED).next_to(chain, UP, buff=0.15)
        res = VGroup(M("M¹³ = M⁸ · M⁴ · M¹", size=32, color=ACCENT),
                     T("3 phép bình phương + 3 phép nhân thay vì 12 phép nhân", size=25, color=MUTED)).arrange(DOWN, buff=0.1)
        fit_stack(prop, VGroup(bits, bitlab), VGroup(sql, chain, sq), res, buff=0.6, max_scale=1.2)
        with self.voice("Phép nhân ma trận có tính kết hợp, nên tính M mũ k giống hệt lũy thừa nhanh của số nguyên: M mũ 2k bằng "
                        "bình phương của M mũ k."):
            self.play(FadeIn(prop), run_time=0.8)
        with self.voice("Ví dụ M mũ 13. Viết 13 trong hệ nhị phân: 1101, gồm các bit ứng với 8, 4 và 1."):
            self.play(FadeIn(bits), FadeIn(bitlab), run_time=0.8)
        with self.voice("Bình phương liên tiếp được M mũ 1, mũ 2, mũ 4, mũ 8; nhân vào kết quả khi bit bằng 1. M mũ 13 bằng M mũ 8 "
                        "nhân M mũ 4 nhân M mũ 1."):
            self.play(FadeIn(sql), LaggedStart(*[FadeIn(c) for c in chain], lag_ratio=0.3),
                      LaggedStart(*[GrowArrow(a) for a in sq], lag_ratio=0.3), run_time=1.5)
            self.play(FadeIn(res), run_time=0.6)

        self.clear_body()
        self.show_header("MATMADEN.CPP: O(3³ · log n)")
        code = code_block(MAT_CODE, size=22)
        cx = tag_box("ĐỘ PHỨC TẠP", [
            "Nhân ma trận k × k: k³ phép; ≈ 2·log₂ n ≤ 120 phép nhân",
            "k = 3: ≈ 120 · 27 ≈ 3 200 phép nhân số",
            "Từ hơn 30 năm xuống dưới một phần triệu giây!",
        ], accent=GOOD, width=7.5, size=26)
        cx[3][2].set_color(GOOD)
        fit_stack(code, cx, buff=0.7, max_scale=1.2)
        with self.voice("Code: step là ma trận M, power bắt đầu là ma trận đơn vị. Duyệt các bit của số mũ n trừ 1: nếu bit bằng 1 "
                        "thì nhân step vào power; luôn bình phương step; rồi dịch số mũ sang phải."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 4, GOOD)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 5, ACCENT)), run_time=0.4)
        with self.voice("Mỗi phép nhân ma trận 3 nhân 3 tốn 27 phép nhân số, có khoảng 2 log n, tối đa 120 phép nhân ma trận: tổng "
                        "khoảng ba nghìn hai trăm phép. Từ hơn 30 năm xuống dưới một phần triệu giây!"):
            self.play(FadeOut(hl), FadeIn(cx), run_time=0.8)

        self.clear_body()
        self.show_header("Khi nào dùng được lũy thừa ma trận?")
        when = tag_box("ĐIỀU KIỆN", [
            "• Công thức chuyển TUYẾN TÍNH (tổng có hệ số",
            "   của các giá trị cũ) và GIỐNG NHAU ở mọi bước",
            "• Số trạng thái mỗi “hàng” nhỏ (k ≤ ~100),",
            "   vì chi phí là k³ · log n",
        ], accent=PURPLE, width=7.5, size=28)
        exs = list_cards([
            ("NHAYDA (Bài 1)", "ma trận 3 × 3 cho bộ ba (f_i, f_{i−1}, f_{i−2})"),
            ("Dãy Fibonacci", "ma trận 2 × 2"),
            ("Đường đi độ dài n trên đồ thị", "lũy thừa của ma trận kề"),
        ], accent=PURPLE)
        fit_stack(when, exs, buff=0.6, max_scale=1.2)
        with self.voice("Khi nào dùng được lũy thừa ma trận? Khi công thức chuyển là tuyến tính, mỗi giá trị mới là tổng có hệ số "
                        "của các giá trị cũ, và giống nhau ở mọi bước; và số trạng thái trong một hàng nhỏ, khoảng không quá "
                        "100, vì chi phí là k mũ 3 nhân log n."):
            self.play(FadeIn(when), run_time=1.0)
        with self.voice("Ví dụ: bài nhảy đá ở Bài 1 dùng ma trận 3 nhân 3; dãy Fibonacci dùng ma trận 2 nhân 2; đếm đường đi độ dài "
                        "n trên đồ thị dùng lũy thừa ma trận kề."):
            self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.3) for c in exs], lag_ratio=0.3), run_time=1.2)
        self.clear_body()


# ----------------------------------------------------------------------------
class B14_06_TongKet(B14Scene):
    def construct(self):
        self.show_header("4. Nhận dạng câu hỏi bên trong công thức")
        rows = [
            ("Tổng đoạn liên tiếp các ô trước", "Mảng cộng dồn", "O(1) mỗi ô", BLUEC),
            ("Max/min cửa sổ trượt", "Hàng đợi đơn điệu", "O(1) khấu hao", GOOD),
            ("Tổng/max theo GIÁ TRỊ nhỏ hơn", "Fenwick + nén giá trị", "O(log n) mỗi ô", ORANGE),
            ("Lặp một phép biến đổi tuyến tính", "Lũy thừa ma trận", "O(k³ log n) cả bài", PURPLE),
        ]
        cards = VGroup()
        for a, b, c, col in rows:
            g = VGroup(T(a, size=26), VGroup(T("→", size=27), TB(b, size=28, color=col), T(c, size=24, color=MUTED)
                                             ).arrange(RIGHT, buff=0.2)).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            p = panel(g, width=7.5, stroke=col, pad=0.22)
            p[1].align_to(p[0], LEFT).shift(RIGHT * 0.22)
            cards.add(p)
        cards.arrange(DOWN, buff=0.25)
        fit_stack(cards, max_scale=1.3)
        sp = ["Mở rộng một: nhận dạng câu hỏi bên trong công thức chuyển. Tổng trên đoạn liên tiếp các ô trước: mảng cộng dồn, O "
              "của 1 mỗi ô.",
              "Max hoặc min trên cửa sổ trượt: hàng đợi đơn điệu, O của 1 khấu hao.",
              "Tổng hoặc max theo giá trị nhỏ hơn: cây Fenwick cùng nén giá trị, O của log n mỗi ô.",
              "Lặp lại một phép biến đổi tuyến tính rất nhiều lần: lũy thừa ma trận, k mũ 3 log n cho cả bài."]
        for c, s in zip(cards, sp):
            with self.voice(s):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Mở rộng 2: Trên đường tới HSG quốc gia")
        adv = list_cards([
            ("Bao lồi (convex hull trick)", "công thức dạng min(a_j · x_i + b_j)"),
            ("Chia để trị", "khi điểm chia tối ưu đơn điệu"),
            ("Cây phân đoạn", "cập nhật và hỏi trên đoạn bất kì"),
        ], accent=PURPLE)
        spirit = TB("Cùng tinh thần: giữ nguyên công thức, thay cách tính", size=30, color=ACCENT)
        fit_stack(adv, spirit, buff=0.7, max_scale=1.3)
        with self.voice("Mở rộng hai: trên con đường tới kì thi học sinh giỏi quốc gia, em sẽ gặp thêm: bao lồi, cho công thức dạng "
                        "min của a j nhân x i cộng b j; chia để trị, khi điểm chia tối ưu đơn điệu; và cây phân đoạn, khi cần cập "
                        "nhật và hỏi trên đoạn bất kì."):
            self.play(LaggedStart(*[FadeIn(c, shift=RIGHT * 0.3) for c in adv], lag_ratio=0.4), run_time=1.5)
        with self.voice("Tất cả đều tuân theo cùng tinh thần của chương này: giữ nguyên công thức, thay cách tính."):
            self.play(FadeIn(spirit), run_time=0.6)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Quên nén giá trị", "mảng Fenwick cỡ 10⁹ phần tử: quá lớn",
             "Bẫy một: quên nén giá trị, mảng Fenwick cỡ 10 mũ 9 phần tử là quá lớn."),
            ("Truy vấn sai ngưỡng", "tăng ngặt: hỏi tới hạng − 1; không giảm: tới hạng",
             "Bẫy hai: truy vấn sai ngưỡng. Tăng ngặt thì hỏi đến hạng trừ 1; không giảm thì hỏi đến hạng."),
            ("Fenwick đánh chỉ số từ 1", "vị trí 0: p += p & −p không bao giờ dừng",
             "Bẫy ba: cây Fenwick đánh chỉ số từ 1. Vị trí 0 làm vòng lặp cộng p AND trừ p không bao giờ dừng."),
            ("Tràn số khi nhân ma trận", "lấy dư NGAY sau mỗi phép nhân",
             "Bẫy bốn: tràn số khi nhân ma trận. Hai số nhỏ hơn 10 mũ 9 cộng 7 nhân nhau vừa long long, nhưng phải lấy dư "
             "ngay sau mỗi phép nhân."),
            ("n = 1", "M⁰ là ma trận đơn vị: chương trình vẫn đúng",
             "Bẫy năm: n bằng 1. Lũy thừa M mũ 0 là ma trận đơn vị; chương trình ở trên xử lí đúng."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 14", [
            "• Tổng hay max của các trạng thái theo GIÁ TRỊ:",
            "   nén giá trị + cây Fenwick, O(log n) mỗi bước",
            "• Truy hồi TUYẾN TÍNH, hệ số cố định, n rất lớn:",
            "   nhân ma trận, lũy thừa nhanh O(k³ log n)",
            "• Công thức QHĐ cho biết CẦN TÍNH GÌ;",
            "   cấu trúc dữ liệu cho biết TÍNH NHANH THẾ NÀO",
        ], accent=GOOD, width=7.5, size=29)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: tổng hay max của các trạng thái theo giá trị thì dùng nén giá trị cùng cây Fenwick, O của log n "
                        "mỗi bước. Truy hồi tuyến tính, hệ số cố định, n rất lớn thì viết thành nhân ma trận, lũy thừa nhanh."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:4]), run_time=1.0)
        with self.voice("Công thức quy hoạch động cho biết cần tính gì; cấu trúc dữ liệu cho biết tính nhanh thế nào."):
            self.play(FadeIn(mem[3][4:]), run_time=0.6)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["MATMADEN với n = 4", "có bao nhiêu cách?"], size=40, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        work = VGroup(M("i=3: (5, 7, 5)", size=30, color=MUTED),
                      M("i=4: d = 7 + 5 = 12, v = 5 + 7 + 5 = 17,", size=26),
                      M("     x = 5 + 7 = 12", size=26)).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        work[2].become(M("x = 5 + 7 = 12", size=26).move_to(work[2], aligned_edge=LEFT))
        ans = TB("12 + 17 + 12 = 41", size=44, color=GOOD)
        fit_stack(q, timer_slot, work, ans, buff=0.6, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: bài MATMADEN với n bằng 4 có bao nhiêu cách? Dừng video và thử nhé!"):
            self.play(FadeIn(q), run_time=0.8)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("Từ hàng 3 là 5, 7, 5: d bằng 7 cộng 5 bằng 12, v bằng 17, x bằng 12. Tổng 41 cách."):
            self.play(FadeIn(work), run_time=0.8)
            self.play(FadeIn(ans), run_time=0.5)

        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
        done = VGroup(TB("HOÀN THÀNH", size=60, color=GOOD), TB("TOÀN BỘ 14 BÀI", size=56, color=ACCENT)).arrange(DOWN, buff=0.2)
        recap = VGroup(*[T(t, size=29) for t in [
            "Chương 1 · Nền tảng quy hoạch động",
            "Chương 2 · Các mô hình kinh điển",
            "Chương 3 · Quy hoạch động nâng cao",
            "Chương 4 · Tối ưu hóa quy hoạch động",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        key = VGroup(T("Mọi bài đều xoay quanh câu hỏi:", size=29, color=MUTED),
                     TB("“Để đi tiếp, ta cần nhớ gì về quá khứ?”", size=32, color=GOOD)).arrange(DOWN, buff=0.15)
        fit_stack(done, recap, key, buff=0.9, max_scale=1.2)
        with self.voice("Chúc mừng các em đã hoàn thành toàn bộ 14 bài của tài liệu quy hoạch động!"):
            self.play(FadeIn(done, scale=1.2), run_time=1.0)
        with self.voice("Từ nền tảng, qua các mô hình kinh điển, quy hoạch động nâng cao, đến tối ưu hóa: mọi bài đều xoay quanh "
                        "một câu hỏi. Để đi tiếp, ta cần nhớ gì về quá khứ? Hãy luyện tập thật nhiều. Chúc các em thành công!"):
            self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in recap], lag_ratio=0.3), run_time=1.6)
            self.play(FadeIn(key), run_time=0.8)
        self.play(FadeOut(VGroup(done, recap, key)), run_time=0.6)
