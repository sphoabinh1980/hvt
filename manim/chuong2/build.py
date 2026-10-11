"""Dựng toàn bộ video Chương 2 (Bài 4–7) (TikTok 1080x1920) + phụ đề thuyết minh .srt.

Cách dùng:
    python build.py            # render mọi cảnh rồi ghép
    python build.py --no-render  # chỉ ghép lại từ các cảnh đã render

Kết quả nằm trong output/:
    Chuong2_Bai4.mp4 / .srt, Chuong2_Bai5..., Chuong2_Bai6...   (video sạch + phụ đề rời)
    Chuong2_Bai4_vietsub.mp4 ...                               (phụ đề in cứng trên video)
    Chuong2_Full.mp4 / .srt                                     (cả chương)
    parts/Chuong2_Bai4_Phan1.mp4 / .srt ...                     (mỗi phần ≤ 10 phút cho TikTok)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "build"
OUT = ROOT / "output"
SUBS = BUILD / "subs"
MANIM = os.environ.get("MANIM", "manim")
TIKTOK_MAX = 10 * 60  # giây

LESSONS = {
    "Bai4": ("bai4.py", ["B4_00_Intro", "B4_01_KhoiDong", "B4_02_NgayTho", "B4_03_BangF", "B4_04_TruyVet",
                         "B4_05_MotMang", "B4_06_KhongGioiHan", "B4_07_TongKet"]),
    "Bai5": ("bai5.py", ["B5_00_Intro", "B5_01_KhoHang", "B5_02_TachNhiPhan", "B5_03_BaloVang", "B5_04_Bitset",
                         "B5_05_TongKet"]),
    "Bai6": ("bai6.py", ["B6_00_Intro", "B6_01_KhoiDong", "B6_02_On2", "B6_03_MangD", "B6_04_TongKet"]),
    "Bai7": ("bai7.py", ["B7_00_Intro", "B7_01_KhoiDong", "B7_02_NgayTho", "B7_03_BangD", "B7_04_TruyVet", "B7_05_LCS",
                         "B7_06_TongKet"]),
}
CHAPTER = "Chuong2"


def run(cmd, **kw):
    subprocess.run(cmd, check=True, **kw)


def scene_video(file, scene):
    return BUILD / "media" / scene / "videos" / Path(file).stem / "1920p30" / f"{scene}.mp4"


def render_scene(file, scene):
    log = BUILD / f"log_{scene}.txt"
    env = dict(os.environ, SUB_DIR=str(SUBS))
    env.pop("PREVIEW", None)
    with open(log, "w") as fh:
        r = subprocess.run([MANIM, "render", "--media_dir", str(BUILD / "media" / scene), "--disable_caching",
                            file, scene], cwd=ROOT, env=env, stdout=fh, stderr=subprocess.STDOUT)
    status = "ok" if r.returncode == 0 else f"LỖI (xem {log})"
    print(f"  render {scene}: {status}", flush=True)
    return r.returncode == 0


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True).stdout
    return float(out.strip())


# ---------------------------------------------------------------------------- phụ đề
def split_caption(text, max_chars=70):
    """Chia một câu thuyết minh dài thành các mẩu ≤ max_chars ký tự, ưu tiên ngắt ở dấu câu."""
    parts = re.split(r"(?<=[.!?:;])\s+", text.strip())
    chunks = []
    for p in parts:
        if len(p) <= max_chars:
            chunks.append(p)
            continue
        # ngắt tiếp ở dấu phẩy, rồi theo từ
        sub = re.split(r"(?<=,)\s+", p)
        cur = ""
        for s in sub:
            if len(cur) + len(s) + 1 <= max_chars:
                cur = (cur + " " + s).strip()
            else:
                if cur:
                    chunks.append(cur)
                if len(s) <= max_chars:
                    cur = s
                else:
                    words, cur = s.split(), ""
                    for w in words:
                        if len(cur) + len(w) + 1 > max_chars:
                            chunks.append(cur)
                            cur = w
                        else:
                            cur = (cur + " " + w).strip()
        if cur:
            chunks.append(cur)
    # gộp các mẩu quá ngắn vào mẩu trước
    merged = []
    for c in chunks:
        if merged and len(c) < 18 and len(merged[-1]) + len(c) + 1 <= max_chars:
            merged[-1] += " " + c
        else:
            merged.append(c)
    return merged


def two_lines(text, width=36):
    """Bẻ một mẩu phụ đề thành tối đa 2 dòng cân đối."""
    if len(text) <= width:
        return text
    words = text.split()
    best, best_diff = text, 10 ** 9
    for k in range(1, len(words)):
        a, b = " ".join(words[:k]), " ".join(words[k:])
        diff = abs(len(a) - len(b))
        if diff < best_diff:
            best, best_diff = a + "\n" + b, diff
    return best


def fmt_time(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def cues_for_scene(scene, offset):
    data = json.loads((SUBS / f"{scene}.json").read_text(encoding="utf-8"))
    cues = []
    for sub in data["subs"]:
        chunks = split_caption(sub["text"])
        total = sum(len(c) for c in chunks)
        # chỉ phần "đọc" của câu (trừ khoảng nghỉ cuối) được chia theo độ dài mẩu
        start, end = sub["start"], sub["end"]
        t = start
        for c in chunks:
            d = (end - start) * len(c) / total
            cues.append((offset + t, offset + t + d - 0.04, c))
            t += d
    return cues


def write_srt(cues, path):
    lines = []
    for k, (a, b, text) in enumerate(cues, 1):
        lines += [str(k), f"{fmt_time(a)} --> {fmt_time(b)}", two_lines(text), ""]
    path.write_text("\n".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------- video
def concat(videos, out):
    lst = out.with_suffix(".txt")
    lst.write_text("".join(f"file '{v}'\n" for v in videos), encoding="utf-8")
    # thêm một rãnh âm thanh câm để tương thích tốt hơn khi đăng tải
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
         "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
         "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "64k", "-shortest",
         "-movflags", "+faststart", str(out)])
    lst.unlink()


def burn(video, srt, out):
    """In cứng phụ đề vào dải an toàn phía dưới (trên vùng chữ của TikTok)."""
    style = ("FontName=Inter,FontSize=9,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,"
             "BackColour=&H80000000,BorderStyle=3,Outline=1.2,Shadow=0,Alignment=2,MarginV=46,MarginL=20,MarginR=34")
    srt_esc = str(srt).replace(":", r"\:").replace("'", r"\'")
    run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-vf", f"subtitles='{srt_esc}':force_style='{style}'",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "copy",
         "-movflags", "+faststart", str(out)])


def split_parts(scenes, durs):
    """Chia danh sách cảnh thành các phần ≤ 10 phút, cắt tại ranh giới cảnh, càng đều càng tốt."""
    total = sum(durs)
    n = max(1, -(-int(total) // TIKTOK_MAX))
    while True:
        target = total / n
        parts, cur, acc = [], [], 0.0
        for s, d in zip(scenes, durs):
            if cur and acc + d / 2 > target * (len(parts) + 1) and len(parts) < n - 1:
                parts.append(cur)
                cur = []
            cur.append((s, d))
            acc += d
        parts.append(cur)
        if all(sum(d for _, d in p) <= TIKTOK_MAX for p in parts):
            return parts
        n += 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-render", action="store_true")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--no-burn", action="store_true")
    ap.add_argument("--lessons", nargs="*", help="chỉ render/ghép các bài này (ví dụ Bai7); cả chương vẫn được ghép lại")
    args = ap.parse_args()
    chosen = set(args.lessons or LESSONS)
    OUT.mkdir(exist_ok=True)
    (OUT / "parts").mkdir(exist_ok=True)

    if not args.no_render:
        print("Đang render các cảnh…", flush=True)
        jobs = [(f, s) for name, (f, scenes) in LESSONS.items() if name in chosen for s in scenes]
        # cảnh dài render trước để cân tải
        with ThreadPoolExecutor(args.jobs) as ex:
            ok = list(ex.map(lambda fs: render_scene(*fs), jobs))
        if not all(ok):
            sys.exit("Có cảnh render lỗi.")

    full_videos, full_cues, offset_full = [], [], 0.0
    summary = []
    for lesson, (file, scenes) in LESSONS.items():
        vids = [scene_video(file, s) for s in scenes]
        durs = [duration(v) for v in vids]
        cues, off = [], 0.0
        for s, d in zip(scenes, durs):
            cues += cues_for_scene(s, off)
            off += d
        base = OUT / f"{CHAPTER}_{lesson}"
        if lesson not in chosen:
            for s, d in zip(scenes, durs):
                full_cues += cues_for_scene(s, offset_full)
                offset_full += d
            full_videos += vids
            continue
        concat(vids, base.with_suffix(".mp4"))
        write_srt(cues, base.with_suffix(".srt"))
        summary.append((base.name, off))
        if not args.no_burn:
            burn(base.with_suffix(".mp4"), base.with_suffix(".srt"), OUT / f"{base.name}_vietsub.mp4")
        # các phần ≤ 10 phút
        parts = split_parts(scenes, durs)
        if len(parts) > 1:
            for k, part in enumerate(parts, 1):
                pv = [scene_video(file, s) for s, _ in part]
                pc, po = [], 0.0
                for s, d in part:
                    pc += cues_for_scene(s, po)
                    po += d
                pbase = OUT / "parts" / f"{CHAPTER}_{lesson}_Phan{k}"
                concat(pv, pbase.with_suffix(".mp4"))
                write_srt(pc, pbase.with_suffix(".srt"))
                if not args.no_burn:
                    burn(pbase.with_suffix(".mp4"), pbase.with_suffix(".srt"),
                         OUT / "parts" / f"{pbase.name}_vietsub.mp4")
                summary.append(("  " + pbase.name, po))
        for s, d in zip(scenes, durs):
            full_cues += cues_for_scene(s, offset_full)
            offset_full += d
        full_videos += vids
    concat(full_videos, OUT / f"{CHAPTER}_Full.mp4")
    write_srt(full_cues, OUT / f"{CHAPTER}_Full.srt")
    summary.append((f"{CHAPTER}_Full", offset_full))
    print("\nHoàn tất:")
    for name, d in summary:
        print(f"  {name:28s} {int(d // 60):2d}:{int(d % 60):02d}")


if __name__ == "__main__":
    main()
