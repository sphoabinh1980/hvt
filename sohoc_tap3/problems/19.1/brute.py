import sys
d = list(map(int, sys.stdin.read().split()))
n, a = d[0], d[1:]
c = 0
for l in range(n):
    s = 0
    for r in range(l, n):
        s += a[r]
        if s == 0: c += 1
print(c)
