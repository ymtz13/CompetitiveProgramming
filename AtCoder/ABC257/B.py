N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

P = [None] * (N + 1)
for i, a in enumerate(A):
  P[a] = i

for l in L:
  l -= 1
  a = A[l]

  if a == N or P[a + 1] is not None: continue
  A[l] = a + 1
  P[a], P[a + 1] = None, P[a]

print(' '.join(map(str, A)))