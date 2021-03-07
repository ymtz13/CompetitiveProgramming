N, M = map(int, input().split())
X = list(range(N))[::-1]

for m in range(M):
  a = int(input())
  X[a-1] = N + m

for x, i in sorted([(-x, i+1) for i, x in enumerate(X)]):
  print(i)
