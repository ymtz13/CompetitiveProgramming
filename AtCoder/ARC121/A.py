N = int(input())
P = [(n, ) +tuple(map(int, input().split())) for n in range(N)]

Px = sorted(P, key=lambda p: p[1])
Py = sorted(P, key=lambda p: p[2])

#print(Px)
#print(Py)

X = []
for p in Px[:2] + Px[-2:] + Py[:2] + Py[-2:]:
  if p not in X: X.append(p)

#print(X)
D = []
for i, (_, x1, y1) in enumerate(X):
  for _, x2, y2 in X[i+1:]:
    d = max(abs(x1-x2), abs(y1-y2))
    D.append(d)

#print(D)
print(sorted(D)[-2])
