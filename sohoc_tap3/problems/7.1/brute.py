import sys
d = sys.stdin.read().split()
out = []
for x in d[1:1 + int(d[0])]:
    n = int(x); ds = [k for k in range(1, n + 1) if n % k == 0]
    out.append('%d %d' % (len(ds), sum(ds)))
print('\n'.join(out))
