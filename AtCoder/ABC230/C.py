N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

for i in range(P, Q + 1):
  C = []
  for j in range(R, S + 1):
    c = '#' if i + j == A + B or i - j == A - B else '.'
    C.append(c)
  print(''.join(C))

