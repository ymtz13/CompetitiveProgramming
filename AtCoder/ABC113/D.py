H, W, K = list(map(int, input().split()))

S=[1, 1]
for i in range(W-1):
    S.append(S[-1]+S[-2])

dp = [0]*W
dp[0] = 1
for h in range(H):
    dp_new=[0]*W
    for w in range(W):
        dp_new[w] = S[w]*S[W-1-w]*dp[w]

    for w in range(W-1):
        dp_new[w  ] += S[w]*S[W-2-w]*dp[w+1]
        dp_new[w+1] += S[w]*S[W-2-w]*dp[w  ]

    dp = [d%1000000007 for d in dp_new]

print(dp[K-1])
