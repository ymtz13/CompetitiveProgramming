def solve(N, A):
  K = N * (N + 1) // 2
  if sum(A) % K != 0: return False
  M = sum(A) // K

  s = 0
  for i in range(N):
    d = A[i] - A[i - 1]  # = M - xN
    if (M - d) % N != 0: return False
    if M - d < 0: return False
    s += (M - d) // N

  return s == M


N = int(input())
A = list(map(int, input().split()))

ans = solve(N, A)

print('YES' if ans else 'NO')
