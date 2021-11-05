M = 101

P = [[[0] * M for _ in range(M)] for _ in range(M)]

for x in range(M):
  P[x][0][0] = pow(1 / 3, x)

  for y in range(M):
    if y > 0: P[x][y][0] = P[x][y - 1][0] / 3 * (x + y) / y

    for z in range(1, M):
      P[x][y][z] = P[x][y][z - 1] / 3 * (x + y + z) / z

C = [None] * M
C[0] = C[1] = 0

for n in range(2, M):
  prob_draw = 0
  e = 0
  s = 0

  for x in range(n + 1):
    for y in range(n - x + 1):
      z = n - x - y

      S = {x, y, z}

      prob = P[x][y][z]
      s += prob

      if n in S or len(S) == 1:
        prob_draw += prob
        continue

      if 0 in S: S.remove(0)
      e += C[min(S)] * prob

  #print(n, e, prob_draw)
  C[n] = (e + 1) / (1 - prob_draw)

print(C[int(input())])
