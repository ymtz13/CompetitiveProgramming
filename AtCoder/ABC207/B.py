A, B, C, D = map(int, input().split())
X = C*D - B
if X<=0:
  print(-1)
else:
  print((A+X-1)//X)