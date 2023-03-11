mod = 998244353

N, A = map(int, input().split())

A2 = A * pow(100, mod - 2, mod) % mod
A1 = 1 - A2

X = [0] * (N + 2)
X[0] = 1

for i in range(N):
  X[i + 1] += X[i] * A1
  X[i + 1] %= mod

  X[i + 2] += X[i] * A2
  X[i + 2] %= mod

E = [0] * (N + 2)
E[1] = 1

for i in range(2, N + 1):
  P1 = X[i - 1] * A1 % mod
  P2 = X[i - 2] * A2 % mod

  S = (P1 + P2) % mod
  Sinv = pow(S, mod - 2, mod)

  E[i] += E[i - 1] * P1 * Sinv % mod
  E[i] += E[i - 2] * P2 * Sinv % mod
  E[i] += 1
  E[i] %= mod

E[N + 1] = E[N - 1] + 1

ans = E[N] * X[N] + E[N + 1] * X[N + 1]
ans %= mod

print(ans)
