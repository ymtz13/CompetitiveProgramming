N, K = map(int, input().split())
A = [(a, i) for i, a in enumerate(map(int, input().split()))]

n = N
p = 0
for a, _ in sorted(A):
  c = min(K // n, a - p)
  p += c
  K -= c * n

  if c < a - p: break

  n -= 1

B = [max(0, a - p) for a, _ in A]
i = 0
while K:
  if B[i] > 0:
    B[i] -= 1
    K -= 1
  i += 1
  i %= N

print(' '.join(map(str, B)))
