R, C, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]

ans = 0
for r, row in enumerate(A):
  for c, a in enumerate(row):
    if r+c<=D and (r+c)%2 == D%2:
      ans = max(ans, a)
print(ans)
