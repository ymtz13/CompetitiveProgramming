N = int(input())
S = [list(map(lambda c: 0 if c=='.' else 1, input())) for _ in range(N)]

def paint(r, c):
  for i in range(c+1): S[r][i] = 1
  if r+1<N:
    for i in range(c, N): S[r+1][i] = 1

ans = 0
for r in range(N):
  for c in range(N-1, -1, -1):
    if S[r][c]==0:
      ans += 1
      paint(r, c)

print(ans)
