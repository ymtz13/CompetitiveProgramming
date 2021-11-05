from collections import deque, defaultdict

N, M = map(int, input().split())
A = [deque(map(int, input().split())) for _ in range(N)]
X = [False] * (M + 1)

ans = N

while True:
  D = defaultdict(int)
  m = 0
  for a in A:
    if len(a) == 0:
      print(ans)
      exit()

    a0 = a[0]
    D[a0] += 1
    m = max(m, D[a0])

  K = [k for k, v in D.items() if v == m]
  for k in K: X[k] = True
  ans = min(ans, m)

  for a in A:
    while a and X[a[0]]: a.popleft()
