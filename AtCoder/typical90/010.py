N = int(input())
X = [[0]*N for _ in range(2)]
for i in range(N):
  C, P = map(int, input().split())
  X[C-1][i] = P

S = [[0]*(N+1) for _ in range(2)]
for s, x in zip(S, X):
  for i in range(1, N+1):
    s[i] = s[i-1] + x[i-1]

for _ in range(int(input())):
  L, R = map(int, input().split())
  print(
    S[0][R] - S[0][L-1],
    S[1][R] - S[1][L-1],
  )
