S = [[c == '#' for c in input()] for _ in range(9)]

ans = 0
for i1 in range(81):
  x1 = i1 // 9
  y1 = i1 % 9
  for i2 in range(81):
    if i1 == i2: continue

    x2 = i2 // 9
    y2 = i2 % 9

    dx = x2 - x1
    dy = y2 - y1

    x3 = x2 + dy
    y3 = y2 - dx
    x4 = x1 + dy
    y4 = y1 - dx

    if x3 < 0 or 9 <= x3: continue
    if y3 < 0 or 9 <= y3: continue
    if x4 < 0 or 9 <= x4: continue
    if y4 < 0 or 9 <= y4: continue

    if S[x1][y1] and S[x2][y2] and S[x3][y3] and S[x4][y4]:
      ans += 1

print(ans // 4)
