N = int(input())
A = list(map(int, input().split()))[:8]
M = len(A)
R = [[] for _ in range(200)]

def dfs(i):
  global Y
  if i==M:
    if len(Y)>0: R[sum(X)%200].append(tuple(Y))
    return
  
  X[i] = 0
  dfs(i+1)

  X[i] = A[i]
  Y.append(i+1)
  dfs(i+1)
  X[i] = None
  Y = Y[:-1]

X = [None]*M
Y = []
dfs(0)

for r in R:
  if len(r)>=2:
    print('Yes')
    B = r[0]
    C = r[1]
    print(len(B), ' '.join(map(str, B)))
    print(len(C), ' '.join(map(str, C)))
    exit()
    
print('No')
