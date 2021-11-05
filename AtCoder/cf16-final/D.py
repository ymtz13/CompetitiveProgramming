from collections import defaultdict

N, M = map(int, input().split())
X = list(map(int, input().split()))

K = [defaultdict(int) for _ in range(M)]
for x in X:
  K[x % M][x] += 1

P = [0] * M
S = [0] * M
for i, k in enumerate(K):
  for v in k.values():
    P[i] += v // 2
    S[i] += v % 2

ans = 0
for a in range(M):
  b = (M - a) % M
  if b < a: continue
  if b == a:
    ans += sum(K[a].values()) // 2
    continue

  pa, sa = P[a], S[a]
  pb, sb = P[b], S[b]

  sm = min(sa, sb)
  sa -= sm
  sb -= sm

  ta = min(sa, 2 * pb)
  tb = min(sb, 2 * pa)
  pb = (2 * pb - ta) // 2
  pa = (2 * pa - tb) // 2

  ans += sm + ta + tb + pa + pb

print(ans)
