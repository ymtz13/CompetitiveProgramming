def ans(a):
  print('Takahashi' if a else 'Aoki')
  exit()


N, M = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(M)]

if M == 0: ans(N % 2 == 1)

px, py = XY[0]
C = 0
for x, y in XY[1:]:
  B = x - px - 1
  p = (y + py) % 2
  px = x
  py = y

  if B == 0: continue

  C += B
  if B % 2 == p: C -= 1

CL = XY[0][0] - 1
CR = N - XY[-1][0]

if CL < 2 and CR >= 2: ans(True)
if CR < 2 and CL >= 2: ans(True)
if CL < 2 and CR < 2: ans((C + CL + CR) % 2 == 1)

m = min(CL, CR)
D = abs(CL - CR)
if D == 0: ans(C % 2 == 1)
if m % 2 == 0 and D == 1: ans(C % 2 == 0)
ans(True)
