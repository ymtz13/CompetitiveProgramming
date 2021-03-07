N, M, L = map(int, input().split())
P, Q, R = map(int, input().split())

D = [
  (P, Q, R), 
  (P, R, Q), 
  (Q, P, R), 
  (Q, R, P), 
  (R, P, Q), 
  (R, Q, P), 
]

ans = 0
for x, y, z in D:
  n = (N//x)*(M//y)*(L//z)
  ans = max(ans, n)
print(ans)
