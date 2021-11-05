N = int(input())
P = list(map(int, input().split()))
Q = [None] * N
for i, p in enumerate(P, 1):
  Q[p - 1] = i
print(' '.join(map(str, Q)))
