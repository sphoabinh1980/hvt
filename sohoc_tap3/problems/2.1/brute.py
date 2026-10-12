import sys
d = sys.stdin.read().split()
out = []
for x in d[1:1 + int(d[0])]:
    n = int(x)
    ds = [k for k in range(1, n + 1) if n % k == 0]
    good = [k for k in ds if 2 <= k <= n // 2]
    if not good:
        out.append('0')
    else:
        r = max(k for k in ds if k * k <= n)
        out.append('%d %d %d' % (len(good), r, n // r))
print('\n'.join(out))
