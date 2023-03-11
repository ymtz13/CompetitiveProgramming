S, T, M = map(int, input().split())
E = [[] for _ in range(T)]
K = [[] for _ in range(S)]
for _ in range(M):
  u, v = map(int, input().split())
  E[v - (S + 1)].append(u - 1)

  K[u - 1].append(v - (S + 1))

for i in range(S):
  K[i].sort()

X = [[None] * T for _ in range(T)]

for s, k in enumerate(K, 1):
  for i, t1 in enumerate(k):
    for t2 in k[i + 1:]:
      if X[t1][t2] is not None:
        print(s, t1 + S + 1, X[t1][t2], t2 + S + 1)
        exit()
      else:
        X[t1][t2] = s

print(-1)
