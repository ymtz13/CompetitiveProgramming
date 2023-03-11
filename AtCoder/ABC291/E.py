N, M = map(int, input().split())
XY = [tuple(map(int, input().split())) for _ in range(M)]

Din = [0] * N
E = [[] for _ in range(N)]
for x, y in XY:
  Din[y - 1] += 1
  E[x - 1].append(y - 1)

Root = []
for i, din in enumerate(Din):
  if din == 0: Root.append(i)

ans = [None] * N

for a in range(1, N + 1):
  if len(Root) != 1:
    print('No')
    exit()

  root = Root[0]

  ans[root] = a

  Root = []
  for y in E[root]:
    Din[y] -= 1
    if Din[y] == 0: Root.append(y)

print('Yes')
print(*ans)
