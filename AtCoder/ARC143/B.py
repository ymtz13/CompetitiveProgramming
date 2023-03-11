mod = 998244353

N = int(input())
if N == 1:
  print(0)
  exit()

F = [1]
for i in range(1, N * N + 10):
  F.append(F[-1] * i % mod)

ans = F[N * N]

for i in range(N * N):
  nm = i - 1
  np = N * N - i

  if nm < N - 1: continue
  if np < N - 1: continue

  Pm = F[nm] * pow(F[nm - N + 1], mod - 2, mod) % mod
  Pp = F[np] * pow(F[np - N + 1], mod - 2, mod) % mod

  ans -= Pm * Pp * F[(N - 1) * (N - 1)] * N * N
  ans %= mod

print(ans)
