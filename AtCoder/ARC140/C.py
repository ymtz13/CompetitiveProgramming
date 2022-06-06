N, X = map(int, input().split())


def f(N, d):
  if N % 2 == 1:
    v0 = N // 2 + 1
  else:
    if d == +1:
      v0 = N // 2
    else:
      v0 = N // 2 + 1

  ret = [v0]
  for i in range(N - 1):
    ret.append(ret[-1] + d)
    d = -(d + 1) if d > 0 else -(d - 1)

  return ret


def solve(N, X):
  P1 = f(N, +1)
  P2 = f(N, -1)

  if P1[0] == X: return P1
  if P2[0] == X: return P2

  P = f(N - 1, +1)

  ret = [X]
  for p in P:
    ret.append(p if p < X else p + 1)
  return ret

ans = solve(N, X)

print(' '.join(map(str, ans)))
