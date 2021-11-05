D = [None]*(10**6)
top = 500000
bottom = top-1

Q = int(input())
for _ in range(Q):
  t, x = map(int, input().split())
  if t==1:
    D[top] = x
    top += 1

  if t==2:
    D[bottom] = x
    bottom -= 1
  
  if t==3:
    print(D[top-x])
