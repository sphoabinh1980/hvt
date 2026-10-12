import sys
d = list(map(int, sys.stdin.read().split()))
n = d[0]; P = [(d[1 + 2 * i], d[2 + 2 * i]) for i in range(n)]
def onseg(p, a, b):
    cr = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
    return cr == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
def inside(p):
    c = False
    for i in range(n):
        a, b = P[i], P[(i + 1) % n]
        if (a[1] > p[1]) != (b[1] > p[1]):
            x = a[0] + (p[1] - a[1]) * (b[0] - a[0]) / (b[1] - a[1])
            if p[0] < x: c = not c
    return c
I = B = 0
xs = [p[0] for p in P]; ys = [p[1] for p in P]
for x in range(min(xs), max(xs) + 1):
    for y in range(min(ys), max(ys) + 1):
        if any(onseg((x, y), P[i], P[(i + 1) % n]) for i in range(n)): B += 1
        elif inside((x, y)): I += 1
print(I, B)
