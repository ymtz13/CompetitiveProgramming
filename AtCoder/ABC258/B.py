N = int(input())
A = [tuple(map(int, input())) for _ in range(N)]

ans = 0
for x in range(N):
  for y in range(N):
    for dx in (-1, 0, +1):
      for dy in (-1, 0, +1):
        if dx == 0 and dy == 0: continue
        s = 0
        for i in range(N):
          s *= 10
          s += A[x][y]

          x += dx
          y += dy
          x %= N
          y %= N

        ans = max(ans, s)

print(ans)
