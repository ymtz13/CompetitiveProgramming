mod = 998244353

N, M, K = map(int, input().split())

dp = [1] * M

for _ in range(N - 1):
  S = [0]
  s = 0
  for v in dp:
    s += v
    s %= mod
    S.append(s)

  dp_next = [0] * M
  for i in range(M):
    if K == 0:
      dp_next[i] = s
      continue

    l = i - K
    r = i + K

    z = S[min(M, r)] - S[max(0, l + 1)]
    dp_next[i] = (s - z) % mod

  dp = dp_next

ans = 0
for v in dp:
  ans += v
  ans %= mod

print(ans)
