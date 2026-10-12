import sys, math
d = sys.stdin.read().split()
n = int(d[0]); a = list(map(int, d[1:1 + n]))
best, idx = -1, -1
for i in range(n):
    g = 0
    for j in range(n):
        if j != i: g = math.gcd(g, a[j])
    if g > best: best, idx = g, i + 1
print(best, idx)
