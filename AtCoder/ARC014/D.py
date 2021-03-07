A, N, M = map(int, input().split())
L = [int(input()) for _ in range(N)]
D = sorted([L[i+1]-L[i]-1 for i in range(N-1)])
L1 = L[0]
LN = L[-1]

Q = []
for m in range(M):
  x, y = map(int, input().split())
  Q.append((x+y, x, y, m))
Q = sorted(Q)

ans = []
n = N
s = 0
i = 0
for r, x, y, m in Q:
  while i<N-1 and D[i]<=r:
    n -= 1
    s += D[i]
    i+=1
  a = r*n + N + s - x + min(x, L1-1) - y + min(y, A-LN)
  ans.append((m, a))
ans = sorted(ans)

for m, a in ans:
  print(a)