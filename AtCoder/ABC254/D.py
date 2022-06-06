from bisect import bisect

N = int(input())

Sq = [n * n for n in range(1, N + 20)]

F = [0] * (N + 1)
for p in range(2, N + 1):
  if F[p] != 0: continue
  for q in range(p, N + 1, p):
    F[q] = p


def factorize(x):
  fs = set()
  while F[x]:
    f = F[x]
    x //= f
    fs.add(f) if f not in fs else fs.remove(f)

  ret = 1
  for f in fs:
    ret *= f
  return ret


ans = 0
for i in range(1, N + 1):
  x = factorize(i)
  m = N // x
  c = bisect(Sq, m)
  ans += c

print(ans)
