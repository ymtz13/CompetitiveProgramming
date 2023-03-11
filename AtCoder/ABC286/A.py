N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = A[:]

for i in range(Q - P + 1):
  l = P - 1 + i
  r = R - 1 + i
  B[l], B[r] = B[r], B[l]

print(*B)
