N, M = map(int, input().split())
S = set()
for _ in range(M):
  X = tuple(map(int, input().split()))[1:]
  for x in X:
    for y in X:
      if x < y: S.add((x, y))

print('Yes' if len(S) == N * (N - 1) // 2 else 'No')
