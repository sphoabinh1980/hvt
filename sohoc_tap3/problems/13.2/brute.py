import sys
d = list(map(int, sys.stdin.read().split()))
m, n, K = d[0], d[1], d[2]
bad = {(d[3 + 2 * i], d[4 + 2 * i]) for i in range(K)}
M = 10**9 + 7
f = [[0] * (n + 1) for _ in range(m + 1)]
for x in range(m + 1):
    for y in range(n + 1):
        if (x, y) in bad: f[x][y] = 0; continue
        if x == 0 and y == 0: f[x][y] = 1; continue
        f[x][y] = ((f[x - 1][y] if x else 0) + (f[x][y - 1] if y else 0)) % M
print(f[m][n])
