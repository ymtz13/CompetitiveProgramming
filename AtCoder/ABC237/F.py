mod = 998244353

N, M = map(int, input().split())
K = M + 1
KK = K * K
KKK = KK * K

dp = [0] * KKK
dp[0] = 1

for _ in range(N):
  dp_next = [0] * KKK

  for i, v in enumerate(dp):
    n1 = i // KK
    n2 = (i % KK) // K
    n3 = i % K

    for xx in range(1, K):
      if xx <= n1 or n1 == 0:
        j = xx * KK + n2 * K + n3

      elif xx <= n2 or n2 == 0:
        j = n1 * KK + xx * K + n3

      elif xx <= n3 or n3 == 0:
        j = n1 * KK + n2 * K + xx

      else:
        break

      dp_next[j] += v
      dp_next[j] %= mod

  dp = dp_next

ans = 0
for i, v in enumerate(dp):
  n1 = i // KK
  n2 = (i % KK) // K
  n3 = i % K

  if n3 > 0:
    ans += v
    ans %= mod

print(ans)