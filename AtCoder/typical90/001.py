N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

B = []
x = 0
for a in A + [L]:
  B.append(a-x)
  x = a
print(B)

def check(X):
  s = 0
  n = 0
  for b in B:
    s += b
    if s>=X:
      s = 0
      n += 1

  return n>=K+1

ok = 1
ng = 10**10
while ng-ok>1:
  tgt = (ng+ok)//2
  if check(tgt):
    ok = tgt
  else:
    ng = tgt

print(ok)
