mod = 998244353

N = int(input())
P = list(map(int, input().split()))

mL = 1
mR = 2
m_ = 3

DPV = [[0] * (N + 1)]
DPM = [[m_] * (N + 1)]
DPV[0][0] = 1

for i, p in enumerate(P, 1):
  dpV_prev = DPV[-1]
  dpM_prev = DPM[-1]

  F = []
  f = p
  for q in P[i:]:
    if q > f:
      F.append(q)
      f = q

  G = []
  g = p
  for q in reversed(P[:i]):
    if q > g:
      G.append(q)
      g = q

  S = []
  SwoR = []
  s = swoR = 0
  for v, m in zip(dpV_prev, dpM_prev):
    s += v
    s %= mod
    if m != mR:
      swoR += v
      swoR %= mod
    S.append(s)
    SwoR.append(swoR)

  dpV = [0] * (N + 1)
  dpM = [m_] * (N + 1)
  for x in [p] + F:
    s0 = S[x]
    s1 = SwoR[-1] - SwoR[x]
    dpV[x] = (s0 + s1) % mod
    if x != p: dpM[x] = mR

  for x in G:
    s = SwoR[-1] - SwoR[x - 1]
    dpV[x] = s % mod
    dpM[x] = mL

  DPV.append(dpV)
  DPM.append(dpM)

ans = 0
for a in dpV:
  ans += a
  ans %= mod

print(ans)
