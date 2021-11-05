N, M = map(int, input().split())
mod = 998244353

Z = 20000
F = [1]*Z
p = 1
for x in range(1, Z):
  F[x] = p = p*x % mod

iF = [1]*Z
iF[Z-1] = p = pow(F[-1], mod-2, mod)
for x in range(Z-2, -1, -1):
  iF[x] = p = p*(x+1)%mod

def comb(k, x):
  return F[k] * iF[k-x] * iF[x] % mod

memo = [{} for _ in range(12)]

def dfs(i, X):
  if X<0: return 0
  if X==0: return 1

  if i==0:
    if X>N or X%2==1: return 0
    return comb(N, X)
  
  if X in memo[i]: return memo[i][X]

  retval = 0
  v = 1<<i
  for n in range(0, N, 2):
    R = X-v*n
    if R<0: break
    retval += comb(N, n) * dfs(i-1, R) % mod
    retval %= mod

  memo[i][X] = retval
  return retval

print(dfs(11, M))
