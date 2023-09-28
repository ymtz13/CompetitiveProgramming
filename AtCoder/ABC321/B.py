N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = -1
for x in range(0, 101):
  B = A[:] + [x]
  S = sum(B) - max(B) - min(B)

  if S >= X:
    ans = x
    break

print(ans)
