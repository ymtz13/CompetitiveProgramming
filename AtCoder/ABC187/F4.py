N, M = map(int, input().split())
E = [1 << i for i in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A - 1] ^= 1 << (B - 1)
  E[B - 1] ^= 1 << (A - 1)

for i in range(N):
  X = [(1 << i) + 0 + (E[i] << 40)]
  for j in range(i):
    e = E[j]
    em = (E[j] << 40) + (1 << 40) - 1
    bp = (1 << j)
    bq = (1 << j) << 20
    br = (1 << j) << 40
    for x in X[:]:
      if x & br:
        X.append((x | bp) & em)

      X.append(x | bq)

  #print('[{}]'.format(i))
  #for p, q, r in zip(P, Q, R):
  #  print('{:018b}'.format(p))
  #  print('{:018b}'.format(q))
  #  print('{:018b}'.format(r))
  #  print()

dp = [20] * (1 << 20)
dp[0] = 0