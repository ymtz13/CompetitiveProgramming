mod = 10**9 + 7
N = int(input())
S = input()
P = [1]*(N+1)
for c in 'atcoder':
  X = [0]*(N+1)
  for i in range(1, N+1):
    X[i] = X[i-1]
    if S[i-1]==c: 
      X[i] += P[i]
      X[i] %= mod
  P = X

print(X[-1] % mod)
