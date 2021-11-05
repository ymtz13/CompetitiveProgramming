from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))
Q = deque()
L = {}

ans = 0
for i, a in enumerate(A):
  if a not in L:
    if len(L)==K:
      length = len(Q)
      while True:
        q, j = Q.popleft()
        if L[q] == j:
          L.pop(q)
          break
      ans = max(ans, length)

  Q.append((a, i))
  L[a] = i
    
ans = max(ans, len(Q))
print(ans)
