N = int(input())
A = list(map(int, input()))

X = [abs(A[i] - A[i + 1]) for i in range(N - 1)]

if 1 in X:
  X = [x % 2 for x in X]
  a = 1

else:
  X = [x // 2 for x in X]
  a = 2


def factorize(x):
  n = 0
  while x and x % 2 == 0:
    n += 1
    x //= 2
  return n


s = 0
c = 0
for i in range(N - 1):
  if i > 0:
    n1 = factorize(i)
    n2 = factorize(N - 1 - i)
    c += n2 - n1
    #print('{} == [odd] * 2^{}'.format(i, n1))
    #print('{} == [odd] * 2^{}'.format(N - 1 - i, n2))


  p = 1 if i == 0 or i == N - 2 or c == 0 else 0
  #print('comb({}, {}) % 2 == {}'.format(N - 2, i, p), c)

  s ^= X[i] * p

print(a * s)
