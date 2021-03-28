N = int(input())
AT = [tuple(map(int, input().split())) for _ in range(N)]
INF = 10**20

C = [0]*N
for i, (a, t) in enumerate(AT):
  if t==1: C[i] = a

S = [0]
for c in C:
  S.append(S[-1] + c)
Z = S[-1]

vmax = +INF
vmin = -INF
for i, (a, t) in enumerate(AT):
  aa = a + Z - S[i]
  if t==2:
    vmin = max(vmin, aa)
    vmax = max(vmax, vmin)
  if t==3:
    vmax = min(vmax, aa)
    vmin = min(vmin, vmax)

def F(x):
  return max(vmin, min(vmax, x + Z))

Q = int(input())
X = list(map(int, input().split()))
for x in X:
  print(F(x))
