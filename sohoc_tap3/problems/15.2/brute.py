import sys
d = list(map(int, sys.stdin.read().split()))
n, K = d[0], d[1]; bad = set(d[2:2 + K])
f = [1] + [0] * n
for x in range(1, n + 1):
    f[x] = 0 if x in bad else sum(f[x - s] for s in (1, 2, 3) if x - s >= 0)
print(f[n] % (10**9 + 7))
