N, A, B, C, D = map(int, input().split())


def solve(N, XX, XY, YX, YY):
  if XX >= 1 and YY >= 1 and XY + YX == 0: return False
  return abs(XY - YX) <= 1


print('Yes' if solve(N, A, B, C, D) else 'No')
