S, K = input().split()
K = int(K)

X = set()

N = len(S)
used = [False] * N
x = [None] * N


def dfs(i):
  if i == N:
    X.add(''.join(x))
    return

  for j, (c, u) in enumerate(zip(S, used)):
    if u: continue
    x[i] = c
    used[j] = True
    dfs(i + 1)
    used[j] = False


dfs(0)
print(sorted(list(X))[K - 1])
