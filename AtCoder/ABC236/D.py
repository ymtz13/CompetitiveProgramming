N = int(input())
N2 = 2 * N
A = [[0] * N2 for _ in range(N2)]

for i in range(N2 - 1):
  row = list(map(int, input().split()))
  for j, a in enumerate(row, i + 1):
    A[i][j] = A[j][i] = a


def dfs(X, B):
  i = None
  J = []
  for k, x in enumerate(X):
    if x:
      if i is None:
        i = k
      else:
        J.append(k)

  if i is None:
    return B

  retval = 0
  for j in J:
    x = X[:]
    x[i] = x[j] = False
    retval = max(retval, dfs(x, B ^ A[i][j]))

  return retval


ans = dfs([True] * N2, 0)
print(ans)
