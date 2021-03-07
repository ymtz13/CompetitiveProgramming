from collections import defaultdict

N, C = map(int, input().split())
D = defaultdict(int)

for _ in range(N):
  a, b, c = map(int, input().split())
  D[a  ] += c
  D[b+1] -= c

ans = 0
X = 0
p = 0
for day, cost in sorted(list(D.items())):
  ans += (day - p) * min(X, C)
  X += cost
  p = day
print(ans)