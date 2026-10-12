import sys
sys.set_int_max_str_digits(0)
a, b = map(int, sys.stdin.read().split())
print(a ** b)
