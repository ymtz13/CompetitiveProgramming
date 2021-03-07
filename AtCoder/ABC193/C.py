N = int(input())
M = 100000
ans = N
X = [False]*(M+1)
for n in range(2, min(N, M)+1):
  if X[n]: continue

  p = n*n
  while p<=N:
    ans -= 1
    if p < len(X): X[p] = True
    p *= n

print(ans)
