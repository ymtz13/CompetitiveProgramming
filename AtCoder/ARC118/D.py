P, a, b = map(int, input().split())

for i in range(1, P):
  print('[{:2d}]'.format(i), end='')
  for j in range(1, P):
    print(' {:2d}'.format(i*j%P), end='')
  print()


