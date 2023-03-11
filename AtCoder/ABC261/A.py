L1, R1, L2, R2 = map(int, input().split())
X = [0] * 200
for i in range(L1, R1):
  X[i] += 1
for i in range(L2, R2):
  X[i] += 1

print(X.count(2))
