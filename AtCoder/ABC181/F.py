N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

D2 = [[0]*N for _ in range(N)]
for i in range(N):
  xi, yi = P[i]
  for j in range(i+1, N):
    xj, yj = P[j]
    dx, dy = xj-xi, yj-yi
    d2 = dx*dx + dy*dy
    D2[i][j] = d2

def makeEdge(r):
  r2 = r*r
  E = [[] for _ in range(N)]
  for i in range(N):
    for j in range(i+1, N):
      if D2[i][j]>4*r2: continue
      E[i].append(j)
      E[j].append(i)
  return E

def check(r):
  queue = [i for i, (x, y) in enumerate(P) if 100-y<r*2]
  iq = 0
  used = [False]*N
  E = makeEdge(r)
  ok = True

  while iq<len(queue):
    q = queue[iq]
    iq += 1

    if used[q]: continue
    used[q] = True

    if P[q][1]+100<r*2:
      ok = False
      break

    for e in E[q]: queue.append(e)

  return ok

max_ok = 0
min_ng = 100
while min_ng-max_ok>0.000001:
  tgt = (max_ok+min_ng)/2
  if check(tgt):
    max_ok = tgt
  else:
    min_ng = tgt

print(max_ok)
