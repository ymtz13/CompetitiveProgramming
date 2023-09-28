N, M, P = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
B.append(1 << 60)

n = sb = 0
ans = 0
for a in reversed(A):
  while B[n] + a < P:
    sb += B[n]
    n += 1

  if a < P:
    ans += n * a + sb + (M - n) * P
  else:
    ans += M * P

print(ans)
