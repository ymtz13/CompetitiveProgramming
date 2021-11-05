from collections import defaultdict

def decomp(x):
  D = defaultdict(int)
  while x%2==0:
    D[2] += 1
    x //= 2
  
  for p in range(3, 100000, 2):
    while x%p==0:
      D[p] += 1
      x //= p

  if x>1: D[x] = 1

  return D

N = int(input())
AB = [tuple(map(decomp, map(int, input().split()))) for _ in range(N)]

a0, b0 = AB[0]
P = defaultdict(int)
for key, value in a0.items(): P[key] = max(P[key], value)
for key, value in b0.items(): P[key] = max(P[key], value)

Pk = sorted(list(P.keys()))
M = len(Pk)

x = [None]*M
X = []

def dfs(i=0, s=1):
  if i==M:
    X.append((s, tuple(x)))
    return

  k = Pk[i]
  r = range(0, P[k]+1) if i==0 else range(-P[k], P[k]+1)
  for v in r:
    x[i] = v
    dfs(i+1, s * (k**abs(v)))

dfs()

def contain(D, c):
  retval = True
  for k, v in D.items():
    if c[k] < v: retval = False

  return retval

for s, x in sorted(X, reverse=True):
  ok = True

  Dpos = defaultdict(int)
  Dneg = defaultdict(int)
  for k, z in zip(Pk, x):
    if z>0: Dpos[k] = z
    else  : Dneg[k] = -z

  for a, b in AB:
    f = (contain(Dpos, a) and contain(Dneg, b)) or (contain(Dpos, b) and contain(Dneg, a))
    ok = ok and f
    if not f: break

  if ok:
    print(s)
    exit()
