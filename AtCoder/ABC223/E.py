X, Y, A, B, C = map(int, input().split())
S = (A, B, C)


def f(X, Y, A, B, C):
  hA = (A + X - 1) // X
  YY = Y - hA
  if YY <= 0: return False

  # horizontal
  hB = (B + X - 1) // X
  hC = (C + X - 1) // X
  if (hB + hC) <= YY: return True

  # vertical
  wB = (B + YY - 1) // YY
  wC = (C + YY - 1) // YY
  if (wB + wC) <= X: return True

  return False


ans = False
for i in range(3):
  j, k = (i + 1) % 3, (i + 2) % 3

  ans = ans or f(X, Y, S[i], S[j], S[k])
  ans = ans or f(Y, X, S[i], S[j], S[k])

print('Yes' if ans else 'No')
