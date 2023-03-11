N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(map(int, input().split()))
X = int(input())

dp = [0] * (200010)
dp[0] = 1

for i in range(X):
  if i in B: continue
  if not dp[i]: continue

  for a in A:
    dp[i + a] = 1

print('Yes' if dp[X] else 'No')
