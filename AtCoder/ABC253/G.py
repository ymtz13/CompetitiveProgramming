N, L, R = map(int, input().split())

cnt = 0
bgn = None
end = None

for l in range(1, N):
  if cnt < R:
    end = (l, l + R - cnt)

  n = N - l
  cnt += n

  if bgn is None and cnt >= L:
    bgn = (l, N - (cnt - L))

#print(bgn, end)

A = list(range(N + 1))

b = bgn[0]
e = end[0]

if b == e:
  for x in range(bgn[1], end[1] + 1):
    A[b], A[x] = A[x], A[b]

else:
  for x in range(bgn[1], N + 1):
    A[b], A[x] = A[x], A[b]

  n = e - 1 - b
  if n > 0:
    A = A[:b + 1] + A[-n:][::-1] + A[b + 1:-n]

  for x in range(e + 1, end[1] + 1):
    A[e], A[x] = A[x], A[e]

print(' '.join(map(str, A[1:])))
