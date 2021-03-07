N = int(input())
ans = 'second'
for _ in range(N):
  if int(input())%2==1: ans = 'first'
print(ans)
