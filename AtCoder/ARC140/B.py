from collections import deque

N = int(input())
S = input()

CA = []
sA = 0
for c in S:
  if c == 'R':
    CA.append(sA)
    sA = 0

  if c == 'A':
    sA += 1

  if c == 'C':
    sA = 0

CC = []
sC = 0
for c in S[::-1]:
  if c == 'R':
    CC.append(sC)
    sC = 0

  if c == 'A':
    sC = 0

  if c == 'C':
    sC += 1

M = [min(ca, cc) for ca, cc in zip(CA, CC[::-1])]
M = [m for m in M if m > 0]

queue = deque(sorted(M))

ans = 0
while queue:
  ans += 1
  x = queue.pop()
  if x > 2:
    queue.append(x - 1)
  elif x == 2:
    queue.appendleft(1)

  if not queue: break

  ans += 1
  queue.popleft()

print(ans)
