N, M = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(M)]
S = input()

C = S.count('"') // 2

A = S[C:].split('"')
T = [0] * (C + 1)

a0 = A[0]
if a0[-1] == 'w':
  T[0] = 1
  a0 = a0[:-1]

X = [0] * (N + 1)
X[int(a0[5:])] = 1

for i, a in enumerate(A[1:], 1):
  if a == 'ww': T[i] = 1

for t in T:
  if t:
    Xnext = [0] * (N + 1)
    for a, b in E:
      if X[b]: Xnext[a] = 1
    
  else:
    Xnext = [X[1:].count(1)] * (N + 1)
    for a, b in E:
      if X[b]: Xnext[a] -= 1
    
    Xnext = [1 if x else 0 for x in Xnext]

  X = Xnext

print(sum(X[1:]))
