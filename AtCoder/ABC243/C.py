from collections import defaultdict

INF = 1 << 60

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
S = input()

DL = defaultdict(lambda: -INF)
DR = defaultdict(lambda: +INF)

for (x, y), d in zip(P, S):
  if d == 'L':
    DL[y] = max(DL[y], x)
  else:
    DR[y] = min(DR[y], x)

ans = 'No'
for y in DL:
  if DL[y] > DR[y]:
    ans = 'Yes'

print(ans)
