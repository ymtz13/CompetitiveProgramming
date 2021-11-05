N, C = map(int, input().split())
A = list(map(int, input().split()))

X = [[] for _ in range(C)]
for i, a in enumerate(A):
  X[a-1].append(i)

for x in X:
  x.append(N)
  p = -1
  ans = N*(N+1)//2
  for i in x:
    l = i-p-1
    ans -= l*(l+1)//2
    p = i
  print(ans)
