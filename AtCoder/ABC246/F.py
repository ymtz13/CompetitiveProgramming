N, L = map(int, input().split())
X = []
for _ in range(N):
  S = input()
  x = 0
  for c in S:
    x += 1 << (ord(c) - ord('a'))

  X.append(x)

B = [1 << i for i in range(26)]

ans = 0
mod = 998244353

for i in range(1, 1 << N):
  n = 0
  for b in B:
    if i & b: n += 1
  sign = +1 if n % 2 == 1 else -1

  z = (1 << 26) - 1
  for j, x in enumerate(X):
    if i & (1 << j): z &= x

  m = 0
  for b in B:
    if z & b: m += 1

  ans += pow(m, L, mod) * sign
  ans %= mod

print(ans)

#urusai
"""
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
"""