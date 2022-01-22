p, n = input().split()
p = 1 - float(p)
n = int(n)

q = 1
while n:
  if n & 1: q = q * p + (1 - q) * (1 - p)
  n >>= 1
  p = p * p + (1 - p) * (1 - p)

print(1 - q)
