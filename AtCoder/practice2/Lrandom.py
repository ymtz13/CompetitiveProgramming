from random import seed, randint
seed(100)

N = 10
Q = 200
print(N, Q)

A = [randint(0, 1) for _ in range(N)]
print(' '.join(map(str, A)))

for _ in range(Q):
    T = randint(1,2)
    L = randint(1, N)
    R = randint(L, N)
    print(T, L, R)
