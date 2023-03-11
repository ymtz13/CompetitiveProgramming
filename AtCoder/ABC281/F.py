from sys import setrecursionlimit

setrecursionlimit(1 << 20)

N = int(input())
A = list(map(int, input().split()))


def dfs(A, i=31):
  if not A: return 0
  if i == -1: return 0

  b = 1 << i

  A0 = []
  A1 = []
  for a in A:
    if a & b:
      A1.append(a - b)
    else:
      A0.append(a)

  v0 = dfs(A0, i - 1)
  v1 = dfs(A1, i - 1)

  if not A0: return v1
  if not A1: return v0

  return min(v0, v1) + b


ans = dfs(A)
print(ans)
