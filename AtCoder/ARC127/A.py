N = list(map(int, input()))


def g(N):
  NV = int(''.join(map(str, N)))
  D = len(N)

  r = 0
  X = [0] * D
  for i in range(D):
    X[i] = 1
    XV = int(''.join(map(str, X)))

    r += NV - XV + 1
    print(i, NV, XV, X)

  return r


ans = g(N)

for d in range(1, len(N)):
  ans += g([9] * d)

print(ans)
