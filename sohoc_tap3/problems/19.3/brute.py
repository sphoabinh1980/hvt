import sys
d = list(map(int, sys.stdin.read().split()))
m, n, k = d[0], d[1], d[2]
a = [d[3 + i * n: 3 + (i + 1) * n] for i in range(m)]
c = 0
for i1 in range(m):
    for i2 in range(i1, m):
        for j1 in range(n):
            for j2 in range(j1, n):
                if sum(a[i][j] for i in range(i1, i2 + 1) for j in range(j1, j2 + 1)) % k == 0: c += 1
print(c)
