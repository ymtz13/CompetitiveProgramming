def test(N, P):
  ans = 0
  for i, p in enumerate(P):
    pass


N = int(input())
P = list(map(int, input().split()))

score0 = 0
diff = 0

dd = [0] * N

for i, p in enumerate(P):
  d = (p - i) % N
  k = min(N - d, d)
  score0 += k

  dnext = (p - (i + 1)) % N
  knext = min(N - dnext, dnext)
  if knext < k: diff -= 1
  if knext > k: diff += 1

  dd[d] += 2
  if N % 2 == 0:
    dd[(d + N // 2) % N] -= 2
  else:
    dd[(d + N // 2) % N] -= 1
    dd[(d + N // 2 + 1) % N] -= 1

ans = score0

for ddv in dd[1:]:
  score0 += diff
  ans = min(score0, ans)
  diff += ddv

print(ans)
