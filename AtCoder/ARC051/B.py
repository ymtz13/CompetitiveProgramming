counter = [0]
def gcd(a, b):
  if b == 0: return a
  counter[0] += 1
  return gcd(b, a%b)

K = int(input())
X = [1, 2]
for i in range(40):
  X.append(X[-1] + X[-2])

if K==1:
  print(1, 1)
else:
  gcd(X[K], X[K-1])
  #print(counter)
  print(X[K], X[K-1])
