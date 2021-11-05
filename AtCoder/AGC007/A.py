H, W = map(int, input().split())
A = [[c == '#' for c in input()] + [False] for _ in range(H)]
A.append([False] * (W + 1))

s = 0
for r in A:
  s += r.count(True)

h = w = c = 0
while True:
  c += 1
  if A[h + 1][w]:
    h += 1
    continue
  if A[h][w + 1]:
    w += 1
    continue

  break

print('Possible' if s == c else 'Impossible')
