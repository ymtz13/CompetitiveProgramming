mod = 998244353

T = int(input())
ans = []

for _ in range(T):
  N = int(input())

  if N == 2:
    ans.append(1)
    continue

  a = pow(2, N - 2, mod) - 1 - (N - 3)
  ans.append(a % mod)

for a in ans:
  print(a)
