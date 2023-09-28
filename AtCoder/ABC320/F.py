def pp(dp):
  for i in range(H, -1, -1):
    v = []
    for j in range(H1):
      x = dp[i * H1 + j]
      v.append(x if x < INF else 'I')

    print('[{}]'.format(i), *v)


INF = 1 << 60

N, H = map(int, input().split())
X = list(map(int, input().split()))
PF = [tuple(map(int, input().split())) for _ in range(N - 1)] + [(0, 0)]

H1 = H + 1
H1sq = H1 * H1

dp = [INF] * H1sq
for i in range(H1):
  dp[H * H1 + i] = 0

prev = 0
for x, (p, f) in zip(X, PF):
  dp_slide = [INF] * H1sq

  d = x - prev
  prev = x
  for i in range(d, H1):
    for j in range(H1 - d):
      dp_slide[(i - d) * H1 + j + d] = dp[i * H1 + j]

  dp_next = dp_slide[:]

  for i in range(H1):
    for j in range(H1):
      idx_next = min(i + f, H) * H1 + j
      dp_next[idx_next] = min(dp_next[idx_next], dp_slide[i * H1 + j] + p)

  for i in range(H1):
    for j in range(H1):
      idx_next = i * H1 + j
      idx_slide = i * H1 + min(j + f, H)
      dp_next[idx_next] = min(dp_next[idx_next], dp_slide[idx_slide] + p)

  dp = dp_next

  #pp(dp)
  #print()

ans = INF
for i in range(H1):
  ans = min(ans, dp[i * H1 + i])

print(ans if ans < INF else -1)
