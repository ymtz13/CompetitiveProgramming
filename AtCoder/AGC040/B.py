N = int(input())
Q = [tuple(map(int, input().split())) for _ in range(N)]
Q = [(L, R + 1) for L, R in Q]

QS = sorted(Q, key=lambda x: (x[1], x[0]))
L0, R0 = QS[0]
QM = max([R - L for L, R in QS[1:]])

ans = max(R0 - L0, QM)

G = [[]]
for L, R in sorted(Q, reverse=True):
  if G[-1] and G[-1][0] and G[-1][0][0] != L:
    G.append([])
  G[-1].append((L, R))

#print(G)
#print(L0, R0)
#print(QS)
#print(QM)

Lmax = None
Rmin = None

for g in G:
  L = g[0][0]
  R = min([r for l, r in g])

  if Lmax is None:
    ans = max(ans, QM + max(0, R0 - L))
    Lmax = L
    Rmin = R

  else:
    ans = max(ans, Rmin - Lmax + R0 - L)

  Rmin = min(Rmin, R)

print(ans)
