N, M = map(int, input().split())

X = []
for _ in range(N):
  inp = tuple(map(int, input().split()))
  X.append(list(zip(inp[1::2], inp[2::2])))

INF = 1 << 60
M1 = M + 1

v0 = X[0] + X[1]
k0 = len(v0)
v1 = v2 = v0
dp1 = dp2 = [[0] + [INF] * M for _ in range(k0)]

for v3 in X:
  dp3 = []
  for x3, d3 in v3:
    z3 = [INF] * M1

    for (x1, d1), z1 in zip(v1, dp1):
      for i in range(1, M1):
        z3[i] = min(z3[i], z1[i - 1] + abs(x1 - x3) * (d1 + d3))

    for (x2, d2), z2 in zip(v2, dp2):
      for i in range(M1):
        z3[i] = min(z3[i], z2[i] + abs(x2 - x3) * (d2 + d3))

    dp3.append(z3)

  v1 = v2
  v2 = v3
  dp1 = dp2
  dp2 = dp3

ans = INF
for z in dp2:
  ans = min(ans, *z)

if M:
  for z in dp1:
    ans = min(ans, *z[:-1])

print(ans)
