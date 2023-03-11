A, B = map(int, input().split())

P = []
for x in range(2, 72):
  if all([x % p for p in P]): P.append(x)

dp = [0] * (1 << len(P))
dp[0] = 1

for x in range(A, B + 1):
  fx = 0
  for i, p in enumerate(P):
    if x % p == 0: fx += (1 << i)

  dp_next = dp[:]
  for f, v in enumerate(dp):
    if f & fx: continue
    dp_next[f + fx] += v

  dp = dp_next

print(sum(dp))
