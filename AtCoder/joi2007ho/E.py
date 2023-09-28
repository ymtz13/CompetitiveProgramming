from collections import deque
from math import gcd

N = int(input())
PQRB = [tuple(map(int, input().split())) for _ in range(N)]

Parent = [None] * (N + 1)
for i, (p, q, r, b) in enumerate(PQRB, 1):
    Parent[r] = Parent[b] = i

for i, p in enumerate(Parent):
    if p is None:
        root = i

print("root", root)


def prod(x, y):
    num = x[0] * y[0]
    den = x[1] * y[1]
    g = gcd(num, den)
    return (num // g, den // g)


queue = deque([root])
T = [None] * (N + 1)
W = [None] * (N + 1) * 2
T[root] = (1, 1)
while queue:
    i = queue.popleft()
    p, q, r, b = PQRB[i - 1]

    wr = prod(T[i], (q, p + q))
    wb = prod(T[i], (p, p + q))

    if r != 0:
        T[r] = wr
        queue.append(r)
    else:
        W[i * 2] = wr

    if b != 0:
        T[b] = wb
        queue.append(b)
    else:
        W[i * 2 + 1] = wb

print(W)
W = list(filter(lambda x: x is not None, W))

for i in range(len(W)):
    winv = (W[i][1], 1)
    W = [prod(winv, w) for w in W]

W = [w[0] for w in W]

g = W[0]
for w in W:
    g = gcd(g, w)

print(sum(W) // g)
