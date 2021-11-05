N = int(input())
A = list(map(int, input().split()))

mod = 10**9 + 7

S = [0]
for a in A:
  S.append(S[-1] + a)

M = N + 1

E = [[None] * M for _ in range(N)]
for q in range(1, M):
  P = [0] + [None] * (q - 1)
  for i, s in enumerate(S[1:], 1):
    r = s % q
    if P[r] is not None: E[P[r]][q] = i
    P[r] = i

dp = [[0] * M for _ in range(M)]
dp[0][0] = 1

for i in range(N):
  for j, e in enumerate(E[i][:i+2]):
    if not e: continue

    dp[e][j] += dp[i][j] + dp[i][j - 1]
    dp[e][j] %= mod

ans = 0
for a in dp[-1]:
  ans += a
  ans %= mod

print(ans)
