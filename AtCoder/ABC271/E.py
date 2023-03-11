N, M, K = map(int, input().split())
D = [tuple(map(int, input().split())) for _ in range(M)]
E = tuple(map(int, input().split()))

INF = 1 << 60
X = [INF] * (N + 1)
X[N] = 0

for e in reversed(E):
  A, B, C = D[e - 1]
  X[A] = min(X[A], X[B] + C)

print(X[1] if X[1] < INF else -1)
