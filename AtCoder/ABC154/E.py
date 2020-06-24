import numpy as np

N = input()
K = int(input())

M = len(N)
dp = np.zeros((M+1, K+1, 2), int)
# dp[i,j,k] = i桁の正整数であって、0でない数をj回使っており、Nの下からi桁目までの数を越えていない(k=0)/いる(k=1) ようなものの数

dp[0,0,0] = 1

for i in range(1,M+1):

    # Nの下からi桁目
    X = int(N[-i])
    
    # i桁目が0の場合
    dp[i,:,0] += dp[i-1,:,0]
    if X>0:
        dp[i,:,0] += dp[i-1,:,1]
    else:
        dp[i,:,1] += dp[i-1,:,1]
        
    for n in range(1,10): # i桁目がn(1以上)の場合
        if n<X:
            dp[i,1:,0] += dp[i-1,:-1,0] + dp[i-1,:-1,1]
        elif X==n:
            dp[i,1:,0] += dp[i-1,:-1,0]
            dp[i,1:,1] += dp[i-1,:-1,1]
        else:
            dp[i,1:,1] += dp[i-1,:-1,0] + dp[i-1,:-1,1]

print(dp[-1, K, 0])
