N = int(input())
A = list(map(int, input().split()))

s = smax = smin = 0
dmax = dmin = 0
for a in A:
  s += a * 2 - 1
  smax = max(smax, s)
  smin = min(smin, s)

  dmax = max(dmax, s - smin)
  dmin = min(dmin, s - smax)

print(dmax - dmin + 1)
