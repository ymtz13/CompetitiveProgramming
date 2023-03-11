mod = 998244353

N, M, K = map(int, input().split())

F = [1]
for i in range(1, N + 20):
  F.append(F[-1] * i % mod)


def comb(P, Q):
  return F[P] * pow(F[P - Q], mod - 2, mod) * pow(F[Q], mod - 2, mod) % mod


C = [0] * N
for _ in range(M):
  U, V = map(int, input().split())
  C[U - 1] += 1
  C[V - 1] += 1

n0 = n1 = 0
for c in C:
  if c % 2 == 0: n0 += 1
  if c % 2 == 1: n1 += 1

ans = 0
for x1 in range(0, K + 1, 2):
  x0 = K - x1
  if x0 > n0 or x1 > n1: continue

  ans += comb(n0, x0) * comb(n1, x1)
  ans %= mod

print(ans)
