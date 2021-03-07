N, M = map(int, input().split())
A = list(map(int, input().split()))
Q = [[] for _ in range(N)]
ans = N+2

if M==1:
  print(1 if min(A)==0 else 0)
  exit()

for i, a in enumerate(A):
  Q[max(  0, i-(M-1))].append((a, +1))
  Q[min(N-1, i+M    )].append((a, -1))

K = [0]*(N+1)
for q in Q[:N-M+1]:
  for a, d in q:
    if K[a]==0 and d==+1:
      st.update(a, 1)
    if K[a]==1 and d==-1:
      st.update(a, 0)
    K[a] += d
  
  ans = min(ans, calcMex(st))

print(ans)
