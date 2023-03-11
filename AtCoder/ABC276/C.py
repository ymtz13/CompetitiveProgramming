N = int(input())
P = list(map(int, input().split()))


def next(P):
  ans = P[:]

  for i in range(N - 2, -1, -1):
    if P[i] < P[i + 1]: break

  k = min([p for p in P[i + 1:] if p > P[i]])
  ans[i] = k

  r = [v for v in range(1, N + 1) if v not in ans[:i + 1]]
  ans = ans[:i + 1] + sorted(r)

  return ans


Pinv = [N + 1 - p for p in P]
Qinv = next(Pinv)
Q = [N + 1 - q for q in Qinv]

print(' '.join(map(str, Q)))
