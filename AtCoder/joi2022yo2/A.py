from collections import deque

Q = int(input())
stack = deque([])

for _ in range(Q):
  s = input()
  if s == 'READ':
    print(stack.pop())
  else:
    stack.append(s)
