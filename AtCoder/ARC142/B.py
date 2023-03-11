N = int(input())
X = [list(range(i * N + 1, (i + 1) * N + 1)) for i in range(N)]

ans = [None] * N
for i in range(N):
  if i % 2 == 0:
    ans[i] = X[i // 2]
  else:
    ans[i] = X[i // 2 + (N + 1) // 2]

for row in ans:
  print(' '.join(map(str, row)))
