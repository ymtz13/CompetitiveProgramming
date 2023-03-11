N, M, K = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(M):
  U, V = map(int, input().split())
  E[U - 1].append(V - 1)
  E[V - 1].append(U - 1)

A = list(map(int, input().split()))
B = list(map(int, input().split()))

