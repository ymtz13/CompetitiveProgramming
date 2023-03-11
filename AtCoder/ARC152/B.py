def ans(x):
  print(x)
  exit()


from bisect import bisect_left

N, L = map(int, input().split())
A = tuple(map(int, input().split()))

if L % 2 == 0 and L // 2 in A: ans(2 * L)

A0 = [a for a in A if a * 2 < L]
A1 = [a for a in A if a * 2 > L]

if not A0:
  a = A1[0]
  ans(a * 4)

if not A1:
  a = A0[-1]
  ans((L - a) * 4)

aans = min(A1[0] * 4, (L - A0[-1]) * 4)

for a in A0:
  b = L - a

  i = bisect_left(A1, b)

  if i == 0:
    s = None
    t = A1[i]

  elif i == len(A1):
    s = A1[-1]
    t = None

  else:
    s = A1[i - 1]
    t = A1[i]

  if s: aans = min(aans, L * 2 + abs(b - s) * 2)
  if t: aans = min(aans, L * 2 + abs(b - t) * 2)

ans(aans)
