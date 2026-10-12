import sys
n = int(sys.stdin.read())
print(sum(sum(map(int, str(x))) for x in range(1, n + 1)))
