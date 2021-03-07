def f(S):
  if '.' not in S: S = S + '.'
  S0, S1 = S.split('.')
  S1 = S1 + '0'*(4-len(S1))
  return int(S0 + S1)

def floor(X):
  return X-X%10000

def ceil(X):
  r = X%10000
  return X+10000-r if r else X

def sqrtfloor(X):
  ok = 0
  ng = X + 1
  while ng-ok>1:
    tgt = (ng+ok)//2
    if tgt*tgt>X: ng = tgt
    else: ok = tgt
  return ok

X, Y, R = map(f, input().split())

Rsq = R * R
ans = 0

for y in range(floor(Y-R), ceil(Y+R)+1, 10000):
  dy = abs(y-Y)
  dxsq = Rsq - dy*dy
  if dxsq<0: continue

  dx = sqrtfloor(dxsq)
  ans += (floor(X+dx) - ceil(X-dx))//10000 + 1

print(ans)
