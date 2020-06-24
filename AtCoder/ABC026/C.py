N = int(input())
S = [[] for _ in range(N)]
for i in range(1,N):
    B = int(input())
    S[B-1].append(i)

def dfs(i):
    if len(S[i])==0: return 1
    m = [dfs(s) for s in S[i]]
    return max(m)+min(m)+1

print(dfs(0))
