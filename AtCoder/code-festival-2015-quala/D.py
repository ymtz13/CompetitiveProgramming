N, M = map(int, input().split())
X = [int(input()) for _ in range(M)]


def check(T):
  p = 0
  for x in X:
    r = max(x - p - 1, 0)
    if r > T: return False
    p = max(x, x + T - r * 2, x + (T - r) // 2)

  return p >= N


ok = N * 2
ng = -1

while ok - ng > 1:
  tgt = (ok + ng) // 2
  if check(tgt):
    ok = tgt
  else:
    ng = tgt

print(ok)
