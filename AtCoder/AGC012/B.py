N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  a, b = map(int, input().split())
  E[a - 1].append(b - 1)
  E[b - 1].append(a - 1)

Q = int(input())
P = [[-1] * 11 for _ in range(N)]
C = 1 << 20
for q in range(Q):
  v, d, c = map(int, input().split())
  P[v - 1][d] = q * C + c

for d0 in range(1, 11):
  Pnext = [Pi[:] for Pi in P]

  for i in range(N):
    Pi = P[i]
    for e in E[i]:
      Pe = Pnext[e]
      for d, (pi, pe) in enumerate(zip(Pi[d0:], Pe[d0:]), d0):
        Pe[d] = max(pi, pe)

  P = Pnext

for i in range(N):
  m = -1
  ans = 0
  for p in P[i]:
    if p > m:
      m = p
      ans = p % C
  print(ans)
