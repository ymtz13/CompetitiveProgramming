N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [tuple(map(int, input().split())) for _ in range(K)]

X = [0]*(N+1)
def dfs(i):
  if i==K:
    n = 0
    for A, B in AB:
      if X[A] and X[B]: n += 1
    return n
  
  C, D = CD[i]
  X[C] += 1
  n1 = dfs(i+1)
  X[C] -= 1

  X[D] += 1
  n2 = dfs(i+1)
  X[D] -= 1

  return max(n1, n2)

print(dfs(0))
