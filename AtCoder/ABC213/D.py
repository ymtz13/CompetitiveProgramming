from sys import setrecursionlimit

setrecursionlimit(1 << 30)

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
  A, B = map(int, input().split())
  E[A - 1].append(B - 1)
  E[B - 1].append(A - 1)

ans = []


def dfs(i, p):
  ans.append(i + 1)

  for c in sorted(E[i]):
    if c != p:
      dfs(c, i)
      ans.append(i + 1)


dfs(0, None)
print(' '.join(map(str, ans)))
