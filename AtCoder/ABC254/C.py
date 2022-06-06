N, K = map(int, input().split())
A = list(map(int, input().split()))
B = [[] for _ in range(K)]

for i, a in enumerate(A):
  B[i % K].append(a)

C = [None] * N
for j, b in enumerate(B):
  b.sort()
  for k, x in enumerate(b):
    C[k * K + j] = x

print('Yes' if C == sorted(C) else 'No')
