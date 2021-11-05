N = int(input())
T = list(map(int, input().split()))
S = sum(T)

M = S+1
dp = [False]*M
dp[0] = True

for t in T:
  for i in range(M-1, t-1, -1):
    dp[i] |= dp[i-t]

ans = M
for v, ok in enumerate(dp):
  #print(v, ok)
  if ok: ans = min(ans, max(v, S-v))

print(ans)
