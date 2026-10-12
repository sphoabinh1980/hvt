import sys
sys.set_int_max_str_digits(0)
from math import factorial
d = list(map(int, sys.stdin.read().split()))
out = []
for n in d[1:]:
    s = str(factorial(n)); t = s.rstrip('0')
    out.append('%d %s' % (len(s) - len(t), t[-1]))
print('\n'.join(out))
