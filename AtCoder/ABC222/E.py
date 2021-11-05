from collections import deque

mod = 998244353

N, M, K = map(int, input().split())
A = list(map(int, input().split()))

E = [[] for _ in range(N)]
C = [[0] * N for _ in range(N)]
for i in range(N - 1):
  U, V = map(int, input().split())
  E[U - 1].append(V - 1)
  E[V - 1].append(U - 1)

for s, t in zip(A[:-1], A[1:]):
  s -= 1
  t -= 1

  queue = deque([(s, None)])
  come_from = [None] * N

  while queue:
    q, c = queue.popleft()
    come_from[q] = c

    for e in E[q]:
      if e != c: queue.append((e, q))

  q = t
  while q != s:
    c = come_from[q]
    if q > c:
      C[c][q] += 1
    else:
      C[q][c] += 1
    q = c

X = []
for row in C:
  X.extend([c for c in row if c > 0])

#print(X)
S = sum(X)

if S % 2 != K % 2:
  print(0)
  exit()

R = (S + K) // 2

if R<0:
  print(0)
  exit()

dp = [0] * (R + 1)
dp[0] = 1
for x in X:
  for i, v in enumerate(dp[:-x]):
    dp[i + x] += v
    dp[i + x] %= mod

#print(dp)

ans = dp[-1] * pow(2, N - 1 - len(X), mod) % mod
print(ans)
