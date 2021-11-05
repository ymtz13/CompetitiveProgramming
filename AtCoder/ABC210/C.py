from collections import defaultdict

N, K = map(int, input().split())
C = list(map(int, input().split()))
S = set()
D = defaultdict(int)
for c in C[:K-1]:
  S.add(c)
  D[c] += 1

ans = 0
for i, c in enumerate(C[K-1:]):
  S.add(c)
  D[c] += 1
  ans = max(ans, len(S))

  x = C[i]
  D[x] -= 1
  if D[x]==0: S.remove(x)
print(ans)
