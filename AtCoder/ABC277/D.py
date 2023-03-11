N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

A2 = A + A

ans = 0

l = 0
while l < N * 2:
  r = l
  prev = A2[l]
  s = 0
  while r < N * 2:
    v = A2[r]
    if v == prev or v == (prev + 1) % M:
      r += 1
      s += v
      prev = v
    else:
      break

  ans = max(ans, s)

  l = r

ans = sum(A) - ans
print(ans if ans >= 0 else 0)
