from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

Deven = defaultdict(int)
Dodd  = defaultdict(int)

s = 0
Deven[0] = 1
ans = 0
for i, a in enumerate(A):
  s = a - s
  if i%2==0:
    ans += Dodd[s]
    ans += Deven[-s]
    Dodd[s] += 1
  else:
    ans += Deven[s]
    ans += Dodd[-s]
    Deven[s] += 1
    
print(ans)
