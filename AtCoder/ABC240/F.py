T = int(input())


def calcsum(x0, d, n):
  return x0 * n + d * n * (n + 1) // 2


for _ in range(T):
  N, M = map(int, input().split())

  B = 0
  A = 0

  XB = []  # debug

  for i in range(N):
    x, y = map(int, input().split())
    if i == 0: ans = x

    Bnext = B + x * y
    Anext = A + calcsum(B, x, y)

    if B >= 0 and Bnext < 0:
      n = B // (-x)
      if n > 0:
        ans = max(ans, A + calcsum(B, x, n))

    #XB.extend([B + x * n for n in range(1, y + 1)])

    B = Bnext
    A = Anext

  #print(XB)
  #XA = []
  #s = 0
  #for xb in XB:
  #  s += xb
  #  XA.append(s)
  #print(XA)

  ans = max(ans, A)
  print(ans)
