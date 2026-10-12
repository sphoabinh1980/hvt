#!/usr/bin/env python3
"""Trình chấm cho bộ lời giải Số học, Tập 3.

Mỗi bài nằm trong một thư mục problems/<id>/ gồm:
  meta.py   : CODE, TL (giây), ML (MB), SUBTASKS = [điểm,...], SOLS = [(tệp, tên hiển thị), ...],
              REF = tệp lời giải mẫu, BRUTE = tệp/lệnh trâu (tùy chọn)
  gen.py    : hàm samples() -> [(inp, out)], tests() -> {subtask: [inp, ...]},
              small(rng) -> inp nhỏ để chấm trâu (tùy chọn), check(inp, out, ans) (tùy chọn)
  *.cpp / *.py : các chương trình

Lệnh:
  judge.py build <id>     sinh test + đáp án (bằng REF), kiểm tra ví dụ trong đề
  judge.py stress <id> N  đối chiếu REF với BRUTE trên N test nhỏ
  judge.py score <id>     chấm mọi chương trình trong SOLS, ghi scores.json
"""
import importlib.util, json, os, random, resource, subprocess, sys, time, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROB = os.path.join(ROOT, 'problems')
WORK = os.environ.get('JUDGE_WORK', '/tmp/claude-0/-home-user-hvt/6a70b7fa-b99c-5363-b5c7-fd50a17adc6d/scratchpad/judge')


def load(pid, name):
    path = os.path.join(PROB, pid, name + '.py')
    spec = importlib.util.spec_from_file_location(pid.replace('.', '_') + '_' + name, path)
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.join(PROB, pid))
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    spec.loader.exec_module(m)
    return m


def compile_prog(pid, fname):
    src = os.path.join(PROB, pid, fname)
    if fname.endswith('.py'):
        return ['python3', src]
    out = os.path.join(WORK, 'bin', pid, fname[:-4])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
        r = subprocess.run(['g++', '-O2', '-std=gnu++17', '-pipe', '-o', out, src],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr)
            raise SystemExit('Compile error: %s/%s' % (pid, fname))
    return [out]


def run(cmd, inp, tl=None, ml=None, cwd=None):
    """Chạy chương trình; trả về (trạng thái, đầu ra, thời gian)."""
    def lim():
        if ml:
            resource.setrlimit(resource.RLIMIT_AS, (ml * 1024 * 1024, ml * 1024 * 1024))
        resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
    t0 = time.time()
    try:
        r = subprocess.run(cmd, input=inp, capture_output=True, text=True,
                           timeout=(tl * 1.0 + 0.05) if tl else None, preexec_fn=lim, cwd=cwd or WORK)
    except subprocess.TimeoutExpired:
        return 'TLE', '', time.time() - t0
    dt = time.time() - t0
    if r.returncode != 0:
        return 'RE', r.stdout, dt
    if tl and dt > tl:
        return 'TLE', r.stdout, dt
    return 'OK', r.stdout, dt


def same(a, b):
    return a.split() == b.split()


def testdir(pid):
    return os.path.join(WORK, 'tests', pid)


def build(pid):
    meta = load(pid, 'meta'); gen = load(pid, 'gen')
    ref = compile_prog(pid, meta.REF)
    ok = True
    for i, (inp, out) in enumerate(gen.samples()):
        st, got, dt = run(ref, inp)
        good = st == 'OK' and (gen.check(inp, got, out) if hasattr(gen, 'check') else same(got, out))
        if not good:
            ok = False
            print('SAMPLE %d MISMATCH (%s)\n--- input\n%s--- expected\n%s--- got\n%s' % (i + 1, st, inp[:500], out[:500], got[:500]))
    print('samples:', 'OK' if ok else 'FAIL')
    td = testdir(pid)
    os.makedirs(td, exist_ok=True)
    for f in os.listdir(td):
        os.remove(os.path.join(td, f))
    tests = gen.tests()
    manifest = {}
    for s, lst in tests.items():
        for j, inp in enumerate(lst):
            name = 's%d_%02d' % (s, j)
            with open(os.path.join(td, name + '.inp'), 'w') as f:
                f.write(inp)
            st, got, dt = run(ref, inp, tl=30)
            if st != 'OK':
                raise SystemExit('REF failed on %s: %s' % (name, st))
            with open(os.path.join(td, name + '.out'), 'w') as f:
                f.write(got)
            manifest.setdefault(str(s), []).append(name)
            print('  %s  ref %.3fs' % (name, dt))
    json.dump(manifest, open(os.path.join(td, 'manifest.json'), 'w'))
    return ok


def stress(pid, n):
    meta = load(pid, 'meta'); gen = load(pid, 'gen')
    ref = compile_prog(pid, meta.REF)
    brs = meta.BRUTE if isinstance(meta.BRUTE, list) else [meta.BRUTE]
    bcmds = [compile_prog(pid, b) for b in brs]
    rng = random.Random(12345)
    for t in range(n):
        inp = gen.small(rng)
        st, a, _ = run(ref, inp)
        for b, bc in zip(brs, bcmds):
            st2, c, _ = run(bc, inp, tl=20)
            good = st == 'OK' and st2 == 'OK' and (gen.check(inp, a, c) if hasattr(gen, 'check') else same(a, c))
            if not good:
                print('STRESS MISMATCH test %d vs %s (%s/%s)\n--- input\n%s--- ref\n%s--- brute\n%s' % (t, b, st, st2, inp[:800], a[:800], c[:800]))
                return False
    print('stress: %d tests OK' % n)
    return True


def score(pid, only=None):
    meta = load(pid, 'meta'); gen = load(pid, 'gen')
    td = testdir(pid)
    manifest = json.load(open(os.path.join(td, 'manifest.json')))
    res_path = os.path.join(PROB, pid, 'scores.json')
    res = json.load(open(res_path)) if os.path.exists(res_path) else {}
    for fname, title in meta.SOLS:
        if only and fname not in only:
            continue
        cmd = compile_prog(pid, fname)
        pts = []
        detail = []
        for si, p in enumerate(meta.SUBTASKS, 1):
            okall = True
            worst = 0.0
            verdict = 'AC'
            for name in manifest.get(str(si), []):
                inp = open(os.path.join(td, name + '.inp')).read()
                ans = open(os.path.join(td, name + '.out')).read()
                st, got, dt = run(cmd, inp, tl=meta.TL, ml=meta.ML)
                worst = max(worst, dt)
                if st == 'OK':
                    good = gen.check(inp, got, ans) if hasattr(gen, 'check') else same(got, ans)
                    if not good:
                        st = 'WA'
                if st != 'OK':
                    okall = False
                    verdict = st
                    break
            pts.append(p if okall else 0)
            detail.append('%s %.2fs' % (verdict, worst))
        res[fname] = {'title': title, 'pts': pts, 'detail': detail}
        print('%-14s %-40s %s  = %d   %s' % (fname, title, pts, sum(pts), detail))
    json.dump(res, open(res_path, 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    os.makedirs(WORK, exist_ok=True)
    cmd, pid = sys.argv[1], sys.argv[2]
    if cmd == 'build':
        build(pid)
    elif cmd == 'stress':
        stress(pid, int(sys.argv[3]) if len(sys.argv) > 3 else 300)
    elif cmd == 'score':
        score(pid, sys.argv[3:] or None)
    elif cmd == 'all':
        ok = build(pid)
        if os.path.exists(os.path.join(PROB, pid, 'meta.py')) and getattr(load(pid, 'meta'), 'BRUTE', None):
            stress(pid, int(sys.argv[3]) if len(sys.argv) > 3 else 300)
        score(pid)
