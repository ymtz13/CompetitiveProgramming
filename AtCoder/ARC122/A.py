N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

if N==1:
  print(A[0] % mod)
  exit()

vP = A[0] + A[1]
nP = 1
vN = A[0] - A[1]
nN = 1

for a in A[2:]:
  vP_next = vP + vN + (nP+nN)*a
  vN_next = vP - nP*a
  vP = vP_next % mod
  vN = vN_next % mod
  nP, nN = (nP+nN) % mod, nP

print((vP + vN) % mod)
