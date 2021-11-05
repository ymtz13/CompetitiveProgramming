N = int(input())
S = input()
S1 = S[:N]
S2 = S[N:][::-1]

XR = [None] * (N + 1)
XB = [None] * (N + 1)


def dp(nR, nB):
  dp = [[0] * (nB + 1) for _ in range(nR + 1)]
  dp[0][0] = 1

  for iR in range(nR + 1):
    for iB in range(nB + 1):
      if iR == nR and iB == nB: break
      if iR < nR and S2[iR + iB] == XR[iR]: dp[iR + 1][iB] += dp[iR][iB]
      if iB < nB and S2[iR + iB] == XB[iB]: dp[iR][iB + 1] += dp[iR][iB]

  return dp[nR][nB]


def dfs(nR, nB):
  n = nR + nB
  if n == N:
    return dp(nR, nB)

  XR[nR] = S1[n]
  aR = dfs(nR + 1, nB)

  XB[nB] = S1[n]
  aB = dfs(nR, nB + 1)

  return aR + aB


print(dfs(0, 0))
