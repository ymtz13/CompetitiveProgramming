H, W = map(int, input().split())
C = [[0] * (W + 2) for _ in range(H + 2)]

for h in range(1, H + 1):
  S = input()
  for w, c in enumerate(S, 1):
    x = 0 if c == '.' else int(c)
    C[h][w] = x

for h in range(1, H + 1):
  for w in range(1, W + 1):
    if C[h][w] > 0: continue

    used = [True] + [False] * 5
    used[C[h - 1][w]] = True
    used[C[h + 1][w]] = True
    used[C[h][w - 1]] = True
    used[C[h][w + 1]] = True
    for x, u in enumerate(used):
      if not u:
        C[h][w] = x
        break

  print(''.join(map(str, C[h][1:-1])))
