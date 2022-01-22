N, D = map(int, input().split())
W = [tuple(map(int, input().split())) for _ in range(N)]
W.sort(key=lambda w: w[1])

ans = 0
d = -1
for L, R in W:
  if d < L:
    ans += 1
    d = R + D - 1

print(ans)
