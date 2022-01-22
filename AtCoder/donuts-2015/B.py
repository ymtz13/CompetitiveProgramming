N, M = map(int, input().split())
A = list(map(int, input().split()))
BCI = [tuple(map(int, input().split())) for _ in range(M)]

ans = 0
for b in range(1 << N):
  X = []
  v = 0
  for i, a in enumerate(A):
    if (b >> i) & 1:
      X.append(i + 1)
      v += a
  X = set(X)

  if len(X) != 9: continue

  for B, C, *I in BCI:
    I = set(I)
    if len(I & X) >= 3:
      v += B

  ans = max(ans, v)

print(ans)
