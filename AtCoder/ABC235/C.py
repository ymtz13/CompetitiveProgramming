from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))

D = defaultdict(list)
for i, a in enumerate(A):
  D[a].append(i + 1)

for _ in range(Q):
  x, k = map(int, input().split())
  if len(D[x]) >= k:
    print(D[x][k - 1])
  else:
    print(-1)
