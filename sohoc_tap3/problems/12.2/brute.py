import sys, math
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    a1, p1, a2, p2 = map(int, d[1 + 4 * i:5 + 4 * i])
    g = math.gcd(p1, p2)
    if (a2 - a1) % g: out.append('-1'); continue
    L = p1 // g * p2
    t = ((a2 - a1) // g) * pow(p1 // g, -1, p2 // g) % (p2 // g) if p2 // g > 1 else 0
    r = a1 + p1 * t
    A = max(a1, a2)
    out.append(str(A + (r - A) % L))
print('\n'.join(out))
