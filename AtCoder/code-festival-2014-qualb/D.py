from collections import defaultdict
from bisect import bisect

N = int(input())
H = [int(input()) for _ in range(N)]
D = defaultdict(list)
for i, h in enumerate(H):
  D[h].append(i)

V = sorted(list(D.items()), reverse=True)

print(D)
print(V)

for k, p in V:


