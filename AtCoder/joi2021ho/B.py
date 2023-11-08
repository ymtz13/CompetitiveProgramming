INF = 1 << 60

N, Q = map(int, input().split())
X = list(map(int, input().split()))

XX = [-INF] + X + [INF]
P = []
for i, (xl, xr) in enumerate(zip(XX, XX[1:])):
    P.append((xr - xl, i))
P.sort()

w = 0
maxw = 0
minw = 0
Z = []
for _ in range(Q):
    W = int(input())
    w += W

    if w > maxw:
        Z.append((w - minw, maxw, -minw, "R"))
        maxw = w

    if w < minw:
        Z.append((maxw - w, maxw, -minw, "L"))
        minw = w

Z.append((INF * 2, maxw, -minw, ""))

ansR = [None] * (N + 2)
ansL = [None] * (N + 2)

j = 0
for p, i in P:
    while Z[j][0] < p:
        j += 1

    s, xr, xl, d = Z[j]

    ansR[i] = xr
    ansL[i + 1] = xl

    r = p - (xr + xl)
    if d == "R":
        ansR[i] += r
    if d == "L":
        ansL[i + 1] += r

# for z in Z:
#     print(z)

# print(ansL)
# print(ansR)

ans = []
for aR, aL in zip(ansR[1:-1], ansL[1:-1]):
    print(aR + aL)
