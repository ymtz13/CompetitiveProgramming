H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(r) for r in zip(*A)]

for r in B:
  print(' '.join(map(str, r)))
