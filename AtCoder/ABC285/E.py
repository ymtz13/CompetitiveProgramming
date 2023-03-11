N = int(input())
A = list(map(int, input().split()))

B = [0] * (2 * N + 10)
for i, a in enumerate(A, 1):
  B[i * 2] = B[i * 2 - 1] + a
  B[i * 2 + 1] = B[i * 2] + a

dp = [0] * (N + 1)
for i in range(N):
  for j in range(i + 1, N + 1):
    d = j - i
    dp[j] = max(dp[j], dp[i] + B[d])

print(dp[-1])
