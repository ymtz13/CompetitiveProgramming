N = int(input())
S = int(input())

if N < S:
    print(-1)
    exit()

if N == S:
    print(N + 1)
    exit()

for b in range(2, 10**6):
    s = 0
    n = N
    while n:
        s += n % b
        n //= b

    if s == S:
        print(b)
        exit()


# bx+y=n
#  x+y=s
# (b-1)x = n-s

D = N - S
B = []

for p in range(1, D + 1):
    if p * p > D:
        break

    if D % p == 0:
        B.append(p + 1)
        B.append(D // p + 1)

B.sort()

for b in B:
    x = D // (b - 1)
    y = S - x

    if 0 <= x < b and 0 <= y < b and b * x + y == N:
        print(b)
        exit()

print(-1)
