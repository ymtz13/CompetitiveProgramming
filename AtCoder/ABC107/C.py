N, K = map(int, input().split())
X = list(map(int, input().split()))

Xp = [0]+[+x for x in X if x>=0]
Xm = [0]+[-x for x in reversed(X) if x< 0]

Np = len(Xp)-1
Nm = len(Xm)-1

ans = 10**10
for np in range(min(Np, K), max(0, K-Nm)-1, -1):
    nm = K-np
    time = min(Xp[np], Xm[nm]) + Xp[np] + Xm[nm]
    ans = min(ans, time)

print(ans)
