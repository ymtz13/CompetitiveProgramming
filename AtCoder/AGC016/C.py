H, W, h, w = map(int, input().split())

if H % h == 0 and W % w == 0:
  print('No')
  exit()

print('Yes')

T = W % w == 0
if T: H, W, h, w = W, H, w, h

n = W // w
A = [n + 1] * W
for i in range(n):
  A[i * w + w - 1] = -(n + 1) * (w - 1) - 1

if T:
  for a in A:
    print(' '.join([str(a)] * H))

else:
  for _ in range(H):
    print(' '.join(map(str, A)))
