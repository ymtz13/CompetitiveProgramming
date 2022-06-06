N = int(input())
T = input()

x = y = 0
dx = 1
dy = 0

for c in T:
  if c=='S':
    x += dx
    y += dy
  
  else:
    dx, dy = dy, -dx
  
print(x, y)
