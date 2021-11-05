N, K = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N-1):
  u, v = map(int, input().split())
  E[u-1].append(v-1)
  E[v-1].append(u-1)

D = [-1]*N
r = 0
for v, e in enumerate(E):
  if len(e)==1:
    D[v] = 0
    if v==r: r += 1

def dfs(v, p):
  if D[v]==-1: D[v] = max([dfs(e, v) for e in E[v] if e!=p]) + 1
  return D[v]
print(r)
dfs(r, None)
#for d in range(1, N+1):
#  queue_new = []
#  for q in queue:
#    for e in E[q]:
#      print(q, e)
#      if D[e] == -1:
#        queue_new.append(e)
#        D[e] = d
#  queue = queue_new

print(D)

X = [0]*N
for d in D:
  X[d] += 1

print(X)

def chk(T):
  x = 0
  for d in range(T, N, 2*T):
    x += X[d]
  return x<=K

ng = 0
ok = N+1
while ok-ng>1:
  tgt = (ok + ng)//2
  if chk(tgt):
    ok = tgt
  else:
    ng = tgt

print(ok)
