from collections import defaultdict

mod = 998244353

P = int(input())
Pm1 = P - 1

D = set()
for d in range(1, P):
    if d * d > P:
        break

    if Pm1 % d == 0:
        D.add(d)
        D.add(Pm1 // d)

D = sorted(list(D))

X = {d: Pm1 // d - 1 for d in D}

ans = 2  # (0, 0), (1, 1)
for d in reversed(D):
    for k in D:
        if k % d == 0 and k > d:
            X[d] -= X[k]

    ans += Pm1 // d * X[d]
    ans %= mod

print(ans)
