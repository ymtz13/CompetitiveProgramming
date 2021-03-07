N = int(input())
A = list(map(int, input().split()))

gmax = 0
ans = None
for k in range(2,1001):
  g = 0
  for a in A:
    if a%k==0: g+=1
  if g>gmax:
    ans = k
    gmax = g

print(ans)