import sys
def isp(x):
    if x < 2: return False
    i = 2
    while i * i <= x:
        if x % i == 0: return False
        i += 1
    return True
d = sys.stdin.read().split()
out = []
for x in d[1:1 + int(d[0])]:
    n = int(x); k = 0
    while True:
        if isp(n - k): out.append(str(n - k)); break
        if isp(n + k): out.append(str(n + k)); break
        k += 1
print('\n'.join(out))
