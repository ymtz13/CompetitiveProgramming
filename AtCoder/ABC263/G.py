def isPrime(x):
  if x <= 1: return False
  if x == 2: return True
  if x % 2 == 0: return False

  for p in range(3, x + 1):
    if p * p > x: break
    if x % p == 0: return False

  return True


for n in range(1, 20):
  print(n, isPrime(n))

N = int(input())
B1 = 0
BE = []
BO = []

for _ in range(N):
  A, B = map(int, input().split())

  if A % 2 == 0:
    BE.append(B)
  elif A==1:
    B1 = B
  else:
    BO.append(B)

M = len(BE) + len(BO)
E = [[0] * (N + 2) for _ in range(N + 2)]

def flow(AE, AO):
  for ae, ao 

