N, L = map(int, input().split())
A = list(map(int, input().split()))

x = -1
for i in range(N-1):
  a, b = A[i:i+2]
  if a+b>=L: x = i

if x<0:
  print('Impossible')
else:
  print('Possible')
  for i in range(x):
    print(i+1)
  for i in range(N-2, x, -1):
    print(i+1)
  print(x+1)
