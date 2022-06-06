N = int(input())
A = list(map(int, input().split()))

C = [None] * N
c = 0
p = None
for i in range(N - 1, -1, -1):
  if A[i] != p:
    c += 1
    p = A[i]
  C[i] = c


if c == 1:
  print('Yes' if A[0] == 0 else 'No')
  exit()

for i, a in enumerate(A):
  if a != i % 2: break
  if i == N - 1:
    print('Yes')
    exit()

  if C[i + 1] <= i + 1:
    print('Yes')
    exit()

print('No')
