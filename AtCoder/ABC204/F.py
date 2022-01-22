mod = 998244353


def dot(v1, v2):
  retval = 0
  for c1, c2 in zip(v1, v2):
    retval += c1 * c2
    retval %= mod
  return retval


def dotvec(M, v):
  retval = [0] * len(v)
  for i, row in enumerate(M):
    retval[i] = dot(row, v)
  return retval

def dotmat(M):
  retval = [[0] * len(v) for _ in range(len(v))]
  for i, row in enumerate(M):
    for j, col in enumerate(M):
      retval[i][j] = dot(row, col)
  return retval


H, W = map(int, input().split())

M = [[0] * (1 << H) for _ in range(1 << H)]

for p1 in range(1 << H):
  for p2 in range(1 << H):
    v = 1
    streak = [[]]
    for h in range(H):
      b = 1 << h
      if (p1 & b) and (p2 & b): v = 0
      if not (p1 & b) and not (p2 & b):
        streak[-1].append(h)
      else:
        streak.append([])

    for s in streak:
      if len(s) == 2: v *= 2
      if len(s) == 3: v *= 3
      if len(s) == 4: v *= 5
      if len(s) == 5: v *= 8
      if len(s) == 6: v *= 13
    M[p2][p1] = v

v = [0] * (1 << H)
v[0] = 1
for i in range(200):
  if W & (1 << i): v = dotvec(M, v)
  M = dotmat(M)

print(v[0])
