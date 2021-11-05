from collections import deque

S = input()
rev = False

D = deque()
for c in S:
  if c=='R': rev = not rev
  else:
    if rev:
      if D and D[0]==c: D.popleft()
      else: D.appendleft(c)
    else:
      if D and D[-1]==c: D.pop()
      else: D.append(c)

if rev: D.reverse()

print(''.join(D))
