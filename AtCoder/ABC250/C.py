N, Q = map(int, input().split())

A = list(range(N + 1))
B = list(range(N + 1))

for _ in range(Q):
  x = int(input())

  i = B[x]
  j = i + 1 if i < N else i - 1

  y = A[j]

  A[i] = y
  A[j] = x
  B[x] = j
  B[y] = i

print(' '.join(map(str, A[1:])))
