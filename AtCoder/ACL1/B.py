def f(a, b):
  x = w = 1
  y = z = 0
  while b:
    q = a // b
    r = a % b

    x, y, z, w = z, w, x - q * z, y - q * w
    a, b = b, r

  return a, x, y


from collections import defaultdict

N = N0 = int(input()) * 2
D = defaultdict(int)

while N % 2 == 0:
  N //= 2
  D[2] += 1

for p in range(3, N, 2):
  if p * p > N: break
  while N % p == 0:
    N //= p
    D[p] += 1

if N > 1: D[N] += 1

K = []
for p, n in D.items():
  a = p**n
  b = N0 // a

  _, _, y = f(a, b)
  K.append(b * y)

M = len(K)

ans = N0

for r in range(1 << M):
  v = 0
  for i, k in enumerate(K):
    if (r >> i) & 1: v += k

  v %= N0
  if v < 2: v += N0
  #print(v - 1, v, (v - 1) * v)
  ans = min(ans, v - 1)
  #R = [(r >> m) & 1 for m in range(M)]
  #print(R)

print(ans)

# a = bq + r
# [b] = [0  1][a]
# [r]   [1 -q][b]

#[0  1] [x  y] = [z    w   ]
#[1 -q] [z  w]   [x-qz y-qw]

# [g] = [x  y][a] = [ax+by]
# [0]   [z  w][b]   [az+aw]

#(k+1) == 0 (mod3)
#(k+1) == 0 (mod5)
#(k+1) = 0
#
#(k+1) == 1 (mod3)
#(k+1) == 0 (mod5)
# k+1  = -5 = 10