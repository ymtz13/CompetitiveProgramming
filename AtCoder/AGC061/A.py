def comb(n, k):
  if n <= 1: return 1
  if n % 2 == 0 and k == n // 2: return 0

  x = 1
  while (x << 1) <= n:
    x <<= 1

  if k % x > n - x: return 0

  return comb(n - x, k % x)


T = int(input())
Ans = []

for _ in range(T):
  N, K = map(int, input().split())
  K -= 1

  Q = N % 2
  X = N // 2 - 1

  L = max(0, K - 3)
  R = min(N - 1, K + 3)
  sw = []
  for p2 in range(L, R):
    if p2 & 1: continue
    p = p2 // 2
    if comb(X, p): sw.append(p2)

  if Q:
    sw.extend([s + 1 for s in sw])

  V = list(range(L, R + 2))
  for s in sw:
    V[s - L], V[s + 1 - L] = V[s + 1 - L], V[s - L]

  Ans.append(V[K - L] + 1)

for a in Ans:
  print(a)
