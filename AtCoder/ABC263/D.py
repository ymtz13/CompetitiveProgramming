N, L, R = map(int, input().split())
A = list(map(int, input().split()))

SL = [0]
s = 0
for n, a in enumerate(A, 1):
  s += a
  if n * L <= s:
    s = n * L
  SL.append(s)

SR = [0]
s = 0
for n, a in enumerate(A[::-1], 1):
  s += a
  if n * R <= s:
    s = n * R
  SR.append(s)

ans = 1 << 60
for nl in range(N + 1):
  ans = min(ans, SL[nl] + SR[N - nl])

print(ans)
