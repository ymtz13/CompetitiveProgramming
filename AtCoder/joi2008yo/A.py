X = 1000 - int(input())

ans = 0
for v in [500, 100, 50, 10, 5, 1]:
  cnt = X // v
  ans += cnt
  X -= cnt * v

print(ans)
