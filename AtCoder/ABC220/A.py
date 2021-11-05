A, B, C = map(int, input().split())


def solve(A, B, C):
  if A % C == 0: return A
  r = (A // C) * C + C
  return r if r <= B else -1


print(solve(A, B, C))