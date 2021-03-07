N, M, K = map(int, input().split())
mod = 998244353

if N==1:
  print(pow(K, M, mod))
  exit()

if M==1:
  print(pow(K, N, mod))
  exit()

X = 0
ans = 0
for k in range(1, K+1):
  X_ = pow(k, N, mod)
  P = (X_ - X) % mod
  X = X_

  Q = pow(K+1-k, M, mod)
  ans += P*Q
  ans %= mod

print(ans)
