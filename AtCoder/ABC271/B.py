N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

ans = []
for _ in range(Q):
  s, t = map(int, input().split())
  ans.append(A[s - 1][t])

for a in ans:
  print(a)
