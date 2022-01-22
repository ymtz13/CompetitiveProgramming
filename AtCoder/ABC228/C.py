N, K = map(int, input().split())
P = [sum(map(int, input().split())) for _ in range(N)]

T = sorted(P, reverse=True)[K - 1]

for i, p in enumerate(P, 1):
  print('Yes' if p + 300 >= T else 'No')
