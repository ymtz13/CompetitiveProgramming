import cmath

N = int(input())
if N==1:
  print('Yes')
  exit()

gSx = gSy = gTx = gTy = 0
S = []
for _ in range(N):
  x, y = tuple(map(int, input().split()))
  S.append((x, y))
  gSx += x
  gSy += y

T = []
for _ in range(N):
  x, y = tuple(map(int, input().split()))
  T.append((x, y))
  gTx += x
  gTy += y

gSx /= N
gSy /= N
gTx /= N
gTy /= N

S = [(x - gSx) + 1j*(y - gSy) for x, y in S]
T = [(x - gTx) + 1j*(y - gTy) for x, y in T]
T = sorted(T, key=lambda t: t.real*10000 + t.imag)

def equal(v1, v2):
  return abs(v1-v2)<1e-5

for s in S:
  if not equal(s, 0): break

for t in T:
  if not equal(abs(s), abs(t)): continue

  r = t/s

  R = [s*r for s in S]
  R = sorted(R, key=lambda r: r.real*10000 + r.imag)

  ok = True
  for t, r in zip(T, R):
    if not equal(t, r):
      ok = False
      break
  
  if ok:
    print('Yes')
    exit()

print('No')
