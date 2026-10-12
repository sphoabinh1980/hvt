import sys
d = list(map(int, sys.stdin.read().split()))
q = d[0]; out = []
for t in range(q):
    x1, y1, x2, y2, x3, y3 = d[1 + 6 * t: 7 + 6 * t]
    def cr(ax, ay, bx, by, px, py): return (bx - ax) * (py - ay) - (by - ay) * (px - ax)
    c = 0
    for x in range(min(x1, x2, x3), max(x1, x2, x3) + 1):
        for y in range(min(y1, y2, y3), max(y1, y2, y3) + 1):
            a = cr(x1, y1, x2, y2, x, y); b = cr(x2, y2, x3, y3, x, y); e = cr(x3, y3, x1, y1, x, y)
            if (a > 0 and b > 0 and e > 0) or (a < 0 and b < 0 and e < 0): c += 1
    out.append(str(c))
print('\n'.join(out))
