N, X = map(int, input().split())

ans = 1 << 60
minB = 1 << 60
s = 0
for n in range(1, N + 1):
  A, B = map(int, input().split())
  minB = min(minB, B)
  s += A + B

  t = s + max(0, X - n) * minB
  ans = min(ans, t)

print(ans)
