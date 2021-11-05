N = int(input())
A = sorted(list(map(int, input().split())))
mod = 998244353
inv2 = pow(2, mod-2, mod)

S = 0
r = 1
for a in A[1:]:
  S += a * r 
  S %= mod
  r = r*2 % mod

ans = 0
for i, a in enumerate(A):
  ans += a*a
  if i==N-1: break
  ans += a*S
  ans %= mod
  S -= A[i+1]
  S *= inv2
  S %= mod

print(ans % mod)