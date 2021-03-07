from collections import deque

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A-1].append(B-1)
  E[B-1].append(A-1)

M = []

K = int(input())
C = list(map(int, input().split()))

for s in range(K):
  V = [-1]*N
  queue = deque([(C[s]-1, 0)])
  while queue:
    q, d = queue.popleft()
    #print(s, q, d)
    if V[q]!=-1: continue
    V[q] = d

    for e in E[q]:
      if V[e]==-1: queue.append((e, d+1))

  M.append([V[c-1] for c in C])

for c1 in range(K):
  for c2 in range(K):
    if M[c1][c2]==-1:
      print(-1)
      exit()

memo = [0]*1000000

def dfs(B, x):
  key = B*K + x
  if memo[key]: return memo[key]

  B_ = B-(1<<x)
  MR = M[x]

  X = []
  for i in range(K):
    b = 1<<i
    if i==x or not B&b: continue
    X.append(dfs(B_, i) + MR[i])
  
  retval = min(X) if X else 0
  memo[key] = retval
  return retval

L = [dfs((1<<K)-1, x) for x in range(K)]
print(min(L)+1)
