N, M = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  a, b = map(int, input().split())
  E[a - 1].append(b - 1)
  E[b - 1].append(a - 1)


def solve(x, k):
  queue = [x]
  visited = set()

  for _ in range(k):
    for q in queue:
      visited.add(q)

    queue_next = []
    for q in queue:
      for e in E[q]:
        if e not in visited: queue_next.append(e)

    queue = queue_next

  for q in queue:
    visited.add(q)

  return sum([q + 1 for q in visited])


Q = int(input())
ans = []
for _ in range(Q):
  x, k = map(int, input().split())
  ans.append(solve(x - 1, k))

for a in ans:
  print(a)
