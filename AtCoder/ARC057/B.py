from math import ceil

N, K = list(map(int, input().split()))
A = [None] + [int(input()) for _ in range(N)]

dp = [0] + [-1 for _ in range(N)]

M = 0
for day in range(1,N+1):
    print(day, dp)
    dp_next = [v for v in dp]
    for n in range(1,day+1):
        win_goodday = ceil((dp[n-1]*A[day]+1)/M) if M>0 else 1
        print(n, win_goodday)
        if win_goodday>A[day]: continue
        if dp_next[n]==-1 or win_goodday+dp[n-1] < dp_next[n] : dp_next[n] = win_goodday+dp[n-1]
    dp = dp_next
    M+=A[day]

print(day, dp)

for n in range(N+1):
    if dp[n]<0: break
print(n)
