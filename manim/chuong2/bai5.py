"""BÀI 5 — Cái túi mở rộng: giới hạn số lượng (KHOHANG), sức chứa khổng lồ (BALOVANG), bitset."""

from shared import *  # noqa: F401,F403
from bai4 import make_truck

ITEMS = [(3, 5, 3), (4, 7, 2), (5, 9, 1)]  # (w, v, q)
CAP = 15


def binary_split(q):
    out, size = [], 1
    while q > 0:
        t = min(size, q)
        out.append(t)
        q -= t
        size *= 2
    return out


PACKS = []
for _w, _v, _q in ITEMS:
    for _t in binary_split(_q):
        PACKS.append((_w * _t, _v * _t))
_best = [0] * (CAP + 1)
for _pw, _pv in PACKS:
    for _c in range(CAP, _pw - 1, -1):
        _best[_c] = max(_best[_c], _best[_c - _pw] + _pv)
assert _best[CAP] == 26
assert binary_split(13) == [1, 2, 4, 6] and binary_split(20) == [1, 2, 4, 8, 5]

GOLD = [(800, 6), (450, 3), (600, 5), (350, 2)]
GCAP = 1000
INF = None
TOTAL_V = sum(v for _, v in GOLD)
LIGHT_ROWS = []
_l = [0] + [INF] * TOTAL_V
for _w, _v in GOLD:
    for _x in range(TOTAL_V, _v - 1, -1):
        if _l[_x - _v] is not None:
            cand = _l[_x - _v] + _w
            if _l[_x] is None or cand < _l[_x]:
                _l[_x] = cand
    LIGHT_ROWS.append(_l[:])
LIGHT = LIGHT_ROWS[-1]
ANS = max(x for x in range(TOTAL_V + 1) if LIGHT[x] is not None and LIGHT[x] <= GCAP)
assert ANS == 7 and LIGHT[9] == 1250 and LIGHT[10] == 1400


def pick_packs(t, packs):
    """Chọn tập con các gói có tổng t (ưu tiên gói dư r nếu t vượt phần nhị phân)."""
    binary = packs[:-1] if packs[-1] != 2 ** (len(packs) - 1) else packs
    rest = packs[-1] if binary is not packs else 0
    chosen = []
    lim = sum(binary)
    if t > lim:
        chosen.append(len(packs) - 1)
        t -= rest
    for k, p in enumerate(binary):
        if t >> k & 1:
            chosen.append(k)
    return sorted(chosen)


for _t in range(14):
    assert sum([1, 2, 4, 6][k] for k in pick_packs(_t, [1, 2, 4, 6])) == _t


class B5Scene(NarratedScene):
    lesson_tag = "BÀI 5"
    lesson_title = "Cái túi mở rộng"


def bottle(scale=1.0, color="#38BDF8"):
    body = RoundedRectangle(width=0.32, height=0.55, corner_radius=0.08, fill_color=color, fill_opacity=1,
                            stroke_color=INK, stroke_width=1.5)
    neck = Rectangle(width=0.14, height=0.12, fill_color=color, fill_opacity=1, stroke_color=INK,
                     stroke_width=1.5).next_to(body, UP, buff=0)
    return VGroup(body, neck).scale(scale)


def light_text(v):
    return "∞" if v is None else str(v)


# ----------------------------------------------------------------------------
class B5_00_Intro(B5Scene):
    def construct(self):
        tag = TB("BÀI 5", size=80, color=ACCENT)
        ttl = VGroup(TB("Cái túi mở rộng", size=50), T("Giới hạn số lượng, sức chứa khổng lồ", size=32, color=MUTED)).arrange(
            DOWN, buff=0.2)
        line = Line(LEFT * 2.5, RIGHT * 2.5, color=ACCENT, stroke_width=5)
        goals = VGroup(*[T(t, size=30) for t in [
            "✓ Giới hạn số lượng: TÁCH NHỊ PHÂN",
            "✓ W khổng lồ, giá trị nhỏ: ĐỔI VAI",
            "✓ Tổng con nhanh gấp 64 lần với bitset",
            "✓ Đọc giới hạn TRƯỚC khi chọn trạng thái",
        ]]).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        fit_stack(VGroup(tag, ttl, line).arrange(DOWN, buff=0.35), goals, buff=0.9, max_scale=1.2)
        with self.voice("Chào mừng các em đến với Bài 5: Cái túi mở rộng, với số lượng giới hạn và sức chứa khổng lồ."):
            self.play(FadeIn(tag, scale=1.4), Write(ttl), GrowFromCenter(line), run_time=1.5)
        with self.voice("Học xong bài này, em sẽ giải cái túi giới hạn số lượng bằng kĩ thuật tách nhị phân, và khi sức chứa "
                        "khổng lồ nhưng giá trị nhỏ, biết đổi vai trò khối lượng và giá trị."):
            self.play(FadeIn(goals[0:2], shift=RIGHT * 0.3), run_time=0.8)
        with self.voice("Em cũng sẽ dùng bitset để tăng tốc bài toán tổng con, và rèn thói quen đọc giới hạn trước khi chọn "
                        "trạng thái: chiều nào nhỏ thì đưa chiều đó vào bảng."):
            self.play(FadeIn(goals[2:], shift=RIGHT * 0.3), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
class B5_01_KhoHang(B5Scene):
    def construct(self):
        self.show_header("Khởi động: Kho có nhiều chiếc mỗi loại")
        recap = VGroup(
            panel(VGroup(TB("Bài 4: 0/1", size=28, color=BLUEC), T("mỗi loại 1 chiếc", size=24)).arrange(DOWN, buff=0.1),
                  width=3.65, stroke=BLUEC),
            panel(VGroup(TB("Bài 4: vô hạn", size=28, color=GOOD), T("mỗi loại vô số chiếc", size=24)).arrange(DOWN, buff=0.1),
                  width=3.65, stroke=GOOD)).arrange(RIGHT, buff=0.2)
        shelf = VGroup()
        for name, q, col in [("nước", 13, "#38BDF8"), ("mì", 5, "#F59E0B"), ("sữa", 2, "#F1F5F9")]:
            bs = VGroup(*[bottle(0.9, col) for _ in range(q)]).arrange(RIGHT, buff=0.06)
            lab = TB(f"{q} thùng {name}", size=26, color=col)
            shelf.add(VGroup(lab, bs).arrange(RIGHT, buff=0.3))
        shelf.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        q = VGroup(T("Coi 13 thùng nước là 13 kiện riêng rồi giải 0/1?", size=28),
                   T("Nếu kho có 10 000 thùng mỗi loại thì sao?", size=28, color=ORANGE)).arrange(DOWN, buff=0.1)
        fit_stack(recap, shelf, q, buff=0.7, max_scale=1.2)
        with self.voice("Ở Bài 4, mỗi kiện hàng chỉ có một chiếc, là cái túi 0/1, hoặc vô số chiếc, là cái túi không giới hạn."):
            self.play(FadeIn(recap), run_time=0.8)
        with self.voice("Thực tế thường nằm ở giữa: kho có 13 thùng nước, 5 thùng mì, 2 thùng sữa."):
            for r in shelf:
                self.play(FadeIn(r[0]), LaggedStart(*[FadeIn(b, shift=DOWN * 0.2) for b in r[1]], lag_ratio=0.05),
                          run_time=0.8)
        with self.voice("Một cách tự nhiên là coi 13 thùng nước như 13 kiện riêng biệt rồi giải cái túi 0/1. "
                        "Nhưng nếu kho có mười nghìn thùng mỗi loại thì sao?"):
            self.play(FadeIn(q), run_time=0.8)

        self.clear_body()
        self.show_header("1. Bài toán KHOHANG")
        box = tag_box("BÀI TOÁN: KHOHANG", [
            "n loại hàng. Mỗi chiếc loại i nặng wᵢ, giá trị vᵢ,",
            "kho có qᵢ chiếc loại này. Xe chở tối đa W kg.",
            "Tổng khối lượng ≤ W, tổng giá trị LỚN NHẤT.",
            "n ≤ 100,  W ≤ 10⁵,  qᵢ ≤ 10⁴",
        ], width=7.5, size=29)
        box[3][3].set_color(ORANGE)
        rows = VGroup()
        for k, (w, v, qq) in enumerate(ITEMS):
            rows.add(VGroup(TB(f"Loại {k + 1}:", size=28, color=ACCENT), T(f"{w} kg, giá trị {v}, có {qq} chiếc", size=28))
                     .arrange(RIGHT, buff=0.2))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        ex = VGroup(T("W = 15 →", size=30), TB("26", size=44, color=GOOD),
                    T("= 2×loại 1 + 1×loại 2 + 1×loại 3", size=26)).arrange(RIGHT, buff=0.25)
        ex2 = T("nặng 6 + 4 + 5 = 15 kg, giá trị 10 + 7 + 9 = 26", size=26, color=MUTED)
        fit_stack(box, rows, VGroup(ex, ex2).arrange(DOWN, buff=0.12), buff=0.6, max_scale=1.2)
        with self.voice("Bài toán KHOHANG: kho có n loại hàng. Mỗi chiếc hàng loại i nặng w i, có giá trị v i, và kho có q i "
                        "chiếc loại này. Xe chở tối đa W. Chọn hàng để tổng khối lượng không vượt quá W và tổng giá trị lớn nhất. "
                        "W tới một trăm nghìn, q i tới mười nghìn."):
            self.play(FadeIn(box, shift=UP * 0.3), run_time=1.0)
        with self.voice("Ví dụ ba loại: loại 1 nặng 3, giá trị 5, có 3 chiếc. Loại 2 nặng 4, giá trị 7, có 2 chiếc. "
                        "Loại 3 nặng 5, giá trị 9, có 1 chiếc. Sức chứa 15."):
            self.play(FadeIn(rows), run_time=0.8)
        with self.voice("Đáp án 26: lấy 2 chiếc loại 1, 1 chiếc loại 2, 1 chiếc loại 3. Nặng đúng 15, giá trị 26."):
            self.play(FadeIn(ex), FadeIn(ex2), run_time=0.8)

        self.clear_body()
        self.show_header("2. Ý tưởng ngây thơ: Tách thành từng chiếc")
        idea = VGroup(T("Loại i sinh ra qᵢ đồ vật giống hệt nhau,", size=30),
                      T("rồi giải cái túi 0/1 một mảng như Bài 4.", size=30)).arrange(DOWN, buff=0.1)
        cnt = tag_box("ĐẾM SỐ PHÉP TÍNH", [
            "Số đồ vật sau khi tách: Σqᵢ ≤ 100 · 10⁴ = 10⁶",
            "Mỗi đồ vật duyệt mảng dài W + 1 = 10⁵ ô",
            "Tổng: 10⁶ · 10⁵ = 10¹¹ phép ≈ mười phút!",
        ], accent=ORANGE, width=7.5, size=29)
        cnt[3][2].set_color(BAD)
        stuck = tag_box("BẾ TẮC", [
            "13 thùng nước giống hệt nhau bị xử lí như",
            "13 đồ vật khác nhau. Câu hỏi thật sự chỉ là:",
            "lấy BAO NHIÊU thùng, từ 0 đến 13?",
            "Có biểu diễn 14 lựa chọn ấy bằng ít đồ vật hơn?",
        ], accent=BAD, width=7.5, size=29)
        fit_stack(idea, cnt, stuck, buff=0.7, max_scale=1.2)
        with self.voice("Ý tưởng ngây thơ: coi mỗi chiếc hàng là một đồ vật riêng. Loại i sinh ra q i đồ vật giống hệt nhau. "
                        "Sau đó giải cái túi 0/1 với mảng một chiều như Bài 4."):
            self.play(FadeIn(idea), run_time=0.8)
        with self.voice("Đếm số phép tính: số đồ vật sau khi tách tối đa một triệu. Mỗi đồ vật duyệt mảng dài một trăm nghìn ô. "
                        "Tổng cộng một trăm tỉ phép, cần khoảng mười phút."):
            self.play(FadeIn(cnt), run_time=0.8)
        with self.voice("Bế tắc! 13 thùng nước giống hệt nhau được xử lí như 13 đồ vật khác nhau. Máy tính lặp lại công việc thêm "
                        "một thùng nước 13 lần, trong khi câu hỏi thật sự chỉ là lấy bao nhiêu thùng, từ 0 đến 13. Có cách nào "
                        "biểu diễn 14 lựa chọn ấy bằng ít đồ vật hơn không?"):
            self.play(FadeIn(stuck), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
SPLIT_CODE = """
for (int size = 1; quantity > 0; size *= 2) {
    int take = min(size, quantity);
    packWeight.push_back(weight * take);
    packValue.push_back(value * take);
    quantity -= take;
}
// rồi cái túi 0/1 một mảng trên các gói:
for (int p = 0; p < packCount; p++)
  for (int c = cap; c >= packWeight[p]; c--)
    best[c] = max(best[c],
                  best[c - packWeight[p]] + packValue[p]);
"""


class B5_02_TachNhiPhan(B5Scene):
    def construct(self):
        self.show_header("3. Phá bế tắc: Tách nhị phân")
        packs = [1, 2, 4, 6]
        cols = [BLUEC, GOOD, PURPLE, ORANGE]
        groups = VGroup()
        for p, col in zip(packs, cols):
            bs = VGroup(*[bottle(0.85) for _ in range(p)]).arrange(RIGHT, buff=0.04)
            frame = SurroundingRectangle(bs, color=col, buff=0.12, corner_radius=0.12, stroke_width=4)
            lab = TB(f"gói {p}", size=26, color=col).next_to(frame, DOWN, buff=0.1)
            groups.add(VGroup(bs, frame, lab))
        groups.arrange(RIGHT, buff=0.3)
        note = VGroup(T("13 = 1 + 2 + 4 + 6  (6 = phần còn lại 13 − 7)", size=28, color=ACCENT),
                      T("Mỗi gói là MỘT đồ vật 0/1 (gói 4 nặng 4w, giá trị 4v)", size=26, color=MUTED)).arrange(DOWN, buff=0.1)
        demo_slot = placeholder(7.4, 1.4)
        sc = fit_stack(groups, note, demo_slot, buff=0.7, max_scale=1.3)
        with self.voice("Ý tưởng: thay vì 13 thùng lẻ, ta đóng thành các gói 1, 2, 4 thùng, và một gói chứa phần còn lại là "
                        "13 trừ 7 bằng 6 thùng."):
            for g in groups:
                self.play(FadeIn(g[0]), Create(g[1]), FadeIn(g[2]), run_time=0.6)
            self.play(FadeIn(note[0]), run_time=0.5)
        with self.voice("Mỗi gói là một đồ vật của cái túi 0/1: gói 4 thùng nặng 4 lần, giá trị 4 lần. Ta chỉ còn 4 đồ vật thay vì 13."):
            self.play(FadeIn(note[1]), run_time=0.6)
        demo = None
        with self.voice("Kiểm tra: mọi số lượng từ 0 đến 13 đều ghép được từ các gói. Ví dụ 5 bằng 1 cộng 4, 11 bằng 1 cộng 4 cộng 6, "
                        "13 là lấy cả bốn gói."):
            for t in range(14):
                ch = pick_packs(t, packs)
                txt = VGroup(TB(f"{t}", size=48, color=ACCENT), T("=", size=40),
                             T(" + ".join(str(packs[k]) for k in ch) if ch else "không lấy gói nào", size=36))
                txt.arrange(RIGHT, buff=0.25).scale(sc).move_to(demo_slot)
                anims = [groups[k][1].animate.set_fill(cols[k], 0.35 if k in ch else 0) for k in range(4)]
                if demo is None:
                    demo = txt
                    anims.append(FadeIn(demo))
                else:
                    anims.append(Transform(demo, txt))
                self.play(*anims, run_time=0.35)
                self.wait(0.25)

        self.clear_body()
        self.show_header("Vì sao mọi số lượng đều ghép được?")
        proof = tag_box("CHỨNG MINH", [
            "q = 1 + 2 + 4 + … + 2ᵏ⁻¹ + r,  0 ≤ r < 2ᵏ",
            "• Gói 1, 2, …, 2ᵏ⁻¹ = các chữ số nhị phân",
            "  ⇒ ghép được MỌI số từ 0 đến 2ᵏ − 1.",
            "• t từ 2ᵏ đến q: dùng gói r, phần còn lại t − r",
            "  nằm trong [2ᵏ − r, 2ᵏ − 1] ⇒ ghép nhị phân.",
            "• Mọi cách chọn gói đều cho tổng ≤ q:",
            "  không tạo ra số lượng “không có thật”.",
        ], accent=GOOD, width=7.5, size=28)
        bits = VGroup()
        for t in (5, 11):
            ch = pick_packs(t, [1, 2, 4, 6])
            bits.add(T(f"{t} = " + " + ".join(str([1, 2, 4, 6][k]) for k in ch), size=30, color=ACCENT))
        bits.arrange(RIGHT, buff=0.8)
        cnt = VGroup(T("Số gói mỗi loại ≈ log₂ q + 1 ≤ 14", size=30),
                     T("Tổng ≤ 1400 gói × 10⁵ ô = 1,4·10⁸ phép ≈ 0,2 giây", size=28, color=GOOD),
                     TB("Nhanh hơn cách ngây thơ khoảng 700 lần!", size=30, color=GOOD)).arrange(DOWN, buff=0.12)
        fit_stack(proof, bits, cnt, buff=0.6, max_scale=1.2)
        with self.voice("Vì sao đúng? Giả sử q bằng 1 cộng 2 cộng 4, cho tới 2 mũ k trừ 1, cộng phần dư r nhỏ hơn 2 mũ k. "
                        "Các gói 1, 2, 4 chính là các chữ số của hệ nhị phân, nên ghép được mọi số từ 0 đến 2 mũ k trừ 1."):
            self.play(FadeIn(proof[0:3]), FadeIn(proof[3][0:3]), run_time=1.0)
        with self.voice("Với số t lớn hơn, dùng gói r, phần còn lại t trừ r vẫn nằm trong khoảng ghép được bằng các gói nhị phân. "
                        "Ngược lại, mọi cách chọn gói đều cho tổng không quá q, nên không tạo ra số lượng không có thật."):
            self.play(FadeIn(proof[3][3:]), FadeIn(bits), run_time=1.0)
        with self.voice("Đếm lại: mỗi loại sinh ra không quá 14 gói. Tổng số gói không quá một nghìn bốn trăm, mỗi gói duyệt một "
                        "trăm nghìn ô: khoảng một trăm bốn mươi triệu phép, chạy trong khoảng 0 phẩy 2 giây. Nhanh hơn cách "
                        "ngây thơ khoảng 700 lần!"):
            self.play(FadeIn(cnt), run_time=0.8)

        self.clear_body()
        self.show_header("Code tách gói")
        code = code_block(SPLIT_CODE, size=20)
        ex = VGroup(T("Ví dụ: loại 1 (q = 3) → gói 1, 2", size=28), T("loại 2 (q = 2) → gói 1, 1;  loại 3 → gói 1", size=28))
        ex.arrange(DOWN, buff=0.1)
        faster = tag_box("CÒN NHANH HƠN ĐƯỢC KHÔNG?", [
            "Có lời giải O(n·W): chia sức chứa theo số dư",
            "khi chia wᵢ, mỗi lớp là “max trên cửa sổ trượt”",
            "⇒ hàng đợi đơn điệu (Bài 13).",
        ], accent=PURPLE, width=7.5, size=27)
        fit_stack(code, ex, faster, buff=0.55)
        with self.voice("Vòng lặp tách gói rất gọn: size nhận lần lượt 1, 2, 4, và cứ thế. Mỗi lần lấy take bằng min của size "
                        "và số còn lại, nên gói cuối cùng tự động là phần dư."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 1, ACCENT)
            self.play(FadeIn(hl), run_time=0.4)
        with self.voice("Với ví dụ, loại 1 có 3 chiếc tách thành gói 1 và gói 2. Loại 2 có 2 chiếc tách thành gói 1 và gói 1. "
                        "Loại 3 là một gói 1. Sau đó giải cái túi 0/1 trên các gói, được 26."):
            self.play(FadeIn(ex), Transform(hl, line_box(code, 8, GOOD)), run_time=0.8)
        with self.voice("Còn nhanh hơn được không? Có một lời giải O của n nhân W: chia các sức chứa theo số dư khi chia cho w i, "
                        "mỗi lớp số dư là một dãy, và công thức trên đó là max trên một cửa sổ trượt. Bài 13 sẽ dạy công cụ "
                        "hàng đợi đơn điệu để làm việc này."):
            self.play(FadeIn(faster), run_time=0.8)
        self.clear_body()


# ----------------------------------------------------------------------------
GOLD_CODE = """
vector<long long> light(total + 1, INF);
light[0] = 0;
for (int i = 0; i < n; i++)
  for (int x = total; x >= value[i]; x--) {
    if (light[x - value[i]] == INF) continue;
    light[x] = min(light[x],
                   light[x - value[i]] + weight[i]);
  }
int answer = 0;
for (int x = 0; x <= total; x++)
  if (light[x] <= capacity) answer = x;
"""


class B5_03_BaloVang(B5Scene):
    def construct(self):
        self.show_header("4. Bài toán BALOVANG: Sức chứa khổng lồ")
        box = tag_box("BÀI TOÁN: BALOVANG", [
            "Túi chịu tối đa W gam. n món cổ vật,",
            "món i nặng wᵢ gam, giá trị vᵢ; mỗi món ≤ 1 lần.",
            "Tìm tổng giá trị lớn nhất.",
            "n ≤ 100,  W ≤ 10⁹,  wᵢ ≤ 10⁹,  vᵢ ≤ 1000",
        ], accent=BLUEC, width=7.5, size=29)
        box[3][3].set_color(ORANGE)
        rows = VGroup(*[T(f"Món {k + 1}: {w} g, giá trị {v}", size=28) for k, (w, v) in enumerate(GOLD)]).arrange(
            DOWN, aligned_edge=LEFT, buff=0.1)
        ex = VGroup(T("W = 1000 →", size=30), TB("7", size=44, color=GOOD), T("(món 3 + món 4: 950 g)", size=26)).arrange(
            RIGHT, buff=0.25)
        stuck = VGroup(T("Mảng best[0..W] với W = 10⁹:", size=30),
                       TB("8 GB bộ nhớ, 10¹¹ phép — KHÔNG THỂ!", size=32, color=BAD)).arrange(DOWN, buff=0.1)
        fit_stack(box, rows, ex, stuck, buff=0.5, max_scale=1.2)
        with self.voice("Bài toán BALOVANG: một nhà thám hiểm mang chiếc túi chịu được tối đa W gam. Có n món cổ vật, món i nặng "
                        "w i gam và có giá trị v i. Mỗi món lấy tối đa một lần. Tìm tổng giá trị lớn nhất có thể mang về."):
            self.play(FadeIn(box), run_time=0.8)
        with self.voice("Ví dụ: bốn món nặng 800, 450, 600, 350 gam, giá trị 6, 3, 5, 2. Túi chịu 1000 gam. Đáp án 7: lấy món 3 "
                        "và món 4, nặng 950 gam."):
            self.play(FadeIn(rows), run_time=0.6)
            self.play(FadeIn(ex), run_time=0.5)
        with self.voice("Bế tắc: cái túi 0/1 của Bài 4 cần mảng theo sức chứa từ 0 đến W. Với W bằng một tỉ, mảng ấy cần 8 gigabyte "
                        "bộ nhớ và một trăm tỉ phép tính. Không thể!"):
            self.play(FadeIn(stuck), run_time=0.8)

        self.clear_body()
        self.show_header("Phá bế tắc: Đổi vai khối lượng và giá trị")
        read = VGroup(T("Đọc lại giới hạn: vᵢ ≤ 1000 ⇒ tổng giá trị ≤ 10⁵", size=29),
                      T("Chiều “giá trị” nhỏ hơn chiều “khối lượng” 10 000 lần!", size=28, color=ACCENT)).arrange(DOWN, buff=0.1)
        ask = VGroup(
            panel(VGroup(T("Bài 4 hỏi:", size=24, color=MUTED), T("sức chứa c ⇒ giá trị", size=26),
                         T("lớn nhất?", size=26)).arrange(DOWN, buff=0.08), width=3.65, stroke=MUTED),
            panel(VGroup(T("Giờ hỏi ngược:", size=24, color=GOOD), T("đạt ĐÚNG giá trị x ⇒", size=26),
                         T("ít nhất bao nhiêu gam?", size=26)).arrange(DOWN, buff=0.08), width=3.65, stroke=GOOD),
        ).arrange(RIGHT, buff=0.2)
        formula = tag_box("CÔNG THỨC ĐỔI VAI", [
            "lightest(x) = khối lượng nhỏ nhất để có",
            "tổng giá trị ĐÚNG BẰNG x (∞ nếu không được)",
            "lightest(0) = 0",
            "lightest(x) ← min(lightest(x), lightest(x−vᵢ) + wᵢ)",
            "x GIẢM dần cho mỗi món (như 0/1)",
            "Đáp án: x lớn nhất có lightest(x) ≤ W",
        ], accent=GOOD, width=7.5, size=27)
        formula[3][3].set_color(ACCENT)
        fit_stack(read, ask, formula, buff=0.6, max_scale=1.2)
        with self.voice("Nhưng hãy đọc lại giới hạn: giá trị mỗi món không quá 1000, nên tổng giá trị không quá một trăm nghìn. "
                        "Chiều giá trị nhỏ hơn chiều khối lượng tới mười nghìn lần."):
            self.play(FadeIn(read), run_time=0.8)
        with self.voice("Thay vì hỏi: với sức chứa c, giá trị lớn nhất là bao nhiêu, ta hỏi ngược lại: muốn đạt đúng giá trị x, "
                        "cần mang ít nhất bao nhiêu gam?"):
            self.play(FadeIn(ask[0]), run_time=0.5)
            self.play(FadeIn(ask[1]), run_time=0.5)
        with self.voice("Đặt lightest của x là khối lượng nhỏ nhất của một tập món có tổng giá trị đúng bằng x, bằng vô cùng nếu "
                        "không tạo được. lightest của 0 bằng 0. Với mỗi món, duyệt x giảm dần như cái túi 0/1, cập nhật min. "
                        "Đáp án là giá trị x lớn nhất mà lightest của x không vượt quá W."):
            self.play(FadeIn(formula), run_time=1.0)

        self.clear_body()
        self.show_header("Chạy tay: bảng lightest(x)")
        XS = 13  # hiển thị x = 0..12 (đủ thấy đáp án 7 và các ô vượt 1000)
        all_rows = [[0] + [None] * TOTAL_V] + LIGHT_ROWS
        heads = ["x", "đầu", "+món 1", "+món 2", "+món 3", "+món 4"]
        cw, ch = 1.15, 0.56
        cols = VGroup()
        for ci, h in enumerate(heads):
            col = VGroup()
            hd = Rectangle(width=cw, height=ch, fill_color=ACCENT if ci else PANEL, fill_opacity=1, stroke_color=BG,
                           stroke_width=2)
            col.add(VGroup(hd, TB(h, size=22, color=BG if ci else MUTED, max_width=cw - 0.1).move_to(hd)))
            for x in range(XS):
                r = Rectangle(width=cw, height=ch, stroke_color=MUTED, stroke_width=1.2, fill_opacity=1)
                if ci == 0:
                    r.set_fill(PANEL, 1)
                    t = TB(str(x), size=24, color=MUTED)
                else:
                    v = all_rows[ci - 1][x]
                    prev = all_rows[ci - 2][x] if ci > 1 else v
                    changed = ci > 1 and v != prev
                    r.set_fill("#166534" if changed else ("#2A1616" if v is None else PANEL_2), 1)
                    t = TB(light_text(v), size=24, color=MUTED if v is None else INK)
                col.add(VGroup(r, t.move_to(r)))
            col.arrange(DOWN, buff=0)
            cols.add(col)
        cols.arrange(RIGHT, buff=0)
        rows = VGroup(*cols[1:])  # mỗi "hàng" cũ giờ là một cột
        res_slot = placeholder(7.4, 1.3)
        sc = fit_stack(cols, res_slot, buff=0.5, max_scale=1.3)
        with self.voice("Chạy tay trên ví dụ. Ban đầu chỉ lightest của 0 bằng 0, mọi ô khác là vô cùng. Ô xanh lá là ô vừa được "
                        "cập nhật."):
            self.play(FadeIn(cols[0]), FadeIn(rows[0]), run_time=0.8)
        sps = ["Thêm món 1, giá trị 6, nặng 800: lightest của 6 bằng 800.",
               "Thêm món 2, giá trị 3, nặng 450: lightest của 3 bằng 450, và lightest của 9 bằng 800 cộng 450, bằng 1250.",
               "Thêm món 3, giá trị 5, nặng 600: thêm các ô 5, 8 và 11.",
               "Thêm món 4, giá trị 2, nặng 350: ô 7 bằng 600 cộng 350, bằng 950."]
        for r in range(1, 5):
            with self.voice(sps[r - 1]):
                self.play(FadeIn(rows[r], shift=DOWN * 0.15), run_time=0.8)
        best_cell = rows[4][ANS + 1]
        ring = SurroundingRectangle(best_cell, color=ACCENT, buff=0.03, stroke_width=6)
        res = VGroup(T("Giá trị x lớn nhất có lightest(x) ≤ 1000:", size=28),
                     TB("x = 7  (950 g)", size=40, color=GOOD)).arrange(DOWN, buff=0.12).scale(sc).move_to(res_slot)
        with self.voice("Đáp án: tìm x lớn nhất có lightest của x không quá 1000. lightest của 7 bằng 950, còn từ 8 trở lên đều quá "
                        "1000. Đáp án 7."):
            self.play(Create(ring), FadeIn(res), run_time=0.8)
            self.play(*[Indicate(rows[4][x + 1], color=BAD, scale_factor=1.1) for x in range(8, XS)
                        if LIGHT[x] is not None], run_time=0.8)

        self.clear_body()
        self.show_header("Độ phức tạp & code")
        cx = VGroup(TB("O(n · Σvᵢ)", size=44, color=GOOD), T("= 100 · 10⁵ = 10⁷ phép, bộ nhớ O(Σvᵢ)", size=28)).arrange(DOWN, buff=0.12)
        code = code_block(GOLD_CODE, size=19)
        msg = T("Bài “không thể” thành dễ, chỉ nhờ chọn đúng chiều làm chỉ số!", size=27, color=ACCENT)
        fit_stack(cx, code, msg, buff=0.6)
        with self.voice("Độ phức tạp O của n nhân tổng giá trị: một trăm nhân một trăm nghìn, bằng mười triệu phép. Bộ nhớ chỉ O của "
                        "tổng giá trị."):
            self.play(FadeIn(cx), run_time=0.8)
        with self.voice("Code: khởi tạo mảng lightest bằng vô cùng, trừ ô 0. Bỏ qua ô nguồn vô cùng trước khi cộng. "
                        "Cuối cùng quét tìm x lớn nhất có lightest không quá sức chứa."):
            self.play(FadeIn(code), run_time=0.8)
            hl = line_box(code, 0, ACCENT)
            self.play(FadeIn(hl), run_time=0.3)
            self.play(Transform(hl, line_box(code, 4, ACCENT)), run_time=0.4)
            self.play(Transform(hl, line_box(code, 10, GOOD)), run_time=0.4)
        with self.voice("Bài toán không thể trở thành dễ dàng, chỉ nhờ chọn đúng chiều để làm chỉ số của bảng."):
            self.play(FadeIn(msg), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B5_04_Bitset(B5Scene):
    def construct(self):
        self.show_header("Nguyên tắc chọn chiều cho bảng")
        rule = tag_box("BA ĐẠI LƯỢNG: n, W, V", [
            "Bảng cần hai trong ba đại lượng làm chiều.",
            "ĐỌC GIỚI HẠN, chọn hai đại lượng nhỏ nhất:",
            "• W nhỏ: f(i, khối lượng) = giá trị lớn nhất",
            "• V nhỏ: f(i, giá trị) = khối lượng nhỏ nhất",
            "• W, V đều lớn nhưng n ≤ 40: chia đôi tập,",
            "  mỗi nửa 2²⁰ tập con, sắp xếp + chặt nhị phân",
            "  (“gặp nhau ở giữa”).",
        ], accent=ACCENT, width=7.5, size=28)
        fit_stack(rule, max_scale=1.25)
        with self.voice("Rút ra nguyên tắc chọn chiều cho bảng. Một bài cái túi luôn có ba đại lượng: số đồ vật n, tổng khối lượng W "
                        "và tổng giá trị V. Bảng phương án cần hai trong ba đại lượng làm chiều. Hãy đọc giới hạn và chọn hai "
                        "đại lượng nhỏ nhất."):
            self.play(FadeIn(rule[0:3]), FadeIn(rule[3][0:2]), run_time=1.0)
        with self.voice("W nhỏ: bảng theo khối lượng, lưu giá trị lớn nhất, như Bài 4. V nhỏ: bảng theo giá trị, lưu khối lượng nhỏ "
                        "nhất, như bài BALOVANG."):
            self.play(FadeIn(rule[3][2:4]), run_time=0.8)
        with self.voice("Cả W và V đều lớn nhưng n không quá 40: chia đôi tập đồ vật, mỗi nửa duyệt khoảng một triệu tập con, rồi "
                        "ghép hai nửa bằng sắp xếp và chặt nhị phân. Đó là kĩ thuật gặp nhau ở giữa."):
            self.play(FadeIn(rule[3][4:]), run_time=0.8)

        self.clear_body()
        self.show_header("5. Tăng tốc tổng con bằng bitset")
        intro = VGroup(T("Tổng con: những tổng nào tạo được từ một tập con?", size=28),
                       M("reach[s] = reach[s] hoặc reach[s − aᵢ]", size=28, color=ACCENT),
                       T("Mỗi ô chỉ là 1 BIT ⇒ gói cả mảng vào một bitset", size=28)).arrange(DOWN, buff=0.12)
        N = 12
        before = {0, 2, 3, 5}
        shifted = {s + 4 for s in before if s + 4 < N}
        after = before | shifted

        def bitrow(sset, label, hi=None):
            r = array_row(["1" if s in sset else "0" for s in range(N)], w=0.55, h=0.65, size=26, label=label,
                          show_index=False, label_size=24)
            for s, c in enumerate(r.cells):
                if s in sset:
                    c[0].set_fill(ACCENT if (hi and s in hi) else BLUEC, 1)
                    c[1].set_color(BG)
            return r

        idx = VGroup(*[T(str(s), size=20, color=MUTED) for s in range(N)])
        r0 = bitrow(before, "reach")
        r1 = bitrow(shifted, "<< 4")
        r2 = bitrow(after, "OR", hi=after - before)
        rows = VGroup(r0, r1, r2).arrange(DOWN, buff=0.25, aligned_edge=RIGHT)
        for t, c in zip(idx, r0.cells):
            t.next_to(c, UP, buff=0.08)
        cap = T("Đã có vật 2, 3 (tổng 0, 2, 3, 5). Thêm vật nặng 4:", size=28, color=MUTED)
        code = code_block("""
bitset<100001> reach;
reach[0] = 1;
for (int i = 0; i < count; i++)
    reach |= (reach << weight[i]);
""", size=22)
        speed = VGroup(T("Máy xử lí 64 bit mỗi phép ⇒ nhanh hơn ≈ 64 lần", size=27, color=GOOD),
                       T("Phép dịch dùng giá trị CŨ của cả dãy: không lo chiều duyệt", size=26, color=MUTED)).arrange(DOWN, buff=0.1)
        fit_stack(intro, cap, VGroup(idx, rows), code, speed, buff=0.4)
        with self.voice("Bài toán tổng con: cho n số nguyên dương, những tổng nào tạo được bằng cách chọn một tập con? Đây là cái túi "
                        "0/1 mà mỗi ô chỉ mang giá trị đúng hoặc sai."):
            self.play(FadeIn(intro[:2]), run_time=0.8)
        with self.voice("Vì mỗi ô chỉ là một bit, ta có thể gói cả mảng reach vào một bitset."):
            self.play(FadeIn(intro[2]), run_time=0.5)
        with self.voice("Ví dụ đã có hai vật nặng 2 và 3, nên các tổng 0, 2, 3, 5 tạo được."):
            self.play(FadeIn(cap), FadeIn(idx), FadeIn(r0), run_time=0.8)
        with self.voice("Thêm vật nặng 4: phép với mọi s, reach s hoặc bằng reach s trừ 4, chính là dịch toàn bộ dãy bit sang trái "
                        "4 vị trí."):
            self.play(TransformFromCopy(r0, r1), run_time=1.2)
        with self.voice("Rồi OR với chính nó. Các ô vàng là tổng mới tạo được: 4, 6, 7 và 9."):
            self.play(FadeIn(r2, shift=DOWN * 0.2), run_time=0.8)
        with self.voice("Code chỉ có một dòng: reach OR bằng reach dịch trái weight i. Máy tính xử lí 64 bit trong một phép toán, "
                        "nên nhanh hơn khoảng 64 lần so với duyệt từng ô. Phép dịch tự động dùng giá trị cũ của toàn bộ dãy, "
                        "nên không cần lo chiều duyệt."):
            self.play(FadeIn(code), run_time=0.6)
            self.play(FadeIn(speed), run_time=0.6)
        self.clear_body()


# ----------------------------------------------------------------------------
class B5_05_TongKet(B5Scene):
    def construct(self):
        self.show_header("6. Mở rộng")
        ext = [
            ("Đồ vật phụ thuộc nhau", "Món chính + phụ kiện = một NHÓM",
             "Mở rộng một: đồ vật phụ thuộc nhau, ví dụ mua máy tính rồi mới mua được bàn phím đi kèm. Liệt kê mọi tổ hợp món chính "
             "cộng tập con phụ kiện thành một nhóm, rồi giải cái túi theo nhóm. Nếu phụ thuộc thành cây nhiều tầng, cần quy hoạch "
             "động trên cây ở Bài 11."),
            ("Đếm cách, số lượng giới hạn", "KHÔNG tách nhị phân; dùng cộng dồn (Bài 13)",
             "Mở rộng hai: đếm số cách chọn với số lượng giới hạn thì không dùng được tách nhị phân, vì cùng một số lượng ghép từ "
             "các gói theo nhiều cách, dẫn tới đếm trùng. Lời giải đúng dùng mảng cộng dồn theo lớp số dư, ở Bài 13."),
        ]
        cards = list_cards([(a, b) for a, b, _ in ext])
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, ext):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.7)

        self.clear_body()
        self.show_header("Bẫy thường gặp")
        traps = [
            ("Tách nhị phân sai", "13 → 1, 2, 4, 8 là SAI: 15 > 13, cho lấy tới 15 chiếc",
             "Bẫy một: tách nhị phân sai. Tách 13 thành 1, 2, 4, 8 là sai, vì tổng bằng 15, cho phép lấy tới 15 chiếc."),
            ("Tràn số khi nhân", "vᵢ · take tới 8·10¹² ⇒ long long",
             "Bẫy hai: tràn số khi nhân giá trị với số chiếc trong gói, phải dùng long long."),
            ("Đổi vai mà quên khởi tạo ∞", "lightest(x > 0) phải là ∞, không phải 0",
             "Bẫy ba: đổi vai mà quên khởi tạo vô cùng. lightest của x lớn hơn 0 phải khởi tạo vô cùng, không phải 0."),
            ("Tách nhị phân cho bài ĐẾM", "Đếm trùng!", "Bẫy bốn: dùng tách nhị phân cho bài đếm, sẽ đếm trùng."),
        ]
        cards = list_cards([(a, b) for a, b, _ in traps], accent=BAD, stroke=BAD, prefix="⚠ ")
        fit_stack(cards, max_scale=1.3)
        for c, e in zip(cards, traps):
            with self.voice(e[2]):
                self.play(FadeIn(c, shift=RIGHT * 0.3), run_time=0.6)

        self.clear_body()
        self.show_header("Ghi nhớ")
        mem = tag_box("GHI NHỚ BÀI 5", [
            "• Số lượng q: tách gói 1, 2, 4, …, phần dư;",
            "   giải cái túi 0/1 trên các gói.",
            "• W lớn, V nhỏ: bảng theo GIÁ TRỊ,",
            "   lưu khối lượng nhỏ nhất.",
            "• Tổng con đúng/sai: bitset + dịch bit.",
            "• Luôn ĐỌC GIỚI HẠN để chọn chiều của bảng.",
        ], accent=GOOD, width=7.5, size=30)
        fit_stack(mem, max_scale=1.25)
        with self.voice("Ghi nhớ: số lượng giới hạn q thì tách thành các gói 1, 2, 4, và phần dư, rồi giải cái túi 0/1 trên các gói. "
                        "W lớn, V nhỏ: bảng theo giá trị, lưu khối lượng nhỏ nhất."):
            self.play(FadeIn(mem[0:3]), FadeIn(mem[3][0:4]), run_time=1.0)
        with self.voice("Tổng con đúng sai: dùng bitset và phép dịch bit. Và luôn đọc giới hạn để quyết định chiều nào làm chỉ số của bảng."):
            self.play(FadeIn(mem[3][4:]), run_time=0.8)

        self.clear_body()
        self.show_header("Tự kiểm tra nhanh")
        q = wrap_lines(["Tách q = 20 thành các gói?"], size=40, align=ORIGIN)
        timer_slot = placeholder(2, 1.4)
        packs = binary_split(20)
        boxes = VGroup(*[panel(TB(str(p), size=44, color=BG), color=c, stroke=c, pad=0.25)
                         for p, c in zip(packs, [BLUEC, GOOD, PURPLE, ORANGE, BAD])]).arrange(RIGHT, buff=0.25)
        ans = T("1 + 2 + 4 + 8 = 15, phần dư 20 − 15 = 5", size=30, color=GOOD)
        nxt = VGroup(TB("Tiếp theo: BÀI 6", size=42, color=ACCENT), T("Dãy con tăng dài nhất", size=32)).arrange(DOWN, buff=0.2)
        fit_stack(q, timer_slot, boxes, ans, nxt, buff=0.6, max_scale=1.15)
        with self.voice("Câu hỏi tự kiểm tra: tách q bằng 20 thành các gói. Dừng video và thử nhé!"):
            self.play(FadeIn(q), run_time=0.6)
            for k in (3, 2, 1):
                t = TB(str(k), size=90, color=ACCENT).move_to(timer_slot)
                self.play(FadeIn(t, scale=1.5), run_time=0.3)
                self.play(FadeOut(t), run_time=0.3)
        with self.voice("Đáp án: 1, 2, 4, 8, và phần dư 5. Vì 1 cộng 2 cộng 4 cộng 8 bằng 15, còn lại 20 trừ 15 bằng 5."):
            self.play(LaggedStart(*[FadeIn(b, scale=0.6) for b in boxes], lag_ratio=0.2), run_time=1.2)
            self.play(FadeIn(ans), run_time=0.5)
        with self.voice("Bài tiếp theo: dãy con tăng dài nhất. Hẹn gặp lại các em!"):
            self.play(FadeIn(nxt, shift=UP * 0.3), run_time=1.0)
        self.clear_body()
        self.play(FadeOut(self._header), run_time=0.5)
