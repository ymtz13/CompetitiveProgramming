N = int(input())
H = list(map(int, input().split()))
X = [[] for _ in range(N)]

D = set()

for _ in range(N):
  M, S, E = map(int, input().split())
  X[M - 1].append((S, E))

  D.add(S)
  D.add(E)

D = {v: i for i, v in enumerate(sorted(list(D)))}

K = len(D) + 1
E = [[] for _ in range(K)]

for x in X:
  x = [(D[s], D[e]) for s, e in sorted(x, key=lambda x: x[1])]

  for s0, e0 in x:
    n = 0
    h = H[0]
    E[s0].append(e0 + h * K)
    for s, e in x:
      if e0 <= s:
        n += 1
        h += H[n]
        e0 = e
        E[s0].append(e0 + h * K)

dp = [0] * K
for i, e in enumerate(E[:-1]):
  for eh in e:
    h, e0 = eh // K, eh % K
    dp[e0] = max(dp[e0], dp[i] + h)

  dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[-1])
