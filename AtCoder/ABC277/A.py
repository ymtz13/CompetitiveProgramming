N, X = map(int, input().split())
P = list(map(int, input().split()))

for k, p in enumerate(P, 1):
  if p == X: print(k)
