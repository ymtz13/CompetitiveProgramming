X, Y = map(int, input().split('/'))

# N+1/2 - M/N = X/Y
# N = X/Y + 2M/N - 1
# M = N(N+1)/2 -N*X/Y

ans = []
N0 = 2 * X // Y - 1
for N in range(N0, N0 + 5):
  if N * X % Y > 0: continue
  M = N * (N + 1) // 2 - N * X // Y

  if 1 <= M and M <= N: ans.append((N, M))

for N, M in ans:
  print(N, M)

if len(ans) == 0:
  print('Impossible')
