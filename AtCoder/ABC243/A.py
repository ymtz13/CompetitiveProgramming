V, A, B, C = map(int, input().split())
V %= (A + B + C)

if V < A:
  print('F')

elif V < A + B:
  print('M')

else:
  print('T')
