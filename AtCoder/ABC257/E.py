N = int(input())
C = list(map(int, input().split()))
minC = min(C)

for i, c in enumerate(C, 1):
  if c == minC: x = i

D = N // minC
R = N % minC

Z = [0] * 10
Z[x] = D

for y in range(9, x, -1):
  cdiff = C[y - 1] - minC
  cnt = R // cdiff
  R %= cdiff

  Z[x] -= cnt
  Z[y] += cnt

ans = [str(d) * v for d, v in enumerate(Z)][::-1]
print(''.join(ans))
