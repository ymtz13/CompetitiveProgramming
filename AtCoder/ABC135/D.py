S = input()
T = []
mod = int(10**9+7)

for k in range(6):
    T.append([])
    r = 10**k
    for j in range(10):
        T[-1].append(j*r%13)

dp = [1]+[0]*12
k = (len(S)-1)%6
for s in S:
    dp_new = [0]*13
    if s=='?':
        tt = T[k]
        for r in range(10):
            m = tt[r]
            print(r,m)
            for i, dd in enumerate(dp):
                dp_new[(i+m)%13] += dd
    else:
        m = T[k][int(s)]
        for i in range(13):
            dp_new[(i+m)%13] = dp[i]
    dp = [d%mod for d in dp_new]
    k=(k+5)%6

print(dp[5]%mod)
