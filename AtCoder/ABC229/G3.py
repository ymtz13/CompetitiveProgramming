from bisect import bisect

S = input()
K = int(input())

INF = 1 << 60

SY = []
SS = []
p = None
cnt = 0
for c in '.' + S + '._':
  if p and c != p:
    if p == 'Y': SY.append(cnt)
    if p == '.': SS.append(cnt)
    cnt = 0
  cnt += 1
  p = c

SS = SS[1:-1]
sAll = sum(SS)

SL = []
s = 0
for sy, ss in zip(SY, SS + [0]):
  SL.append((s, sy))
  s += ss

SR = []
s = 0
for sy, ss in zip(SY[::-1], SS[::-1] + [0]):
  SR.append((s, sy))
  s += ss

print(SL, SR)

sl = 0
sr = sAll
for iy, (ss, sy) in enumerate(SL):
  print(SL[iy + 1:])
  print(SR[len(SR) - iy:])
  print(s)
  print()

  ok = 0
  ng = K + 1
  while ng - ok > 1:
    tgt = (ng + ok) // 2

    il = bisect(SL, (tgt + sl, INF))
    ir = bisect(SR, (tgt + sr, INF))

  sl += ss
  sr -= ss

