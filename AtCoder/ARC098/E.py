N, K, Q = map(int, input().split())
A = list(map(int, input().split()))

INF = 1 << 60
ans = INF

for Y in A:
  G = [[]]
  for a in A:
    if a < Y:
      if G[-1]: G.append([])
    else:
      G[-1].append(a)

  B = []
  for g in G:
    n = len(g) - K + 1
    if n > 0: B.extend(sorted(g)[:n])

  if len(B) < Q: continue

  X = sorted(B)[Q - 1]
  ans = min(ans, X - Y)

print(ans)
