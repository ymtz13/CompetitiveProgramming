from bisect import bisect_left

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
maxA = max(A)
sumA = sum(A)

D = maxA * N - sumA
if K >= D:
  print(maxA + (K - D) // N)
  exit()


def check(V):
  s = 0
  for v in range(1, maxA + 1, V):
    i = bisect_left(A, v)
    s += (N - i) * V

  return sumA + K >= s


ans = 1
for V in range(2, maxA):
  if check(V): ans = V

print(ans)
