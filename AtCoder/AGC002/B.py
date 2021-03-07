N, M = map(int, input().split())
D = [1]*N
R = [0]*N
R[0] = 1

for _ in range(M):
  x, y = map(int, input().split())
  D[x-1] -= 1
  D[y-1] += 1
  if R[x-1]==1: R[y-1]=1
  if D[x-1]==0: R[x-1]=0

print(sum(R))
