def score(l, r):
    st = sa = 0
    for i in range(l, r+1):
        if (i-l)%2==0: st+=A[i]
        else:      sa+=A[i]
    return st, sa

N = int(input())
A = list(map(int, input().split()))
ans = -10000000
for t in range(N):
    sa_max = st_max = -10000000
    for a in range(N):
        if t==a: continue
        st, sa = score(*sorted((t,a)))
        if sa>sa_max:
            sa_max = sa
            st_max = st

    ans = max(ans, st_max)
print(ans)
        
