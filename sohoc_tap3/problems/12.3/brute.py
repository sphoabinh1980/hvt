import sys, math
d = list(map(int, sys.stdin.read().split()))
k, Q = d[0], d[1]; ms = d[2:2 + k]; p = 2 + k
L_ = 1
for m in ms: L_ = L_ * m // math.gcd(L_, m)
out = [str(L_ % (10**9 + 7))]
for _ in range(Q):
    cs = d[p:p + k]; L, R = d[p + k], d[p + k + 1]; p += k + 2
    r, M, ok = 0, 1, True
    for m, c in zip(ms, cs):
        g = math.gcd(M, m)
        if (c - r) % g: ok = False; break
        t = ((c - r) // g) * pow(M // g, -1, m // g) % (m // g) if m // g > 1 else 0
        r, M = r + M * t, M // g * m
    if not ok: out.append('0'); continue
    first = L + (r - L) % M
    out.append('0' if first > R else '%d %d' % ((R - first) // M + 1, first))
print('\n'.join(out))
