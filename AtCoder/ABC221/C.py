N = input()
M = len(N)

ans = 0

for i in range(1 << M):
  A = []
  B = []
  for j, c in enumerate(N):
    if (i >> j) & 1:
      A.append(c)
    else:
      B.append(c)

  A = sorted(A, reverse=True)
  B = sorted(B, reverse=True)

  if len(A) == 0 or len(B) == 0 or A[0] == '0' or B[0] == '0': continue

  nA = int(''.join(A))
  nB = int(''.join(B))
  ans = max(ans, nA * nB)

print(ans)
