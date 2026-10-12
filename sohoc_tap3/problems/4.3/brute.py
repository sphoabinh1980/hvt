import sys, math
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    m, p, a, q, b, T = map(int, d[1 + 6 * i:7 + 6 * i])
    D, E = (a - b) % m, (q - p) % m
    g = math.gcd(D, m)
    if E % g: out.append('-1 0'); continue
    M = m // g
    t0 = (E // g) * pow(D // g, -1, M) % M if M > 1 else 0
    out.append('%d %d' % (t0, 0 if t0 > T else (T - t0) // M + 1))
print('\n'.join(out))
