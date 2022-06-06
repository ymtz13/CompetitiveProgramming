N, W = map(int, input().split())
A = list(map(int, input().split())) + [0, 0]

ans = [0] * (W + 1)
for i in range(N + 2):
  for j in range(i + 1, N + 2):
    for k in range(j + 1, N + 2):
      s = A[i] + A[j] + A[k]
      if s <= W: ans[s] = 1

print(sum(ans))
