from collections import defaultdict
from bisect import bisect

N = int(input())
A = list(map(int, input().split()))

D = defaultdict(list)
S = defaultdict(lambda: [0])
ans = 0

for l, a in enumerate(A):
  r = N - 1 - l
  ans += (l + 1) * (r + 1)

  D[a].append(l)
  S[a].append(S[a][-1] + l + 1)

  cl = bisect(D[a], r)
  cr = len(D[a]) - cl

  ml = S[a][cl]
  mr = cr * (r + 1)
  m = (ml + mr) * 2 - min(l, r) - 1

  ans -= m

print(ans // 2)
