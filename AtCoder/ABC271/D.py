N, S = map(int, input().split())
C = [tuple(map(int, input().split())) for _ in range(N)]

M = 10010
dp = [None] * M
dp[0] = (-1, -1)
DP = [dp]

for a, b in C:
  dp_next = [None] * (M + 110)
  for i, v in enumerate(dp[:M]):
    if not v: continue

    dp_next[i + a] = (i, 'H')
    dp_next[i + b] = (i, 'T')

  dp = dp_next
  DP.append(dp)

if not dp[S]:
  print('No')
  exit()

print('Yes')

ans = []
i = S
for dp in DP[::-1]:
  i, a = dp[i]
  ans.append(a)

print(''.join(ans[-2::-1]))
