N, a, b = map(int, input().split())
A = list(map(int, input().split()))


def check(X):
  cnta = cntb = 0
  for v in A:
    if v < X:
      cnta += (X - v + a - 1) // a
    if v > X:
      cntb += (v - X) // b

  return cnta <= cntb


ok = 0
ng = max(A) + 1

while ng - ok > 1:
  tgt = (ng + ok) // 2
  if check(tgt):
    ok = tgt
  else:
    ng = tgt

print(ok)
