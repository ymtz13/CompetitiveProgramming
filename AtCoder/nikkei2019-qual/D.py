N, M = map(int, input().split())
E = [[] for _ in range(N)]
R = [True]*N
for _ in range(N-1+M):
    A, B = map(int, input().split())
    E[A-1].append(B-1)
    R[B-1] = False

for i in range(N):
    if R[i]: root = i
    
ans = [-1]*N

memo = [0]*N
def dfs(i):
    if memo[i]>0: return memo[i]
    if len(E[i])==0: return 0

    m = -1
    for e in E[i]:
        v = dfs(e)
        m = max(m, v)

    for e in E[i]:
        if ans[e]<0: ans[e]=i

    memo[i] = m+1
    return m+1

dfs(root)

for a in ans:
    print(a+1)
