from sys import setrecursionlimit
setrecursionlimit(10**6)

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N-1):
  A, B = map(int, input().split())
  E[A-1].append(B-1)
  E[B-1].append(A-1)

ans = 0
def dfs(i, p):
  global ans
  D = [0, 0]
  for c in E[i]:
    if c==p: continue
    D.append(dfs(c, i) + 1)
  
  D = sorted(D, reverse=True)
  ans = max(ans, sum(D[:2]))

  return  D[0]

dfs(0, None)

print(ans + 1)
