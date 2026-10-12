import sys, math
d = list(map(int, sys.stdin.read().split()))
lcm = lambda x, y: x * y // math.gcd(x, y)
def f(N, a, b, c):
    if N <= 0: return 0
    AB = lcm(a, b); AC = lcm(a, c); BC = lcm(b, c); ABC = lcm(AB, c)
    return N // a + N // b - N // AB - (N // AC + N // BC - N // ABC)
out = []
for i in range(d[0]):
    L, R, a, b, c = d[1 + 5 * i:6 + 5 * i]
    out.append(str(f(R, a, b, c) - f(L - 1, a, b, c)))
print('\n'.join(out))
