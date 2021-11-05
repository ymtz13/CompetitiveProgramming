D = {'G': 0, 'C': 1, 'P': 2}

N, M = map(int, input().split())
A = [[D[a] for a in input()] for _ in range(2 * N)]

W = [0] * (2 * N)
R = list(range(2 * N))

for m in range(M):
  for i, j in zip(R[0::2], R[1::2]):
    ai = A[i][m]
    aj = A[j][m]

    if ai == aj: continue
    if (ai + 1) % 3 == aj:
      W[i] += 1
      continue
    W[j] += 1

  R = [i for _, i in sorted([(-w, i) for i, w in enumerate(W)])]

for r in R:
  print(r + 1)
