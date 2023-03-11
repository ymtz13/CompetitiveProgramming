from math import sqrt

P = []
M = 10**7
F = [None] * M
for m in range(2, M):
  if F[m] is None:
    P.append(m)
    for i in range(m, M, m):
      F[i] = m

T = int(input())
ans = []

for _ in range(T):
  N = int(input())

  for p in P:
    if N % p == 0: break

  p2 = p * p

  if N % p2 == 0:
    a = (p, N // p2)
  else:
    q = int(sqrt(N // p) + 0.1)
    a = (q, p)
  
  ans.append(a)

for a in ans:
  print(*a)
