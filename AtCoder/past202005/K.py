N, Q = map(int, input().split())
top = list(range(N+1))
par = [0]*(N+1)

for _ in range(Q):
    f, t, x = map(int, input().split())
    buf=top[f]
    top[f]=par[x]
    par[x]=top[t]
    top[t]=buf

ans = [None]*(N+1)
for i in range(1, N+1):
    x = top[i]
    while x>0:
        ans[x] = i
        x = par[x]

for a in ans[1:]:
    print(a)
