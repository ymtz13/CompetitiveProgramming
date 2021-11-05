from heapq import heappop, heappush

R, C = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(R)]
B = [tuple(map(int, input().split())) for _ in range(R-1)]

INF = 10**20
queue = [0]
P = 250000
Q = 500
D = [[INF]*C for _ in range(R)]
X = [[False]*C for _ in range(R)]

while not X[R-1][C-1]:
  q = heappop(queue)
  d = q//P
  r = (q%P)//Q
  c = q%Q
  if X[r][c]: continue
  D[r][c] = d
  X[r][c] = True

  if c < C-1:
    dd = d + A[r][c]
    if dd < D[r][c+1]:
      D[r][c+1] = dd
      heappush(queue, dd*P + r*Q + (c+1))
  
  if c > 0:
    dd = d + A[r][c-1]
    if dd < D[r][c-1]:
      D[r][c-1] = dd
      heappush(queue, dd*P + r*Q + (c-1))
  
  if r < R-1:
    dd = d + B[r][c]
    if dd < D[r+1][c]:
      D[r+1][c] = dd
      heappush(queue, dd*P + (r+1)*Q + c)
  
  for h in range(r):
    dd = d + r - h + 1
    if dd < D[h][c]:
      D[h][c] = dd
      heappush(queue, dd*P + h*Q + c)

print(D[R-1][C-1])
