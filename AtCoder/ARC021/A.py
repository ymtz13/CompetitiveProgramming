A = [tuple(map(int, input().split())) for _ in range(4)]
ans = 'GAMEOVER'
for i in range(4):
  for j in range(3):
    if A[i][j] == A[i][j+1]: ans = 'CONTINUE'
    if A[j][i] == A[j+1][i]: ans = 'CONTINUE'

print(ans)