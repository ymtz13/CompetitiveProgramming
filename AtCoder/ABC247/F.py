mod = 998244353

N = int(input())

v00, v01, v10, v11 = 1, 0, 0, 1
X = [1]
for _ in range(N + 10):
  v00, v01, v10, v11 = v01, (v00 + v01) % mod, v11, (v10 + v11) % mod
  X.append((v01 + v10 + v11) % mod)

P = list(map(int, input().split()))
Q = list(map(int, input().split()))

iQ = [None] * (N + 1)
for i, q in enumerate(Q):
  iQ[q] = i

E = [None] * N
for i, p in enumerate(P):
  E[i] = iQ[p]

U = [False] * N
ans = 1
for st in range(N):
  if U[st]: continue

  i = st
  cnt = 0
  while True:
    U[i] = True
    i = E[i]
    cnt += 1
    if i == st: break

  ans = ans * X[cnt - 1] % mod

print(ans)
