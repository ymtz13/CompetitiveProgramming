X, A, D, N = map(int, input().split())


def solve(X, A, D, N):
  if D == 0: return abs(X - A)

  M = A + D * (N - 1)

  if D < 0:
    A, M = M, A
    D = -D

  if X <= A: return A - X
  if X >= M: return X - M

  R = (X - A) % D
  return min(R, D - R)


print(solve(X, A, D, N))
