from collections import deque

N, x = map(int, input().split())
M = 2 * N - 1

if x == 1 or x == M:
  print('No')
  exit()

print('Yes')

ans = [None] * M
used = [False] * (M + 1)

if x == 2:
  ans[N - 1] = 2
  ans[N] = 1
  used[1] = used[2] = True

elif x == M - 1:
  ans[N - 1] = M - 1
  ans[N] = M
  used[M - 1] = used[M] = True

else:
  ans[N - 1] = x
  ans[N - 2] = x - 1
  ans[N - 3] = x + 1
  ans[N] = x + 2
  ans[N + 1] = x - 2
  for i in range(-2, 3):
    used[x + i] = True

queue = deque([i for i, u in enumerate(used[1:], 1) if not u])

for i in range(M):
  if ans[i] is None:
    ans[i] = queue.popleft()

for a in ans:
  print(a)