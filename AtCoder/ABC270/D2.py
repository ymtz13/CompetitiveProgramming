N, K = map(int, input().split())
A = list(map(int, input().split()))[::-1] + [0]

print(A)

i = 0
turn = 0
ans = 0
while A[i] > 0:
  while A[i] > N:
    i += 1
  N -= A[i]

  if turn == 0: ans += A[i]
  turn = 1 - turn

print(ans)
