N, X = map(int, input().split())
ans = N
S = 0
for i in range(N):
  V, P = map(int, input().split())
  S += V*P
  if S>X*100: ans = min(ans, i)

print(ans+1 if ans<N else -1)
