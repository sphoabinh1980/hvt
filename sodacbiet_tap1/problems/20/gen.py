import random
def samples():
    return [('10\n', '12\n'), ('15\n', '24\n'), ('1500\n', '859963392\n')]
def tests():
    r = random.Random(20)
    return {1: ['%d\n' % x for x in [1, 2, 7, 500, r.randint(1, 500), 499]],
            2: ['%d\n' % x for x in [10000, 9999, r.randint(1000, 10000), 5000, 8000]]}
def small(r):
    return '%d\n' % r.randint(1, r.choice([20, 150, 400]))
