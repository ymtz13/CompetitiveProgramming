def ans(b):
  print('Yes' if b else 'No')
  exit()


N = int(input())
S = [input() for _ in range(N)]

if len(set(S)) < N: ans(False)

for s in S:
  if s[0] not in 'HDCS': ans(False)
  if s[1] not in 'A23456789TJQK': ans(False)

ans(True)
