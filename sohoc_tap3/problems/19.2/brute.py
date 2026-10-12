import sys
d = list(map(int, sys.stdin.read().split()))
n, k, a = d[0], d[1], d[2:]
best = None
for l in range(n):
    s = 0
    for r in range(l, n):
        s += a[r]
        if s % k == 0:
            L = r - l + 1
            if best is None or L > best[0] or (L == best[0] and l + 1 < best[1]): best = (L, l + 1)
print(0 if best is None else '%d %d' % best)
