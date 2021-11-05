A, K = input().split()
S = int(A)
A = list(map(int, A))
K = int(K)

if K == 10:
  print(0)
  exit()

M = len(A)
X = [None] * M
INF = 1 << 60


def dfs(i, t, u):
  if i == M: return abs(S - int(''.join(map(str, X))))

  if t < 0:
    v = 9 if len(u) < K else max(u)
    for j in range(i, M):
      X[j] = v
    return dfs(M, None, None)

  if t > 0:
    v = 0 if len(u) < K else min(u)
    for j in range(i, M):
      X[j] = v
    return dfs(M, None, None)

  retval = INF
  if len(u) < K:
    if A[i] > 0:
      v = A[i] - 1
      X[i] = v
      retval = min(retval, dfs(i + 1, -1, u | {v} if u or v > 0 else u))

    if A[i] < 9:
      v = A[i] + 1
      X[i] = v
      retval = min(retval, dfs(i + 1, +1, u | {v}))

    v = A[i]
    X[i] = v
    retval = min(retval, dfs(i + 1, 0, u | {v}))

    return retval

  un = {v for v in u if v < A[i]}
  up = {v for v in u if v > A[i]}

  if un:
    X[i] = max(un)
    retval = min(retval, dfs(i + 1, -1, u))

  if up:
    X[i] = min(up)
    retval = min(retval, dfs(i + 1, +1, u))

  if A[i] in u:
    X[i] = A[i]
    retval = min(retval, dfs(i + 1, 0, u))

  return retval


ans = dfs(0, 0, set())
print(ans)
