N, M, S = map(int, input().split())
A = list(map(int, input().split()))[::-1]

ans = 0
st = 0
while st < N:
  s = maxavg = 0
  for i, a in enumerate(A[st:], st):
    s += a
    avg = s / (i - st + 1)

    if avg > maxavg:
      maxavg = avg
      j = i

  n = j - st + 1
  x = min(M, S / n)
  S -= x * n
  for i in range(st, j + 1):
    ans += x * A[i]

  st = j + 1

print(ans)
