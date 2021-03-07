def gcd(a, b):
  if a>b: a, b = b, a
  while a: a, b = b%a, a
  return b

ans = 1
for n in range(2, 31):
  ans = ans * n // gcd(ans, n)
ans += 1

print(ans)
