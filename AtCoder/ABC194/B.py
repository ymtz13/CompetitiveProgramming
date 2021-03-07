N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

ans = 10**6
for i, (a, _) in enumerate(AB):
  for j, (_, b) in enumerate(AB):
    if i==j:
      ans = min(ans, a+b)
    else:
      ans = min(ans, max(a, b))

print(ans)
