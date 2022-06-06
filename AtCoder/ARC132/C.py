def pr(dp):
  D = {}
  for i, v in enumerate(dp):
    if v == 0: continue
    D['{:05b}'.format(i)] = v
  print(D)


mod = 998244353

N, D = map(int, input().split())
A = list(map(int, input().split())) + list(range(N + 1, N + 10))
S = set(A)
M = 1 << (D * 2 + 1)
P = [1 << i for i in range(D * 2 + 1)]

dp = [0] * M
j = 0
for i in range(1, D + 1):
  if i not in S: j += 1
  j <<= 1
dp[j >> 1] = 1

#pr(dp)

for n in range(1, N + 1):
  dp_next = [0] * M

  f = 1 if n + D not in S else 0
  for k, v in enumerate(dp):
    kk = (k * 2 + f) % M

    if A[n - 1] == -1:
      for p in P:
        if kk & p:
          dp_next[kk - p] += v
          dp_next[kk - p] %= mod

    else:
      dp_next[kk] += v
      dp_next[kk] %= mod

  dp = dp_next

print(dp[0])
