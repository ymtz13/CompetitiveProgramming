def f(x):
  y = sum(map(int, str(x)))
  return (x + y) % 100000

N, K = map(int, input().split())
V = [False]*100001

L = []
x = N
while not V[x]:
  V[x] = True
  L.append(x)
  x = f(x)

if K<len(L):
  print(L[K])
  exit()

C = L.index(x)
R = L[C:]
print(R[(K-C)%(len(R))])
