N, A, B = map(int, input().split())


def gcd(a, b):
  while a:
    a, b = b % a, a
  return b


def s(n, d):
  return d * n * (n + 1) // 2


LCM = A * B // gcd(A, B)

nA = N // A
nB = N // B
nL = N // LCM

ans = s(N, 1) - s(nA, A) - s(nB, B) + s(nL, LCM)
print(ans)
