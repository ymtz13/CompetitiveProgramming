N, M = map(int, input().split())

ans = (0, 0)
for K in range(1, 10):
  r = 0
  a = 0
  for i in range(1, N + 1):
    r = (r * 10 + K) % M
    if r==0: a = i
  
  if a>=ans[1]: ans=(K, a)

if ans[1]==0:
  print(-1)
  exit()

print(str(ans[0])*ans[1])
