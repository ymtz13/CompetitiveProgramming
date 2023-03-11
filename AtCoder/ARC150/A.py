T = int(input())
ans = []

for _ in range(T):
  N, K = map(int, input().split())
  S = input()

  if S.count('1') == 0:
    t = 0
    T = []
    for c in S:
      if c == '0':
        T.append(t)
        t = 0
      else:
        t += 1
    T.append(t)

    ans.append('Yes' if max(T) == K and T.count(K) == 1 else 'No')

  else:
    a = 'Yes'

    L = None
    for i, c in enumerate(S):
      if c == '1':
        if L is None: L = i
        R = i

    for i in range(L + 1, R):
      if S[i] == '0':
        a = 'No'

    cntL = 0
    for i in range(L - 1, -1, -1):
      if S[i] != '?': break
      cntL += 1

    cntR = 0
    for i in range(R + 1, N):
      if S[i] != '?': break
      cntR += 1

    M = R - L + 1

    if M > K: a = 'No'

    if M < K:
      if cntL == 0 or cntR == 0:
        if M + cntL + cntR < K: a = 'No'
      else:
        if M + cntL + cntR != K: a = 'No'

    ans.append(a)

for a in ans:
  print(a)
