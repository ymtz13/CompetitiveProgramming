from collections import defaultdict

N = int(input())
M = 100001
RC = [0] * M
HC = [[0] * 3 for _ in range(M)]
RH = []

for _ in range(N):
  R, H = map(int, input().split())
  RC[R] += 1
  HC[R][H - 1] += 1
  RH.append((R, H - 1))

S = []
s = 0
for rc in RC:
  s += rc
  S.append(s)

for r, h in RH:
  win = S[r - 1] + HC[r][(h + 1) % 3]
  draw = HC[r][h] - 1
  lose = N - 1 - win - draw
  print(win, lose, draw)
