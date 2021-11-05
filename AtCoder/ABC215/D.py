N, M = map(int, input().split())
A = list(map(int, input().split()))

Z = 10**5 + 10
D = [[] for _ in range(Z)]

for x in range(2, Z):
  if D[x]: continue
  for i in range(x, Z, x):
    D[i].append(x)

C = [False] * Z
for a in A:
  for d in D[a]:
    C[d] = True

C = {i for i, c in enumerate(C) if c}

X = [True]*(M+1)
for c in C:
  for j in range(c, M+1, c):
    X[j] = False

ans = [i for i, x in enumerate(X[1:], 1) if x]
print(len(ans))
for a in ans:
  print(a)
