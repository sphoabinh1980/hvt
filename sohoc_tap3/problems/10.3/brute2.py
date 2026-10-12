import sys
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    a, c, m, L, R = map(int, d[1 + 5 * i:6 + 5 * i])
    xs = [x for x in range(L, R + 1) if (a * x - c) % m == 0]
    out.append('%d %d' % (len(xs), xs[0]) if xs else '0')
print('\n'.join(out))
