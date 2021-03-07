from sys import setrecursionlimit
setrecursionlimit(1000000)

N, X = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N-1):
  x, y, c = map(int, input().split())
  E[x-1].append((y-1, c))
  E[y-1].append((x-1, c))

C = [None]*N

def dfs(i, s):
  C[i] = s

  for e, c in E[i]:
    if C[e] is not None: continue
    dfs(e, s^c)

dfs(0, 0)

D = {}
for c in C:
  if c not in D: D[c] = 0
  D[c] += 1

ans = 0
for k1, n1 in D.items():
  k2 = X^k1
  if k2 not in D: continue
  n2 = D[k2]
  if X>0:
    ans += n1*n2 
    D[k2] = 0
  else:
    ans += n1*(n1-1)//2
  

print(ans)