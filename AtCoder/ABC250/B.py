N, A, B = map(int, input().split())

for a in range(A * N):
  S = []
  for b in range(B * N):
    p = (a // A) + (b // B)
    S.append('.' if p % 2 == 0 else '#')
  print(''.join(S))
