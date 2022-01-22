N, X = map(int, input().split())
A = list(map(int, input().split()))
C = []
for a in A[1:]:
  c = X % a
  C.append(c)
  X -= c
C.append(X)

for i, a in enumerate(A):
  C[i] //= a

R = []
for i in range(N - 1):
  R.append(A[i + 1] // A[i])

R += [None]

memo = {}


def dfs(X, A):
  if len(X) == 1:
    return X[0]

  key = tuple(X)
  if key in memo: return memo[key]

  r1 = X[0] + dfs(X[1:], A[1:])

  X2 = X[1:]
  X2[0] += 1
  r2 = A[0] - X[0] + dfs(X2, A[1:])

  retval = min(r1, r2)
  memo[key] = retval
  return retval


ans = dfs(C, R)

print(ans)
