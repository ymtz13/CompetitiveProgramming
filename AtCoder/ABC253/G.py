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

print(bgn, end)

A = list(range(N + 1))

if bgn[0] == end[0]:
  pass

else:
  for i in range(bgn[1], N):
    A[i], A[i + 1] = A[i + 1], A[i]
  
  O = []
  for k in range(bgn[0])

  for j in range(1, end[1]):
    A[i], A[i + 1] = A[i + 1], A[i]

print(' '.join(map(str, A)))
