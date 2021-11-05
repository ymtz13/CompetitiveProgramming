from collections import deque

N = int(input())
P = list(map(int, input().split()))
K = N + 2

X = [-2] * (K * K)
Z = [1] * (K * K)

for i in range(N):
  for j in range(N):
    X[(i + 1) * K + j + 1] = min(i, j, N - 1 - i, N - 1 - j)

ans = 0
for p in P:
  i, j = (p - 1) // N, (p - 1) % N
  s = (i + 1) * K + j + 1
  queue = deque([s])
  ans += X[s]
  Z[s] = 0

  while queue:
    q = queue.popleft()
    #if X[q] > 0 and q != s: X[q] -= 1

    x = X[q] + Z[q]
    for p in (q - 1, q + 1, q - K, q + K):
      if X[p] > x:
        X[p] -= 1
        queue.append(p)
    #if X[q - 1] > x: queue.append(q - 1)
    #if X[q + 1] > x: queue.append(q + 1)
    #if X[q - K] > x: queue.append(q - K)
    #if X[q + K] > x: queue.append(q + K)

print(ans)
