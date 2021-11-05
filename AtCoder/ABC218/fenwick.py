K = 20
val = [0] * (K + 1)


def addf(i, x):
  while i <= K:
    val[i] += x
    i += i & -i


def sumf(i):
  ret = 0
  while i > 0:
    ret += val[i]
    i -= i & -i
  return ret


def getf(i):
  ok = K + 1
  ng = -1
  while ok - ng > 1:
    tgt = (ng + ok) // 2
    if sumf(tgt) >= i:
      ok = tgt
    else:
      ng = tgt

  return ok


add(3, 5)
print(val[1:])

add(5, 2)
print(val[1:])

add(K, 10)
print(val[1:])

print(2, sum(2))
print(3, sum(3))
print(4, sum(4))
print(5, sum(5))
print(6, sum(6))
print(K, sum(K))

print('---')
for n in range(20):
  print(n, get(n))
