from math import sqrt

N, M = map(int, input().split())
L = N + M
LL = 1 << L

XY = [tuple(map(int, input().split())) for _ in range(N)]
PQ = [tuple(map(int, input().split())) for _ in range(M)]
C = XY + PQ

D0 = [0] * L
D = [[0] * L for _ in range(L)]
for i, (xi, yi) in enumerate(C):
  D0[i] = sqrt(xi * xi + yi * yi)
  for j, (xj, yj) in enumerate(C):
    dx = xj - xi
    dy = yj - yi
    D[i][j] = D[j][i] = sqrt(dx * dx + dy * dy)

Speed = []
for visited in range(LL):
  s = 0
  for i in range(N, N + M):
    if visited & (1 << i): s += 1
  Speed.append(1 << s)

INF = 1 << 60
T = [INF] * LL * L

for i in range(L):
  T[i * LL + (1 << i)] = D0[i]


def pp(T):
  for i, t in enumerate(T):
    if t == INF: continue
    node = i // LL
    visited = i % LL
    print(node, '{:010b}'.format(visited), t)


#pp(T)

for next_visited in range(1, LL):
  for to in range(L):
    bit_to = 1 << to
    if not (next_visited & bit_to): continue

    visited = next_visited - bit_to
    speed = Speed[visited]

    if visited == 0: break

    t = INF
    for fro in range(L):
      bit_from = 1 << fro
      if not (visited & bit_from): continue

      t = min(t, T[fro * LL + visited] + D[fro][to] / speed)

    #print('set', to, '{:010b}'.format(visited), t)
    T[to * LL + next_visited] = t

    #pp(T)

#print(T)

ALL = (1 << N) - 1
ans = INF
for i in range(1 << M):
  visited = ALL + (i << N)
  speed = Speed[visited]
  for fro in range(L):
    time = T[fro * LL + visited] + D0[fro] / speed
    ans = min(ans, time)

print(ans)
