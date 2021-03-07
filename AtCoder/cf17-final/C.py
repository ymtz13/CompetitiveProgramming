N = int(input())
D = list(map(int, input().split()))
X = [0]*13
for d in D:
  X[d] += 1

if max(X)>2 or X[0]>0 or X[12]>1:
  print(0)
  exit()

A = [0]
if X[12]>0: A.append(12)
Z = []
for d in range(1,12):
  if X[d]==1: Z.append(d)
  if X[d]==2: A += [d, 24-d]

A = [None]*len(Z) + A

ans = 0

def dfs(i):
  global ans
  if i==len(Z):
    B = sorted(A) + [24]
    m = 100
    for i in range(len(B)-1):
      m = min(m, B[i+1]-B[i])
    ans = max(ans, m)
    return
  
  A[i]=Z[i]
  dfs(i+1)

  A[i]=24-Z[i]
  dfs(i+1)

dfs(0)
print(ans)
    



