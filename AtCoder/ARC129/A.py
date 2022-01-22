N, L, R = map(int, input().split())


def f(N, X):
  a = 0
  for i in range(60):
    if N & (1 << i) == 0: continue
    s = (1 << (i + 1)) - 1
    m = (1 << i) - 1
    a += max(0, min(s, X) - m)

  return a


ans = f(N, R) - f(N, L - 1)
print(ans)
