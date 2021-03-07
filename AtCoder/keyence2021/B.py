N, K = map(int, input().split())
A = map(int, input().split())
D =[0] * (N+1)
for a in A: D[a] += 1

S = 0
for a, n in enumerate(D):
  X = K - min(n, K)
  K -= X
  S += X * a

print(S)
