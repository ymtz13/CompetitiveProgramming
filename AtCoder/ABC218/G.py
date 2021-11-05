from sys import setrecursionlimit

setrecursionlimit(10**5)

K = 1 << 17
val = [0] * (K + 1)


def addf(i, x):
  while i <= K:
    val[i] += x
    i += i & -i


def sumf(i):
  ret = 0
  while i > 0:
    ret += val[i]
    i -= i & -i
  return ret


def getf(i):
  ok = K + 1
  ng = 0
  while ok - ng > 1:
    tgt = (ng + ok) // 2
    if sumf(tgt) >= i:
      ok = tgt
    else:
      ng = tgt

  return ok


N = int(input())
A = list(map(int, input().split()))

sA = [None] + sorted(A)
D = {a: i for i, a in enumerate(sA)}

E = [[] for _ in range(N)]
for _ in range(N - 1):
  u, v = map(int, input().split())
  E[u - 1].append(v - 1)
  E[v - 1].append(u - 1)


def dfs(i, p, depth):
  a = A[i]
  d = D[a]
  #print(i, p, a, d)
  addf(d, 1)

  vals = []
  for e in E[i]:
    if e == p: continue
    vals.append(dfs(e, i, depth + 1))

  if len(vals) == 0:
    cnt = depth + 1
    if cnt % 2 == 0:
      median = (sA[getf(cnt // 2)] + sA[getf(cnt // 2 + 1)]) // 2
    else:
      median = sA[getf(cnt // 2 + 1)]

    #print('mediab->', i, median, val[:7])
    addf(d, -1)
    return median

  addf(d, -1)
  return max(vals) if depth % 2 == 0 else min(vals)


print(dfs(0, None, 0))
