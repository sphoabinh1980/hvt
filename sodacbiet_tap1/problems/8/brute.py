import sys
d = list(map(int, sys.stdin.read().split()))
out = []
for n in d[1:]:
    pos = {}; r = 1 % n; i = 0
    while r != 0 and r not in pos:
        pos[r] = i; r = r * 10 % n; i += 1
    out.append('%d 0' % i if r == 0 else '%d %d' % (pos[r], i - pos[r]))
print('\n'.join(out))
