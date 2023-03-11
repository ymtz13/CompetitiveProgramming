N, K = map(int, input().split())

if K > N // 2:
  print(-1)
  exit()

ans = []
for i in range(N // (2 * K)):
  s = i * (2 * K) + 1
  ans.extend(list(range(s + K, s + 2 * K)))
  ans.extend(list(range(s, s + K)))

r = list(range(len(ans) + 1, N + 1))

if len(r) <= K:
  ans = ans[:-K] + r + ans[-K:]
else:
  t = len(r) % K
  ans = ans[:-(K - t)] + r[t:] + ans[-(K - t):] + r[:t]

print(' '.join(map(str, ans)))