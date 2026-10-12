import sys, bisect
d = sys.stdin.read().split()
n, q = int(d[0]), int(d[1])
xs = list(map(int, d[2:2 + q]))
ds = [k for k in range(1, n + 1) if n % k == 0]
out = [str(len(ds)), ' '.join(map(str, ds))]
for x in xs:
    i = bisect.bisect_left(ds, x)
    out.append(str(ds[i]) if i < len(ds) else '-1')
print('\n'.join(out))
