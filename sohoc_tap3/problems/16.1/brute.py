import sys
from sympy import divisor_sigma
n = int(sys.stdin.read())
print(sum(int(divisor_sigma(x)) for x in range(1, n + 1)) % (10**9 + 7))
