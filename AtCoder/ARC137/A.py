def gcd(a, b):
  while a:
    a, b = b % a, a
  return b


L, R = map(int, input().split())

ans = 1
for l in range(L, L + 1000):
  for r in range(max(R - 1000, l + 1), R + 1):
    if gcd(l, r) == 1:
      ans = max(ans, r - l)

print(ans)
