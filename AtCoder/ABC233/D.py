from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

D = defaultdict(int)
S = 0
ans = 0
for a in A:
  D[S] += 1
  S += a
  X = S - K
  ans += D[X]

print(ans)
