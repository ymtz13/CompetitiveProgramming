N, M, K = map(int, input().split())

for n in range(N + 1):
  for m in range(M + 1):
    b = n * m + (N - n) * (M - m)
    if b == K:
      print('Yes')
      exit()

print('No')
