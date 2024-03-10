r = input()
N = int(input())

r = r[2:]
r += "0" * (18 - len(r))
r = int(r)

T = 10**18

V = (r, T)

Z = [None]
for i in range(100):
    x, y = V
    if y == 0:
        break
    z = x // y
    V = (y, x % y)
    Z.append(z)

print(Z)

P = [1, Z[1]]
Q = [0, 1]

for n, z in enumerate(Z[2:], 2):
    P.append(z * P[-1] + P[-2])
    Q.append(z * Q[-1] + Q[-2])

for p, q in zip(P[1:], Q[1:]):
    print(p / q, p, q)
