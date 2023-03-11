A, B = map(int, input().split())

X = (A / (2 * B))**(2 / 3) - 1

ans = A + 100
for n in range(max(0, int(X) - 100000), int(X) + 100000):
  t = n * B + A / ((n + 1)**0.5)
  ans = min(ans, t)

print(ans)
