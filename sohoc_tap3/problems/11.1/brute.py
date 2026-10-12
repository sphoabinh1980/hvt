import sys
from sympy import totient
d = sys.stdin.read().split()
print('\n'.join(str(int(totient(int(x)))) for x in d[1:1 + int(d[0])]))
