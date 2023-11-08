from math import gcd

N, a, b, c = map(int, input().split())
A = list(map(int, input().split()))

s = a * b // gcd(a, b)
t = b * c // gcd(b, c)
u = c * a // gcd(c, a)

z = s * c // gcd(s, c)


Xa = [(((v + a - 1) // a) * a - v, i) for i, v in enumerate(A)]
Xb = [(((v + b - 1) // b) * b - v, i) for i, v in enumerate(A)]
Xc = [(((v + c - 1) // c) * c - v, i) for i, v in enumerate(A)]

Xs = [(((v + s - 1) // s) * s - v, i) for i, v in enumerate(A)]
Xt = [(((v + t - 1) // t) * t - v, i) for i, v in enumerate(A)]
Xu = [(((v + u - 1) // u) * u - v, i) for i, v in enumerate(A)]

Xz = [(((v + z - 1) // z) * z - v, i) for i, v in enumerate(A)]


Xa.sort()
Xb.sort()
Xc.sort()

Xs.sort()
Xt.sort()
Xu.sort()

Xz.sort()

Xa = Xa[:10]
Xb = Xb[:10]
Xc = Xc[:10]

Xs = Xs[:10]
Xt = Xt[:10]
Xu = Xu[:10]

ans = Xz[0][0]

for xa, ia in Xa:
    for xb, ib in Xb:
        if ia == ib:
            continue
        for xc, ic in Xc:
            if ia == ic or ib == ic:
                continue

            ans = min(ans, xa + xb + xc)

for X1, X2 in [(Xa, Xt), (Xb, Xu), (Xc, Xs)]:
    for x1, i1 in X1:
        for x2, i2 in X2:
            if i1 == i2:
                continue

            ans = min(ans, x1 + x2)


print(ans)
