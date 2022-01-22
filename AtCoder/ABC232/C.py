from itertools import permutations

N, M = map(int, input().split())
E1 = [[False] * N for _ in range(N)]
E2 = [[False] * N for _ in range(N)]

for _ in range(M):
  A, B = map(int, input().split())
  E1[A - 1][B - 1] = E1[B - 1][A - 1] = True

for _ in range(M):
  A, B = map(int, input().split())
  E2[A - 1][B - 1] = E2[B - 1][A - 1] = True


for P in permutations(tuple(range(N))):
  ok = True
  for i in range(N):
    for j in range(N):
      if E1[i][j] != E2[P[i]][P[j]]:
        ok = False
  
  if ok:
    print('Yes')
    exit()

print('No')
