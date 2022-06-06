mod = 998244353

N, M, K, S, T, X = map(int, input().split())

E = [[] for _ in range(N)]
for _ in range(M):
  U, V = map(int, input().split())
  E[U - 1].append(V - 1)
  E[V - 1].append(U - 1)

dpE = [0] * N
dpO = [0] * N
dpE[S - 1] = 1

for k in range(K):
  dpE_next = [0] * N
  dpO_next = [0] * N

  for i in range(N):
    if i == X - 1:
      for e in E[i]:
        dpE_next[i] += dpO[e]
        dpE_next[i] %= mod
        dpO_next[i] += dpE[e]
        dpO_next[i] %= mod

    else:
      for e in E[i]:
        dpE_next[i] += dpE[e]
        dpE_next[i] %= mod
        dpO_next[i] += dpO[e]
        dpO_next[i] %= mod

  dpE = dpE_next
  dpO = dpO_next

print(dpE[T - 1])
