import sys
sys.setrecursionlimit(1000000)

N = int(input())
C = list(map(int, input().split()))
E = [[] for _ in range(N)]
for _ in range(N-1):
  a, b = map(int, input().split())
  E[a-1].append(b-1)
  E[b-1].append(a-1)

U = [0]*100001

ans = []
def dfs(i, p):
  c = C[i]
  if U[c]==0:
    ans.append(i + 1)
  
  U[c] += 1
  for e in E[i]:
    if e==p: continue
    dfs(e, i)
  U[c] -= 1

dfs(0, None)

for a in sorted(ans):
  print(a)
