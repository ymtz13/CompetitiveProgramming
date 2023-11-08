from collections import defaultdict

mod = 998244353

A, B = map(int, input().split())

D = defaultdict(int)

for p in range(2, 1000010):
    while A % p == 0:
        D[p] += 1
        A //= p

if A > 1:
    D[A] += 1

X = B
p = 1 if B % 2 == 1 else 0
for q in D.values():
    k = B * q + 1

    X *= k
    X %= mod

    if k % 2 == 0:
        p = 0

X -= p
X %= mod

X *= pow(2, mod - 2, mod)
X %= mod

print(X)
