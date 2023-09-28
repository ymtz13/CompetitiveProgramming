from itertools import product

N, A1, A2, A3 = map(int, input().split())
M = 4

MORE = 2
SAME = 1
LESS = 0


def compare(s, v):
    if s > v:
        return LESS
    if s < v:
        return MORE
    return SAME


ret = []
for p in product(((0, 0, 0), (1, 1, 0), (0, 1, 1), (1, 0, 1)), repeat=M):
    s1 = s2 = s3 = 0
    for i, (b1, b2, b3) in enumerate(p):
        x = 1 << i
        s1 += b1 * x
        s2 += b2 * x
        s3 += b3 * x

    r = (
        s1 % A1,
        s2 % A2,
        s3 % A3,
        compare(N % (1 << M), s1),
        compare(N % (1 << M), s2),
        compare(N % (1 << M), s3),
    )

    if r == (0, 0, 0, 0, 0, 0):
        print(p, s1, s2, s3)

    ret.append(r)

ret.sort()
for x in ret:
    print(x)
