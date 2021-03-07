import sys
sys.setrecursionlimit(2000)

N = int(input())
E = [[] for _ in range(N)]
for i in range(N-1):
    p = int(input())
    E[i+1].append(p)
    E[p].append(i+1)

K = [False]*N
ans = [None]*N
queue = []
def dfs(i):
    retval = 1
    a = 0
    K[i] = True
    for e in E[i]:
        if K[e]: continue
        d = dfs(e)
        a = max(a, d)
        retval += d
        
    ans[i] = max(a, N-retval)
    return retval

dfs(0)
print('\n'.join(map(str, ans)))
