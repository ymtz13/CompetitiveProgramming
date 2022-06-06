def gcd(x, y):
  while x:
    x, y = y % x, x
  return y


def lcm(x, y):
  return x * y // gcd(x, y)


T = int(input())

Ans = []

for _ in range(T):
  N, A, B, C1, CA, CB = map(int, input().split())

  # ASSERT perf(A) >= perf(B)
  if B * CA > A * CB: A, B, CA, CB = B, A, CB, CA

  # ASSERT perf(A) > perf(1)
  if CA >= A * C1:
    Ans.append((N * C1, 1))
    continue

  # ASSERT perf(B) > perf(1)
  if CB >= B * C1:
    nA = N // A
    n1 = N % A
    Ans.append((C1 * n1 + CA * nA, 2))
    continue

  if A >= 1000:
    ans = 1 << 60
    for nA in range(N):
      if A * nA > N: break

      nB = (N - nA * A) // B
      n1 = N - nA * A - nB * B
      ans = min(ans, C1 * n1 + CA * nA + CB * nB)
    Ans.append((ans, 3))
    continue

  if B >= 1000:
    ans = 1 << 60
    for nB in range(N):
      if B * nB > N: break

      nA = (N - nB * B) // A
      n1 = N - nA * A - nB * B
      ans = min(ans, C1 * n1 + CA * nA + CB * nB)
    Ans.append((ans, 4))
    continue

  ans = 1 << 60
  L = lcm(A, B)

  for n1 in range(min(A, B)):
    if n1 > N: continue
    K = N - n1

    Q = K // L
    R = K % L
    o = Q * (L // A) * CA

    print('{} * {} + {} = {} = {} - {}, cost = {}'.format(
        Q, L, R, K, N, n1, o))

    if A < B:
      for nB in range(R // B + 1):
        if (nB * B > R): continue
        if (R - nB * B) % A == 0:
          nA = (R - nB * B) // A
          ans = min(ans, C1 * n1 + CA * nA + CB * nB + o)
        
          print(  'nA, nB = {}, {} '.format(nA, nB))
    else:
      for nA in range(R // A + 1):
        if (nA * A > R): continue
        if (R - nA * A) % B == 0:
          nB = (R - nA * A) // B
          ans = min(ans, C1 * n1 + CA * nA + CB * nB + o)

  Ans.append((ans, 5))

for a in Ans:
  print(a[0])
