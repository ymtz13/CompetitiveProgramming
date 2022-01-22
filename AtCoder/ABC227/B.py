N = int(input())
S = list(map(int, input().split()))

X = [False] * 1001
for a in range(1, 250):
  for b in range(1, 250):
    s = 4 * a * b + 3 * (a + b)
    if s < 1001: X[s] = True

ans = 0
for s in S:
  if not X[s]: ans += 1

print(ans)
