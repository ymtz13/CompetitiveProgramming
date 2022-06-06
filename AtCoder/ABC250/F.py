N = int(input())
P = []
SX = SY = 0
for _ in range(N):
  X, Y = map(int, input().split())
  X *= N
  Y *= N

  P.append((X, Y))
  SX += X
  SY += Y

x0 = SX // N
y0 = SY // N


def f(xi, yi, xj, yj):
  dxi = xi - x0
  dyi = yi - y0
  dxj = xj - x0
  dyj = yj - y0
  return dxi * dyj - dyi * dxj


S = []
for i in range(N):
  j = (i + 1) % N
  S.append(abs(f(*P[i], *P[j])))
  # xi, yi = P[i]
  # xj, yj = P[j]

  # dxi = xi - x0
  # dyi = yi - y0
  # dxj = xj - x0
  # dyj = yj - y0

  # S.append(abs(dxi * dyj - dyi * dxj))

Z = sum(S)

SS = [0]
for s in S * 2:
  SS.append(SS[-1] + s)

#print('x0, y0 = {}, {}'.format(x0, y0))
#print(SS)

ans = 1 << 200

for p1 in range(N):
  ng = N - 1
  ok = 1
  while ng - ok > 1:
    tgt = (ng + ok) // 2

    sb = SS[p1 + tgt] - SS[p1]

    p2 = (p1 + tgt) % N

    sf = f(*P[p1], *P[p2])

    ss = sb - sf  # +かも
    ans = min(ans, abs(Z - 4 * ss))

    if ss * 4 <= Z:
      ok = tgt
    else:
      ng = tgt

print(ans // N // N)
