N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
M = 10**10
S = {x * M + y for x, y in P}

ans = 0
for i, (x1, y1) in enumerate(P):
  for (x2, y2) in P[i + 1:]:
    if x1 == x2 or y1 == y2: continue
    if (x1 * M + y2 in S) and (x2 * M + y1) in S: ans += 1

print(ans // 2)
