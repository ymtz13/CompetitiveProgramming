from itertools import permutations
from collections import defaultdict

N = 3
ans = 0
X = defaultdict(list)
for p in permutations(range(N * 2)):
  D = [None] * N
  cA = cB = 0
  ok = True
  z = []
  for v in p:
    if D[v // 2] is None:
      D[v // 2] = cA
      cA += 1
      z.append(v)

    else:
      if D[v // 2] != cB:
        ok = False
        break
      cB += 1
  
  if ok:
    ans += 1
    X[tuple(z)].append(p)
  if not ok:
    print([v + 1 for v in p])

print(ans)
print(X)
for k, v in X.items():
  print(k, v)