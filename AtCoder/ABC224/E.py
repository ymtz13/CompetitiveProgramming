from collections import defaultdict

H, W, N = map(int, input().split())
Q = [(i, *map(int, input().split())) for i in range(N)]
P = sorted(Q, key=lambda x: -x[3])

a = P[0][3]
G = [[]]
for p in P:
  if a != p[3]:
    a = p[3]
    G.append([])
  G[-1].append(p)

R = [0] * H
C = [0] * W
ans = [None] * N

for g in G:
  UR = defaultdict(int)
  UC = defaultdict(int)
  for i, r, c, _ in g:
    v = max(R[r - 1], C[c - 1])
    ans[i] = v
    UR[r - 1] = max(UR[r - 1], v + 1)
    UC[c - 1] = max(UC[c - 1], v + 1)

  for r, v in UR.items():
    R[r] = v
  for c, v in UC.items():
    C[c] = v

for a in ans:
  print(a)
