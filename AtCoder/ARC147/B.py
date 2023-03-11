N = int(input())
P = list(map(int, input().split()))

ans = []


def swap(i, j):
  P[i], P[j] = P[j], P[i]
  ans.append((i, j))


for io in range(1, N, 2):
  if P[io] % 2 == 0: continue

  for ie in range(0, N, 2):
    if P[ie] % 2 == 0: break

  while abs(ie - io) > 1:
    if ie > io:
      swap(ie - 2, ie)
      ie -= 2
    else:
      swap(ie, ie + 2)
      ie += 2

  swap(ie, io)

for _ in range(N):
  for i in range(0, N - 2, 2):
    if P[i] > P[i + 2]:
      swap(i, i + 2)

for _ in range(N):
  for i in range(1, N - 2, 2):
    if P[i] > P[i + 2]:
      swap(i, i + 2)

print(len(ans))
for i, j in ans:
  T = 'A' if abs(i - j) == 1 else 'B'
  print(T, min(i, j) + 1)
