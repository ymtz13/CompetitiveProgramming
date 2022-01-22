X = list(map(int, input()))
K = len(X)
INF = 1 << 60

if K == 1:
  print(X[0])
  exit()


def parse(X):
  return int(''.join(map(str, X)))


# 1. 最上位の桁を変更する場合
a1 = INF
if X[0] < 9:
  y0 = X[0] + 1
  dmax = 0
  for d in range(-1, -10, -1):
    if y0 + d * (K - 1) >= 0: dmax = d
  Y = list(range(y0, y0 + dmax * K, dmax)) if dmax != 0 else [y0] * K
  a1 = parse(Y)

# 2. 上1桁をXから変更しない場合
a2 = INF
y0 = X[0]
for d in range(-9, 10):
  last = y0 + d * (K - 1)
  if last < 0 or last > 9: continue
  Y = list(range(y0, y0 + d * K, d)) if d != 0 else [y0] * K
  if parse(Y) >= parse(X):
    a2 = min(a2, parse(Y))

# 3. 上2桁をXから変更しない場合
a3 = INF
y0 = X[0]
d = X[1] - X[0]
last = y0 + d * (K - 1)
Y = list(range(y0, y0 + d * K, d)) if d != 0 else [y0] * K

if 0 <= last <= 9 and parse(Y) >= parse(X):
  a3 = parse(Y)

print(min(a1, a2, a3))
