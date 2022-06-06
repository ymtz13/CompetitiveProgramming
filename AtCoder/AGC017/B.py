N, A, B, C, D = map(int, input().split())

diff = B - A
M = N - 1

if abs(diff) > M * D:
  print('NO')
  exit()

if C == 0:
  print('YES')
  exit()

# Mu + Md = M
# Mu - Md = X
# Mu = (M+X)//2
# Md = (M-X)//2

X = diff // C
if M % 2 != X % 2: X -= 1

Mu = (M + X) // 2
Md = M - Mu

if X * C + Mu * (D - C) >= diff:
  print('YES')
  exit()

if Md > 0 and (X + 2) * C - (Md - 1) * (D - C) <= diff:
  print('YES')
  exit()

print('NO')
