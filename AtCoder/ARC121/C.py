T = int(input())
for _ in range(T):
  N = int(input())
  P = [0] + list(map(int, input().split()))

  ans = []
  hands = 1
  for tgt in range(N-2):
    pos = P.index(tgt)

    while pos != tgt:
      if pos%2 == hands%2:
        if pos >= tgt+2:
          x = pos - 2
        else:
          x = pos
          pos += 1
      else:
        x = pos - 1
        pos -= 1

      #print(P, x)
      P[x], P[x+1] = P[x+1], P[x]
      hands += 1
      ans.append(x)
  
  #print(P)
  while P[-3:] != [N-2, N-1, N]:
    if hands%2==0: x = N-2 if N%2==0 else N-1
    else         : x = N-1 if N%2==0 else N-2
    #print(P, x)
    P[x], P[x+1] = P[x+1], P[x]
    hands += 1
    ans.append(x)

  print(len(ans))
  print(' '.join(map(str, ans)))
