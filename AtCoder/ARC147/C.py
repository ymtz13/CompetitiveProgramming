  N = int(input())

  M = N + 10
  M2 = M * 2

  X = []
  for i in range(N):
    L, R = map(int, input().split())
    #X.append((L, 0, i))
    #X.append((R, 1, i))
    X.append(L * M2 + 0 * M + i)
    X.append(R * M2 + 1 * M + i)

  X.sort()

  ans = 0
  s = 0

  confirming = [False] * N
  cntConfirming = 0
  cntConfirmed = 0
  cntRemain = N

  flag = False

  for xti in X:
    x = xti // M2
    ti = xti % M2
    t = ti // M
    i = ti % M

    if t == 0:
      if flag:
        #print('immed confirmed', i, 'at', x, ' / score', x * cntConfirmed - s)
        ans += x * cntConfirmed - s
        s += x
        cntConfirmed += 1
        cntRemain -= 1
      else:
        #print('begin confirming', i, 'at', x)
        confirming[i] = True
        cntConfirming += 1
        cntRemain -= 1

        if not flag and cntRemain <= cntConfirmed:
          flag = True

          for j in range(N):
            if not confirming[j]: continue

            #print(' and confirmed', j, 'at', x, ' / score', x * cntConfirmed - s)
            ans += x * cntConfirmed - s
            s += x
            cntConfirmed += 1
            confirming[j] = False
            cntConfirming -= 1

    else:
      if not confirming[i]: continue

      #print('confirmed', i, 'at', x, ' / score', x * cntConfirmed - s)
      ans += x * cntConfirmed - s
      s += x
      cntConfirmed += 1
      confirming[i] = False
      cntConfirming -= 1

      if not flag and cntRemain <= cntConfirmed:
        flag = True
        for j in range(N):
          if not confirming[j]: continue

          #print(' and confirmed', j, 'at', x, ' / score', x * cntConfirmed - s)
          ans += x * cntConfirmed - s
          s += x
          cntConfirmed += 1
          confirming[j] = False
          cntConfirming -= 1

  print(ans)
