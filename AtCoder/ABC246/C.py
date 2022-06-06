from audioop import reverse
import re

N, K, X = map(int, input().split())
A = list(map(int, input().split()))

R = []
for a in A:
  k = min(K, a // X)
  K -= k
  a -= X * k
  R.append(a)

R.sort(reverse=True)

ans = 0
for r in R:
  if K > 0:
    K -= 1
  else:
    ans += r

print(ans)
