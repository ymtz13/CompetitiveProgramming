N, Q = map(int, input().split())
P = [None, 0] + list(map(int, input().split()))

C = [0] * (N + 1)
for p in P[1:]:
  C[p] += 1

ans = []
for _ in range(Q):
  V = set(tuple(map(int, input().split()))[1:])

  a = 0
  for v in V:
    if P[v] in V:
      a += C[v] - 1
    else:
      a += C[v] + 1

  ans.append(a)

for a in ans:
  print(a)
