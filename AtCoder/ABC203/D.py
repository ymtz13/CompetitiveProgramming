N, K = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]
B = [[None]*N for _ in range(N)]

half = K*K//2 if K%2==0 else K*K//2+1

def check(v):
  for i in range(N):
    for j in range(N):
      B[i][j] = (A[i][j] <= v)

  R = [[0]*(N+1) for _ in range(N)]
  for brow, rrow in zip(B, R):
    for i, (b, r) in enumerate(zip(brow, rrow)):
      rrow[i+1] = r + (1 if b else 0)
  
  S = [[0]*(N+1) for _ in range(N+1)]
  for i in range(1, N+1):
    for j in range(N):
      S[j+1][i] = S[j][i] + R[j][i]

  for i in range(N-K+1):
    for j in range(N-K+1):
      count = S[i+K][j+K] - S[i+K][j] - S[i][j+K] + S[i][j]
      if count >= half: return True
      #print(i, j, count)

  #print(R)
  #print(S)

  return False

#check(5)
#exit()

ok = 10**9
ng = -1
while ok-ng>1:
  tgt = (ok+ng)//2
  if check(tgt):
    ok = tgt
  else:
    ng = tgt

print(ok)
