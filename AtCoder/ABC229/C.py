N, W = map(int, input().split())
C = [tuple(map(int, input().split())) for _ in range(N)]
C.sort(reverse=True)

ans = 0
w = 0
for a, b in C:
  c = min(b, W - w)
  ans += a * c
  w += c

print(ans)
