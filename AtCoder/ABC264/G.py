INF = 1 << 40

Z = 26
M = 1 + Z + Z * Z  # 1 + 26 + 26^2
M2 = M * M
oa = ord('a')

E = [0] * (M2)
for f in range(M):
  E[f * M] = INF

for t in range(Z+1, M):
  E[t] = INF

for f in range(1, M):
  for t in range(1, Z + 1):
    E[f * M + t] = INF

N = int(input())
for _ in range(N):
  T, P = input().split()
  P = int(P)

  if len(T) == 1:
    c = ord(T) - oa

    t = c + 1
    E[1 + c] -= P  # _ -> c

    for f in range(1, Z + 1):
      t = (f - 1) * Z + c + Z + 1
      E[f * M + t] -= P

    for f in range(Z + 1, M):
      t = ((t - Z - 1) % Z) * Z + c + Z + 1
      E[f * M + t] -= P

  if len(T) == 2:
    c0 = ord(T[0]) - oa
    c1 = ord(T[1]) - oa

    f = c0 + 1
    t = c0 * Z + c1 + Z + 1
    E[f * M + t] -= P

    for f in range(c0 + 27, M, Z):
      E[f * M + t] -= P

  if len(T) == 3:
    c0 = ord(T[0]) - oa
    c1 = ord(T[1]) - oa
    c2 = ord(T[2]) - oa

    f = c0 * Z + c1 + Z + 1
    t = c1 * Z + c2 + Z + 1
    E[f * M + t] -= P

dist = [INF] * M
dist[0] = 0

for _ in range(M):
  for f, df in enumerate(dist):
    for t, dt in enumerate(dist):
      if f == t: continue
      d = df + E[f * M + t]
      if dt > d: dist[t] = d

for f, df in enumerate(dist):
  for t, dt in enumerate(dist):
    if f == t: continue
    d = df + E[f * M + t]
    if dt > d:
      print('Infinity')
      exit()

print(-min(dist[1:]))
