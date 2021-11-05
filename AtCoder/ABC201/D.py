H, W = map(int, input().split())
A = [[+1 if c=='+' else -1 for c in input()] for _ in range(H)]
X = [[0]*W for _ in range(H)]
A[0][0] = 0

p = (H+W)%2*2-1
X[H-1][W-1] = p * A[H-1][W-1]

for h in range(H-2, -1, -1):
  p = (h+W-1)%2*2-1
  X[h][W-1] = p * A[h][W-1] + X[h+1][W-1]

for w in range(W-2, -1, -1):
  p = (H-1+w)%2*2-1
  X[H-1][w] = p * A[H-1][w] + X[H-1][w+1]

for h in range(H-2, -1, -1):
  for w in range(W-2, -1, -1):
    p = (h+w)%2*2-1
    if p==+1:
      X[h][w] = +A[h][w] + min(X[h+1][w], X[h][w+1])

    else:
      X[h][w] = -A[h][w] + max(X[h+1][w], X[h][w+1])

print('Takahashi' if X[0][0]>0 else 'Aoki' if X[0][0]<0 else 'Draw' )
