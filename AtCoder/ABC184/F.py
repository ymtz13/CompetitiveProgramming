N, T = map(int, input().split())
A = list(map(int, input().split()))

if N==1:
  print(A[0] if A[0]<=T else 0)
  exit()

if min(A)>T:
  print(0)
  exit()

def dfs(i, A, t, L):
  if i==len(A):
    L.append(t)
    return
  
  dfs(i+1, A, t, L)
  dfs(i+1, A, t+A[i], L)

A1 = A[:N//2]
A2 = A[N//2:]

L1 = []
L2 = []

dfs(0, A1, 0, L1)
dfs(0, A2, 0, L2)

L1.sort(reverse=True)
L2.sort()
L2.append(10**10)

#print(L1)
#print(L2)

ans = 0
i = -1
for x in L1:
  while x + L2[i+1]<=T: i+=1
  if i>=0: ans = max(ans, x + L2[i])
print(ans)
