N, A, B = map(int, input().split())

if N < A:
  print(0)
  exit()

if A <= B:
  print(N - (A - 1))
  exit()

ans = (N // A - 1) * B + min(N % A + 1, B)
print(ans)
