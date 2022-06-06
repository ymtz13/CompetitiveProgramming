N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
B = [None] * (M + 1)

for ib in range(M, -1, -1):
  ic = N + ib

  S = C[ic]
  for ia in range(max(ic - M, 0), ic - ib):
    S -= A[ia] * B[ic - ia]

  B[ib] = S // A[ic - ib]

print(' '.join(map(str, B)))
