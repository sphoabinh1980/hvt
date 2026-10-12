import sys, math
d = sys.stdin.read().split()
n = int(d[0]); a = list(map(int, d[1:1 + n]))
def L(xs):
    v = 1
    for x in xs: v = v * x // math.gcd(v, x)
    return v
tot = L(a)
print(tot % (10**9 + 7))
print(sum(1 for i in range(n) if L(a[:i] + a[i + 1:]) < tot))
