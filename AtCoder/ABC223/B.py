from collections import deque

S = deque(input())
X = []
for i in range(len(S)):
  X.append(tuple(S))
  S.append(S.popleft())

X = sorted(X)
print(''.join(X[0]))
print(''.join(X[-1]))
