import sys, math
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    a, b = int(d[1 + 2 * i]), int(d[2 + 2 * i])
    g = math.gcd(a, b)
    out.append('%d %d' % (g, (a // g) * (b // g)))
print('\n'.join(out))
