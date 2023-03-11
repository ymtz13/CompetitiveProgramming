H, W, N, Dh, Dw = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

INF = 1000

T = [+INF] * N
B = [-INF] * N
L = [+INF] * N
R = [-INF] * N

P = set()

for h, row in enumerate(A):
  for w, a in enumerate(row):
    a -= 1
    T[a] = min(T[a], h)
    B[a] = max(B[a], h)
    L[a] = min(L[a], w)
    R[a] = max(R[a], w)

    P.add(a)

P = len(P)

SH = H - Dh + 1
SW = W - Dw + 1
S = [[0] * SW for _ in range(SH)]

for t, b, l, r in zip(T, B, L, R):
  if t == INF: continue
  if b - t + 1 > Dh or r - l + 1 > Dw: continue

  xt = max(0, b - Dh + 1)
  xb = t + 1
  xl = max(0, r - Dw + 1)
  xr = l + 1

  S[xt][xl] += 1
  if xr < SW: S[xt][xr] -= 1
  if xb < SH: S[xb][xl] -= 1
  if xr < SW and xb < SH: S[xb][xr] += 1

for h in range(SH):
  for w in range(1, SW):
    S[h][w] += S[h][w - 1]

for w in range(SW):
  for h in range(1, SH):
    S[h][w] += S[h - 1][w]

for h, srow in enumerate(S):
  ans = [P - v for v in srow]
  print(' '.join(map(str, ans)))
