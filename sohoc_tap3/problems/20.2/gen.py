import random, math
def F(P): return '%d\n' % len(P) + ''.join('%d %d\n' % p for p in P)
def star(r, n, M):
    # đa giác đơn điệu theo x: xích trên (y > 0) từ trái sang phải, xích dưới (y < 0) quay về
    xs = sorted(r.sample(range(-M, M + 1), n))
    mid = xs[1:-1]
    top = set(r.sample(mid, (n - 2) // 2))
    P = [(xs[0], 0)] + [(x, r.randint(1, M)) for x in mid if x in top] + [(xs[-1], 0)]
    P += [(x, -r.randint(1, M)) for x in reversed(mid) if x not in top]
    return P if r.random() < 0.5 else P[::-1]
def rect(r, n, M):
    # đa giác vuông góc dạng "bậc thang" (histogram) không tự cắt
    k = n // 2 - 1
    xs = sorted(r.sample(range(-M, M + 1), k + 1))
    base = -M
    P = [(xs[0], base)]
    hs = [r.randint(-M + 1, M) for _ in range(k)]
    for i in range(k):
        P.append((xs[i], hs[i])); P.append((xs[i + 1], hs[i]))
    P.append((xs[k], base))
    Q = [P[0]]
    for p in P[1:]:
        if p != Q[-1]: Q.append(p)
    if Q[-1] == Q[0]: Q.pop()
    return Q if r.random() < 0.5 else Q[::-1]
def samples():
    return [(F([(0, 0), (6, 0), (6, 4), (2, 6), (0, 3)]), '22 16\n'), (F([(0, 0), (0, 4), (2, 2), (4, 0)]), '3 12\n'), (F([(0, 0), (3, 1), (1, 0)]), '0 3\n')]
def tests():
    r = random.Random(202)
    M = 10**6
    return {1: [F(star(r, 100, 100)), F(star(r, 50, 100)), F(rect(r, 100, 100)), F([(-100, -100), (100, -100), (100, 100), (-100, 100)])],
            2: [F(rect(r, 10**5, M)), F(rect(r, 1000, M)), F([(-M, -M), (M, -M), (M, M), (-M, M)])],
            3: [F(star(r, 10**5, M)), F(star(r, 1000, M)), F([(-M, -M), (M, M - 1), (M, M)]), F([(-M, -M), (M, -M), (0, M)])]}
def small(r):
    return F(star(r, r.randint(3, 8), 15) if r.random() < 0.7 else rect(r, 2 * r.randint(2, 4), 10))
