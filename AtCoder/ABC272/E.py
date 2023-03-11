from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))

X = [[] for _ in range(M)]
for i, a in enumerate(A, 1):
  for b in range(a % i, N, i):
    m = (b - a) // i
    if m <= 0 or m > M: continue
    X[m - 1].append(b)

for x in X:
  x = deque(sorted(set(x)))

  mex = 0
  while x and x.popleft() == mex:
    mex += 1

  print(mex)
