X, K = input().split()
K = int(K)

Z = [0] * 20
for i, c in enumerate(X[::-1]):
  Z[i] = int(c)

for i in range(K):
  c = 1 if Z[i] >= 5 else 0
  for j in range(i + 1):
    Z[j] = 0

  for j in range(i + 1, 20):
    Z[j] += c
    c = Z[j] // 10
    Z[j] %= 10

ans = 0
for i, z in enumerate(Z):
  ans += z * (10**i)

print(ans)
