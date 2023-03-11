N, x, y = map(int, input().split())
A = tuple(map(int, input().split()))

x -= A[0]
A0 = A[2::2]
A1 = A[1::2]

M = 10020
offset = M // 2

dp0 = [0] * M
dp0[sum(A0) + offset] = 1
for a in A0:
  for i, v in enumerate(dp0):
    if not v: continue
    dp0[i - a * 2] = 1

dp1 = [0] * M
dp1[sum(A1) + offset] = 1
for a in A1:
  for i, v in enumerate(dp1):
    if not v: continue
    dp1[i - a * 2] = 1

ix = x + offset
iy = y + offset
if ix < 0 or ix >= M or iy < 0 or iy >= M:
  print('No')
  exit()

print('Yes' if dp0[ix] and dp1[iy] else 'No')
