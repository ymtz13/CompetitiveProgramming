L, R = map(int, input().split())
if L == 1: L += 1

M = 10**6 + 10

F = [0] * M
for p in range(2, M):
  if F[p] == 0:
    for k in range(p, M, p):
      if F[k] >= 0: F[k] += 1

    for k in range(p * p, M, p * p):
      F[k] = -1

ans = 0
for v in range(L, R + 1):
  c = R // v
  ans -= c * 2 - 1

for v in range(2, R + 1):
  if F[v] == -1: continue
  sign = (-1)**(F[v] - 1)
  c = R // v - (L - 1) // v
  ans += c * c * sign

print(ans)
