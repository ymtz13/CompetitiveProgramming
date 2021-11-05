from collections import defaultdict

N, M = map(int, input().split())
Z = 200501

mod = 998244353

S = [None]*Z
P = []
for p in range(2, Z):
  if S[p] is None:
    P.append(p)
    for j in range(p, Z, p): S[j] = p

def f(x):
  D = defaultdict(int)
  while True:
    p = S[x]
    if p is None: break
    D[p] += 1
    x//=p
  return D

F = [1]*Z
p = 1
for x in range(1, Z):
  F[x] = p = p*x % mod

iF = [1]*Z
iF[Z-1] = p = pow(F[-1], mod-2, mod)
for x in range(Z-2, -1, -1):
  iF[x] = p = p*(x+1)%mod

ans = 1
for AN in range(2, M+1):
  D = f(AN)
  x = 1
  for v in D.values():
    x = x * F[N-1+v] * iF[N-1] * iF[v] % mod
  ans = (ans + x) % mod

print(ans)