N = int(input())
A = list(map(int, input().split()))
C = [0] * (1 << 20)
S = [0] * (1 << 20)
Xij = 0
Xjk = 0
Xik = 0

for i, a in enumerate(A):
  nL = i
  nR = N - 1 - i

  Xij += C[a] * nR
  Xjk += S[a]
  Xik += (i - 1) * C[a] - S[a]

  C[a] += 1
  S[a] += i

Xijk = 0
for c in C:
  if c < 3: continue
  Xijk += c * (c - 1) * (c - 2) // 6

Z = N * (N - 1) * (N - 2) // 6
print(Z - Xij - Xjk - Xik + Xijk * 2)
