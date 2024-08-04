from random import randint

M = 10**9

N = randint(2, 500_000)
P = []
for _ in range(N):
    l = randint(0, M - 1)
    r = randint(l + 1, M)
    P.append((l, r))

print(N)
for l, r in P:
    print(l, r)
