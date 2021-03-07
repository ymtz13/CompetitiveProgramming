from sys import setrecursionlimit
setrecursionlimit(1000000)

N = int(input())
P = list(map(int, input().split()))
C = [[] for _ in range(N)]
for i, p in enumerate(P):
  C[p-1].append(i+1)

def dfs(i):
  if not C[i]: return 0, 1, True

  X = []
  q1 = 0
  q2 = 1
  r1 = r2 = 0
  for c in C[i]:
    p1, p2, swap = dfs(c)
    if swap:
      X.append((p2-p1, p1, p2))
    elif p1 > p2:
      q1 += p1
      q2 += p2
    else:
      r1 += p1
      r2 += p2

  X.sort()
  for j, (_, p1, p2) in enumerate(X):
    if j%2==0:
      q1 += p1
      q2 += p2
    else:
      q1 += p2
      q2 += p1
  
  if len(X)%2==0:
    q1 += r1
    q2 += r2
    swap = True
  else:
    q1 += r2
    q2 += r1
    swap = False

  return q1, q2, swap

print(dfs(0)[1])
