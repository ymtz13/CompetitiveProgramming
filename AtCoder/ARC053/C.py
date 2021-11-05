N = int(input())
X = [tuple(map(int, input().split())) for _ in range(N)]

Xp = sorted([(a, b) for a, b in X if a <= b])
Xn = sorted([(a, b) for a, b in X if a > b], key=lambda x: -x[1])

s = 0
ans = 0
for a, b in Xp + Xn:
  s += a
  ans = max(ans, s)
  s -= b
  ans = max(ans, s)

print(ans)
