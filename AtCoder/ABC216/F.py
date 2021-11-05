mod = 998244353
K = 5001

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = sorted(list(zip(A, B)), reverse=True)
A = [a for a, _ in AB]
B = [b for _, b in AB]

dp = [0] * K
dp[0] = 1

dpTable = []
dpTable.append(dp)

for b in B[::-1]:
  dp_next = dp[:]
  for t in range(b, K):
    dp_next[t] += dp[t - b]
    dp_next[t] %= mod

  dp = dp_next
  dpTable.append(dp)

#print(B)
#for dp in dpTable:
#  print(dp[:10])

ans = 0

for i, (a, b) in enumerate(zip(A, B)):
  s = a - b
  if s < 0: continue

  dp = dpTable[-2 - i]
  S = []
  v = 0
  for d in dp:
    v += d
    v %= mod
    S.append(v)

  ans += S[s]
  ans %= mod

print(ans)
