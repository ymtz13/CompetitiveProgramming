from heapq import heappop, heappush

N, M = map(int, input().split())

row = list(range(1, N + 1))
events = [tuple(map(int, input().split())) for _ in range(M)]
ans = [0] * (N + 1)

while events:
  e = heappop(events)

  if e[1] != -1:
    T, W, S = e
    if not row:
      continue

    person = heappop(row)
    ans[person] += W
    heappush(events, (T + S, -1, person))
  else:
    person = e[2]
    heappush(row, person)

for a in ans[1:]:
  print(a)