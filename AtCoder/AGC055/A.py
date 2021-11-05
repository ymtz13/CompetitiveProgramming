from collections import deque

N = int(input())
S = [ord(c) - ord('A') for c in input()]

D = {
    (0, 1, 2): '1',
    (0, 2, 1): '2',
    (1, 0, 2): '3',
    (1, 2, 0): '4',
    (2, 0, 1): '5',
    (2, 1, 0): '6',
}

ans = [None] * (N * 3)
U = [False] * (N * 3)

for X in range(3):
  Y = (X + 1) % 3
  Z = (X + 2) % 3

  pX = deque()
  for i, c in enumerate(S[:N]):
    if c == X: pX.append(i)
  M = len(pX)

  cnt = 0
  pY = deque()
  pZ = deque()
  for i, c in enumerate(S[N:], N):
    if c == X or U[i]: continue
    if cnt < M:
      cnt += 1
      if c == Y:
        pY.append(i)
      else:
        pZ.append(i)

    else:
      if c == Y and pZ:
        ix = pX.popleft()
        iy = i
        iz = pZ.popleft()
        d = D[(X, Z, Y)]
        ans[ix] = ans[iy] = ans[iz] = d
        U[iy] = U[iz] = True
        cnt += 1

      if c == Z and pY:
        ix = pX.popleft()
        iy = pY.popleft()
        iz = i
        d = D[(X, Y, Z)]
        ans[ix] = ans[iy] = ans[iz] = d
        U[iy] = U[iz] = True
        cnt += 1

      if cnt == M * 2: break

print(''.join(map(str, ans)))

#for i in range(1, 7):
#  print(i, ''.join([chr(c + ord('A')) for v, c in zip(ans, S) if v == str(i)]))
