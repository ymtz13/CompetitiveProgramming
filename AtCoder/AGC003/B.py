N = int(input())
A = [int(input()) for _ in range(N)]
r = 0
ans = 0
for a in A:
  p = (a+r)//2
  ans += p
  r = (a+r)%2
  if a==0: r = 0

print(ans)
