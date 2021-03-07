from collections import deque

H, W = map(int, input().split())
A = [input() for _ in range(H)]

T = [[] for _ in range(26)]
INF = 1000000000
orda = ord('a')

dist = [[-1]*W for _ in range(H)]

for h, row in enumerate(A):
  for w, a in enumerate(row):
    if a=='S': st = (h, w)
    if a=='G': gl = (h, w)
    if a=='#': dist[h][w] = INF
    if 'a' <= a: T[ord(a) - orda].append((h, w))

queue = deque([(st, 0)])
while queue:
  (h, w), d = queue.popleft()
  if h<0 or w<0 or h>=H or w>=W: continue
  if dist[h][w] >=0: continue

  dist[h][w] = d

  queue.append(((h-1, w  ), d+1))
  queue.append(((h+1, w  ), d+1))
  queue.append(((h  , w-1), d+1))
  queue.append(((h  , w+1), d+1))

  a = A[h][w]
  if 'a' <= a:
    ia = ord(a) - orda
    t = T[ia]
    for thw in t:
      queue.append((thw, d+1))
    T[ia] = []

gh, gw = gl
print(dist[gh][gw])
