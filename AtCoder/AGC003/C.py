N = int(input())
A = [int(input()) for _ in range(N)]
A0 = A[0::2]
C = sorted(A)
C1 = set(C[1::2])

ans = 0
for a in A0:
  if a in C1: ans += 1

print(ans)
