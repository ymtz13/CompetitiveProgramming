mod = 998244353

N = int(input())
W = list(map(int, input().split()))
S = sum(W)
if S%2==1:
  print(0)
  exit()
S //= 2

dp = [[0]*(5200) for _ in range(N+1)] # dp[n][s] := n個のみかんで重さの合計がsになるような撮り方
dp[0][0] = 1

for i, w in enumerate(W):
  for n in range(N-1, -1, -1):
    for s in range(0, 5000):
      dp[n+1][s+w] += dp[n][s]
      dp[n+1][s+w] %= mod

f = [1]
for i in range(1, 110):
  f.append(f[-1]*i%mod)

#print(f[:20])

ans = 0
for n, d in enumerate(dp):
  #print(n, end=':')
  #print(d[:20])

  a = d[S] * f[N-n] * f[n] % mod
  #print(n, d[S], f[n], a)
  ans += a
  
print(ans% mod)
