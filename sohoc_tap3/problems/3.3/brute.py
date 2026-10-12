import sys, math
d = sys.stdin.read().split()
n, q = int(d[0]), int(d[1])
t = list(map(int, d[2:2 + n]))
out = []
p = 2 + n
for _ in range(q):
    l, r = int(d[p]), int(d[p + 1]); p += 2
    v = 1
    for x in t[l - 1:r]: v = v * x // math.gcd(v, x)
    out.append(str(v) if v <= 10**18 else '-1')
print('\n'.join(out))
