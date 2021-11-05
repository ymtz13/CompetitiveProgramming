from functools import cmp_to_key

N = int(input())
P = []
INF = 1 << 40

for i in range(N):
  x, y = map(int, input().split())
  P.append((x * 2 - 2, y * 2, 1, i))
  P.append((x * 2, y * 2 - 2, 0, i) if y > 1 else (INF, 2, 0, i))


def cmp(v1, v2):
  x1, y1, t1, _ = v1
  x2, y2, t2, _ = v2
  return x1 * y2 - x2 * y1 + t1 - t2


P.sort(key=lambda v: v[0] / v[1])
P.sort(key=cmp_to_key(cmp))
E = [None] * N
dp = [0] * (N * 2)
for j, (_, _, t, i) in enumerate(P):
  dp[j] = dp[j - 1]

  if t == 1:
    E[i] = j
  else:
    dp[j] = max(dp[j], dp[E[i]] + 1)

print(dp[-1])
