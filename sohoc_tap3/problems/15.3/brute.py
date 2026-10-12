import sys
d = list(map(int, sys.stdin.read().split()))
n, m, q = d[0], d[1], d[2]
E = [(d[3 + 2 * i] - 1, d[4 + 2 * i] - 1) for i in range(m)]
p = 3 + 2 * m
out = []
for _ in range(q):
    s, t, K = d[p] - 1, d[p + 1] - 1, d[p + 2]; p += 3
    v = [0] * n; v[s] = 1
    for _ in range(K):
        w = [0] * n
        for a, b in E: w[b] += v[a]
        v = w
    out.append(str(v[t] % (10**9 + 7)))
print('\n'.join(out))
