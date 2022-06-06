N = int(input())
A = list(map(int, input().split()))

INF = 1 << 60

dp00 = 0
dp01 = INF
dp10 = INF
dp11 = A[0]

for i in range(1, N):
  (dp00, dp01, dp10, dp11) = (dp01, min(dp00, dp01) + A[i], dp11,
                              min(dp10, dp11) + A[i])

print(min(dp01, dp10, dp11))
