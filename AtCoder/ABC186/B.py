H, W = map(int, input().split())
A = []
for _ in range(H):
  A += list(map(int, input().split()))

M = min(A)
S = sum(A)
print(S - M*H*W)