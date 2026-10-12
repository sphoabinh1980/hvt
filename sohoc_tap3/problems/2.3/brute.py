import sys
N, k = map(int, sys.stdin.read().split())
def s(n):
    t, d = 0, 1
    while d * d <= n:
        if n % d == 0:
            t += d
            if d * d != n: t += n // d
        d += 1
    return t - n
res = []
for a in range(1, N + 1):
    b = s(a) - k
    if a < b <= N and s(b) == a + k:
        res.append((a, b))
print(len(res))
for a, b in res: print(a, b)
