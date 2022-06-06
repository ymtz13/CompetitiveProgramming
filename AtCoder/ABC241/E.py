N, K = map(int, input().split())
A = list(map(int, input().split()))

X = 0
S = [None] * N
C = [None] * N
cnt = 0
while (S[X % N] is None) and cnt < K:
  S[X % N] = X
  C[X % N] = cnt
  X += A[X % N]
  cnt += 1

if cnt == K:
  print(X)
  exit()

#print(S, C)

nloop = cnt - C[X % N]
sloop = X - S[X % N]
#print(nloop, sloop)

cloop = (K - C[X % N]) // nloop

ans = S[X % N] + cloop * sloop

for _ in range(K - C[X % N] - nloop * cloop):
  ans += A[X % N]
  X += A[X % N]

print(ans)
