H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
ans = 0
for h in range(H-1):
  for w in range(W-1):
    d = B[h][w] - A[h][w]
    ans += abs(d)
    A[h  ][w  ] += d
    A[h  ][w+1] += d
    A[h+1][w  ] += d
    A[h+1][w+1] += d

ch = [A[h][-1]==B[h][-1] for h in range(H)]
cw = [A[-1][w]==B[-1][w] for w in range(W)]
if all(ch) and all(cw):
  print('Yes')
  print(ans)
else:
  print('No')
