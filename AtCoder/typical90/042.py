mod = 10**9+7

K = int(input())
if K%9>0:
  print(0)
  exit()

dp = [0]*10+[1]
s = 1
for i in range(K):
  dp.append(s)
  s = (s*2 - dp[-10])%mod

print(dp[-1])
