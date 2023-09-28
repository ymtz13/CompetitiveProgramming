W, H = map(int, input().split())
M = [[1] * (W + 1) for _ in range(H + 1)]
N = int(input())

for w in range(W + 1):
  M[0][w] = 0
for h in range(H + 1):
  M[h][0] = 0

for _ in range(N):
  w, h = map(int, input().split())
  M[h][w] = 0

X = [[0] * (W + 1) for _ in range(H + 1)]
X[0][1] = 1

for h in range(1, H + 1):
  for w in range(1, W + 1):
    X[h][w] = (X[h - 1][w] + X[h][w - 1]) * M[h][w]

print(X[-1][-1])
