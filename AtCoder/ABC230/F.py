from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

mod = 998244353

dp0 = [1]
dp1 = [0]
s = 0
D = defaultdict(int)
for i, a in enumerate(A[:-1]):
  s += a
  v0 = (dp0[i] + dp1[i]) % mod
  v1 = (dp0[i] + dp1[i] - D[s]) % mod
  dp0.append(v0)
  dp1.append(v1)
  D[s] += v1
  D[s] %= mod

#print(dp0)
#print(dp1)
print((dp0[-1] + dp1[-1]) % mod)
