def f(X):
  ok = 0
  ng = 1500

  while ng - ok > 1:
    tgt = (ng + ok) // 2
    if tgt * (tgt + 1) // 2 <= X:
      ok = tgt
    else:
      ng = tgt

  return ok


def decomp(X):
  retval = []
  while X:
    n = f(X)
    retval.append(n)
    X -= n * (n + 1) // 2

  return retval


N = int(input())
R = decomp(N)
ans = [7] * (sum(R) + len(R) - 1)

s = 0
for i, r in enumerate(R[:-1]):
  s += r
  d = pow(10, s + i, 7)
  k = pow(d, 5, 7)
  ans[s + i] = k

print(''.join(map(str, ans[::-1])))
exit()

def test(R):
  return sum([r * (r + 1) // 2 for r in R])


maxL = 0
for i in range(1, 1000001):
  R = decomp(i)
  maxL = max(maxL, len(R))
  #print(i, test(R), R)
  if i % 100000 == 0: print(i)
  assert i == test(R)

print(maxL)
