N, M, K = map(int, input().split())
mod = 998244353
E = []
for _ in range(M):
  U, V = map(int, input().split())
  E.append((U - 1, V - 1))

dp = [0] * N
dp[0] = 1

for k in range(K):
  S = 0
  for v in dp:
    S = (S + v) % mod

  dp_next = [(S - v) % mod for v in dp]

  for u, v in E:
    dp_next[u] = (dp_next[u] - dp[v]) % mod
    dp_next[v] = (dp_next[v] - dp[u]) % mod

  dp = dp_next

print(dp[0] % mod)
