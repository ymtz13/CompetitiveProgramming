S = input()
K = int(input())

F = [1]
for i in range(1, 31):
  F.append(F[-1] * i)

NK = S.count('K')
NE = S.count('E')
NY = S.count('Y')

if K > 450:
  fK = F[NK]
  fE = F[NE]
  fY = F[NY]
  print(F[len(S)] // fK // fE // fY)
  exit()

M = 500

dp = [[[[0] * M for _ in range(NY + 1)] for _ in range(NE + 1)]
      for _ in range(NK + 1)]

IK = []
IE = []
IY = []
BK = []
BE = []
BY = []
bK = bE = bY = 0
for i, c in enumerate(S):
  BK.append(bK)
  BE.append(bE)
  BY.append(bY)
  if c == 'K': bK += 1
  if c == 'E': bE += 1
  if c == 'Y': bY += 1
  if c == 'K': IK.append(i)
  if c == 'E': IE.append(i)
  if c == 'Y': IY.append(i)

dp[0][0][0][0] = 1
for nK in range(NK + 1):
  for nE in range(NE + 1):
    for nY in range(NY + 1):
      s = nK + nE + nY
      dp0 = dp[nK][nE][nY]

      if nK < NK:
        i = IK[nK]
        cost = max(0, BK[i] - nK) + max(0, BE[i] - nE) + max(0, BY[i] - nY)
        dpK = dp[nK + 1][nE][nY]
        for m in range(M - cost):
          dpK[m + cost] += dp0[m]

      if nE < NE:
        i = IE[nE]
        cost = BK[i] + BE[i] + BY[i] - s
        cost = max(0, BK[i] - nK) + max(0, BE[i] - nE) + max(0, BY[i] - nY)
        dpE = dp[nK][nE + 1][nY]
        for m in range(M - cost):
          dpE[m + cost] += dp0[m]

      if nY < NY:
        i = IY[nY]
        cost = BK[i] + BE[i] + BY[i] - s
        cost = max(0, BK[i] - nK) + max(0, BE[i] - nE) + max(0, BY[i] - nY)
        dpY = dp[nK][nE][nY + 1]
        for m in range(M - cost):
          dpY[m + cost] += dp0[m]

#print(dp[0][1][0][:20])
#print(dp[1][1][0][:20])
#print(dp[1][1][1][:20])

ans = 0
for nK in range(NK + 1):
  for nE in range(NE + 1):
    for nY in range(NY + 1):
      for m in range(M):
        if nK + nE + nY == len(S) and m <= K:
          ans += dp[nK][nE][nY][m]

print(ans)
