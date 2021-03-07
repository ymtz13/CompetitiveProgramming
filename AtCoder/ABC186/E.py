def gcd(x, y):
  if x>y: x,y = y,x
  while x: x,y = y%x, x
  return y

def inverse(x, mod):
  u, ut = mod, 0
  v, vt = x, 1

  while v:
    q = u//v
    u, v = v, u%v
    ut, vt = vt, ut - q*vt

  return ut % mod

def solve(N, S, K):
  if S==N: return 0

  P = gcd(K, N)
  if S%P!=0: return -1

  N//=P
  S//=P
  K//=P

  return -S * inverse(K, N) % N



T = int(input())
for _ in range(T):
  N, S, K = map(int, input().split())
  print(solve(N, S, K))
