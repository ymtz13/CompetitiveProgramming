R, X, Y = map(int, input().split())
D2 = X*X + Y*Y

R2 = R*R

if R2 > D2:
  print(2)
  exit()

for i in range(10**6):
  if i*i*R2 >= D2:
    print(i)
    exit()
