from collections import defaultdict

N = int(input())
D = defaultdict(int)
for p in range(2, 10**6+10):
  while N%p==0:
    N//=p
    D[p] += 1
if N>1: D[N] += 1

S = sum(D.values())
if S==1:
  print(0)
  exit()

S-=1
ans = 1
while S>1:
  S//=2
  ans += 1
print(ans)
