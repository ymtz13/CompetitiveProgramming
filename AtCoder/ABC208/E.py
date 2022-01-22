from bisect import bisect
from collections import defaultdict

INF = 1 << 60

S = [[(0, 0), (1, 1)]]
for i in range(20):
  s = defaultdict(int)
  for k, v in S[-1]:
    for d in range(10):
      s[k * d] += v
  S.append(sorted(list(s.items())))

T = []
for s in S:
  t = []
  x = 0
  for k, v in s:
    x += v
    t.append((k, x))
  t.append((INF, t[-1][1]))
  T.append(t)

N, K = input().split()
N = list(map(int, N))
K = int(K)
M = len(N)

P = [1]
for d in N:
  P.append(P[-1] * d)

ans = 1 if P[-1] <= K else 0

for i, (d, p) in enumerate(zip(N, P)):
  m = M - i - 1

  for x in range(d):
    if i == 0 and x == 0: continue
    t = p * x
    if t:
      j = bisect(T[m], (K // t, INF)) - 1
      _, n = T[m][j]
    else:
      n = 10**m

    ans += n

for m in range(1, M):
  for x in range(1, 10):
    j = bisect(T[m - 1], (K // x, INF)) - 1
    _, n = T[m - 1][j]
    ans += n

print(ans)
