N = int(input())
S = [ord(c) - ord('A') for c in input()]

K = 1 << 10
dp = [[0] * 11 for _ in range(1 << 10)]
dp[0][10] = 1
mod = 998244353

for c in S:
  for k in range(K):
    if not k & (1 << c): continue

    d = 2 * dp[k][c] % mod
    for l in range(11):
      if l != c and (k & (1 << l) or l == 10):
        d = (d + dp[k - (1 << c)][l]) % mod

    dp[k][c] = d

ans = -1
for d in dp:
  for v in d:
    ans = (ans + v) % mod

print(ans)
