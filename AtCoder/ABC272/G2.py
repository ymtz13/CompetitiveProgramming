from collections import defaultdict

M = 1000000
F = list(range(M))
P = []
for p in range(2, M):
  if F[p] != p: continue
  P.append(p)
  for r in range(p * 2, M, p):
    F[r] = p

memo = {}


def factor(X):
  if X < M: return F[X]
  if X in memo: return memo[X]

  for p in P:
    if p * p > X:
      memo[X] = X
      break
    if X % p == 0:
      memo[X] = p
      break

  return memo[X]


N = int(input())
A = list(map(int, input().split()))

for a0 in A:
  D = [abs(a - a0) for a in A if a != a0]
  count = defaultdict(int)

  for d in D:
    if d == 1: continue

    p = d
    s = set()
    while p > 1:
      f = factor(p)
      p //= f
      if f in s: continue
      s.add(f)

      if f == 2: continue
      count[f] += 1

    if d % 4 == 0: count[4] += 1

  for key, value in count.items():
    if value >= N // 2:
      print(key)
      exit()

print(-1)
