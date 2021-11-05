K = 18
P = []
for i in range(1, K+1):
  for j in range(i+1, K+1):
    P.append((i, j))


print(18, len(P))
for a, b in P:
  print(a, b)
