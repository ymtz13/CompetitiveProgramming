from collections import deque
#from this import d

N = int(input())
S = input()

D = deque([N])

for i in range(N-1, -1, -1):
  if S[i]=='L':
    D.append(i)
  else:
    D.appendleft(i)

print(' '.join(map(str, D)))

