N, M = map(int, input().split())
E = [1 << i for i in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A - 1] ^= 1 << (B - 1)
  E[B - 1] ^= 1 << (A - 1)

for i in range(N):
  #P = [1 << i]
  #Q = [0]
  #R = [E[i]]
  #X = [(1 << i, 0, E[i])]
  X = [(1 << i) + 0 + (E[i] << 40)]
  for j in range(i):
    #Pnext = []
    #Qnext = []
    #Rnext = []
    #Xnext = []
    e = E[j]
    em = (E[j] << 40) + (1 << 40) - 1
    #b = 1 << j
    bp = (1 << j)
    bq = (1 << j) << 20
    br = (1 << j) << 40
    #for p, q, r in zip(P, Q, R):
    #for p, q, r in X:
    for x in X[:]:
      #if r & b:
      if x & br:
        #Pnext.append(p | b)
        #Qnext.append(q)
        #Rnext.append(r & e)
        #Xnext.append((p | b, q, r & e))
        #Xnext.append((x | bp) & em)
        X.append((x | bp) & em)

      #Pnext.append(p)
      #Qnext.append(q | b)
      #Rnext.append(r)
      #Xnext.append((p, q | b, r))
      #Xnext.append(x | bq)
      X.append(x | bq)

      #Pnext.append(p)
      #Qnext.append(q)
      #Rnext.append(r)
      #Xnext.append((p, q, r))
      #Xnext.append(x)

    #P = Pnext
    #Q = Qnext
    #R = Rnext
    #X = Xnext

  #print('[{}]'.format(i))
  #for p, q, r in zip(P, Q, R):
  #  print('{:018b}'.format(p))
  #  print('{:018b}'.format(q))
  #  print('{:018b}'.format(r))
  #  print()

dp = [20] * (1 << 20)
dp[0] = 0