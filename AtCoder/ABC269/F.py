mod = 998244353

N, M = map(int, input().split())


def series(a0, n, d):
  return (a0 * n + d * (n - 1) * n // 2) % mod


def S(P, Q):
  if P <= 0 or Q <= 0: return 0

  P2 = P // 2
  Q2 = Q // 2

  #R = (M + 3) * Q2 + 2 * (Q2 - 1) * Q2
  #S = R * P2 + 2 * M * Q2 * (P2 - 1) * P2
  R = series(M + 3, Q2, 4)
  S = series(R, P2, 4 * M * Q2)

  if P % 2 == 1:
    S += series((P - 1) * M + 1, Q2, 2)

  if Q % 2 == 1:
    S += series(Q, P2, M * 2)

  if P % 2 == 1 and Q % 2 == 1:
    S += (P - 1) * M + Q

  return S % mod


Q = int(input())
ans = []
for _ in range(Q):
  A, B, C, D = map(int, input().split())

  S00 = S(A - 1, C - 1)
  S01 = S(A - 1, D)
  S10 = S(B, C - 1)
  S11 = S(B, D)

  a = (S11 - S10 - S01 + S00) % mod
  ans.append(a)

for a in ans:
  print(a)
