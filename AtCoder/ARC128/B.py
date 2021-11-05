T = int(input())
INF = 1 << 60
for _ in range(T):
  C = tuple(map(int, input().split()))
  R, G, B = C

  ans = INF
  if R == G: ans = min(ans, R)
  if G == B: ans = min(ans, G)
  if B == R: ans = min(ans, B)

  for p in range(3):
    q, r = (p + 1) % 3, (p + 2) % 3
    if C[q] < C[r]: q, r = r, q
    if (C[q] - C[r]) % 3 != 0: continue

    X = [C[p], C[q], C[r]]
    #print(p, X)

    cnt = 0

    # a
    cnta = X[2]
    cnt += cnta
    Xa = [X[0] + cnta * 2, X[1] - cnta, 0]

    # b
    cntb = (Xa[1] - Xa[2]) // 3
    cnt += cntb * 2
    Xb = [Xa[0] + cntb, Xa[1] - cntb * 2, Xa[2] + cntb]

    # c
    cntc = Xb[2]
    cnt += cntc
    Xc = [Xa[0] + cntc * 2, 0, 0]

    #print('a:', cnta, Xa)
    #print('b:', cntb, Xb)
    #print('c:', cntc, Xc)
    #print(cnt)
    #print()
    ans = min(ans, cnt)

  print(ans if ans < INF else -1)
