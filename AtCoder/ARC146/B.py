N, M, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(32, -1, -1):
  b = 1 << i

  #print()
  #print(i, M)
  #print('{:032b}'.format(b))
  #for a in A:
  #  print('{:032b}'.format(a), 'o' if a & b else b - a)

  k = 0
  Y = []
  X = []
  for a in A:
    if a & b:
      k += 1
      Y.append(a)
    else:
      X.append(a)

  m = 0
  X = sorted(X, reverse=True)[:max(K - k, 0)]
  for x in X:
    m += b - x

  if m <= M:
    M -= m
    ans += b

    A = Y + [0] * len(X)

  A = [a & (~b) for a in A]

print(ans)
