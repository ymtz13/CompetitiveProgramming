def solve(A, B):
  if B % A == 0: return 0
  if B < A: return A - B

  D = B // A

  a = A * (D + 1) - B
  for d in range(max(D - 100000, 1), D + 1):
    Y = 0 if B % d == 0 else d - B % d
    X = (B + Y) // d - A
    a = min(a, X + Y)

  for X in range(100000):
    AX = A + X
    Y = 0 if B % AX == 0 else AX - B % AX
    a = min(a, X + Y)

  return a


T = int(input())

ans = []
for _ in range(T):
  A, B = map(int, input().split())

  a = solve(A, B)
  ans.append(a)

for a in ans:
  print(a)
