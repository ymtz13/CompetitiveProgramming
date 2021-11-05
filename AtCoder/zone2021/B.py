N, D, H = map(int, input().split())
ans = 0
for i in range(N):
  d, h = map(int, input().split())
  x = (h*D-H*d)/(D-d)
  ans = max(ans, x)
print(ans)
