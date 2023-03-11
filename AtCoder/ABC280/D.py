from collections import defaultdict

K = int(input())
k = K

f = defaultdict(int)
for p in range(2, K):
  if p * p > k: break

  while k % p == 0:
    f[p] += 1
    k //= p

if k > 1: f[k] += 1

ans = 2
for p, v in f.items():
  ok = K
  ng = 1

  while ok - ng > 1:
    tgt = (ok + ng) // 2

    count = 0
    pp = p
    while pp <= tgt:
      count += tgt // pp
      pp *= p

    if count >= v:
      ok = tgt
    else:
      ng = tgt

  ans = max(ans, ok)

print(ans)
