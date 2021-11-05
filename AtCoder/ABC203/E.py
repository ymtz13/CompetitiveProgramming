from collections import defaultdict

N, M = map(int, input().split())
XY = sorted([tuple(map(int, input().split())) for _ in range(M)])

Z = []
p = None
z = []
for x, y in XY:
  if p is not None and p!=x:
    Z.append(z)
    z = []

  z.append(y)
  p = x
  
Z.append(z)

#print(Z)

INF = 10**10
cols = defaultdict(lambda: INF)
cols[N] = 0

for x, z in enumerate(Z):
  x += 1
  updates = []
  for y in z:
    if cols[y-1] < x or cols[y+1] < x:
      #cols[y] = x
      updates.append((y, x))
    else:
      #cols[y] = INF
      updates.append((y, INF))

  for y, v in updates:
    cols[y] = v

  #print(x, cols)

#print(cols)

print(len([a for a in cols.values() if a<INF]))
