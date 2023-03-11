from collections import deque

N = int(input())
E = [[] for _ in range(N)]
D = [0] * N
for _ in range(N - 1):
  a, b = map(int, input().split())
  a -= 1
  b -= 1

  E[a].append(b)
  E[b].append(a)

  D[a] += 1
  D[b] += 1

dp0 = [0, 0]
dp1 = [0, 1]
mod = 998244353
for _ in range(N + 10):
  v0 = dp1[-1]
  v1 = dp1[-1] + dp0[-1]
  dp0.append(v0 % mod)
  dp1.append(v1 % mod)

nLeaf = D.count(1)
exist = False
for i, d in enumerate(D):
  if d >= 3:
    cnt = 0
    cnt3 = 0
    for e in E[i]:
      if D[e] == 1: cnt += 1
      if D[e] >= 3: cnt3 += 1

    if cnt >= 2:
      print(0, 333333)
      exit()

    if cnt3 >= 1:
      print(0, 1111111)
      # exit()

    if cnt == 1:
      if exist:
        print(0, 222222)
        exit()

      exist = True

linear = True
for root in range(N):
  if D[root] >= 3:
    linear = False
    break

if linear:
  print(dp1[N - 2] * 2 % mod)
  exit()

queue = deque([(root, None, 0)])
C = []
CL = []
while queue:
  q, p, c = queue.popleft()

  if D[q] == 1:
    C.append(c - 1)
    CL.append()
    c = 0

  if D[q] >= 3:
    C.append(c - 1)
    c = 0

  for e in E[q]:
    if e != p: queue.append((e, q, c + 1))

C = C[1:]
print(C)

P = 1
for c in C:
  if c == 0: continue
  P *= dp1[c]
  P %= mod

if exist:
  print(P)

else:
  ans = 0
  for c in CL:
    inv = pow(dp1[c], mod - 2, mod)
    ans += P * inv * dp1[c + 1] % mod
    ans %= mod

  print(ans)
