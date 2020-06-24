def P(a,b,mod):
    r=1
    for i in range(b):
        r = (r*(a-i)) % mod
    return r

N, K = [int(c) for c in input().split()]
E = [[] for n in range(N)]
mod = 1000000007

for i in range(N-1):
    a, b = [int(c) for c in input().split()]
    E[a-1].append(b-1)
    E[b-1].append(a-1)


n = K * P(K-1, len(E[0]), mod) % mod
for i in range(1, N):
    n = (n * P(K-2, len(E[i])-1, mod)) % mod

print(n)
