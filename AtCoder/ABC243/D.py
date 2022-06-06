from collections import deque

N, X = map(int, input().split())
S = input()

A = deque()
while X:
  A.appendleft(X & 1)
  X >>= 1

for c in S:
  if c == 'U': A.pop()
  if c == 'L': A.append(0)
  if c == 'R': A.append(1)

ans = 0
X = 1
while A:
  ans += X * A.pop()
  X *= 2

print(ans)
