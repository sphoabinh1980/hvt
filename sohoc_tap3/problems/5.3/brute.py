import sys
from sympy import isprime
d = sys.stdin.read().split()
print('\n'.join('YES' if isprime(int(x)) else 'NO' for x in d[1:1 + int(d[0])]))
