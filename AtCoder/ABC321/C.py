X = []

for b in range(1, 1 << 10):
  x = [str(9 - i) for i in range(10) if (b >> i) & 1]
  n = int(''.join(x))
  X.append(n)

X.sort()
K = int(input())
print(X[K])
