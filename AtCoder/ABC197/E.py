from collections import defaultdict

N = int(input())
INF = 10**20
fINF = lambda: INF

Xmin = [+INF]*(N+1)
Xmax = [-INF]*(N+1)
for _ in range(N):
  X, C = map(int, input().split())
  Xmin[C] = min(Xmin[C], X)
  Xmax[C] = max(Xmax[C], X)

dp = defaultdict(fINF)
dp[0] = 0
for C in range(1, N+1):
  if Xmin[C]==INF: continue
  xmin, xmax = Xmin[C], Xmax[C]

  dp_new = defaultdict(fINF)
  for loc, time in dp.items():
    if   xmin > loc: dp_new[xmax] = min(dp_new[xmax], time + xmax - loc)
    elif xmax < loc: dp_new[xmin] = min(dp_new[xmin], time + loc - xmin)
    else:
      dl = loc - xmin
      dr = xmax - loc
      dp_new[xmax] = min(dp_new[xmax], time + dl*2 + dr)
      dp_new[xmin] = min(dp_new[xmin], time + dr*2 + dl)
  
  dp = dp_new

ans = min([abs(k)+v for k, v in dp.items()])
print(ans)
