N = int(input())
ok = 10**9
ng = 0

while ok-ng>1:
  tgt = (ok+ng)//2
  if tgt*(tgt+1)>=2*N:
    ok = tgt
  else:
    ng = tgt

print(ok)
