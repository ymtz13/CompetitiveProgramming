N = int(input())
ans = 0
for x in range(1, 10**6):
  if int(str(x)*2) <= N: ans += 1
print(ans)
