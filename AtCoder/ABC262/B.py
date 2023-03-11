N, M = map(int, input().split())
E = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
  U, V = map(int, input().split())
  E[U][V] = E[V][U] = 1

ans = 0
for i in range(1, N + 1):
  for j in range(i + 1, N + 1):
    for k in range(j + 1, N + 1):
      if E[i][j] and E[j][k] and E[k][i]: ans += 1

print(ans)
