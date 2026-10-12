import sys
d = sys.stdin.read().split(); p = 1; out = []
for _ in range(int(d[0])):
    if d[p] == '1':
        L, R, k = int(d[p + 1]), int(d[p + 2]), int(d[p + 3]); p += 4
        out.append(str(sum(1 for x in range(L, R + 1) if bin(x).count('1') == k)))
    else:
        k, m = int(d[p + 1]), int(d[p + 2]); p += 3
        x = 0
        while m:
            x += 1
            if bin(x).count('1') == k: m -= 1
        out.append(str(x))
print('\n'.join(out))
