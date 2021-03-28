N = int(input())
F = [f-1 for f in map(int, input().split())]

V = [None]*N
M = 0
for st in range(N):
  if V[st]: continue
  x = st

  while True:
    if V[x] is not None:
      if V[x] == st: M += 1
      break

    V[x] = st
    x = F[x]

mod = 998244353
print((pow(2, M, mod) - 1)%mod)
