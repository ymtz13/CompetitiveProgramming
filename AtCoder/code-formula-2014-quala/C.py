N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [[0]*K for _ in range(N)]
C = set()

for k in range(K):
  B[k%N][k//N] = 1

for n in range(N):
  d = 0
  p = []
  for a, b in zip(A[n], B[n]):
    if b == 0: break
    if a in C: d += 1
    else: 
      p.append(a)
      C.add(a)

  while d>0:
    k += 1
    d -= 1
    t, u = k%N, k//N
    B[t][u] = 1
    if t <= n:
      a = A[t][u]
      if a in C: d += 1
      else:
        p.append(a)
        C.add(a)
  
  print(' '.join(map(str, sorted(p))))