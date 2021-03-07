N, X = map(int, input().split())
H = list(map(int, input().split()))
E = [[] for _ in range(N)]
for _ in range(N-1):
  a, b = map(int, input().split())
  E[a-1].append(b-1)
  E[b-1].append(a-1)

V = [False]*N

def dfs(i):
  V[i] = True
  s = 0
  for e in E[i]:
    if V[e]: continue
    n, f = dfs(e)
    if f: s += n + 2
  
  return s, s>0 or H[i]==1

print(dfs(X-1)[0])
