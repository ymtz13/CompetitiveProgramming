from collections import deque

N = int(input())
N2 = N * N

if N == 3:
  print(4, 5, 9)
  print(2, 7, 3)
  print(6, 8, 1)
  exit()

ans = [[None] * N for _ in range(N)]

if N % 2 == 0:
  O = list(range(1, N2 + 1, 2))
  E = list(range(N2 - 2, 0, -2)) + [N2]

  k = 0
  for i in range(N // 2 - 1, -1, -1):
    for j in range(N):
      ans[i][j] = E[k]
      k += 1

  k = 0
  for i in range(N // 2, N):
    for j in range(N):
      ans[i][j] = O[k]
      k += 1

else:
  Nh = N // 2
  ans[Nh][Nh] = 1
  ans[Nh][Nh - 1] = N2 - 1
  ans[Nh + 1][Nh + 1] = 5
  ans[Nh + 1][Nh] = N2 - 5
  ans[Nh + 2][Nh + 1] = 3
  ans[Nh + 2][Nh] = N2 - 3

  v = 5
  for i in range(Nh):
    v += 2
    ans[i][Nh] = v
    ans[i][Nh - 1] = N2 - v

  for i in range(Nh + 3, N):
    v += 2
    ans[i][Nh + 1] = v
    ans[i][Nh] = N2 - v

  E = deque(range(2, N2, 2))
  O = deque(range(N * 2 + 1, N2 + 1, 2))

  for i in range(N):
    for j in range(N):
      if ans[i][j] is not None: continue
      if j < Nh:
        v = E.popleft()
      else:
        v = O.popleft()
      ans[i][j] = v

for row in ans:
  print(' '.join(map(str, row)))
