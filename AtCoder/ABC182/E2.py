H, W, N, M = map(int, input().split())
R = [[(0, 2), (W+1, 2)] for _ in range(H)]
C = [[(0, 2), (H+1, 2)] for _ in range(W)]
for n in range(N):
  h, w = map(int, input().split())
  R[h-1].append((w, 1))
  C[w-1].append((h, 1))
for m in range(M):
  h, w = map(int, input().split())
  R[h-1].append((w, 2))
  C[w-1].append((h, 2))


for r in R:
