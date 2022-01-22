N, X = map(int, input().split())
A = [0] + list(map(int, input().split()))
K = [False] * (N + 1)

ans = 0
while not K[X]:
  K[X] = True
  X = A[X]
  ans += 1

print(ans)
