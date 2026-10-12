import random
def F(P): return '%d\n' % len(P) + ''.join('%d %d\n' % p for p in P)
def mono(r, n, M, axis=False):
    # đường gấp khúc đơn điệu theo x tăng chặt -> không tự cắt
    xs = sorted(r.sample(range(-M, M + 1), n))
    if axis:
        P = []; y = r.randint(-M, M); x = xs[0]
        P.append((x, y))
        i = 1
        while len(P) < n:
            if len(P) % 2 == 1:
                ny = r.randint(-M, M)
                if ny == P[-1][1]: ny = P[-1][1] + 1 if P[-1][1] < M else P[-1][1] - 1
                P.append((P[-1][0], ny))
            else:
                P.append((xs[i], P[-1][1])); i += 1
        return P
    P = [(x, r.randint(-M, M)) for x in xs]
    return P
def samples():
    return [(F([(1, 1), (13, 9), (13, 2)]), '12\n'), (F([(-10**9, -10**9), (10**9, 10**9)]), '2000000001\n'), (F([(0, 0), (2, 0), (5, 0), (5, 3)]), '9\n')]
def tests():
    r = random.Random(201)
    B = 10**9
    return {1: [F(mono(r, 100, 100)), F(mono(r, 100, 100, True)), F([(-100, -100), (100, 100), (100, -100)])],
            2: [F(mono(r, 10**5, B, True)), F([(-B, -B), (B, -B), (B, B), (-B + 1, B)]), F(mono(r, 1000, B, True))],
            3: [F(mono(r, 10**5, B)), F([(-B, -B), (B, B), (B, -B), (-B + 2, -B + 2)][:3]), F([(r.randint(-5, 5) * 2 * 10**8 + i * 0, 0) for i in range(1)] + [(0, B)]), F(mono(r, 10**5, B))]}
def small(r):
    n = r.randint(2, 8)
    return F(mono(r, n, 30, r.random() < 0.3))
