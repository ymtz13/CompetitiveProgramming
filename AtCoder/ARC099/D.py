def S(n):
  return sum(map(int, str(n)))


X = []
for i in range(1, 10000000):
  X.append((i, S(i), i / S(i)))

m = 1 << 60
cnt = 0
for n, s, v in reversed(X):
  if v <= m:
    print(n, s, v)
    m = v
    cnt += 1

print(cnt)
