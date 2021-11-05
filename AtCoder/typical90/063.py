from collections import defaultdict

H, W = map(int, input().split())
P = [[None]*H for _ in range(W)]
for h in range(H):
  for w, p in enumerate(map(int, input().split())):
    P[w][h] = p

ans = 0
for x in range(1, 1<<H):
  mask = [(x>>h)&1 for h in range(H)]
  cnt = sum(mask)

  D = defaultdict(int)
  for w, Pw in enumerate(P):
    q = None
    for p, m in zip(Pw, mask):
      if m==0: continue
      if q is None: q = p
      if q != p: 
        q = None
        break
    if q is not None: D[q] += 1
  #print('{:08b} {} {}'.format(x, cnt, D))
  ans = max(ans, cnt*max(list(D.values()) + [0]))

print(ans)
