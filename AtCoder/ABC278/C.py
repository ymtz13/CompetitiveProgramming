from collections import defaultdict

N, Q = map(int, input().split())
D = defaultdict(set)

ans = []
for _ in range(Q):
  T, A, B = map(int, input().split())

  if T == 1: D[A].add(B)
  if T == 2: D[A].discard(B)
  if T == 3: ans.append('Yes' if B in D[A] and A in D[B] else 'No')

for a in ans:
  print(a)
