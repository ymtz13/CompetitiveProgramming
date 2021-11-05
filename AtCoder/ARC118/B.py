K, N, M = map(int, input().split())
A = list(map(int, input().split()))

B0 = []
B = [None] * K
for i, a in enumerate(A):
  b0 = (M*a-1)//N
  B0.append((N*b0 - M*a, i))
  B[i] = b0

R = M - sum(B)
for _, i in sorted(B0)[:R]:
  B[i] += 1

print(' '.join(map(str, B)))
