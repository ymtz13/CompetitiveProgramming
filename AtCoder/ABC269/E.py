N = int(input())

def bisect(row):
  L = 1
  R = N
  while R != L:
    M = (L + R) // 2
    expected = M - L + 1

    if row:
      print('? 1 {} {} {}'.format(N, L, M))
    else:
      print('? {} {} 1 {}'.format(L, M, N))      
    result = int(input())

    if result == expected:
      L = M + 1
    else:
      R = M
  
  return L

X = bisect(False)
Y = bisect(True)

print('! {} {}'.format(X, Y))
