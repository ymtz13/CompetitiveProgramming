N, P = map(int, input().split())
f = 2
F = {}
while f*f<=P:
  if P%f==0: F[f] = 0
  while P%f==0:
    F[f] += 1
    P//=f
  f += 1

if P > 1: F[P] = 1

ans = 1
for k, v in F.items():
  ans *= k**(v//N)

print(ans)
