import sys
from fractions import Fraction
d = sys.stdin.read().split()
n = int(d[0]); M = 10**9 + 7
p1 = Fraction(1); q = Fraction(1)
for i in range(n):
    x, y = int(d[1 + 2 * i]), int(d[2 + 2 * i])
    p1 *= Fraction(x, x + y); q *= Fraction(y, x + y)
p2 = 1 - q
f = lambda F: F.numerator % M * pow(F.denominator % M, M - 2, M) % M
print(f(p1)); print(f(p2))
