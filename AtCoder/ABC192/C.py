N, K = map(int, input().split())

def g(x: int, reverse: bool):
  return int(''.join(sorted(list(str(x)), reverse=reverse)))

def f(x: int):
  return g(x, True) - g(x, False)

for k in range(K):
  N = f(N)

print(N)
