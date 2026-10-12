import random
def samples():
    return [('1 100 10\n', '9\n'), ('2000 2026 10\n', '3\n'), ('1 1000000000 1\n', '10\n')]
def tests():
    r = random.Random(15)
    s1 = []
    for _ in range(6):
        a = r.randint(1, 10**6); b = r.randint(a, 10**6); s1.append('%d %d %d\n' % (a, b, r.randint(1, 54)))
    s2 = ['1 1000000000000000000 81\n', '1 1000000000000000000 162\n', '1 999999999999999999 162\n', '123456789012345678 987654321098765432 90\n',
          '1 1000000000000000000 1\n', '999999999999999999 1000000000000000000 1\n']
    for _ in range(4):
        a = r.randint(1, 10**18); b = r.randint(a, 10**18); s2.append('%d %d %d\n' % (a, b, r.randint(1, 162)))
    return {1: s1, 2: s2}
def small(r):
    a = r.randint(1, 3000); b = r.randint(a, a + r.choice([10, 100, 5000])); return '%d %d %d\n' % (a, b, r.randint(1, 30))
