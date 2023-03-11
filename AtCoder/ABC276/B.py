N, M = map(int, input().split())
E = [[] for _ in range(N + 1)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A].append(B)
  E[B].append(A)

for e in E[1:]:
  print(len(e), *sorted(e))
