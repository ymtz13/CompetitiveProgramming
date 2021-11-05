H, W = map(int, input().split())
S = [input() for _ in range(H)]
mod = 998244353

ans = 1
for w in range(W):
  R = B = D = False
  for h in range(min(H, w+1)):
    c = S[h][w-h]
    if c == 'R': R = True
    if c == 'B': B = True
    if c == '.': D = True
  if R and B: ans = 0
  if not R and not B and D: ans = ans * 2 % mod

for h in range(1, H):
  R = B = D = False
  w = W-1
  while w >= 0 and h<H:
    c = S[h][w]
    if c == 'R': R = True
    if c == 'B': B = True
    if c == '.': D = True
    h+=1
    w-=1
  if R and B: ans = 0
  if not R and not B and D: ans = ans * 2 % mod

print(ans)
