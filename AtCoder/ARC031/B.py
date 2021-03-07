from collections import deque

A = [input() for _ in range(10)]
X = [[0]*10 for _ in range(10)]

x = 0
for i in range(10):
  for j in range(10):
    if X[i][j] != 0 or A[i][j]=='x': continue
    x += 1

    queue = deque([(i, j)])
    while queue:
      pi, pj = queue.popleft()
      if X[pi][pj]!=0 or A[pi][pj]=='x': continue
      X[pi][pj] = x

      if pi>0: queue.append((pi-1, pj  ))
      if pi<9: queue.append((pi+1, pj  ))
      if pj>0: queue.append((pi  , pj-1))
      if pj<9: queue.append((pi  , pj+1))

ans = 'NO'

for i in range(10):
  for j in range(10):
    if A[i][j]=='o': continue

    n = []
    if i>0: n.append(X[i-1][j])
    if i<9: n.append(X[i+1][j])
    if j>0: n.append(X[i][j-1])
    if j<9: n.append(X[i][j+1])

    if len(set(n)-{0})==x: ans = 'YES'

print(ans)




