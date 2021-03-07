n = int(input())

ok = 1
ng = n+1
while ng-ok>1:
  tgt = (ok+ng)//2
  if tgt*(tgt+1)<=2*(n+1):
    ok = tgt
  else:
    ng = tgt

print(n-ok+1)
