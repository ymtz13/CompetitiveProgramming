H, W = map(int, input().split())
A = [input() for _ in range(H)]

sa = sb = 0
Q = int(input())
for i in range(Q):
  a, b = map(int, input().split())
  if i % 2 == 0:
    sa -= a
    sb -= b
  else:
    sa += a
    sb += b

sa %= H
sb %= W

XH = list(range(H)) * 2
XW = list(range(W)) * 2

XH = XH[H - sa:H * 2 - sa]
XW = XW[W - sb:W * 2 - sb]

if Q % 2 == 1:
  XH = XH[::-1]
  XW = XW[::-1]

ans = [[None] * W for _ in range(H)]

for h, xh in enumerate(XH):
  for w, xw in enumerate(XW):
    ans[h][w] = A[xh][xw]

for row in ans:
  print(''.join(row))
