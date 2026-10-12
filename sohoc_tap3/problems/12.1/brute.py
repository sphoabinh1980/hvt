import sys
d = sys.stdin.read().split()
k, L = int(d[0]), int(d[1])
r, M = 0, 1
for i in range(k):
    m, a = int(d[2 + 2 * i]), int(d[3 + 2 * i])
    t = (a - r) * pow(M, -1, m) % m if m > 1 else 0
    r, M = r + M * t, M * m
x = L + (r - L) % M
print(x)
