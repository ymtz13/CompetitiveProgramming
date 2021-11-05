N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A-1].append(B-1)
  E[B-1].append(A-1)

ans1 = []
visited = [False]*N
p = 0
while p is not None:
  ans1.append(p+1)
  visited[p] = True
  
  q = None
  for e in E[p]:
    if not visited[e]:
      q = e
      break
  
  p = q

ans2 = []
p = 0
while p is not None:
  ans2.append(p+1)
  visited[p] = True
  
  q = None
  for e in E[p]:
    if not visited[e]:
      q = e
      break
  
  p = q

  
print(len(ans1 + ans2) - 1)
print(' '.join(map(str, ans1[::-1] + ans2[1:])))
