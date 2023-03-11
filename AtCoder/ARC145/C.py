mod = 998244353

N = int(input())

F = [1]
for i in range(1, N + 10):
  F.append(F[-1] * i % mod)

print(pow(2, N, mod) * F[N] * F[N] % mod)
