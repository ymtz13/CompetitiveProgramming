from math import gcd

T = int(input())
ans = []

for _ in range(T):
  N, D, K = map(int, input().split())

  g = gcd(N, D)
  L = N // g

  S = (K - 1) // L
  T = (K - 1) % L

  a = D * T % N + S
  ans.append(a)

for a in ans:
  print(a)