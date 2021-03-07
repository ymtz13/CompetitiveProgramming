N = int(input())
H = [int(input()) for _ in range(N)]

upward = True
i = 0
h = H[0]
S = []

for j in range(1, N+1):
  if j==N or (upward and H[j]<H[j-1]) or (not upward and H[j]>H[j-1]):
    S.append((i, j-1))
    i = j-1
    upward = not upward

if len(S)%2 != 0: S.append((N-1, N-1)) 

ans = 0
for i in range(0, len(S), 2):
  ans = max(ans, S[i+1][1]-S[i][0] + 1)

print(ans)
