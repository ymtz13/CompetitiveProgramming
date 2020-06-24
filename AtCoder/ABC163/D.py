N, K = map(int, input().split())
mod = 10**9+7
S = T = 0
for i in range(K):
    S = (S+i  )%mod
    T = (T+N-i)%mod
ans = 0
for k in range(K, N+2):
    ans += T-S+1
    ans %= mod
    S = (S+k  )%mod
    T = (T+N-k)%mod

print(ans)
