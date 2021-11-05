S = input()

mod = 10**9 + 7
oa = ord('a')

dp = [0] * 26
nc = nv = None
for i, c in enumerate(S):
  v = (sum(dp) + 1) % mod

  if nc: dp[ord(nc) - oa] = nv
  nc = c
  nv = v

dp[ord(nc) - oa] = nv
#print(dp)
print(sum(dp) % mod)
