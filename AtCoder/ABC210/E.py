N, M = map(int, input().split())
AC = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x: x[1])

def gcd(x, y):
  while x: x, y = y%x, x
  return y

ans = 0
for A,C in AC:
  n = gcd(N, A)

  s = N//n
  ans += C*(s-1)*n
  N = n

print(ans if N==1 else -1)
