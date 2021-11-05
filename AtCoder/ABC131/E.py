N, K = map(int, input().split())
if K > (N - 2) * (N - 1) // 2:
  print(-1)
  exit()

k = (N - 1) * (N - 2) // 2
ans = []
for i in range(1, N):
  ans.append((i, N))

for i in range(1, N):
  for j in range(i + 1, N):
    if k == K: continue
    ans.append((i, j))
    k -= 1

print(len(ans))
for i, j in ans:
  print(i, j)
