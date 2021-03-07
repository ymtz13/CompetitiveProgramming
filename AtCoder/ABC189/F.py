N, M, K = map(int, input().split())
A = set(map(int, input().split()))

P = [0]*(N+M+1)
S = [0]*(N+1)
P[0] = 1
S[1] = 1

X = [0]*(N+M+1)
T = [0]*(N+1)

Z = [0]*(N+1)
Z[1] = 1

for i in range(1, N+M):
  p = (S[min(N, i)] - S[max(0, i-M)])/M

  #L = min(N, i) - max(0, i-M)
  L = Z[min(N, i)] - Z[max(0, i-M)]
  if L==0:
    print(-1)
    exit()
  x = (T[min(N, i)] - T[max(0, i-M)])/L + 1

  P[i] = p
  X[i] = x

  if i < N:
    a = i not in A
    S[i+1] = S[i] + p if a else S[i]
    T[i+1] = T[i] + x if a else T[i]
    Z[i+1] = Z[i] + 1 if a else Z[i]

Pok = 0
Lok = 0
for i in range(N, N+M):
  Pok += P[i]
  Lok += X[i]*P[i]
Lok /= Pok

if 1-Pok<1e-10:
  print(Lok)
  exit()

Png = 1 - Pok
Lng = 0
for i in range(1, N-1):
  if i not in A: continue
  Lng += X[i]*P[i]/Png

ans = Lok
k = Lng*p
pp = (1-p)
for n in range(100000):
  ans += k*pp*n
  pp *= 1-p

print(ans)
