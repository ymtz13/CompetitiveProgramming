from collections import deque

N = int(input())
S = list(map(int, input().split()))
S.sort(reverse=True)

T = [S[0]]
S = deque(S[1:])

print(T, S)

for _ in range(N):
  Snext = deque()
  Tappend = []
  for t in T:
    while S and S[0] >= t:
      Snext.append(S.popleft())

    if not S:
      print('No')
      exit()

    Tappend.append(S.popleft())

  S = Snext + S

  T = T + Tappend
  T.sort(reverse=True)

  print(T, S)

print('Yes')
