N, K = map(int, input().split())
S = sorted([input() for _ in range(N)][:K])

for c in S:
  print(c)
