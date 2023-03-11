from collections import deque, defaultdict

M, N = map(int, input().split())
A = [(0, ) + tuple(map(int, input().split())) + (0, ) for _ in range(M)]
B = [(0, ) + tuple(map(int, input().split())) + (0, ) for _ in range(M)]

C = []
C += [(2, ) * (N + 2)]
C += [tuple([a if a != b else 2 for a, b in zip(*AB)]) for AB in zip(A, B)]
C += [(2, ) * (N + 2)]

K = M * N
E = [defaultdict(int) for _ in range(K + 2)]

S = K
G = K + 1
ans = 0

for m in range(1, M + 1):
  for n in range(1, N + 1):
    i = (m - 1) * N + n - 1
    if C[m][n] != 2: ans += 1
    if C[m][n] == 0: E[S][i] = 1
    if C[m][n] == 1: E[i][G] = 1

    if C[m][n] != 0: continue

    if C[m - 1][n] == 1: E[i][i - N] = 1
    if C[m + 1][n] == 1: E[i][i + N] = 1
    if C[m][n - 1] == 1: E[i][i - 1] = 1
    if C[m][n + 1] == 1: E[i][i + 1] = 1

while True:
  queue = deque([(S, -1)])
  come_from = [None] * (K + 2)
  while queue:
    q, f = queue.popleft()
    if come_from[q] is not None: continue
    come_from[q] = f
    if q == G: break

    for e, c in E[q].items():
      if c == 1: queue.append((e, q))

  if come_from[G] is None: break
  ans -= 1

  q = G
  while q != S:
    f = come_from[q]
    E[f][q] = 0
    E[q][f] = 1
    q = f

print(ans)
