def rotate(A, L, N):
  vL = A[L]
  for i in range(L, L + N - 1):
    A[i] = A[i + 1]
  A[L + N - 1] = vL


P = [4, 9, 5, 7, 11, 13, 17, 19, 23]
O = [2, 6, 4, 6, 10, 12, 16, 18, 22]

prod = 1
for p in P:
  prod *= p

I = [[pow(p, o - 1, m) if p != m else 1 for p in P] for m, o in zip(P, O)]
PP = []
for m, row in zip(P, I):
  pp = 1
  for p in row:
    pp *= p
  PP.append(pp % m)

M = sum(P)
A = list(range(1, M + 1))

s = 0
for p in P:
  rotate(A, s, p)
  s += p

print(M)
print(*A)

B = list(map(int, input().split()))

ans = 0
s = 0
for p, pp in zip(P, PP):
  r = B[s] - A[s]
  ans += pp * r * prod // p
  s += p

ans %= prod

print(ans + 1)
