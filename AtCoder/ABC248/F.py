N, P = map(int, input().split())
N1 = N + 10

dp01 = [0] * N1
dp10 = [0] * N1
dp11 = [0] * N1

dp10[1] = 1
dp11[0] = 1

for _ in range(N - 1):
  dp01_next = [0] * N1
  dp10_next = [0] * N1
  dp11_next = [0] * N1

  for i, v in enumerate(dp01[:-10]):
    dp01_next[i + 1] += v
    dp01_next[i + 1] %= P
    dp11_next[i] += v
    dp11_next[i] %= P

  for i, v in enumerate(dp10[:-10]):
    dp10_next[i + 1] += v
    dp10_next[i + 1] %= P
    dp11_next[i] += v
    dp11_next[i] %= P

  for i, v in enumerate(dp11[:-10]):
    dp01_next[i + 2] += v
    dp01_next[i + 2] %= P
    dp10_next[i + 2] += v
    dp10_next[i + 2] %= P
    dp11_next[i + 1] += v * 3
    dp11_next[i + 1] %= P
    dp11_next[i] += v
    dp11_next[i] %= P

  dp01 = dp01_next
  dp10 = dp10_next
  dp11 = dp11_next

print(' '.join(map(str, dp11[1:-10])))
