N, M = map(int, input().split())
E = [1 << i for i in range(N)]
for _ in range(M):
  A, B = map(int, input().split())
  E[A - 1] ^= 1 << (B - 1)
  E[B - 1] ^= 1 << (A - 1)

dp = [20] * (1 << 20)
dp[0] = 0

for p in range(N):
  for q in range(1 << p, 2 << p):
    C0 = []
    ok = True
    for i in range(p + 1):
      if (q >> i) & 1 and E[i] & q != q:
        ok = False
        break
      C0.append(1 << i)

    if not ok: continue

    K = len(C0)
    for k in range(1 << K):
      s = 0
      for j, c0 in enumerate(C0):
        if (k >> j) & 1: s += c0  #(1 << c0)

      dp[q + s] = min(dp[q + s], dp[s] + 1)

print(dp[(1 << N) - 1])
