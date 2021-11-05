X2 = []
X3 = []
X5 = []
XA = []

for x in range(2, 10000):
  if x%2!=0 and x%3==0 and x%5==0: X2.append(x)
  if x%2==0 and x%3!=0 and x%5==0: X3.append(x)
  if x%2==0 and x%3==0 and x%5!=0: X5.append(x)
  if x%2==0 and x%3==0 and x%5==0: XA.append(x)

N = int(input())
ans = [6, 10, 15] + (X2[1:] + X3[1:] + X5[1:] + XA)[:N-3]
print(' '.join(map(str, ans)))
