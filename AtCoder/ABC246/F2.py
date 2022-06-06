N, L = map(int, input().split())
X = []
for _ in range(N):
  S = input()
  x = 0
  for c in S:
    x += 1 << (ord(c) - ord('a'))

  X.append(x)

for x in X:
  print('{:10b}'.format(x))

B = [1 << i for i in range(26)]

ans = 0
mod = 998244353
for s in range(1 << 26):
  n = 0
  for b in B:
    if s & b: n += 1

  for x in X:
    if not (s & (~x)):
      print('{:10b} {:10b}'.format(s, x))
      ans += pow(n, L, mod)
      ans %= mod
      break
