import numpy as np
from heapq import heappush, heappop

class Heap:
  def __init__(self):
    self.heap = []
  
  def push(self, item):
    heappush(self.heap, item)

  def pop(self):
    return heappop(self.heap)

C = int(input())
P = np.array([tuple(map(int, input().split())) for _ in range(50)])
N = np.array([[4]*50 for _ in range(50)])
N[ 0, :] -= 1
N[49, :] -= 1
N[ :, 0] -= 1
N[ :,49] -= 1

F = np.array([[False]*50 for _ in range(50)])
Q = Heap()

for i in range(49):
  Q.push((-P[  0,  i] + C * N[  0,  i],   0,   i))
  Q.push((-P[  i, 49] + C * N[  i, 49],   i,  49))
  Q.push((-P[1+i,  0] + C * N[1+i,  0], 1+i,   0))
  Q.push((-P[ 49,1+i] + C * N[ 49,1+i],  49, 1+i))

n = 2500
s = 0
S = []
H = []
while n>0:
  ss, x, y = Q.pop()
  if F[x,y]: continue
  F[x,y] = True
  n -= 1
  H.append((x, y))

  s += ss
  S.append(s)
  if x> 0:
    N[x-1, y] -= 1
    Q.push((-P[x-1, y] + C * N[x-1, y], x-1, y))
  if x<49:
    N[x+1, y] -= 1
    Q.push((-P[x+1, y] + C * N[x-1, y], x+1, y))
  if y> 0:
    N[x, y-1] -= 1
    Q.push((-P[x, y-1] + C * N[x, y-1], x, y-1))
  if y<49:
    N[x, y+1] -= 1
    Q.push((-P[x, y+1] + C * N[x, y+1], x, y+1))

print(S)
im = -1
m = 0
for i, s in enumerate(S):
  if s<m:
    im = i
    m = s

print(im+1)
for x, y in H[:im+1]:
  print(x, y)
