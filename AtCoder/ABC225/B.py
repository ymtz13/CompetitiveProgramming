from collections import defaultdict

N = int(input())
C = [0] * N
for _ in range(N - 1):
  a, b = map(int, input().split())
  C[a - 1] += 1
  C[b - 1] += 1

D = defaultdict(int)
for c in C:
  D[c] += 1

print('Yes' if D[N - 1] == 1 and D[1] == N - 1 else 'No')
