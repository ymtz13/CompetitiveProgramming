mod = 10**9+7

def comb(n, k):
  r = 1
  for i in range(k):
    r = r * (n-i) % mod
    r = r * pow(i+1, mod-2, mod) % mod
  return r

N, K = map(int, input().split())
print(comb(N+K-1, N-1) if K<N else comb(N, K%N))
