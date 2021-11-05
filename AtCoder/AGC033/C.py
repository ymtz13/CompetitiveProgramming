from sys import setrecursionlimit

setrecursionlimit(1000000)

N = int(input())
E = [[] for _ in range(N)]
for _ in range(N - 1):
  a, b = map(int, input().split())
  E[a - 1].append(b - 1)
  E[b - 1].append(a - 1)

R = 0


def dfs(i, p):
  global R
  d = [0, 0] + sorted([dfs(e, i) for e in E[i] if e != p])
  R = max(R, sum(d[-2:]))
  return d[-1] + 1


dfs(0, None)

print('Second' if R % 3 == 1 else 'First')
