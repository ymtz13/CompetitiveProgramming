W, H = map(int, input().split())
mod = 10**9+7
f = [1]*(100010)
p = 1
for x in range(1, 100010):
    f[x] = p = p*x%mod

ans = f[W+H-2] * pow(f[W-1], mod-2, mod) * pow(f[H-1], mod-2, mod) % mod
print(ans)
