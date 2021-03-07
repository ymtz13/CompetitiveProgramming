N = int(input())
S = input()
x = 0
ans = 1
mod = 10**9+7
for c in S:
  if (c=='B' and x%2==0) or (c=='W' and x%2==1):
    x += 1
  elif x>0:
    ans = ans*x%mod
    x -= 1
  else:
    ans = 0

if x>0: ans = 0

for i in range(1, N+1):
  ans = ans*i%mod

print(ans)
