from bisect import bisect

N = int(input())
M = 1 << 20

X = [True] * M
P = []
ans = 0
for q in range(2, M):
  if not X[q]: continue

  q3 = q * q * q
  pmax = N // q3
  ans += bisect(P, pmax)

  P.append(q)
  for i in range(q, M, q):
    X[i] = False

print(ans)
