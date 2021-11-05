from heapq import heappush, heappop

def g(t, d):
  R = d**0.5 - t - 1
  if R<0: return d//(t+1)

  return min([r + d//(t+r+1) for r in range(int(R)-1, int(R)+2) if t+r+1>0])


def f(t, d):
  if t>d: return 0
  P0 = 0
  P3 = d-t+1
  width = P3 - P0
  while width>=3:
    w = width//3
    P1 = P0 + w
    P2 = P0 + w*2

    f1 = P1 + d//(t+P1+1)
    f2 = P2 + d//(t+P2+1)
    #print('P0, P1, P2, P3 = ', P0, P1, P2, P3, 'f1, f2 = ', f1, f2)

    if f1<f2: P3 = P2
    else:     P0 = P1

    width = P3-P0
  
  #print('P0, P1, P2, P3 = ', P0, P1, P2, P3)
  #for P in range(P0, P0+3):
  #  print(P, P+d//(t+P+1))
  #print('retval = ', min([P + d//(t+P+1) for P in range(P0, P0+3)]))

  return min([P + d//(t+P+1) for P in range(P0, P0+3)])

#print('f', f(0, 3))
#exit()

N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  A, B, C, D = map(int, input().split())
  E[A-1].append((B-1, C, D))
  E[B-1].append((A-1, C, D))

queue = [(0, 0)]
time = [None]*N
while queue:
  t, q = heappop(queue)
  if time[q] is not None: continue
  time[q] = t
  #print('visit ', q, '  time ', t, queue)

  for e, c, d in E[q]:
    if time[e] is not None: continue
    heappush(queue, (t + c + g(t, d), e))

print(time[N-1] if time[N-1] is not None else -1)
