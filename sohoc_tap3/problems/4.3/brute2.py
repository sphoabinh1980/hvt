import sys
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    m, p, a, q, b, T = map(int, d[1 + 6 * i:7 + 6 * i])
    hit = [t for t in range(max(T + 1, m)) if (p + a * t) % m == (q + b * t) % m]
    out.append('%d %d' % (hit[0], sum(1 for t in hit if t <= T)) if hit else '-1 0')
print('\n'.join(out))
