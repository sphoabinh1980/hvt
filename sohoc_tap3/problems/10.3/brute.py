import sys, math
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    a, c, m, L, R = map(int, d[1 + 5 * i:6 + 5 * i])
    a %= m; c %= m
    g = math.gcd(a, m)
    if c % g: out.append('0'); continue
    M = m // g
    x0 = (c // g) * pow(a // g, -1, M) % M if M > 1 else 0
    first = L + (x0 - L) % M
    out.append('0' if first > R else '%d %d' % ((R - first) // M + 1, first))
print('\n'.join(out))
