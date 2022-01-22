n, _ = map(int, input().split())
P = [input() for _ in range(n)]
E = [1 << i for i in range(n)]

for i in range(n):
  for j in range(i + 1, n):
    ok = True
    for ci, cj in zip(P[i], P[j]):
      if ci != '*' and cj != '*' and ci != cj:
        ok = False
        break
    if ok:
      E[i] |= 1 << j
      E[j] |= 1 << i

#for e in E:
#  print('{:05b}'.format(e))

N = 1 << n
X = [None] * N
for x in range(1, N):
  ok = True
  for i in range(n):
    if x & (1 << i) == 0: continue
    if x & E[i] != x:
      ok = False
      continue
  if ok:
    #print('{:05b}'.format(x))
    X[x] = [x]


def dfs(x):
  if X[x] is not None: return X[x]

  B = [1 << b for b in range(n) if x & (1 << b)]
  retval = [None] * 20
  for j in range(1, (1 << len(B)) - 1):
    s1 = 0
    for i, b in enumerate(B):
      if j & (1 << i): s1 += b
    s2 = x - s1

    r = dfs(s1) + dfs(s2)
    if len(r) < len(retval):
      retval = r

  X[x] = retval
  return retval


r = dfs(N - 1)

print(len(r))
