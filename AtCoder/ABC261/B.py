N = int(input())
A = [input() for _ in range(N)]

ans = 'correct'
for i in range(N):
  for j in range(i + 1, N):
    aij = A[i][j]
    aji = A[j][i]

    if aij == 'W' and aji != 'L': ans = 'incorrect'
    if aij == 'L' and aji != 'W': ans = 'incorrect'
    if aij == 'D' and aji != 'D': ans = 'incorrect'

print(ans)
