from bisect import bisect_left

N, M, Q = map(int, input().split())
Bus = []
From = [[] for _ in range(N)]
for i in range(M):
  A, B, S, T = tuple(map(int, input().split()))
  Bus.append((i, A - 1, B - 1, S, T))
  From[A - 1].append((S, i))

for f in From:
  f.sort()

#print(Bus)
#print(From)

# バスから次に乗るバスへ辺を張る
K = 20
E = [[None] * M for _ in range(K)]

for i, _, b, _, t in Bus:
  ifrom = bisect_left(From[b], (t, -1))
  if ifrom < len(From[b]):
    next_bus = From[b][ifrom]
    E[0][i] = next_bus[1]

#print(E[0])

# 2^k回後に乗るバスへ辺を張る
for k in range(1, K):
  for m in range(M):
    next_bus = E[k - 1][m]
    if next_bus is not None:
      next_next_bus = E[k - 1][next_bus]
      E[k][m] = next_next_bus


def get_next_x_bus(start, x):
  now_bus = start
  for k in range(K):
    b = 1 << k
    if x & b: now_bus = E[k][now_bus]

    if now_bus is None: return None

  return Bus[now_bus]


for _ in range(Q):
  X, Y, Z = map(int, input().split())
  y = Y - 1

  ifrom = bisect_left(From[y], (X, -1))
  first_bus = From[y][ifrom] if ifrom < len(From[y]) else None

  # 時刻XからZまでの間にYからバスが出ていないなら、Yにとどまっている
  if first_bus is None or first_bus[0] >= Z:
    print(Y)
    continue

  # 最後に乗ったバスを二分探索で求める
  take = 0
  last_bus = first_bus[1]
  not_take = M + 1

  while not_take - take > 1:
    tgt = (take + not_take) // 2
    bus = get_next_x_bus(first_bus[1], tgt)

    if bus is None:
      not_take = tgt
      continue

    i, _, _, S, _ = bus
    if S >= Z:
      not_take = tgt
      continue

    else:
      take = tgt
      last_bus = i

  _, a, b, _, T = Bus[last_bus]
  if Z <= T:
    print(a + 1, b + 1)
  else:
    print(b + 1)
