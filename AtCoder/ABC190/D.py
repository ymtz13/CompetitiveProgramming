N = int(input())
M = 2*N
p = 1
D = set()
while p*p<=M:
  if M%p==0:
    D.add(p)
    D.add(M//p)
  p += 1

ans = 0
for d in D:
  f = M//d
  if (f-d+1)%2==0: ans += 1

print(ans)
