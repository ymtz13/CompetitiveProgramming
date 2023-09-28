from random import randint

N = 10**5
X = 10
Y = 10
PT = [(randint(1, 8), randint(1, 10**9)) for _ in range(N - 1)]

Q = 0

print(N, X, Y)
for pt in PT:
    print(*pt)

print(Q)
