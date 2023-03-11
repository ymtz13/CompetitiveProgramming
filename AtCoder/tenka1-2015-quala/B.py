def parse(X):
  HH, MM, SSmmm = X.split(':')
  SS, mmm = SSmmm.split('.')

  min = int(MM) + int(HH) * 60
  sec = int(SS) + 60 * min
  msec = int(mmm) + sec * 1000

  return msec


INF = 1 << 60

N = int(input())
SE = []
l = -INF
r = +INF
for _ in range(N):
  S, E = map(parse, input().split())
  SE.append((S, E))

  if E <= S:
    l = max(l, S)
    r = min(r, E + 1000)


def correct(t):
  if t <= l - 1000: return t
  if t >= r: return t + 1000
  return None


ans = []
for s, e in SE:
  if e <= s:
    print(e - s + 1000)
    continue

  s = correct(s)
  e = correct(e)

  print(-1 if s is None or e is None else e - s)
