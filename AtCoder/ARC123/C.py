F = 2
CO = [
    [0, F, F, F, F, F, F, F, F, F],
    [F, 0, 0, 0, F, F, F, F, F, F],
    [F, F, 0, 0, 0, 0, 0, F, F, F],
    [F, F, F, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, F, 0, 0, 0, 0, 0, 0],
]


def check(N, i, k, co):
  if i == len(N): return co == 0

  n = (N[i] - co) % 10
  co_next = CO[k][n]
  if co_next == F: return False

  if N[i] == 0 and co == 1: co_next = 1

  for k_next in range(k + 1):
    if check(N, i + 1, k_next, co_next): return True

  return False


def solve(N):
  for k in range(1, 5):
    if check(N, 0, k, 0): return k
  return 5


H = []


def dfs(i=0, v=0):
  if i > 5: return
  if v: H.append(v)
  dfs(i + 1, v * 10 + 1)
  dfs(i + 1, v * 10 + 2)
  dfs(i + 1, v * 10 + 3)


dfs()
#print(H)

T = int(input())

for _ in range(T):
  N = list(map(int, input()))[::-1]
  print(solve(N))
