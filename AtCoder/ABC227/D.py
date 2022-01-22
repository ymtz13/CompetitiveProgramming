N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
S = sum(A)


def check(X):
  if K * X > S: return False
  s = 0
  for i, a in enumerate(A, 1):
    s += a
    if (K - i) * X > S - s: return False
  
  return True


ok = 0
ng = sum(A) + 1
while ng - ok > 1:
  tgt = (ng + ok) // 2
  if check(tgt):
    ok = tgt
  else:
    ng = tgt

print(ok)
