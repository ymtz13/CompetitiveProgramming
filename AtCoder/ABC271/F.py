from collections import defaultdict

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
tA = [t[::-1] for t in A[::-1]]


def f(A):
  dp = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
  dp[0][0][A[0][0]] = 1

  for i, Arow in enumerate(A):
    for j, a in enumerate(Arow[:N - i]):
      vT = dp[i - 1][j] if i > 0 else {}
      vL = dp[i][j - 1] if j > 0 else {}
      v = dp[i][j]

      for key, value in vT.items():
        v[key ^ a] += value

      for key, value in vL.items():
        v[key ^ a] += value

  return dp


dp1 = f(A)
dp2 = f(tA)

ans = 0
for i in range(N):
  j = N - 1 - i

  v2 = dp2[j][i]
  a = A[i][j]
  for key, value in dp1[i][j].items():
    ans += value * v2[key ^ a]

print(ans)
