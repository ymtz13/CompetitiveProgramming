N = int(input())
P = list(map(int, input().split()))

C = [0] * N

for i, p in enumerate(P):
  x = (i - p) % N
  C[x] += 1
  C[(x - 1) % N] += 1
  C[(x + 1) % N] += 1

print(max(C))
