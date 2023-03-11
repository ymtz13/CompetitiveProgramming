N = int(input())
A = list(map(int, input().split()))
#A  = [1]*N

X = 10**12
INF = 1 << 60

D = [[INF] * N for _ in range(N)]
for f in range(N):
  S = input()
  for t, c in enumerate(S):
    if c == 'Y': D[f][t] = X - A[t]

for k in range(N):
  for f in range(N):
    for t in range(N):
      d = D[f][k] + D[k][t]
      if D[f][t] > d: D[f][t] = d

Q = int(input())
ans = []

for _ in range(Q):
  U, V = map(int, input().split())
  U -= 1
  V -= 1

  s = -A[U] + D[U][V]

  n = (s // X) + 1
  m = -s + n * X
  ans.append((n, m))

for n, m in ans:
  if n > N:
    print('Impossible')
  else:
    print(n, m)
