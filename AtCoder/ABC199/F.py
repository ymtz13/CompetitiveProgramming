mod = 10**9 + 7

N, M, K = map(int, input().split())
A = list(map(int, input().split()))

inv2M = pow(2 * M, mod - 2, mod)

Z = [[0] * N for _ in range(N)]
D = [0] * N
for _ in range(M):
  X, Y = map(int, input().split())
  X -= 1
  Y -= 1

  Z[X][Y] = Z[Y][X] = inv2M
  D[X] += 1
  D[Y] += 1

for i in range(N):
  Z[i][i] = (1 - D[i] * inv2M) % mod


def inner(v1, v2):
  ret = 0
  for x1, x2 in zip(v1, v2):
    ret += x1 * x2
    ret %= mod
  return ret


def matsq(Z):
  ret = [[None] * N for _ in range(N)]
  for i, zi in enumerate(Z):
    for j, zj in enumerate(Z[i:], i):
      ret[i][j] = ret[j][i] = inner(zi, zj)
  return ret


def multiply(Z, v):
  return [inner(z, v) for z in Z]


for i in range(32):
  if K & (1 << i):
    A = multiply(Z, A)
  Z = matsq(Z)

for a in A:
  print(a)