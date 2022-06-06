#from math import isqrt


def isqrt(X):
  ok = 0
  ng = 1 << 60
  while ng - ok > 1:
    tgt = (ng + ok) // 2
    if tgt * tgt <= X:
      ok = tgt
    else:
      ng = tgt

  return ok


T = int(input())
for _ in range(T):
  X = int(input())
  X1 = isqrt(X)
  X2 = isqrt(X1)

  V = []
  for i in range(1, X2 + 1):
    v = X1 - i * i + 1
    V.append(v)

  #print(X1, X2, V, X1, X2)

  while len(V) > 1:
    S = [None] * len(V)
    s = 0
    for i, v in enumerate(reversed(V)):
      s += v
      S[-(i + 1)] = s

    Vnext = []
    for i in range(1, len(V) + 1):
      x = i * i
      if x - 1 >= len(V): break
      Vnext.append(S[x - 1])

    V = Vnext
    #print('S, V = ', S, V)

  print(V[0])
