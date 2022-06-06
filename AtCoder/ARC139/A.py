N = int(input())
T = list(map(int, input().split()))

A = 1 << T[0]
for i in range(1, N):
  if T[i] < T[i - 1]:
    A += 1 << T[i]
    # print(i, 'T = ', T[i], '<', '{:08b}'.format(A))

  if T[i] == T[i - 1]:
    A += 2 << T[i]
    # print(i, 'T = ', T[i], '=', '{:08b}'.format(A))

  if T[i] > T[i - 1]:
    X = 1 << T[i]
    A >>= T[i]
    A += 2 if A % 2 else 1
    A <<= T[i]
    # A += X
    # print(i, 'T = ', T[i], '>', '{:08b}'.format(A), '{:08b}'.format(X))

print(A)
