import sys
sys.set_int_max_str_digits(0)
n, m = map(int, sys.stdin.read().split())
print(int(''.join(map(str, range(1, n + 1)))) % m)
