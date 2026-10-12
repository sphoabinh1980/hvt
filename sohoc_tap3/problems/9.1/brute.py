import sys
d = sys.stdin.read().split()
M = 10**9 + 7
print('\n'.join(str(pow(int(d[1 + 2 * i]), int(d[2 + 2 * i]), M)) for i in range(int(d[0]))))
