N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = [A[i+1]-A[i] for i in range(N-1)]
S = sum(map(abs, B))

for _ in range(Q):
  L, R, V = map(int, input().split())

  if L>1:
    l = L-2
    S -= abs(B[l])
    B[l] += V
    S += abs(B[l])

  if R<N:
    r = R-1
    S -= abs(B[r])
    B[r] -= V
    S += abs(B[r])

  print(S)
