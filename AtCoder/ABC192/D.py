X = list(map(int, input()))
M = int(input())
d = max(X)

if len(X)==1:
  print(1 if d <= M else 0)
  exit()

def check(n):
  v = 0
  r = 1
  for x in reversed(X):
    v += r * x
    if v > M: return False
    r *= n
  return True

ok = d
ng = M+1
while ng-ok>1:
  tgt = (ok+ng)//2
  if check(tgt):
    ok = tgt
  else:
    ng = tgt

print(ok-d)