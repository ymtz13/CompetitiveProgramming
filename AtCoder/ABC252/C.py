N = int(input())
S = [input() for _ in range(N)]

ans = 100 * N
for k in range(10):
  k = str(k)
  cnt = [0] * 10
  t = 0
  for s in S:
    i = s.index(k)
    t = max(t, cnt[i] * 10 + i)
    cnt[i] += 1

  ans = min(ans, t)

print(ans)
