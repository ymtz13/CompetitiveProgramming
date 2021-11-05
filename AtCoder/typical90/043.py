from heapq import heappop, heappush

H, W = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())

S = [[False]*(W+2)] + [[False] + list(map(lambda c: c=='.', input())) + [False] for _ in range(H)] + [[False]*(W+2)]

M = 1002
M2 = M*M
M3 = M*M*4
D = [None]*4*M2

def zip(r, c, dir, d):
  return r + c*M + dir*M2 + d*M3

def unzip(z):
  r = z%M
  c = (z//M)%M
  dir = (z//M2)%4
  d = z//M3
  return r, c, dir, d

Dr = [0, 0, +1, -1]
Dc = [+1, -1, 0, 0]

queue = [zip(rs, cs, dir, 0) for dir in range(4)]
while queue:
  v = heappop(queue)
  if D[v%M3] is not None: continue

  r, c, dir, d = unzip(v)
  D[v%M3] = d

  for dd in range(4):
    if dd != dir: heappush(queue, zip(r, c, dd, d+1))

  dr = Dr[dir]
  dc = Dc[dir]
  if S[r+dr][c+dc]: heappush(queue, zip(r+dr, c+dc, dir, d))

print(min([D[rt + ct*M + dir*M2] for dir in range(4)]))
