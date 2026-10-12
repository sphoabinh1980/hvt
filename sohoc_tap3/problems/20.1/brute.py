import sys
from math import gcd
d = list(map(int, sys.stdin.read().split()))
n = d[0]; P = [(d[1 + 2 * i], d[2 + 2 * i]) for i in range(n)]
pts = set()
for i in range(n - 1):
    (x1, y1), (x2, y2) = P[i], P[i + 1]
    g = gcd(abs(x2 - x1), abs(y2 - y1))
    for t in range(g + 1):
        pts.add((x1 + (x2 - x1) // g * t, y1 + (y2 - y1) // g * t))
print(len(pts))
