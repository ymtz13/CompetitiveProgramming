from collections import deque

N = int(input())
T = [None] * N
K = [None] * N
A = [None] * N
for i in range(N):
  V = list(map(int, input().split()))
  T[i] = V[0]
  K[i] = V[1]
  A[i] = V[2:]

X = [False] * N
X[-1] = True

ans = 0
for i in range(N - 1, -1, -1):
  if not X[i]: continue
  ans += T[i]

  for a in A[i]:
    X[a - 1] = True

print(ans)
