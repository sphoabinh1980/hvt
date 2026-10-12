import sys
d = list(map(int, sys.stdin.read().split()))
out = []
for k in d[1:]:
    L = 1; cnt = 9; start = 1
    while k > L * cnt:
        k -= L * cnt; L += 1; cnt *= 10; start *= 10
    num = start + (k - 1) // L
    out.append(str(num)[(k - 1) % L])
print('\n'.join(out))
