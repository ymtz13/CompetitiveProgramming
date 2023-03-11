from collections import defaultdict

N = int(input())

D = defaultdict(list)
E = defaultdict(int)

for i in range(N):
  m = int(input())
  for _ in range(m):
    p, e = map(int, input().split())
    if E[p] < e:
      E[p] = e
      D[p] = []

    if E[p] == e:
      D[p].append(i)

X = [False] * N
for d in D.values():
  if len(d) > 1: continue
  for i in d:
    X[i] = True

cnt = X.count(True)
print(min(cnt + 1, N))
