H, W, N = map(int, input().split())
B = [[] for _ in range(W)]
for _ in range(N):
  X, Y = map(int, input().split())
  B[Y - 1].append(X - 1)

for b in B:
  b.sort()

PX = [0]
px = 0
for py in range(W - 1):
  px += 1
  for bx in B[py + 1]:
    if bx < px: continue
    if bx == px: px += 1
  PX.append(px)

ans = H
for px, b in zip(PX, B):
  for bx in b:
    if bx < px: continue
    ans = min(ans, bx)


print(ans)