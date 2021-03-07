N = int(input())
R = B = 0
for _ in range(N):
  S = input()
  R += S.count('R')
  B += S.count('B')

print('TAKAHASHI' if R>B else 'AOKI' if R<B else 'DRAW')
