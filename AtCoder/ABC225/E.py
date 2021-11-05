from functools import cmp_to_key


def gcd(x, y):
  while x:
    x, y = y % x, x
  return y


def f(x, y):
  if x == 0: return (0, 1)
  if y == 0: return (1, 0)
  g = gcd(x, y)
  return (x // g, y // g)


N = int(input())
XL = []
XR = []
P = set()
T = 30

for _ in range(N):
  x, y = map(int, input().split())
  pl = f(x - 1, y)
  pr = f(x, y - 1)
  xl = (pl[0] << T) + pl[1]
  xr = (pr[0] << T) + pr[1]
  XL.append(xl)
  XR.append(xr)
  P.add(pl)
  P.add(pr)


def cmp(v1, v2):
  x1, y1 = v1
  x2, y2 = v2
  return x1 * y2 - x2 * y1


INF = 1 << 60
P = sorted(list(P), key=cmp_to_key(cmp))
D = {(x << T) + y: i for i, (x, y) in enumerate(P)}

M = len(P)
G = [[] for _ in range(M)]
for xl, xr in zip(XL, XR):
  G[D[xr]].append(D[xl])

dp = [0] * M
for i, g in enumerate(G[1:], 1):
  dp[i] = dp[i - 1]
  for zl in g:
    dp[i] = max(dp[i], dp[zl] + 1)

print(dp[-1])
