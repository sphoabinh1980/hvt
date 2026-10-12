import sys
from sympy import factorint
d = sys.stdin.read().split()
print('\n'.join(str(sum(1 for p, e in factorint(int(x)).items() if e >= 2)) for x in d[1:1 + int(d[0])]))
