N = int(input())
E = [[] for _ in range(N)]

for _ in range(N - 1):
  u, v = map(int, input().split())
  E[u - 1].append(v - 1)
  E[v - 1].append(u - 1)
