H, W, Y, X = map(int, input().split())
S = ['#'*(W+2)] + [None]*H + ['#'*(W+2)]
for h in range(1, H+1):
  S[h] = '#' + input() + '#'

ans = 1
for h in range(Y-1, -1, -1):
  if S[h][X]=='.':
    ans += 1
  else:
    break

for h in range(Y+1, H+2, +1):
  if S[h][X]=='.':
    ans += 1
  else:
    break

for w in range(X-1, -1, -1):
  if S[Y][w]=='.':
    ans += 1
  else:
    break

for w in range(X+1, W+2, +1):
  if S[Y][w]=='.':
    ans += 1
  else:
    break

print(ans)