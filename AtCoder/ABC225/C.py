def ans(ans):
  print(ans)
  exit()


N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

b00 = B[0][0]
r = (b00 - 1) % 7

if r + len(B[0]) > 7: ans('No')

for i in range(M):
  if B[0][i] != b00 + i: ans('No')

for j in range(N):
  for i in range(M):
    if B[j][i] != B[0][i] + j * 7: ans('No')

ans('Yes')
