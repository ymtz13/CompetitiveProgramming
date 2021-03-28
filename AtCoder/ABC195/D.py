N, M, Q = map(int, input().split())
WV = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda wv: -wv[1]) 
X = list(map(int, input().split()))

for _ in range(Q):
  L, R = map(int, input().split())
  B = sorted(X[:L-1] + X[R:])
  ans = 0
  U = [False]*M
  for w, v in WV:
    for ix, x in enumerate(B):
      if x>=w and not U[ix]: 
        ans += v
        U[ix] = True
        break

  print(ans)

