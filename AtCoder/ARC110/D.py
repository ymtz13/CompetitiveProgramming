N, M = map(int, input().split())
A = list(map(int, input().split()))

mod = 10**9+7

X = M + N
Y = N + sum(A)
ans = 1
for p in range(Y):
  ans = ans * (X-p) % mod
  ans = ans * pow(p+1, mod-2, mod) % mod

print(ans)