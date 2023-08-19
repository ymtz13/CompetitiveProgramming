from itertools import combinations


def prod(v):
    r = 1
    for x in v:
        r *= x
    return r


for v in combinations(range(1, 41), 6):
    p = prod(v)
    s = sum([p // x for x in v])
    if p == s:
        print(v)
