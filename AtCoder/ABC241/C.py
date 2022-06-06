N = int(input())
S = [[1 if c == '#' else 0 for c in input()] for _ in range(N)]

for r in range(N):
  for c in range(N - 5):
    s = 0
    for i in range(6):
      s += S[r][c + i]
    if s >= 4:
      print('Yes')
      exit()

for r in range(N - 5):
  for c in range(N):
    s = 0
    for i in range(6):
      s += S[r + i][c]
    if s >= 4:
      print('Yes')
      exit()

for r in range(N - 5):
  for c in range(N - 5):
    s = 0
    for i in range(6):
      s += S[r + i][c + i]
    if s >= 4:
      print('Yes')
      exit()

for r in range(5, N):
  for c in range(N - 5):
    s = 0
    for i in range(6):
      s += S[r - i][c + i]
    if s >= 4:
      print('Yes')
      exit()

print('No')
