INF = 1 << 60

N, M = map(int, input().split())
S = [input() for _ in range(N)]

E = [[] for _ in range(N)]
Einv = [[] for _ in range(N)]

for i, s in enumerate(S):
  for j, c in enumerate(s, i + 1):
    if c == '1':
      E[i].append(j)
      Einv[j].append(i)

dpF = [INF] * N
dpB = [INF] * N
dpF[0] = 0
dpB[-1] = 0

for i in range(N - 1):
  dpi = dpF[i]
  for j in E[i]:
    dpF[j] = min(dpF[j], dpi + 1)

for i in range(N - 1, 0, -1):
  dpi = dpB[i]
  for j in Einv[i]:
    dpB[j] = min(dpB[j], dpi + 1)

Ans = []

for k in range(1, N - 1):
  ans = INF

  for i in range(max(0, k - M), k):
    di = dpF[i]
    for j in E[i]:
      if j <= k: continue
      dj = dpB[j]
      ans = min(ans, di + dj + 1)

  Ans.append(ans if ans < INF else -1)

print(*Ans)
