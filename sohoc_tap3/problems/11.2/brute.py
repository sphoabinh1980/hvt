import sys, math
d = sys.stdin.read().split()
out = []
for i in range(int(d[0])):
    L, R = int(d[1 + 2 * i]), int(d[2 + 2 * i])
    out.append(str(sum(1 for b in range(max(L, 2), R + 1) for a in range(1, b) if math.gcd(a, b) == 1)))
print('\n'.join(out))
