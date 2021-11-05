from collections import deque

A = [tuple(map(int, input().split())) for _ in range(4)]
T = [[0] * 4 for _ in range(4)]

for x in range(4):
  for y in range(4):
    if A[x][y]:
      sx, sy = x, y

ans = 0
for b in range(1, 1 << 16):
  ok = True
  cnt = 0
  for i in range(16):
    x, y = i // 4, i % 4
    t = (b >> i) & 1
    T[x][y] = t
    cnt += t

    if A[x][y] and not t:
      ok = False
      break

  if not ok: continue

  # 連結チェック
  cnt_check = 0
  queue = deque([(sx, sy)])
  while queue:
    x, y = queue.popleft()
    if T[x][y] != 1: continue
    T[x][y] = 2
    cnt_check += 1

    if x > 0: queue.append((x - 1, y))
    if y > 0: queue.append((x, y - 1))
    if x < 3: queue.append((x + 1, y))
    if y < 3: queue.append((x, y + 1))

  if cnt != cnt_check: continue

  for x in range(3):
    for y in range(3):
      if T[x][y] and T[x+1][y+1] and not T[x+1][y] and not T[x][y+1]:
        ok = False
      if not T[x][y] and not T[x+1][y+1] and T[x+1][y] and T[x][y+1]:
        ok = False

  if not ok: continue

  for ssx in range(1, 3):
    for ssy in range(1, 3):
      if T[ssx][ssy]: continue
      ok_close = False
      queue = deque([(ssx, ssy)])
      while queue:
        x, y = queue.popleft()
        if T[x][y] != 0: continue
        T[x][y] = 9
        
        if x==0 or y==0 or x==3 or y==3:
          ok_close = True
          continue
        queue.append((x - 1, y))
        queue.append((x, y - 1))
        queue.append((x + 1, y))
        queue.append((x, y + 1))
      
      if not ok_close: ok = False

  #if not ok:
  #  print()
  #  for row in T:
  #    print(row)

  if not ok: continue


  ans += 1

print(ans)
