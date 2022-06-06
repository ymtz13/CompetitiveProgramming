N, L, W = map(int, input().split())
A = list(map(int, input().split()))

x = 0
ans = 0
for a in A + [L]:
  n = max(0, (a - x + W - 1) // W)
  ans += n
  x = a + W

print(ans)
