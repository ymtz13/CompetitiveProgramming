N = list(map(int, input()))

S = sum(N)%3
K = [0]*3
for n in N: K[n%3]+=1

ans = -1
if S%3==0: ans = 0
if S%3==1:
  if K[1]>0: ans = 1
  elif K[2]>1: ans = 2
if S%3==2:
  if K[2]>0: ans = 1
  elif K[1]>1: ans = 2

if ans>=len(N): ans=-1
print(ans)