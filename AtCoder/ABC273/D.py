from collections import defaultdict
from bisect import bisect

H, W, rs, cs = map(int, input().split())
Br = defaultdict(list)
Bc = defaultdict(list)

N = int(input())
for _ in range(N):
  r, c = map(int, input().split())
  Br[r].append(c)
  Bc[c].append(r)

for b in Br.values():
  b.sort()
for b in Bc.values():
  b.sort()

Q = int(input())
ans = []
for _ in range(Q):
  d, l = input().split()
  l = int(l)

  if d == 'L':
    B = Br[rs]
    x = bisect(B, cs) - 1
    cb = B[x] if x >= 0 else 0
    cs = max(cb + 1, cs - l)

  if d == 'R':
    B = Br[rs]
    x = bisect(B, cs)
    cb = B[x] if x < len(B) else W + 1
    cs = min(cb - 1, cs + l)

  if d == 'U':
    B = Bc[cs]
    x = bisect(B, rs) - 1
    rb = B[x] if x >= 0 else 0
    rs = max(rb + 1, rs - l)

  if d == 'D':
    B = Bc[cs]
    x = bisect(B, rs)
    rb = B[x] if x < len(B) else H + 1
    rs = min(rb - 1, rs + l)

  ans.append((rs, cs))

for rs, cs in ans:
  print(rs, cs)
