import sys

N, Q = list(map(int, input().split()))
sys.setrecursionlimit(N*10)

E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    E[a].append(b)
    E[b].append(a)

X = [0 for _ in range(N+1)]
for _ in range(Q):
    p, x = list(map(int, input().split()))
    X[p] += x

def dfs(child, parent):
    X[child] += X[parent]
    for e in E[child]:
        if e==parent: continue
        dfs(e, child)

dfs(1,0)
print(*X[1:])
