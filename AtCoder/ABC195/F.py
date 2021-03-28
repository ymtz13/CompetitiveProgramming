A, B = map(int, input().split())

def gcd(a, b):
  if a<b: a, b = b,a
  while b:
    a, b = b, a%b
  return a

E = [[] for _ in range(B-A+1)]

for x in range(A, B+1):
  for y in range(x+1, B+1):
    if gcd(x, y)>1:
      #print(x, y)
      #E[x-A].append(y-A)
      E[y-A].append(x-A)

print(E)

for i, e in enumerate(E):
  

