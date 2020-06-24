N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
cost = [None,2,5,5,4,5,6,3,7,6]

Aset = {}
for a in A:
    c = cost[a]
    Aset[c] = max(Aset[c], a) if c in Aset else a
A = sorted([v for k,v in Aset.items()])

dp = [None]*(N+1)
dp[0] = (0,[0]*len(A))

for ia, a in enumerate(A):
    c = cost[a]
    for i in range(c, N+1):
        t = dp[i-c]
        if t and (dp[i]==None or t[0]+1>=dp[i][0]):
            dp[i] = (t[0]+1, t[1].copy())
            dp[i][1][ia] += 1

l=[]
for i in range(len(A)):
    l += [A[len(A)-1-i]]*dp[N][1][len(A)-1-i]

print(*l, sep='')
